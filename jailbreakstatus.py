#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from sys import exit

import requests


VERSION = '0.0.4'


def jailbreakstatus():
    r = requests.get('https://canijailbreak.com/jailbreaks.json')
    r.raise_for_status()

    try:
        return r.json()['jailbreaks'][0]['jailbroken']
    except (IndexError, KeyError):
        pass

    return False


def jailbreakstatus_main():
    status = jailbreakstatus()

    if not status:
        exit(1)


if __name__ == '__main__':
    jailbreakstatus_main()
