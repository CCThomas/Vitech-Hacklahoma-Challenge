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
