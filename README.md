# **SIMPLE CRUD USING FASTAPI, SQLALCHEMY, POSTGRESQL**

## Setting Up
1. first create a folder and clone.
2. create a python environment using python-venv and install needed libraries.
```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. This project requires specific environment variables to be set up correctly. If you are unsure about the required values or need assistance, please contact the admin.
4. run the app and open in your browser http://localhost:5090/docs to test if all is running.
```shell
uvicorn app:app --reload --port=5090 --host=0.0.0.0
```
