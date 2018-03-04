class PreCondition:

    def __init__(self):
        """PreCondition Constructor"""
        self.condition_name = "null"
        self.icd_code = "null"
        self.risk_factor = "null"

    def __str__(self):
        """
        :return: Return Condition Name
        """
        return self.condition_name

    def initialize_from_csv(self, pre_condition_as_string):
        """
        Initialize Pre Condition Object with Data read from CSV
        :param pre_condition_as_string: Pre Condition Data as String
        """
        data_split = pre_condition_as_string.split("^")
        self.condition_name = data_split[0]
        self.icd_code = data_split[1]
        self.risk_factor = data_split[2]

    def initialize_from_server(self, pre_condition_as_string):
        """
        Initialize Pre Condition Object with Data read from Server
        :param pre_condition_as_string: Pre Condition Data as String
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

    def get_csv_format(self):
        """
        :return: String of PreCondition Formatted for a CSV, similar to how it was read from the Server
        """
        return str(self.condition_name).replace(",", "COMMA") + "^" + str(self.icd_code) + "^" + str(self.risk_factor)

    def get_risk_factor_as_int(self):
        """
        :return: Risk Factor Represented as an Integer
        """
        if self.risk_factor == "Low":
            return "1"
        if self.risk_factor == "Medium":
            return "2"
        if self.risk_factor == "High":
            return "3"


