#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
# 1) place script inside a Node->Right Mouse Button -> Type Properties -> scripts
# 2) script will add for any preexistent children node as comment the headline taken from online documentation
# NOTE: some scripts don't have headline or entire documentation 

import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/",os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')
   
def getHeader(path):
    path = path.lower()
    path = path.replace("operator:","").replace("object/","obj/").split("?")[0]
   
    if "invalid" in path:
        return ""
    
    try:
        nodeHelpContent = ARCHIVE.read(path+".txt")
        splitted = nodeHelpContent.split("\"\"\"")
        return splitted[1] if len(splitted)>1 else "Not found"
    except:
        return "Not found"

def iterateChildren(node):
     for child in node.children():
 
        if len(child.comment())==0 and child.isEditable():
            description = getHeader(child.type().defaultHelpUrl())
            child.setComment(description)
            child.setGenericFlag(hou.nodeFlag.DisplayComment,True)
            
        if child.isLockedHDA(): 
            hou.ui.displayMessage("LOCKED: "+child.name())
            return
        elif child.children()>0 :
            iterateChildren(child)
                
    

def main():
    iterateChildren(hou.node("/"))

main()
