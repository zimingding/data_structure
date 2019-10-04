class Browser:
    def __init__(self):
        self.prev = []
        self.fwd = []

    def browse(self, url):
        print('browsing ' + url)
        self.prev.append(url)
        self.fwd.clear()

    def back(self):
        if len(self.prev) <= 1:
            print('nothing to go back')
            return
        url = self.prev.pop()
        self.fwd.append(url)
        prev_url = self.prev[-1]
        print('back to ' + prev_url)

    def forward(self):
        if not self.fwd:
            print('nothing to go forward')
            return
        url = self.fwd.pop()
        print('forward to ' + url)
        self.prev.append(url)


browser = Browser()
browser.browse('domain')
browser.browse('amazon')
browser.browse('google')

browser.forward()
browser.back()
browser.back()
browser.forward()
browser.forward()

browser.browse('apple')
browser.forward()
