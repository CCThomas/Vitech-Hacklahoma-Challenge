from object.precondition import PreCondition


class Patient:
    def __init__(self, json_participant, json_detail, json_quote):
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
            self._version_ = json_participant["_version_"]
        elif "_version_" in json_detail:
            self._version_ = json_detail["_version_"]
        elif "_version_" in json_quote:
            self._version_ = json_quote["_version_"]

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
            self.pre_conditions = []
            for json_pre_condition in json_detail["PRE_CONDITIONS"]:
                self.pre_conditions.append(PreCondition(json_pre_condition))
        if "EMPLOYMENT_STATUS" in json_detail:
            self.employment_status = json_detail["EMPLOYMENT_STATUS"]
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
        if "GOLD" in json_detail:
            self.gold = json_detail["GOLD"]
        if "BRONZE" in json_detail:
            self.bronze = json_detail["BRONZE"]
        if "SILVER" in json_detail:
            self.silver = json_detail["SILVER"]
        if "PLATINUM" in json_detail:
            self.platinum = json_detail["PLATINUM"]
        if "PURCHASED" in json_detail:
            self.purchased = json_detail["PURCHASED"]

    def __str__(self):
        return str(self.id)

    def calculateBMI(self):
        # wight_lb + height_in^2 x 703
        return self.weight + pow(self.height, 2) * 203


