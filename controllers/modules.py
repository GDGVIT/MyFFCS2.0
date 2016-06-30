
'''
Middleware for controller to contain all the modules
'''
import tornado.web
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash, ErrorHandler
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine

#Other Libraries

import json
import time
import datetime
import urllib
import tornado.web
import tornado.gen
from raven.contrib.tornado import SentryMixin
from raven.contrib.tornado import AsyncSentryClient
import requests
import os
import urllib2
import hashlib
import httplib2
from bson.objectid import ObjectId
import re
import pymongo
from bson import json_util
from motor import MotorClient
import uuid
db = MotorClient('mongodb://gdgvit:baapbaaphotahain@ds011495.mlab.com:11495/myffcs')['myffcs']

					