import requests
import json

Email = []
for i in range(37):
    url = f"http://shop.bancocn.com/rest/products/{i}/reviews"
    json_data = requests.get(url)
    response = json_data.text
    dicit  = json.loads(response)
    lista = dicit['data']
    for dicionario in lista:
        email = dicionario['author']       
        if email not in Email:
            Email.append(email)
            print(email)
