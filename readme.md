mkdir my-python-project
cd my-python-project

python -m venv venv

.\venv\Scripts\activate

source venv/bin/activate
pip install "fastapi[standard]"
deactivate


#Git Comments
1. Initialize a Git Repository (if not already)
Navigate to your project folder (like GenAIpython), and run:

bash
Copy
Edit
cd /f/pythonProject/GenAIpython
git init
#2. Add a .gitignore File
Ensure you ignore unnecessary files (e.g., virtual environments for Python). A typical .gitignore might include:

gitignore
Copy
Edit
__pycache__/
*.py[cod]
venv/
.env
#3. Stage Your Files
bash
Copy
Edit
git add .
#4. Commit Your Changes
bash
Copy
Edit
git commit -m "Initial commit"
#5. Link to the GitHub Repo
If your GitHub repository is named your-repo, run:

bash
Copy
Edit
git remote add origin https://github.com/rajeshpola/your-repo.git
git branch -M main
git push -u origin main

##Merge the code 
Option 1 – Merge GitHub changes into your code (safe)
bash
Copy
Edit
git pull origin main --rebase
git push origin main
This downloads changes from GitHub and puts your commits on top.

Option 2 – Overwrite GitHub with your local code (dangerous — deletes GitHub commits)
bash
Copy
Edit
git push origin main --force
git pull origin main --rebase



# 1️⃣ Fetch remote changes from GitHub
git fetch origin main

# 2️⃣ Rebase your local changes on top of GitHub's changes
git rebase origin/main

# 3️⃣ Push your updated branch to GitHub
git push origin main


git push origin main
