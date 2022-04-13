### The relative path for all of the commands executed in this makefile is the WORKING DIRECTORY ###

main-file = discord_bot.py

run:
	python3 $(main-file)

# make git-init: makes the directory a git repository
git-init:
	git init
# make git-user email="you@email.com" name="username"
git-user:
	git config --global user.email $(email)
	git config --global user.name $(name)
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
	git rm $(file)
# make git-commit msg="Commit\ message": updates the git and the GitHub repositories
git-commit:
	git add -u
	git commit -m $(msg)
	git push -u origin master