'''
Created on 15.03.2016
Abstract base class for all connectors
@author: Alvaro.Ortiz
'''
class AbstractConnector:
    
    def login(self):
        raise NotImplementedError        
        
    def createPage(self, content):
        raise NotImplementedError