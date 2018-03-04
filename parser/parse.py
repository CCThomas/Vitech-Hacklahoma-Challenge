from object.patient import Patient
from file.file import save_patients_to_csv
import requests


def parse_patient_data():
    # https://v3v10.vitechinc.com/solr/v_us_participant/select?indent=on&q=*:*&wt=json
    url_participant = "https://v3v10.vitechinc.com/solr/v_us_participant/select"
    url_detail = "https://v3v10.vitechinc.com/solr/v_us_participant_detail/select"
    url_quote = "https://v3v10.vitechinc.com/solr/v_us_quotes/select"
    params = {"indent": "on", "q": "*:*", "wt": "json"}

    patients = []
    times = 1
    for id in range(1, 45000):
        if id % 100 == 0:
            print("Saving to vitech_data_temp.csv")
            save_patients_to_csv("vitech_data_temp.csv", patients, True)
        print("Parsing", times, "out of 45000")
        times = times + 1
        params["q"] = "id:" + str(id)

        # sending get request and saving the response as response object
        my_request = requests.get(url=url_participant, params=params)

        # extracting data in json format
        data_participants = my_request.json()

        for data_participant in data_participants["response"]["docs"]:

            # Get Patient ID
            patient_id = data_participant["id"]
            params["q"] = "id:" + str(patient_id)

            # Get Detail data
            my_request = requests.get(url=url_detail, params=params)
            data_detail = my_request.json()

            # Get Quote Data
            my_request = requests.get(url=url_quote, params=params)
            data_quote = my_request.json()

            # Create Patient Object
            patient = Patient()
            patient.from_server(data_participant, data_detail["response"]["docs"][0], data_quote["response"]["docs"][0])
            patients.append(patient)

    return patients
