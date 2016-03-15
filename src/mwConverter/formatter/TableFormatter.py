'''
Created on 15.03.2016
Format data into mediawiki format 
@author: Alvaro.Ortiz
'''
from mwConverter.formatter.AbstractFormatter import AbstractFormatter

class TableFormatter( AbstractFormatter ):
    
    '''
    Format an array of data into a Mediawiki table
    
    @param: data array
    @return: String
    '''
    def format(self, data):
        response = '{| class="wikitable"\n'
        response += '|-\n'
        
        if len( data ) > 0:
            # table headers
            headers = data[0].keys();
            for h in headers:
                response += '! scope="col" | %s\n' % h
            response += '|-\n';
            
            # data rows
            for r in data:
                values = r.values()
                for v in values:
                    response += '| %s\n' % v
                response += '|-\n'

        # close table
        response += '|}\n';
        return response;
        