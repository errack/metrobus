# Demo Metrobus

_This repo is to test the API of Open CDMX data

## Getting Started :rocket:

_This intructions will help you to prepare a dev enviroment in your **local host**._

### Pre-requisites :clipboard:

**Python 3.6** [link](https://www.python.org/downloads/)

_IDE with support for python:_

* Visual Studio Code
* Atom
* Anaconda

### Installing :wrench:

_Enable a python virtual enviroment and install dependencies:_
_Important to use the **requirements-test.txt** file which includes dependencies to run tests_
```shellscript
python -m venv dev_env --clear
source ./dev_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
For windows:
```shellscript
python -m venv dev_env --clear
dev_env\Scripts\activate.bat
pip install -r requirements.txt
```

## Running the tests :computer:

_Execute all unit tests **locally** with the following command:_

```shellscript
nosetests tests
```
_Arguemnts for testing are not longer needed since the addition of the setup.cfg file, which contains all nose configurations_

_This command will run all unit tests and create an HTML report with test results and an HTML coverage report in the following **local** paths:_

```shellscript
test-report.html
coverage-report/index.html
```

## Running the application :runner:

_Execute the application with the following commands:_

```shellscript
source ./dev_env/bin/activate
python /bin/api_demo.py
```
For windows:
```shellscript
dev_env\Scripts\activate.bat
python /bin/api_demo.py
```

## Execute we servie :earth_americas:

_Get information of vehicle y id, <vehicle_d> it must be replacer by the param value_

localhost:5000/findMetrobus/vehicleId/<vehicle_id>


_Get information of all vehicles in to a mayoralty, <alcaldia> it must be replacer by the param value_

localhost:5000//findMetrobusByAlcaldia/alcaldia/<alcaldia>
