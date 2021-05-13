import requests
import json
import sqlite3

response = requests.get('http://coronavirus-tracker-api.herokuapp.com/v2/locations/133')

# print(response.status_code)
# print(response.headers)
# print(response.text)
result_json = response.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
locat = res['location']
virusData = locat['latest']
countryGe = locat['country']
confirmedGe = virusData["confirmed"]
deathsGe = virusData["deaths"]

# print(f'ქვეყანა: {countryGe}')
# print(f'დადასტურებული: {confirmedGe}')
# print(f'გარდაცვლილი: {deathsGe}')

# ბაზის შექმნა

conn = sqlite3.connect("my_database.sqlite")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE covidata
(id INTEGER PRIMARY KEY AUTOINCREMENT,
country VARCHAR(50),
confirmed INTEGER,
deaths INTEGER);''')

cursor.execute('INSERT INTO coviddata (country, confirmed, deaths) VALUES (?, ?, ?)', (countryGe, confirmedGe, deathsGe))

conn.commit()
conn.close()





