import requests
import pprint
r = requests.get('https://api.tfl.gov.uk/Disruptions/Lifts/')
results = r.json()

# pprint.pprint(results[0]['message'])

for item in results:
    print(item['message'])


# lista = [0, 2, 999, 8]

# for numero in lista:
#     print(numero)



# lista2 = ["palavra", 3, True]

# dic = {
#     "chave1": 10,
#     "outra": True,
#     "valores": [0, 2, 3, 4]
# }

# lista_dic = [{
#     "chave1": 10,
#     "outra": True,
#     "valores": [0, 2, 3, 4]
# }, {
#     "chave1": 20,
#     "outra": False,
#     "valores": [10, 12, 13, 14]
# }]
# print(lista_dic[1]["chave1"])