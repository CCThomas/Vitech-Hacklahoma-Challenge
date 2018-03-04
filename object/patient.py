from object.precondition import PreCondition


class Patient:

    def __init__(self):
        """Constructor"""

    def from_csv(self, csv_data):
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

    def from_server(self, json_participant, json_detail, json_quote):
        # Shared Data
        if "id" in json_participant:
            self.id = json_participant["id"]
        elif "id" in json_detail:
            self.id = json_detail["id"]
        elif "id" in json_quote:
            self.id = json_quote["id"]
        else:
            self.id = "null"

        if "collection_id" in json_participant:
            self.collection_id = json_participant["collection_id"]
        elif "collection_id" in json_detail:
            self.collection_id = json_detail["collection_id"]
        elif "collection_id" in json_quote:
            self.collection_id = json_quote["collection_id"]
        else:
            self.collection_id = "null"

        if "_version_" in json_participant:
            self.version = json_participant["_version_"]
        elif "_version_" in json_detail:
            self.version = json_detail["_version_"]
        elif "_version_" in json_quote:
            self.version = json_quote["_version_"]
        else:
            self.version = "null"

        # Participant Data
        if "city" in json_participant:
            self.city = json_participant["city"]
        else:
            self.city = "null"

        if "DOB" in json_participant:
            self.DOB = json_participant["DOB"]
        else:
            self.DOB = "null"

        if "address" in json_participant:
            self.address = json_participant["address"]
        else:
            self.address = "null"

        if "longitude" in json_participant:
            self.longitude = json_participant["longitude"]
        else:
            self.longitude = "null"

        if "sex" in json_participant:
            self.sex = json_participant["sex"]
        else:
            self.sex = "null"

        if "state" in json_participant:
            self.state = json_participant["state"]
        else:
            self.state = "null"

        if "latitude" in json_participant:
            self.latitude = json_participant["latitude"]
        else:
            self.latitude = "null"

        if "name" in json_participant:
            self.name = json_participant["name"]
        else:
            self.name = "null"

        # Detail Data
        if "EMPLOYMENT_STATUS" in json_detail:
            self.employment_status = json_detail["EMPLOYMENT_STATUS"]
        else:
            self.employment_status = "null"

        if "PRE_CONDITIONS" in json_detail:
            self.pre_conditions = self.parse_pre_conditions(json_detail["PRE_CONDITIONS"])
        else:
            self.pre_conditions = []

        if "PEOPLE_COVERED" in json_detail:
            self.people_covered = json_detail["PEOPLE_COVERED"]
        else:
            self.people_covered = "null"

        if "ANNUAL_INCOME" in json_detail:
            self.annual_income = json_detail["ANNUAL_INCOME"]
        else:
            self.annual_income = "null"

        if "MARITAL_STATUS" in json_detail:
            self.marital_status = json_detail["MARITAL_STATUS"]
        else:
            self.marital_status = "null"

        if "HEIGHT" in json_detail:
            self.height = json_detail["HEIGHT"]
        else:
            self.height = "null"

        if "WEIGHT" in json_detail:
            self.weight = json_detail["WEIGHT"]
        else:
            self.width = "null"

        if "TOBACCO" in json_detail:
            self.tobacco = json_detail["TOBACCO"]
        else:
            self.tobacco = "null"

        # Quote Data
        if "GOLD" in json_quote:
            self.gold = json_quote["GOLD"]
        else:
            self.gold = "null"

        if "BRONZE" in json_quote:
            self.bronze = json_quote["BRONZE"]
        else:
            self.bronze = "null"

        if "SILVER" in json_quote:
            self.silver = json_quote["SILVER"]
        else:
            self.silver = "null"

        if "PLATINUM" in json_quote:
            self.platinum = json_quote["PLATINUM"]
        else:
            self.platinum = "null"

        if "PURCHASED" in json_quote:
            self.purchased = json_quote["PURCHASED"]
        else:
            self.purchased = "null"

    def __str__(self):
        return str(self.id)

    def calculate_age(self):
        from datetime import date
        today = date.today()
        born = {
            "year": int(self.DOB[0:4]),
            "month": int(self.DOB[5:7]),
            "day": int(self.DOB[8:10])
        }
        return today.year - born["year"] - ((today.month, today.day) < (born["month"], born["day"]))

    def calculate_bmi(self):
        # wight_lb + height_in^2 x 703
        return self.weight + pow(self.height, 2) * 203

    def get_csv_format(self):
        return_string = str(self.id) + "," + str(self.collection_id) + "," + str(self.version) + "," + str(self.city) + "," + str(self.DOB) + "," + str(self.address).replace(",", "COMMA") + "," + str(self.longitude) + "," + str(self.sex) + "," + str(self.state) + "," + str(self.latitude) + "," + str(self.name).replace(",", "COMMA") + "," + str(self.employment_status) + ","
        if len(self.pre_conditions) >= 2:
            for i in range(len(self.pre_conditions)-1):
                return_string = return_string + self.pre_conditions[i].get_csv_format() + "&"
            return_string = return_string + self.pre_conditions[len(self.pre_conditions)-1].get_csv_format() + ", " + str(self.people_covered) + ", " + str(self.annual_income) + ", " + str(self.marital_status) + ", " + str(self.height) + ", " + str(self.weight) + ", " + str(self.tobacco) + ", " + str(self.gold) + ", " + str(self.bronze) + ", " + str(self.silver) + ", " + str(self.platinum) + ", " + str(self.purchased) + "\n"
        elif len(self.pre_conditions) == 1:
            return_string = return_string + self.pre_conditions[0].get_csv_format() + ", " + str(self.people_covered) + ", " + str(
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
        pre_conditions_string = pre_conditions_string[2: len(pre_conditions_string)-2]
        pre_conditions_array = pre_conditions_string.split("},{")
        pre_conditions = []
        for pre_condition_data in pre_conditions_array:
            pre_condition = PreCondition()
            pre_condition.from_server(pre_condition_data)
            pre_conditions.append(pre_condition)
        return pre_conditions

    def parse_pre_conditions_from_csv(self, csv_data):
        print(csv_data)
        pre_conditions = []
        for data in csv_data.split("&"):
            pre_condition = PreCondition()
            pre_condition.from_csv(data)
            pre_conditions.append(pre_condition)
        return pre_conditions



