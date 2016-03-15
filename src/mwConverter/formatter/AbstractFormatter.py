'''
Created on 15.03.2016
Abstract base class for all formatters
@author: Alvaro.Ortiz
'''
class AbstractFormatter:
    
    '''
    Format an array of data into Mediawiki markup
    
    @param data array
    '''
    def format(self, data):
        raise NotImplementedError