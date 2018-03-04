# Documentation

- \_\_main__.py
  - Add Description

## Package file
- file.py
  - def load_patients_from_csv(file_name)
    - Description
      - Loads Patient Data from File
    - Param
      - file_name: Name of File to Load From
    - Return
      - a List of Patient Objects
  - def save_patients_to_csv(file_name, patients, append_patients)
    - Description
      - Save Patient Objects to CSV File in the same format read from the Server
    - Param
      - file_name: Name of File to save to
      - patients: List of Patient Objects
      - append_patients: Boolean Value of whether to Append Patient Data or Rewrite File
  - def save_patients_to_brandon(file_name, patients)
    - Description
      - Save Patient Objects to CSV File in a Format for Brandon Wong to Easily Read
    - Param
      - file_name: Name of File to save to
      - patients: List of Patient Objects

# Package object
- patient.py
  - Patient Class
    - \_\_init__(json)
      - Constructor for Patient Class
      - Parses JOSN data 
    - calculateBMI()
      - BMI = weight_kg + height_meters^2 = wight_lb + height_in^2 x 703
 
# Package parser
- parser.py
  - parse_patient_data(data)

