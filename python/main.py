import requests
import json
from datetime import datetime

def httpGet(url, params):
    r = requests.get(url, params)
    return json.loads(r.content)

def httpPost(url, params):
    r = requests.post(url, params)
    return json.loads(r.content)

# 获取微信token
def getAccessToken(appId, appSecret):
    params = {
        'grant_type': 'client_credential',
        'appid': appId,
        'secret': appSecret
    }
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    return httpGet(url, params)

# 获取天气
def getWeather(abCode, key):
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': key,
        'city': abCode,
        'extensions': 'base',
        'output': 'JSON',
    }
    return httpGet(url, params)

# 获取一句情话
def getHua():
    url = 'https://yuxinghe.top/api/love.php'
    hua = httpGet(url, {'type': 'json'})
    return hua['ishan']

# 获取生日倒计时
def getBirthDays(birthDay):
    birthDay = datetime.strptime(birthDay, '%Y-%m-%d')
    interval = birthDay - datetime.now()
    return interval.days

# 获取在一起天数
def getTogetherDays(togetHerDay):
    togetHerDay = datetime.strptime(togetHerDay, '%Y-%m-%d')
    interval = datetime.now() - togetHerDay
    return interval.days

# 发送模版消息
def sendTemplateMessage(content, accessToken):
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + accessToken
    return httpPost(url, content)

# 获取星期
def getWeek():
    w = datetime.now().strftime('%w')
    data = {
        0: '天',
        1: '一',
        2: '二',
        3: '三',
        4: '四',
        5: '五',
        6: '六'
    }
    return data[int(w)]

if __name__ == '__main__':
    # 微信公众号的appId和appSecret
    appId = 'wxc4b2963cdc386b85'
    appSecret = '648c4639ee0eaa316229497b74c25be4'
    # 要发送人的openId列表
    openIdList = ['ojKlj6q-t9TNkIBh659v0Tp_URI4']
    # 模版Id
    templateId = '7JJFCS-TYlDl-aCOoIrttO9Iuccyk5alIkb8JhQuL0s'
    # 高德天气API key
    gaoDeKey = '244e75e78d7110304a626f6b1c3e5f03'
    # 所在地点abCode（高德后台可以获取 https://a.amap.com/lbs/static/amap_3dmap_lite/AMap_adcode_citycode.zip）
    abCode = '110105'
    # 最近一次生日的日期
    birthDay = '2022-11-13'
    # 在一起的时间
    togetHerDay = '2018-07-14'

    accessTokenInfo = getAccessToken(appId, appSecret)
    accessToken = accessTokenInfo['access_token']
    weatherInfo = getWeather(abCode, gaoDeKey)
    weather = weatherInfo['lives'][0]
    hua = getHua()
    birthDays = getBirthDays(birthDay)
    togetHerDays = getTogetherDays(togetHerDay)
    week = getWeek()

    for i in range(len(openIdList)):
        data = {
            'touser': openIdList[i],
            'template_id': templateId,
            'topcolor' : '#FF0000',
            'data': {
                'date': {
                    'value': datetime.now().strftime('%Y-%m-%d'),
                },
                'province': {
                    'value': weather['province']
                },
                'city': {
                    'value': weather['city']
                },
                'temperature': {
                    'value': weather['temperature'],
                    'color': '#4d79ff'
                },
                'humidity': {
                    'value': weather['city'],
                    'color': '#4d79ff'
                },
                'winddirection': {
                    'value': weather['winddirection'],
                },
                'windpower': {
                    'value': weather['windpower']
                },
                'togetherDays': {
                    'value': togetHerDays,
                    'color': '#ff4dff'
                },
                'birthDays': {
                    'value': birthDays,
                    'color': '#ff4dff'
                },
                'week': {
                    'value': week,
                },
                'hua': {
                    'value': hua,
                    'color': '#b3ff66'
                }
            }
        }
        params = json.dumps(data)

        print(sendTemplateMessage(params, accessToken))


