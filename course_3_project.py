import requests_with_caching
import json


def get_movies_from_tastedive(str):
    base_url = "https://tastedive.com/api/similar"
    param = {}
    param['q'] = str
    param['type'] = "movies"
    param['limit'] = "5"
    url = requests_with_caching.get(base_url, params=param)
    return url.json()


def extract_movie_titles(txt):
    return([i['Name'] for i in txt["Similar"]["Results"]])


def get_related_titles(lst):
    l = []
    for m in lst:
        l.extend(extract_movie_titles(get_movies_from_tastedive(m)))
    return set(l)


get_movies_from_tastedive("Black Panther")


def get_movie_data(title):
    burl = "https://www.omdbapi.com/"
    param = {}
    param['t'] = title
    param['r'] = "json"
    this_page_cache = requests_with_caching.get(burl, params=param)
    return json.loads(this_page_cache .text)


def get_movie_rating(dic):
    ranking = dic['Ratings']
    for dic_item in ranking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            rating = int(dic_item['Value'][:-1])
    return rating


def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
