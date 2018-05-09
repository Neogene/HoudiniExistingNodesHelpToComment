# HoudiniExistingNodesHelpToComment
A script which auto populate PREEXISTENT nodes comment with online documentation headline

## AUTHOR: ## 
eng. ANDREA LEGANZA

## TESTED VERSION/S: ## 
HOUDINI 16/16.5

## DESCRIPTION: ## 
When learning Houdini it may be hard to undestand the flow of nodes and to take a sneak peak on the purpose of a single node: a user has to select right click on node -> help and wait for Houdini internal browser to load the help page. This script simply read node headline (the title) from the internal documentation ad uses to populate ALL node comment.

## RESULTS: ##
![Script result](https://github.com/Neogene/HoudiniExistingNodesHelpToComment/blob/master/before_after.png)

## INSTALLATION: ##
1. place script inside a Geo/Node->Right Mouse Button -> Type Properties -> scripts -> OnUpdate (remember to select PYTHON on bottom right dropdown menu)
2. script will add for any preexistent children nodes as comment the headline taken from online documentation

## NOTE: ## 
Some nodes don't have headline or the whole documentation file.

## CONTRIBUTING: ##
Please feel free to optimize the script and add/report missing nodes documentation. 
