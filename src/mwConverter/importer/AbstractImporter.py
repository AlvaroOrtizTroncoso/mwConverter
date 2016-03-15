'''
Created on 15.03.2016
Abstract base class for all importers

@author: Alvaro.Ortiz
'''
class AbstractImporter():
    
    def load(self):
        raise NotImplementedError
