from object.patient import Patient


def load_patients_from_csv(file_name):
    patients = []

    csv_file = open("resources/" + file_name, "r")
    for line in csv_file.readlines():
        patient = Patient()
        patient.from_csv(line.split(","))
        patients.append(patient)

    csv_file.close()

    return patients


def save_patients_to_csv(file_name, patients, append_patients):
    csv_file = None
    if append_patients:
        csv_file = open("resources/" + file_name, "a")
    else:
        csv_file = open("resources/" + file_name, "w")

    for patient in patients:
        csv_file.write(patient.get_csv_format())

    csv_file.close()


def save_patients_to_brandon(file_name, patients):
    """
    ID as Integer
    calculate_age
    sex as boolean. 0 or 1.
    Emplyement Status as Boolean. 0 or 1
    List of pre_conditions
    - 0 equals null
    - 1: low
    - 2: medium
    - 3: high
    People Covered as Integer
    Annual income as Integer
    Marrital Status as Bool
    BMI
    tabacco
    gold
    bronze
    platinum
    silver
    purchased
    - 0 through 3

    :return:
    """
    csv_file = open("resources/" + file_name, "w")

    for patient in patients:
        csv_file.write(patient.get_brandon_format())

    csv_file.close()
