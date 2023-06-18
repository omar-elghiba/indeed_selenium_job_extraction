import csv
from hrflow import Hrflow


hrflow = Hrflow(api_secret='X-API-KEY', user_email='X-USER-EMAIL')


csv_file_path = 'output.csv'

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for data in reader:
        profile_data = {
            "reference": data['reference'],
            "name": data['name'],
            "sections": data['sections'],
            "skills": data['skills'],
            "tags": data['tags']
        }


        response = hrflow.profile.add(source_key='BOARD_KEY', profile_json=profile_data)
        if response['code'] == 201:
            print("added successfully")
        else:
            print(f"Failed to add")

