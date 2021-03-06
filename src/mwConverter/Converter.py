'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
class Converter:
    
    def __init__( self, parser, renderer, connector ):
        self._parser = parser
        self._renderer = renderer
        self._connector = connector
        
    def run(self, path, title ):
        data = self._parser.load( path )
        content = self._renderer.renderMW( data )
        self._connector.createPage( title, content )

