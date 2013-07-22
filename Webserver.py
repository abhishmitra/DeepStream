# -*- coding: cp1252 -*-
import codecs
from bottle import route, run, template, request
import time
import urllib2
import urllib
import json as m_json
import os
import sys
from urllib import FancyURLopener
import time
from BeautifulSoup import BeautifulSoup
import json as simplejson
import sqlite3
Soup = BeautifulSoup
from nltk import sent_tokenize, word_tokenize
from collections import Counter
from math import log10
# -*- coding: utf-8 *-*



profanity = ['fuck','asshole','sex','faggot','negro','nigger','boob','tit']
@route('/')
def login_form():
    return "Hello World"


