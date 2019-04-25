# Foundations in Digital Development (for the Cloud)

Course Repository Version 1.0.0

## Introduction
The is the course reference material. It includes:
1. The course slide-deck presented on the day, with helpful references.
2. Example files that may be useful in completing the course activities.

## Recommended pre-requisites
* Install "Git": https://git-scm.com/downloads
* Install "Python 3": https://www.python.org/downloads/
* Install "Atom Text Editor": https://atom.io
* Install "Putty": https://www.putty.org/
* Sign-up to "Github": https://github.com/
* Set-up Python language support for `Atom`: https://atom.io/packages/ide-python
* Set-up HTML language support for `Atom`: https://atom.io/packages/ide-html
* Set-up Jupyter Notebook file support for `Atom`: https://atom.io/packages/jupyter-notebook

## Clone this repository and checkout master branch
```
git clone https://github.com/ArupAus/digital-foundations-cloud.git
git checkout master
```

## Activate a virtual environment and install project dependencies
```
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

## Print "Hello, world!" and time.now
```
python
do = printer.Printer()
do.hello_world()
do.time_now()
```

## Edit "my-first-page.html" and view on localhost
Open "my-first-page.html" in suitable text editor and edit text content with ``<body/>`` tag.

## Use "my-first-request.ipynb" to make an API request and work with response payload_raw
```
jupyter notebook
```
Navigate to "my-first-request.ipnyb" and run all cells.

## Run the Flask web application
```
cd ./app
python plotter.py
```
View using web browser using link displayed in terminal
