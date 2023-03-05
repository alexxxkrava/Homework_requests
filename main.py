import requests

link = 'https://akabab.github.io/superhero-api/api//all.json'

def req(url):

    response = requests.get(url)

    param = {}
    superhero = ['Hulk', 'Captain America', 'Thanos']
    for i in response.json():
        if i['name'] in superhero:
            param[i['name']] = i['powerstats']['intelligence']
    for key, val in param.items():
        if val == max(param.values()):
            print(f'Самый умный: {key} \nУровень интеллекта: {val}\n')
        if val == min(param.values()):
            print(f'Самый глупый: {key} \nУровень интеллекта: {val}\n')

if __name__ == '__main__':
    req(link)


