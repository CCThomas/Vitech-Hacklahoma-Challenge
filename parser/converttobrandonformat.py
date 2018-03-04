from file.file import save_patients_to_brandon, load_patients_from_csv
import sys

# Started 8:33:00pm

# Verify User is Using Python 3+
if sys.version_info < (3, 0):
    print("Python version 3+ required")
    print("Download Python 3: https://www.python.org/downloads/")
    sys.exit(0)

import time
my_time = time.time()
patients = load_patients_from_csv("vitech_data_temp.csv")
save_patients_to_brandon("vitech_data_brandon.csv", patients)
print(time.time() - my_time)
