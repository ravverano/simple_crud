# **SIMPE CRUD USING FASTAPI, SQLALCHEMY, POSTGRESQL**

## Setting Up
1. first create a folder and clone the main module.
2. create a python environment using python-venv and install needed libraries.
```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. run the app and open in your browser http://localhost:5090/docs to test if all is running.
```shell
uvicorn app:app --reload --port=5090 --host=0.0.0.0
```
