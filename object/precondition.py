class PreCondition:

    def init(self):
        """Constructor"""

    def from_csv(self, pre_condition_as_string):
        data_split = pre_condition_as_string.split("^")
        self.condition_name = data_split[0]
        self.icd_code = data_split[1]
        self.risk_factor = data_split[2]

    def from_server(self, pre_condition_as_string):
        """
        '"condition_name":"Unspecified fracture of specified metacarpal bone with unspecified laterality","ICD_CODE":"S62.308","Risk_factor":"Low"'
        :param pre_condition_as_string:
        """
        pre_condition_split = pre_condition_as_string.split("\",\"")
        for pre_condition_data in pre_condition_split:
            key = pre_condition_data.split(":")[0].replace("\"", "")
            val = pre_condition_data.split(":")[1].replace("\"", "")

            if key == "condition_name":
                self.condition_name = val
            if key == "ICD_CODE":
                self.icd_code = val
            if key == "Risk_factor":
                self.risk_factor = val

    def __str__(self):
        return self.condition_name

    def get_csv_format(self):
        return str(self.condition_name).replace(",", "COMMA") + "^" + str(self.icd_code) + "^" + str(self.risk_factor)


