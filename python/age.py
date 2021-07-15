import requests

name = 'cail'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json() # json은 어떤 언어나 할수 있는 언어로 변환시켜라

print(response)
print(response['age'])