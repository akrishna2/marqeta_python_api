# Marqeta API Automation

### Installation of Project
##(One time process only while setting up project to run automation scripts)
- Checkout this project as `git clone https://github.com/akrishna2/marqeta_python_api.git`
- Go to the project `cd "Path to Project"`
- Create a local virtual environment using `python -m venv venv`.
- Activate virtual environment using `venv\Scripts\activate`
- `pip install -U pip setuptools`
- `pip install -r requirements.txt`

### Installation of allure
- (One time process only while setting up system to run automation scripts)
- Install allure to system following these steps : [allure setup]("https://docs.qameta.io/allure/)

### Execution

## User needs to active virtual environment before executing the scripts :
- `venv\Scripts\activate`

### To run test:
- `pytest -s --alluredir results`

