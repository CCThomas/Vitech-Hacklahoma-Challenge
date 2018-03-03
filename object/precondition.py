class PreCondition:
    def __init__(self, json_pre_condition):
        if "condition_name" in json_pre_condition:
            self.condition_name = json_pre_condition["condition_name"]
        if "ICD_CODE" in json_pre_condition:
            self.icd_code = json_pre_condition["ICD_CODE"]
        if "Risk_factor" in json_pre_condition:
            self.risk_factor = json_pre_condition["Risk_factor"]

    def __str__(self):
        return self.condition_name




