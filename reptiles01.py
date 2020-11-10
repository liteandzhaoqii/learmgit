from urllib import urlopen

response = urlopen("http://www.baidu.com")

info = response.response()

print(info)



