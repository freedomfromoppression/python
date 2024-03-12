import requests
def get_naver(query):
    s =  1
    url = "https://openapi.naver.com/v1/search/blog?query={0}&start={1}&display=100".format(query, s)
    CLIENT_ID = "xA7lR4icaYTq8dkYHbFL"
    SECRET = "7xXTjpCHqu"
    header = {"X-Naver-Client-Id": CLIENT_ID
              ,"X-Naver-Client-Secret":SECRET}
    res = requests.get(url, headers=header)
    json_data = res.json()
    return json_data


