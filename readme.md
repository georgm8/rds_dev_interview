# General Instructions

- Clone this repository
- Complete the **three** exercises outlined in the 'Exercises' section below
- Push your code to a new repository under your Github account
  - Make sure to set your repository to Private
  - Add georgm8 as a Collaborator in your repository settings
- When pushing to your own repository please do not include any virtual environment folders or files (feel free to use a .gitignore for this)
- Do not push to this repository under main or any other branch

# Enivronment Setup Instructions

You can use the following instructions to create a virtual environment and install the required dependencies. However you may prefer to use your own environment manager (for example condas). The list of dependencies are specified in the `requirements.txt` file.

## Windows
```console
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Linux
```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The Flask app can then be run with the following command:

```console
flask run
```

If you have problems running the app using the above command you can also try the following:

```console
python app.py
```
# Exercises

The app should be running at accessible via the url localhost:5000/patients. You will encounter an error when you first load this page, this is to be expected! Completion of the following exercises will enable the app to run correcly.

## 1. SQL Task

Open the `query.sql` file and write a SQL script that brings in the following information about each patients' inpatient spell. Make sure to only include patients that are not deceased:

- Patient ID
- Patients Gender
- Patients Current Age
- Admission Date
- Discharge Date
- Diagnosis
- Diagnosis Code

The database is a SQLlite database contained within the `database.db` file in the projects root directory.
You can view the database schema in the `database_schema.pdf` file. Note that the data within the `database_schema.pdf` file is not the same as the data contained within the database.

NB - You can navigate to localhost:5000/query to see the results of your query as you are constructing it.


## Python Task

Open the `app.py` file. You will see that the `def patients()` function calls three other functions that are currently not implemented. Your task is to implement those functions:

- `def get_avg_age()`
- `def get_common_diagnosis()`
- `def get_inpatient_info()`

## Javascript Task

There is a dropdown selection menu to filter the patients displayed on the screen by gender. Please complete the javascript code so that the filter works correctly. I.e. if you select 'Female' from the dropdown option only Female patients should be displayed on the screen.
