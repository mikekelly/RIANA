"""
The handler script.

@author: Michael Hausenblas, http://sw-app.org/mic.xhtml#i
@since: 2011-06-21
@status: inital version
"""
import sys
sys.path.insert(0, 'lib')
import logging
import cgi
import os
import platform
import urllib
import urllib2
import StringIO
import csv
import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

DEFAULT_CONTENT_TYPE = "text/plain" # should be "application/hal+xml"

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = DEFAULT_CONTENT_TYPE
    self.response.out.write(template.render('main.hal', {"motd": "Hello World!"}))

class MediaTypesHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = DEFAULT_CONTENT_TYPE
        self.response.out.write(template.render('media-types.hal',{"content_types": [
          {"name": "application"},
          {"name": "audio"},
          {"name": "image"},
          {"name": "text"},
          {"name": "video"}
        ]}))


class ReadmeHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('readme.html',None))

class NotFoundHandler(webapp.RequestHandler):
	def get(self):
		self.error(404)
		self.response.out.write(template.render('a404.html', None))

class TestHandler(webapp.RequestHandler):
	def get(self):
		doc_url = urllib.unquote(self.request.get('url'))
		logging.info('Got URL [%s]' %doc_url)

		self.response.headers.add_header("Access-Control-Allow-Origin", "*") # CORS-enabled API
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write("Thank you for the <a href='%s'>URL</a> -  tastes yummy!" %doc_url)
