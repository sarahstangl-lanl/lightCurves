1. Make changes to your files

2. git add <your single file> OR
2. git add <your directory> OR
2. git add <nothing here -- it'll add everything new below here>

### now that you told GIT what files you care about, you need to commit them
### to your local STAGING area (not github.com, but local)
### and if you don't specify -am "comment" it'll prompt you, but I like -am "comment"
3. git commit -am "some comment for this local commit in double-quotes"

### now we want to PUSH our changes from our STAGING area to github
### use your ss@umn.edu as your username, and then your password
4. git push

### IF you have a list of files you don't EVER want "git add" to pick up
### like *.xxx or *.temp or *.crap, then we'll need to create a .gitignore file
### right at the top, and put lines in it like:
*.xxx
*.crap
