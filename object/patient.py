from object.precondition import PreCondition


class Patient:

    def __init__(self):
        """Patient Constructor"""
        self.purchased = "null"
        self.platinum = "null"
        self.silver = "null"
        self.bronze = "null"
        self.gold = "null"
        self.tobacco = "null"
        self.weight = "null"
        self.height = "null"
        self.marital_status = "null"
        self.annual_income = "null"
        self.people_covered = "null"
        self.pre_conditions = []
        self.employment_status = "null"
        self.name = "null"
        self.state = "null"
        self.latitude = "null"
        self.sex = "null"
        self.longitude = "null"
        self.address = "null"
        self.DOB = "null"
        self.city = "null"
        self.version = "null"
        self.collection_id = "null"
        self.id = "null"

    def __str__(self):
        """
        :return: Return Patient ID as String
        """
        return str(self.id)

    def initialize_from_csv(self, csv_data):
        """
        Initialize Patient Object with Data read from CSV
        :param csv_data:
        """
        for i in range(len(csv_data)):
            if i == 0:
                self.id = csv_data[0]
            elif i == 1:
                self.collection_id = csv_data[1]
            elif i == 2:
                self.version = csv_data[2]
            elif i == 3:
                self.city = csv_data[3]
            elif i == 4:
                self.DOB = csv_data[4]
            elif i == 5:
                self.address = csv_data[5]
            elif i == 6:
                self.longitude = csv_data[6]
            elif i == 7:
                self.sex = csv_data[7]
            elif i == 8:
                self.state = csv_data[8]
            elif i == 9:
                self.latitude = csv_data[9]
            elif i == 10:
                self.name = csv_data[10]
            elif i == 11:
                self.employment_status = csv_data[11]
            elif i == 12:
                if csv_data[12] == "":
                    self.pre_conditions = []
                else:
                    self.pre_conditions = self.parse_pre_conditions_from_csv(csv_data[12])
            elif i == 13:
                self.people_covered = csv_data[13]
            elif i == 14:
                self.annual_income = csv_data[14]
            elif i == 15:
                self.marital_status = csv_data[15]
            elif i == 16:
                self.height = csv_data[16]
            elif i == 17:
                self.weight = csv_data[17]
            elif i == 18:
                self.tobacco = csv_data[18]
            elif i == 19:
                self.gold = csv_data[19]
            elif i == 20:
                self.bronze = csv_data[20]
            elif i == 21:
                self.silver = csv_data[21]
            elif i == 22:
                self.platinum = csv_data[22]
            elif i == 23:
                self.purchased = csv_data[23]

    def initialize_from_server(self, json_participant, json_detail, json_quote):
        """
        Initialize Patient Object with Data read from Server
        :param json_participant: JSON Data retrieved from the Participant url
        :param json_detail: JSON Data retrieved from the Participant Detail url
        :param json_quote: JSON Data retrieved from the Quote url
        """

        # Shared Data
        if "id" in json_participant:
            self.id = json_participant["id"]
        elif "id" in json_detail:
            self.id = json_detail["id"]
        elif "id" in json_quote:
            self.id = json_quote["id"]

        if "collection_id" in json_participant:
            self.collection_id = json_participant["collection_id"]
        elif "collection_id" in json_detail:
            self.collection_id = json_detail["collection_id"]
        elif "collection_id" in json_quote:
            self.collection_id = json_quote["collection_id"]

        if "_version_" in json_participant:
            self.version = json_participant["_version_"]
        elif "_version_" in json_detail:
            self.version = json_detail["_version_"]
        elif "_version_" in json_quote:
            self.version = json_quote["_version_"]

        # Participant Data
        if "city" in json_participant:
            self.city = json_participant["city"]
        if "DOB" in json_participant:
            self.DOB = json_participant["DOB"]
        if "address" in json_participant:
            self.address = json_participant["address"]
        if "longitude" in json_participant:
            self.longitude = json_participant["longitude"]
        if "sex" in json_participant:
            self.sex = json_participant["sex"]
        if "state" in json_participant:
            self.state = json_participant["state"]
        if "latitude" in json_participant:
            self.latitude = json_participant["latitude"]
        if "name" in json_participant:
            self.name = json_participant["name"]

        # Detail Data
        if "EMPLOYMENT_STATUS" in json_detail:
            self.employment_status = json_detail["EMPLOYMENT_STATUS"]
        if "PRE_CONDITIONS" in json_detail:
            self.pre_conditions = self.parse_pre_conditions(json_detail["PRE_CONDITIONS"])
        if "PEOPLE_COVERED" in json_detail:
            self.people_covered = json_detail["PEOPLE_COVERED"]
        if "ANNUAL_INCOME" in json_detail:
            self.annual_income = json_detail["ANNUAL_INCOME"]
        if "MARITAL_STATUS" in json_detail:
            self.marital_status = json_detail["MARITAL_STATUS"]
        if "HEIGHT" in json_detail:
            self.height = json_detail["HEIGHT"]
        if "WEIGHT" in json_detail:
            self.weight = json_detail["WEIGHT"]
        if "TOBACCO" in json_detail:
            self.tobacco = json_detail["TOBACCO"]

        # Quote Data
        if "GOLD" in json_quote:
            self.gold = json_quote["GOLD"]
        if "BRONZE" in json_quote:
            self.bronze = json_quote["BRONZE"]
        if "SILVER" in json_quote:
            self.silver = json_quote["SILVER"]
        if "PLATINUM" in json_quote:
            self.platinum = json_quote["PLATINUM"]
        if "PURCHASED" in json_quote:
            self.purchased = json_quote["PURCHASED"]

    def calculate_age(self):
        """
        :return: Calculated Age from Patient's DOB
        """
        from datetime import date
        today = date.today()
        born = {
            "year": int(self.DOB[0:4]),
            "month": int(self.DOB[5:7]),
            "day": int(self.DOB[8:10])
        }
        return today.year - born["year"] - ((today.month, today.day) < (born["month"], born["day"]))

    def calculate_bmi(self):
        """
        Formula: (weight_lb / height_in^2) x 703
        :return: Calculated BMI of Patient
        """
        return (float(self.weight) / pow((float(self.height)), 2)) * 703

    def get_brandon_format(self):
        """
        Similar to get_csv_format, except formatted all strings to integers for Brandon Wong (https://github.com/BW0ng)

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
        :return: String to be printed to a CSV File
        """

        return_string = str(self.id) + "," + str(self.calculate_age()) + ","
        if self.sex == "M":
            return_string = return_string + "1,"
        else:
            return_string = return_string + "0,"

        if self.employment_status == "Employed":
            return_string = return_string + "1,"
        else:
            return_string = return_string + "0,"

        if len(self.pre_conditions) == 0:
            for i in range(10):
                return_string = return_string + "0,"
        else:
            for pre_condition in self.pre_conditions:
                return_string = return_string + pre_condition.get_risk_factor_as_int() + ","

        return_string = return_string + str(self.people_covered) + "," + str(self.annual_income) + ","

        if self.employment_status == "M":
            return_string = return_string + "1,"
        else:
            return_string = return_string + "0,"

        return_string = return_string + str(self.calculate_bmi()) + ","

        if self.employment_status == "Yes":
            return_string = return_string + "1,"
        else:
            return_string = return_string + "0,"

        return_string = return_string + str(self.bronze) + "," + str(self.silver) + "," + str(self.gold) + "," \
                        + str(self.platinum) + ","

        if "Bronze" in self.purchased:
            return_string = return_string + "0"
        elif "Silver" in self.purchased:
            return_string = return_string + "1"
        elif "Gold" in self.purchased:
            return_string = return_string + "2"
        elif "Platinum" in self.purchased:
            return_string = return_string + "3"

        return return_string + "\n"

    def get_csv_format(self):
        """
        :return: String of Patient Data Formatted for a CSV, similar to how it was read from the Server
        """
        return_string = str(self.id) + "," + str(self.collection_id) + "," + str(self.version) + "," + str(self.city) \
                        + "," + str(self.DOB) + "," + str(self.address).replace(",", "COMMA") + "," \
                        + str(self.longitude) + "," + str(self.sex) + "," + str(self.state) + "," + str(self.latitude) \
                        + "," + str(self.name).replace(",", "COMMA") + "," + str(self.employment_status) + ", "
        if len(self.pre_conditions) >= 2:
            for i in range(len(self.pre_conditions)-1):
                return_string = return_string + self.pre_conditions[i].get_csv_format() + "&"
            return_string = return_string + self.pre_conditions[len(self.pre_conditions)-1].get_csv_format() + ", " \
                            + str(self.people_covered) + ", " + str(self.annual_income) + ", " \
                            + str(self.marital_status) + ", " + str(self.height) + ", " + str(self.weight) + ", " \
                            + str(self.tobacco) + ", " + str(self.gold) + ", " + str(self.bronze) + ", " \
                            + str(self.silver) + ", " + str(self.platinum) + ", " + str(self.purchased) + "\n"
        elif len(self.pre_conditions) == 1:
            return_string = return_string + self.pre_conditions[0].get_csv_format() + ", " + str(self.people_covered) \
                            + ", " + str(
                self.annual_income) + ", " + str(self.marital_status) + ", " + str(self.height) + ", " + str(
                self.weight) + ", " + str(self.tobacco) + ", " + str(self.gold) + ", " + str(self.bronze) + ", " + str(
                self.silver) + ", " + str(self.platinum) + ", " + str(self.purchased) + "\n"
        else:
            return_string = return_string + ", " + str(
                self.people_covered) + ", " + str(
                self.annual_income) + ", " + str(self.marital_status) + ", " + str(self.height) + ", " + str(
                self.weight) + ", " + str(self.tobacco) + ", " + str(self.gold) + ", " + str(self.bronze) + ", " + str(
                self.silver) + ", " + str(self.platinum) + ", " + str(self.purchased) + "\n"

        return return_string

    def parse_pre_conditions(self, pre_conditions_string):
        """
        Parse Pre Conditions Data into a list of PreCondition Objects
        :param pre_conditions_string: Pre Conditions Data as a String
        :return: list of PreCondition Objects
        """
        pre_conditions_string = pre_conditions_string[2: len(pre_conditions_string)-2]
        pre_conditions_array = pre_conditions_string.split("},{")
        pre_conditions = []
        for pre_condition_data in pre_conditions_array:
            pre_condition = PreCondition()
            pre_condition.initialize_from_server(pre_condition_data)
            pre_conditions.append(pre_condition)
        return pre_conditions

    def parse_pre_conditions_from_csv(self, csv_data):
        """
        Parse Pre Conditions Data from CSV File, into a list of PreCondition Objects
        :param csv_data: Pre Conditions Data from a CSV File
        :return: list of PreCondition Objects
        """
        pre_conditions = []
        for data in csv_data.split("&"):
            pre_condition = PreCondition()
            pre_condition.initialize_from_csv(data)
            pre_conditions.append(pre_condition)
        return pre_conditions
