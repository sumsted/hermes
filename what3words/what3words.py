import os
import requests

what3words_url = os.environ['WHAT3WORDS_URL']
what3words_key = os.environ['WHAT3WORDS_KEY']


def get_words(latitude, longitude):
    params = {'key': what3words_key, 'coords': '%f,%f' % (latitude, longitude)}
    response = requests.get(what3words_url+'/reverse', params=params)
    result = response.json()
    return result['words']


def get_coords(three_words):
    params = {'key': what3words_key, 'addr': '%s' % three_words}
    response = requests.get(what3words_url+'/forward', params=params)
    result = response.json()
    return [result['geometry']['lat'], result['geometry']['lng']]

if __name__ == '__main__':
    words = get_words(35.0, -89.0)
    coords = get_coords(words)
    print('%s = %s' % (words, str(coords)))
