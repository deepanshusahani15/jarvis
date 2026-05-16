# Git & GitHub Commands Cheat Sheet
# Account: deepanshusahani15

# GitHub Profile
https://github.com/deepanshusahani15


# -----------------------------------
# BASIC GIT SETUP
# -----------------------------------

# Check git version
git --version

# Set username
git config --global user.name "Deepanshu Sahani"

# Set email
git config --global user.email "deepanshu.sahani68@gmail.com"

# Check config
git config --list


# -----------------------------------
# INITIALIZE REPOSITORY
# -----------------------------------

# Initialize git
git init

# Clone repository
git clone https://github.com/deepanshusahani15/REPO.git


# -----------------------------------
# GIT STATUS
# -----------------------------------

# Check current status
git status


# -----------------------------------
# STAGING & COMMIT
# -----------------------------------

# Add one file
git add main.py

# Add all files
git add .

# Commit
git commit -m "initial commit"


# -----------------------------------
# REMOTE REPOSITORY
# -----------------------------------

# Add remote
git remote add origin https://github.com/deepanshusahani15/REPO.git

# Check remote
git remote -v

# Remove remote
git remote remove origin

# Change remote URL
git remote set-url origin https://github.com/deepanshusahani15/REPO.git


# -----------------------------------
# PUSH & PULL
# -----------------------------------

# First push
git push -u origin main

# Normal push
git push

# Pull latest changes
git pull


# -----------------------------------
# BRANCHES
# -----------------------------------

# Show branches
git branch

# Create branch
git branch feature1

# Switch branch
git checkout feature1

# Create + switch
git checkout -b feature1

# Rename branch
git branch -M main

# Delete branch
git branch -d feature1


# -----------------------------------
# LOGS & HISTORY
# -----------------------------------

# Commit history
git log

# One-line history
git log --oneline

# Terminal command history
history


# -----------------------------------
# RESET / UNDO
# -----------------------------------

# Unstage file
git reset main.py

# Soft reset last commit
git reset --soft HEAD~1

# Hard reset
git reset --hard HEAD

# Restore file
git restore main.py


# -----------------------------------
# SSH SETUP
# -----------------------------------

# Generate SSH key
ssh-keygen -t ed25519 -C "deepanshu.sahani68@gmail.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key
ssh-add --apple-use-keychain ~/.ssh/deepanshu

# Show loaded keys
ssh-add -l

# Show public key
cat ~/.ssh/deepanshu.pub


# -----------------------------------
# SSH CONFIG
# -----------------------------------

# Open SSH config
nano ~/.ssh/config

# Add this config

Host github-deepanshu
    HostName github.com
    User git
    IdentityFile ~/.ssh/deepanshu
    IdentitiesOnly yes


# -----------------------------------
# TEST SSH
# -----------------------------------

ssh -T git@github-deepanshu


# -----------------------------------
# SSH REMOTE URL
# -----------------------------------

# Set SSH remote
git remote set-url origin git@github-deepanshu:deepanshusahani15/REPO.git


# -----------------------------------
# USEFUL COMMANDS
# -----------------------------------

# Show current branch
git branch --show-current

# Show tracked files
git ls-files

# Show differences
git diff

# Remove file from git
git rm filename.py


# -----------------------------------
# .GITIGNORE
# -----------------------------------

# Create .gitignore
touch .gitignore

# Example .gitignore content

__pycache__/
.env
venv/
node_modules/


# -----------------------------------
# GITHUB TOKEN
# -----------------------------------

# Store credentials
git config --global credential.helper store
