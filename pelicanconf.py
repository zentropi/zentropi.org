#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Harshad Sharma'
SITENAME = 'zentropi.org'
SITETITLE = 'zentropi.org'
SITESUBTITLE = 'Script Your World'
SITEDESCRIPTION = ''
SITEURL = ''
SITELOGO = SITEURL + '/images/logo.png'
FAVICON = SITEURL + '/images/icon.png'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('@github', 'https://github.com/zentropi/'),
            ('zencelium', 'https://github.com/zentropi/python-zencelium/'),
            ('python-zentropi', 'https://github.com/zentropi/python-zentropi/'),
            ('micropython-zentropi', 'https://github.com/zentropi/micropython-zentropi/'),
            ('javascript-zentropi', 'https://github.com/zentropi/javascript-zentropi/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'themes/Flex'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
USE_GOOGLE_FONTS = False
