# Git Commands Used in This Project 💻

## Initial Setup
git --version
git config --global user.name "Nisadi Bernard"
git config --global user.email "nisadibernard@gmail.com"

## Creating the Project
mkdir powerbi-project
cd powerbi-project
git init

## Connecting to GitHub
git remote add origin https://github.com/nisadibernard/Powerbi---Project.git
git branch -M main

## Saving and Uploading Files
git add .
git commit -m "Add cleaned Netflix reviews data"
git push -u origin main

## Checking Status
git status
git config --global --list
