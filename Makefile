### The relative path for all of the commands executed in this makefile is the WORKING DIRECTORY ###

# make run: runs the executable file created by the function build
run:
	python3 discord_bot.py

# make git-init: makes the directory a git repository
git-init:
	git init
# make git-connect url="https://github.com/user/repo.git": connects the git repository to the GitHub one
git-connect:
	git remote add origin $(url)
	git branch -M master
# make git-disconnect: disconnects GitHub from the git repository
git-disconnect:
	git remote rm origin
# make git-status: shows the files that are syncronised with the git repository, the ones that had been modified and the untracked ones
git-status:
	git status
# make git-add file="code.cpp": adds files to the git repository
git-add:
	git add $(file)
# make git-rm file="code.cpp": removes files from the git repository
git-rm:
	git rm $(file) --cached
# make git-commit msg="Commit\ message": updates the git repository
git-commit:
	git add -u
	git commit -m $(msg)

# make git-push: updates the GitHub repository
git-push:
	git push -u origin master
