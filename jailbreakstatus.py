#!/usr/bin/env python
from __future__ import print_function
from os import uname
from os.path import expanduser
import logging
import sys

from praw import Reddit


VERSION = '0.0.1'
LOG_NAME = 'jbstatus'

"""As of 2016-06-19"""
BAD_LINE = 'iOS 9.2, 9.2.1, 9.3, 9.3.1 and 9.3.2 do not have a jailbreak.'


log = logging.getLogger(LOG_NAME)


def jailbreakstatus():
    un = uname()
    ua = '{} {}:jailbreakstatus:v{} (by /u/Tatsh2DX)'.format(
        un.sysname.lower(), un.machine.lower(), VERSION)
    log.debug('User agent: {}'.format(ua))
    r = Reddit(user_agent=ua)
    desc = r.get_subreddit('jailbreak').description

    if BAD_LINE in desc:
        log.info(BAD_LINE)
        return BAD_LINE

    should_log = False
    data = ''

    for line in desc.splitlines():
        if line.startswith('# '):
            if 'Latest jailbreaks' in line:
                should_log = True
            else:
                break

        if should_log:
            data += line + '\n'

    data = data.strip()
    log.info(data)

    return data


if __name__ == '__main__':
    logger = logging.getLogger(LOG_NAME)
    formatter = logging.Formatter('%(message)s')
    channel = logging.StreamHandler(sys.stdout)

    logger.setLevel(logging.DEBUG)
    channel.setLevel(logging.INFO)
    channel.setFormatter(formatter)
    logger.addHandler(channel)

    jailbreakstatus()
