import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

from sympy import content

api_key = 'tzGnnTKCTOuA'
Project_token = 't5ochWXK3uDe'
run_token = 'tTFkxM9nUD1B'


class responce:
    def __init__ (self , api_key , project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key" : self.api_key
        }
        self.get_data()

    def get_data (self):
        responce = requests.get(f'https://www.parsehub.com/api/v2/projects/{Project_token}/last_ready_run/data' , params={"api_key" : api_key })

        self.data = json.loads(responce.text)
    
    def total_cases (self):
        Total = self.data['selection1']
        for i in Total:
            if i["name"] == 'Coronavirus Cases:':
                return i['Number']
        return 0
    def total_death (self):
        Total = self.data['selection1']
        for i in Total:
            if i["name"] == 'Deaths:':
                return i['Number']
        return 0
    def total_recovered (self):
        Total = self.data['selection1']
        for i in Total:
            if i["name"] == 'Recovered:':
                return i['Number']
        return 0
    def country (self, country):
        Total = self.data["Table"]
        for i in Total:
            if i['name'].lower() == country.lower():
                return ("Country name : "+i['name']+' Total Cases : '+i['cases']+' Deaths  : '+i['Deaths']+' Recovered  : '+i['Recovered']+' Tests  : '+i['Tests']+' Population  : '+i['Population'])
        return 0
    def Total_csv(self):
        list = []
        for i in self.data['selection1']:
            list.append(i)
        df = pd.DataFrame(list)
        return df
    def Country_cases_csv(self):
        list = []
        for i in self.data['Table']:
            list.append(i)
        df  = pd.DataFrame(list)
        return df
    def country_list(self):
        list = []
        for i in self.data['Table']:
            list.append(i["name"].lower())
        return list


data = responce(api_key,Project_token)

## To save the file to csv
data.Country_cases_csv().to_csv("country.csv" , index = False)
data.Total_csv().to_csv("Total_cases.csv" , index = False)

## To dry check every data manually
while (1) :
    n  = input("Enter the data You want to view : ")
    n = n.lower()
    if n == 'total cases' :
        print('Covid Cases : ', data.total_cases())
    elif n == 'total deaths' :
        print('Covid Cases : ', data.total_death())
    elif n == 'recovered' :
        print('Covid Cases : ', data.total_recovered())
    elif n in data.country_list():
        print(data.country(n))
    else:
        print("Error")
    x = (input("Do you want to continue : Y/N ")).lower()
    if x == 'y':
        continue
    else:
        break






