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
        patient.from_csv(line.split(","))
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

    # File Format
    00: ID as Integer
    01: calculate_age() -> Returns age based on DOB
    02: sex as Integer -> 0: Female, 1: Male
    03: Employment Status as Integer -> 0: False, 1: True
    04-14: List of pre_condition's Risk Factor
        - 0: equals null
        - 1: low
        - 2: medium
        - 3: high
    15: People Covered as Integer
    16: Annual Income as Integer
    17: Marital Status as Integer -> 0: False, 1: True
    18: calculate_bmi() -> returns BMI based on width & height
    19: tobacco as integer -> 0: No, 1: Yes
    20: Bronze as Integer
    21: Silver as Integer
    22: Gold as Integer
    23: Platinum as Integer
    24: Purchased as Integer
        - 0: Bronze
        - 1: Silver
        - 2: Gold
        - 3: Platinum

    :param file_name: Name of File to Save to
    :param patients: List of Patients Objects to write to file
    """
    csv_file = open("resources/" + file_name, "w")

    for patient in patients:
        csv_file.write(patient.get_brandon_format())

    csv_file.close()
