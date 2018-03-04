from file.file import save_patients_to_csv
from object.patient import Patient
import urllib.request
import json


def get_param_string(params):
    """
    Turn Param Dict into to String to be tacked onto a URL
    :param params: Dictionary of Parameters.
    :return: String to be tacked onto a URL
    """
    return_string = "?"
    for param in params:
        return_string = return_string + param + "=" + params[param] + "&"
    return return_string


def parse_patient_data():
    """
    - Parse Patient Data from vitech URLs into a list of Patient Objects
    :return: List of Patient Objects
    """
    url_participant = "https://v3v10.vitechinc.com/solr/v_us_participant/select"
    url_detail = "https://v3v10.vitechinc.com/solr/v_us_participant_detail/select"
    url_quote = "https://v3v10.vitechinc.com/solr/v_us_quotes/select"
    params = {"indent": "on", "q": "*:*", "wt": "json"}

    patients = []
    number_of_patients_parsed = 1
    number_of_patients_to_parsed = 45000
    for patient_id in range(45000, 45000 + number_of_patients_to_parsed):
        if patient_id % 100 == 0:
            print("Saving to vitech_data_temp.csv")
            save_patients_to_csv("vitech_data_temp.csv", patients, True)
        print("Parsing", number_of_patients_parsed, "out of", number_of_patients_to_parsed)
        number_of_patients_parsed = number_of_patients_parsed + 1

        # Set param for query to get Patient ID for current iteration
        params["q"] = "id:" + str(patient_id)

        # sending get request and saving the response as response object
        # my_request = requests.get(url=url_participant, params=params)
        my_request = urllib.request.urlopen(url_participant + get_param_string(params))

        # extracting data in json format
        # data_participants = my_request.json()
        data_participants = json.loads(my_request.read())

        for data_participant in data_participants["response"]["docs"]:
            # Get Detail data
            # my_request = requests.get(url=url_detail, params=params)
            my_request = urllib.request.urlopen(url_detail + get_param_string(params))
            data_detail = json.loads(my_request.read())

            # Get Quote Data
            # my_request = requests.get(url=url_quote, params=params)
            my_request = urllib.request.urlopen(url_quote + get_param_string(params))
            data_quote = json.loads(my_request.read())

            # Create Patient Object
            patient = Patient()
            patient.initialize_from_server(data_participant, data_detail["response"]["docs"][0], data_quote["response"]["docs"][0])
            patients.append(patient)

    return patients
