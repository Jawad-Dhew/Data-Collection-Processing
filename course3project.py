import requests
import json


def get_movies_from_tastedive(movieName, key):
    base_url = "https://tastedive.com/api/similar"
    param = {}
    param['q'] = movieName
    param['k'] = key
    param['type'] = "movies"
    param['limit'] = "5"
    final_url = requests.get(base_url, params=param)
    print(final_url.url)
    respDic = json.loads(final_url.text)
    print(type(respDic))
    return respDic


def extract_movie_titles(dic):
    l = []
    for movies in dic['Similar']['Results']:
        l.append(movies['Name'])
    return l


print(get_movies_from_tastedive("3 Idiots", "327878-course3p-I4ZNBN4A"))
print(extract_movie_titles(get_movies_from_tastedive(
    "3 Idiots", "327878-course3p-I4ZNBN4A")))
