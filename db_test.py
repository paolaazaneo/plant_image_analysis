import psycopg2
import pandas as pd

#AZRYE001
def connect_to_db():
    try:
        connection = psycopg2.connect(
            database="plantimages",
            user="plant_images",
            password="azaneoweedcontrol",
            host="experimentalplantdata.chdr5c3vfqt2.ap-southeast-2.rds.amazonaws.com",
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Error while connecting to the database: {error}")
        return None

def fetch_trial_data(trial_id, connection):
    try:
        query = f"SELECT * FROM trial_images WHERE trial_id = {trial_id};"
        data = pd.read_sql_query(query, connection)
        return data
    except Exception as error:
        print(f"Error while fetching data: {error}")
        return 

def save_data_to_csv(data, filename):
    try:
        data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as error:
        print(f"Error while saving data: {error}")

def main():
    trial_id = input("Enter the trial ID: ")
    connection = connect_to_db()

    if connection:
        data = fetch_trial_data(trial_id, connection)
        if data is not None:
            filename = f"trial_data_{trial_id}.csv"
            save_data_to_csv(data, filename)

        connection.close()

if __name__ == "__main__":
    main()