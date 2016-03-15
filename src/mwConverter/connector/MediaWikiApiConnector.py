'''
Created on 15.03.2016
Connector for the MediaWiki http API
@author: Alvaro.Ortiz
'''
import requests
import urlparse
import sys, traceback
from mwConverter.connector.AbstractConnector import AbstractConnector

class MediaWikiApiConnector( AbstractConnector ):
    #The URL to the Mediawiki API
    _apiUrl = None
    #The URL to MediaWiki pages
    _contentUrl = None
    #Authentication to the MediaWiki API
    _username = None
    _password = None
    #Token available after Login
    _loginToken = None
    #Cookie available after Login
    _cookies = None

    
    def __init__(self, config):
        baseMwUrl = config.get( 'defaults', 'baseMwURL' )
        self._apiUrl = urlparse.urljoin( baseMwUrl, 'api.php')
        self._contentUrl = urlparse.urljoin( baseMwUrl, 'index.php')
        self._username = config.get( 'defaults', 'username' )
        self._password = config.get( 'defaults', 'password' )
    
    
    def login(self):
        try:
            # Login request
            payload = {'action': 'login', 'format': 'json', 'utf8': '', 'lgname': self._username, 'lgpassword': self._password}
            r1 = requests.post( self._apiUrl, data=payload)
            
            # Check http status
            if r1.status_code != 200: raise Exception( 'Failed login request url %s status %d' % (self._apiUrl, r1.status_code) )
            #Check response code
            if 'error' in r1.json(): raise Exception( 'Failed login request %s : %s' % ( self._apiUrl, r1.json()['error']['info'] ) )
            # store login token
            self._loginToken = r1.json()['login']['token']
            
            # Workaround MediaWiki bug
            # see https://www.mediawiki.org/wiki/API:Login
            if r1.json()['login']['result'] == 'NeedToken':
                payload = { 'action': 'login', 'format': 'json', 'utf8': '', 'lgname': self._username, 'lgpassword': self._password, 'lgtoken': self._loginToken }
                r2 = requests.post( self._apiUrl, data=payload, cookies=r1.cookies)
            
            #Store cookies
            self._cookies = r1.cookies
            
            return True
        
        except:
            traceback.print_exc(file=sys.stdout)
            return False
        
     
    def loadPage(self, title):
        try:
            # Attempt to Login
            if self.login() == False: return False

            # Read a page
            payload = {'action': 'parse', 'page': title, 'format': 'json' }
            r1 = requests.post( self._apiUrl, data=payload, cookies=self._cookies )
            
            # Check http status
            if r1.status_code != 200: raise Exception( 'Failed read request status %d' % ( r1.status_code) )
            #Check response code
            if 'error' in r1.json(): raise Exception( 'Failed login request %s : %s' % ( self._apiUrl, r1.json()['error']['info'] ) )
            
            return r1.content
        
        except:
            traceback.print_exc(file=sys.stdout)
            return False
        
        
    def createPage(self, content):
        pass
