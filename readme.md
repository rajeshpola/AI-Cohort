mkdir my-python-project
cd my-python-project

python -m venv venv

.\venv\Scripts\activate

source venv/bin/activate
pip install "fastapi[standard]"
deactivate