def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "--servers", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)

def simulateOneServer():
    import urllib.parse
    import urllib.request

    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

    data = urllib.parse.urlencode(values)
        data = data.encode('ascii')  # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

class Server():
    def __init__(self, ppm):
        self.page_rate = ppm

    self.current_task = None
    self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1

    if self.time_remaining <= 0:
        self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True

        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 /
            self.page_rate


class Request():
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp