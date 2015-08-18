from datetime import datetime
from requests import post
from urlparse import urlparse
import json

class AlgalonClient(object):

    def __init__(self, dsn, csrf_token):
        self.url = None
        self._dsn = None
        self.token = None
        self.dsn = dsn
        self.csrf_token = csrf_token

    def send_alarm(self, title, text):
        headers = {'content-type': 'application/json',
                   'X-CSRFToken': self.csrf_token}
        message = {'token': self.token, 'title': title, 'text': text}
        return post(self.url, data=json.dumps(message), headers=headers)

    @property
    def dsn(self):
        return self._dsn

    @dsn.setter
    def dsn(self, dsn):
        try:
            urlpart = urlparse(dsn)
            token, host = urlpart.netloc.split('@')
        except ValueError:
            self._dsn = ''
            self.token = ''
            self.url = ''
        else:
            self._dsn = dsn
            self.token = token
            self.url = 'http://{host}{path}api/alarm/'.format(
                host=host, path=urlpart.path)

algalon = AlgalonClient('http://81de5c6a016846cc82148c9906a80f51@algalon-web.intra.hunantv.com/', 'xiaoliulaoshihuoerzhenhaomemeda')
algalon.send_alarm('this is from elegon', 'just try it, from %s' % datetime.now())
