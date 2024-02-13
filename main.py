import subprocess
import time
import requests
import json

# Define the index
index = {
    1: "Bon (Bleu)",
    2: "Moyen (Vert)",
    3: "Dégradé (Jaune)",
    4: "Mauvais (Orange)",
    5: "Très mauvais (Rouge)",
    6: "Extrêmement mauvais (Violet)"
}

url = 'https://api.naonair.org/geoserver/aireel/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=aireel%3Apoi_data&outputFormat=application%2Fjson'

response = requests.get(url)

if response.status_code == 200:
    resultData = response.json()

    data = [feature for feature in resultData['features'] if feature['properties']['poi_id'] == 216]

    for elt in data:
        indice_value = elt['properties']['indice']
        indice_string = index.get(indice_value, 'Unknown')

    valueToDisplay = data[0]['properties']['indice']

    print(data[0]['properties']['lieu'])
    print(data[0]['properties']['adresse'])
    print('\n')
    print(str(valueToDisplay))

    command = f"sudo /home/airpdl/rpi_ws281x/test --color {valueToDisplay}"
    process = subprocess.Popen(command, shell=True)
    time.sleep(10)
    process.terminate()

else:
    print("Failed to fetch data. Status code:", response.status_code)
