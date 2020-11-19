# git-tools
 
 ## usage :
 
 * run git command on every repository in infrastructure group :
 ```bash
 python execute.py infrastructure git status
 ```
 
 
 ## **important command**
 
 * if you want to commit with message insert single quote between each double quote, example :
 ```bash
 python execute.py infrastructure git commit -m '"'[name] your message'"'
 ```
 
 
 ## **additional**
 
 * command only current branch are shown :
 ```bash
 python execute.py infrastructure git current branch
 ```
 
 
> note: change variable `pathRoot` with your repository group root path 
