import urllib.parse
import urllib.request

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

class Server():

class Request():