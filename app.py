from flask import Flask, render_template, request
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import libs.db as db

app = Flask(__name__)


def get_avg_age(df):

    """
        Calculates and returns the average age of all the patients in the dataframe, df

        Parameters
        ----------
        df: pd.Dataframe
            Dataframe containing patient information
        
        Returns
        -------
        int
            Average (mean) age of all the patients in the dataframe 
    """
    pass

def get_common_diagnosis(df):

    """
        Returns the most common diagnosis from the list of patients in the dataframe, df

        Parameters
        ----------
        df: pd.DataFrame
            Dataframe containing patient information
        
        Returns
        -------
        str
            The most common diagnosis from all the patients in the dataframe 
    """       
    
    pass

def get_inpatient_info(df):

    """
        Groups the dataframe by patient and returns a dataframe containing aggregated
        information about each patient including their id, age, gender, total number of inpatients spells
        and average length of all their inpatient spells

        Parameters
        ----------
        df: pd.DataFrame
            Dataframe containing patient information
        
        Returns
        -------
        pd.Dataframe
            A dataframe containing the following columns:

            PATIENT_ID: The unique patient ID
            CURRENT_AGE: Patients current age
            GENDER: Patients gender
            SPELL_COUNT: The total number of inpatient spells the patients has had
            AVERAGE_DURATION: The Average (mean) lenght of all their inpatient spells
    """    
    pass


@app.route('/patients', methods=['GET', 'POST'])
def patients():

    # Connect to the SQLite database
    engine = create_engine('sqlite:///database.db')

    # Open and execute the SQL query 
    with open('query.sql') as f:
        sql_query = f.read()

    df = pd.read_sql_query(sql_query, engine)

    # Calculate the average age of patients
    avg_age = get_avg_age(df) 
    inpatient_info = get_inpatient_info(df)
    common_diagnosis = get_common_diagnosis(df)

    # Render the results in a HTML template
    return render_template(
        template_name_or_list='patients.html', 
        avg_age=avg_age, 
        inpatient_info=inpatient_info,
        common_diagnosis=common_diagnosis
    )
 
@app.route('/query', methods=['GET', 'POST'])
def query():
    # Connect to the SQLite database
    engine = create_engine('sqlite:///database.db')

    # Open and execute the SQL query 
    with open('query.sql') as f:
        sql_query = f.read()

    df = pd.read_sql_query(sql_query, engine)

    print(df)

    # Convert the DataFrame to HTML
    table = df.to_html()

    return render_template(
        template_name_or_list='query.html', 
        table=table
    )


if __name__ == "__main__":
    db.setup()
    app.run(debug=True)