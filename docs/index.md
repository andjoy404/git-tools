# git-tools
 
 ## usage :
 * run git command on every repository in infrastructure group :
 ```sh
 python execute.py infrastructure git status
 ```
 
 ## **important command**
 * if you want to commit with message insert single quote between each double quote, example :
 ```sh
 python execute.py infrastructure git commit -m '"'[name] your message'"'
 ```
 
 ## **additional**
 * command only current branch are shown :
 ```sh
 python execute.py infrastructure git current branch
 ```
 
 
> note: change variable `pathRoot` with your repository grop root path 
