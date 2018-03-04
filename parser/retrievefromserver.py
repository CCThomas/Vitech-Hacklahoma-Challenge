from parser.parse import parse_patient_data
from file.file import save_patients_to_csv, load_patients_from_csv
import time
import sys

# Started 8:33:00pm
# 37k at 5:41


# Verify User is Using Python 3+
if sys.version_info < (3, 0):
    print("Python version 3+ required")
    print("Download Python 3: https://www.python.org/downloads/")


my_time = time.time()
patients = parse_patient_data()
save_patients_to_csv("vitech_data.csv", patients, False)
print(time.time() - my_time)