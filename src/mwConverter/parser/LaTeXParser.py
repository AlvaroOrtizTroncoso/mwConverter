'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
from plasTeX.TeX import TeX

from mwConverter.parser.AbstractParser import AbstractParser

class LaTeXParser( AbstractParser ):
    def load(self, path):
        texFile = None
        try:
            tex = TeX()
            # Open the file to read the headers in the right order
            texFile = open( path, 'rb' )
            tex.input(texFile)
            document = tex.parse()
            return document
            
        except:
            raise
        
        finally:
            if texFile: texFile.close()