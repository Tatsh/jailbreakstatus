#!/usr/bin/env python
from __future__ import print_function
import re
import sys

from bs4 import BeautifulSoup as Soup
import requests

VERSION = '0.0.2'
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 '
              'Safari/537.36')


def jailbreakstatus():
    r = requests.get('https://canijailbreak.com/')
    r.raise_for_status()
    soup = Soup(r.content, 'html5lib')
    danger = soup.select('.most-recent .text-danger')

    if len(danger):
        contents = [x for x in danger[0].contents if isinstance(x, basestring)]
        contents = re.sub(r'\s+', ' ', ' '.join(contents).strip())
        return contents

    success = soup.select('.most-recent .text-success')
    if len(success):
        return 'Jailbreak: {}'.format(success.select('a')[0]['href'])

if __name__ == '__main__':
    status = jailbreakstatus()

    if not status():
        sys.exit(1)

    print(status)
