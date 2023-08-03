# Setup Instructions

Once you have cloned the repo setup a virtual environment and install the dependencies within `requirements.txt`

## Windows
```console
python3 -m venv venv
myenv\Scripts\activate
pip install requirements.txt
```

## Linux
```console
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```

The Flask app can then be run with the following command:

```console
flask run
```

If you have problems running the app using the above command you can also try the following:

```console
python app.py
```


# Questions

## SQL Task

Open `query.sql` and write a SQL script that brings in the following information about each patients' spell. Make sure to only include patients that are not deceased:

- Patient ID
- Patients Gender
- Patients Current Age
- Admission Date
- Discharge Date
- Diagnosis
- Diagnosis Code


## Python Task

Open `app.py`. The `def patients()` function calls three other functions that are currently not implemented. Your task is to implement those functions:

`def get_avg_age()`
`def get_common_diagnosis()`
`def get_inpatient_info()`

## Javascript Task

There is a dropdown selection menu to filter the patients displayed on the screen by gender. Please complete the javascript code so that the filter works correctly. I.e. if you select 'Female' from the dropdown option only Female patients should be displayed on the screen.