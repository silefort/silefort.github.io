#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'@si_lefort'
SITENAME = u'Tech This Out'
SITEURL = u''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'themes/voce'
SITEIMAGE = 'site-cover.jpg'
SITEDESCRIPTION = 'An online version of my "How to"\'s and "Today I Learned"\'s'
FAVICON = 'avatar.png'
LOGO = 'avatar.png'
FIRST_NAME = 'Simon'

TWITTER_USERNAME = '@silefort'
TWITTER = 'https://twitter.com/si_lefort'
GITHUB = 'https://github.com/silefort'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
# FEED_ATOM = None
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

# Blogroll
LINKS = (('Home', '/'),)
         # ('About', '/About'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/si_lefort'),
        ('Github', 'https://github.com/silefort'),
        ('Feed','/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

### VOCE
USER_LOGO_URL = 'images/avatar.png'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
