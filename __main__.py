from parser.parse import parse_patient_data
from file.file import save_patients_to_csv, load_patients_from_csv
import time
import sys

# Verify User is Using Python 3+
if sys.version_info < (3, 0):
    print("Python version 3+ required")
    print("Download Python 3: https://www.python.org/downloads/")


patients = parse_patient_data()
my_time = time.time()
save_patients_to_csv("vitech_data.csv", patients, False)
print(time.time() - my_time)


"""patients_loaded = load_patients_from_csv("vitech_data.csv")
if len(patients) == len(patients_loaded):
    print(patients == patients_loaded)
    for i in range(len(patients)):
        print("Save", patients[i].get_csv_format())
        print("Load", patients_loaded[i].get_csv_format())
else:
    print("Fail")"""