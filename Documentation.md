# Documentation

- \_\_main__.py
  - Add Description

## Package file
- [file.py]()
  - load_patients_from_csv(file_name)
  - save_patients_to_csv(file_name, patients, append_patients)
  - save_patients_to_brandon(file_name, patients)

# Package object
- [patient.py]()
  - Patient Class
    - \_\_init__()
    - \_\_str__()
    - initialize_from_csv()
    - initialize_from_server()
    - calculate_age()
    - calculate_bmi()
    - get_brandon_format()
    - get_csv_format()
    - parse_pre_conditions(pre_conditions_string)
    - parse_pre_conditions_from_csv(csv_data)
    
- [precondition.p]()
  - PreCondition Class
    - \_\_init__()
    - \_\_str__()
    - initialize_from_csv(pre_condition_as_string)
    - initialize_from_server(pre_condition_as_string)
    - get_csv_format()
    - get_risk_factor_as_int
 
# Package parser
- [parser.py]()
  - get_param_string(params)
  - parse_patient_data()

