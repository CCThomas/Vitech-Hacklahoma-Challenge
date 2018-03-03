from object.patient import Patient
import requests


def parse_patient_data():
    # https://v3v10.vitechinc.com/solr/v_us_participant/select?indent=on&q=*:*&wt=json
    url_participant = "https://v3v10.vitechinc.com/solr/v_us_participant/select"
    url_detail = "https://v3v10.vitechinc.com/solr/v_us_participant_detail/select"
    url_quote = "https://v3v10.vitechinc.com/solr/v_us_quotes/select"
    params = {"indent": "on", "q": "*:*", "wt": "json"}

    # sending get request and saving the response as response object
    my_request = requests.get(url=url_participant, params=params)

    # extracting data in json format
    data_participants = my_request.json()

    # Get Number of Rows
    # Note: Following lines of code commented out, as not to request the 1482000 patient data.
    # rows = data["response"]["numFound"]
    # params["rows"] = rows

    patients = []
    for data_participant in data_participants["response"]["docs"]:
        print("parsing...", data_participant)

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
        patients.append(Patient(data_participant, data_detail["response"]["docs"][0], data_quote["response"]["docs"][0]))
