'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
from pyMwImport.importer.AbstractImporter import AbstractImporter
import csv

class CSVImporter( AbstractImporter ):
    
    '''
    Load a ';' separated list of entries into an array of dict. CSV column headers are dict keys.
    
    @param: String $path
    @return: array
    '''
    def load(self, path):
        data = []
        csvFile = open( path, 'rb' )
        csvReader = csv.DictReader( csvFile, delimiter=';' )
        for row in csvReader:
            data.append( row )
        return data
    
    