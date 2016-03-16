'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
class Converter:
    
    def __init__( self, importer, formatter, connector ):
        self._importer = importer
        self._formatter = formatter
        self._connector = connector
        
    def run(self, title, path):
        data = self._importer.load( path )
        content = self._formatter.format( data )
        self._connector.createPage( title, content )

