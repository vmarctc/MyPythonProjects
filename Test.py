import requests
import json

"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно выполнить запрос и как выглядит ответ сервера.
"""


def get_token():
    client_id = "af77e6c4dc0a15ef1f2c"
    client_secret = "ceb11138ba4a5dc3ec14fd4fcd913aaa"
    post_params = {"client_id": client_id, "client_secret": client_secret}

    res = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=post_params)

    j = json.loads(res.text)

    return j["token"]


def artists_info(artists_names):
    header = {"X-Xapp-Token": get_token()}
    dict_artists = {}

    for name in artists_names:
        res = requests.get("https://api.artsy.net/api/artists/" + name, headers=header)
        res.encoding = 'utf-8'
        j = json.loads(res.text)
        dict_artists[j["sortable_name"]] = j["birthday"]

    return dict_artists


def get_artists_names(path):
    names = []

    with open(path, 'r') as inf:
        for line in inf:
            names.append(line.strip('\n'))

    return names


dict = artists_info(get_artists_names("art_names.txt"))
sorted_by_birthday = sorted(dict.items(), key=lambda x: (x[1], x[0]))

with open("sorted_artists.txt", 'w', encoding='utf-8') as ouf:
    for i in sorted_by_birthday:
        ouf.write(i[0] + '\n')

print("end.")
