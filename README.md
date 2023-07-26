# 8x8 interview

# Introduction
This is an interview consisting of 3 usecases/coding tests:

Usecase 1 - a simple backend API calling MessageBird API written in Python/FastAPI, showcasing logging and test-driven development

Usecase 2 - a full-stack web project consisting of a backend API written in Python/FastAPI and Javascript/React, showcasing containerization using Docker

Usecase 3 - a simple script written in Python

# Installation/Usage

## usecase1

runs a test which runs the post request from the server to the MessageBird API and retrieves the wanted data

```console
cd usecase3
setx MESSAGEBIRD_API_KEY "yQCal4N2rxPhtXCNJ2uVnzt2D" (Windows)
export MESSAGEBIRD_API_KEY="yQCal4N2rxPhtXCNJ2uVnzt2D" (macOs/Linux)
python3 -m venv env 
env\Scripts\activate (Windows)
source env/bin/activate (macOS/Linux)
pip3 install -r requirements.txt
pytest
```

## usecase2

website with the table filled with data from the spreadsheet using Google Sheets API

```console
cd usecase2
docker-compose build
docker-compose up
```

open http://localhost:8080/


## usecase3
creates the joined csv files in the dataset folder

```console
cd usecase3
python3 -m venv env 
env\Scripts\activate (Windows)
source env/bin/activate (macOS/Linux)
pip3 install -r requirements.txt
python3 -m src.merge_csv
```

