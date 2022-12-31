import requests
import json


def SymptomCheck(year, symptomnumber, gendermedical):
    token = "oaXBzdGFydCI6IjIwMjItMTItMjgiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTY3MjUzMjc1MywibmJmIjoxNjcyNTI1NTUzfQ.xHYertT_Sc4Wt3tloiRColC0uDZWRrdK66bH6oX60UQ"
    r = requests.get(
        f"https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[{symptomnumber}]&gender={gendermedical}&year_of_birth={year}&token={token}&format=json&language=en-gb"
    )
    response = r.json()
    print(response)
    retStr = f"based on the symptoms you have provided the problem is most likely: {response[0]['Issue']['Name']}."
    retStr+=f" We can say this with {response[0]['Issue']['Accuracy']} percent accuracy."
    retStr+=f" We reccomend you to visit a {response[0]['Specialisation'][0]['Name']} doctor."
    try:
        retStr+= f" another viable doctor would be a {response[0]['Specialisation'][1]['Name']} doctor."
    except IndexError:
        retStr+=" There is no other type of doctor to deal with these symptoms, the previously mentioned doctor is the only one."
    return retStr
