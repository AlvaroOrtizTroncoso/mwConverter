'''
Created on 15.03.2016
Abstract base class for all parsers

@author: Alvaro.Ortiz
'''
class AbstractParser():
    
    def load(self):
        raise NotImplementedError
