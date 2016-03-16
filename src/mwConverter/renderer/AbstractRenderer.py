'''
Created on 15.03.2016
Abstract base class for all renderers
@author: Alvaro.Ortiz
'''
class AbstractRenderer:
    
    '''
    Render an array of data into Mediawiki markup
    
    @param data array
    '''
    def format(self, data):
        raise NotImplementedError