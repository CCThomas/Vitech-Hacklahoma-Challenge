from object.patient import Patient


def load_patients_from_csv(file_name):
    """
    Load Patient Data from CSV
    :param file_name: Name of File to Load From
    :return: List if Patient Objects
    """
    patients = []

    csv_file = open("resources/" + file_name, "r")
    for line in csv_file.readlines():
        patient = Patient()
        patient.initialize_from_csv(line.split(","))
        patients.append(patient)

    csv_file.close()

    return patients


def save_patients_to_csv(file_name, patients, append_patients):
    """
    Save Patient Objects to CSV
    :param file_name: Name of File to Save to
    :param patients: List of Patients Objects to write to file
    :param append_patients: If True, Append to existing file, else create new file.
    """
    if append_patients:
        csv_file = open("resources/" + file_name, "a")
    else:
        csv_file = open("resources/" + file_name, "w")

    for patient in patients:
        csv_file.write(patient.get_csv_format())

    csv_file.close()


def save_patients_to_brandon(file_name, patients):
    """
    Save Patient Objects to CSV
    :param file_name: Name of File to Save to
    :param patients: List of Patients Objects to write to file
    """
    csv_file = open("resources/" + file_name, "w")

    for patient in patients:
        csv_file.write(patient.get_brandon_format())

    csv_file.close()
