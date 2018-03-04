import random
for x in range(6000):
    num = ""
    for y in range(19):
        if y != 0:
            num = num + ", " + str(random.randint(0, 4))
        else:
            num += str(random.randint(0, 4))

    for y in range(5):
            num = num + ", " + str(random.randrange(20, 70))

    print(num)

'''
conditions = {}

amount = 1000

for i in range(1, 45000, amount):
    print(i)
    url = ('https://v3v10.vitechinc.com/solr/v_us_participant_detail/select?indent=on&wt=json&q=id:[{0}%20TO%20{1}]&rows={2}').format(i, (i+amount), amount)

    response = urllib.request.urlopen(url)
    response = json.loads(response.read())["response"]["docs"]
    for j in range(amount):
        blah = response[j]
        preconditions = blah.get("PRE_CONDITIONS")
        if preconditions is None:
            if(conditions.get("None") is None):
                conditions["None"] = 1
            else:
                conditions["None"] = conditions.get("None")+1
        else:
            preconditions = preconditions[2:len(preconditions)-2]
            precondition_array = preconditions.split("},{")
            for precondition in precondition_array:
                condition = precondition.replace("\",\"", ":").replace("\":\"", ":").split(':')[3]

                if (conditions.get(condition)) is None:
                    conditions[condition] = 1
                else:
                    conditions[condition] = conditions.get(condition)+1

print(conditions)
print()
'''
