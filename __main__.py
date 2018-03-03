from parser.parse import parse_patient_data
import sys

# Verify User is Using Python 3+
if sys.version_info < (3, 0):
    print("Python version 3+ required")
    print("Download Python 3: https://www.python.org/downloads/")


parse_patient_data()
