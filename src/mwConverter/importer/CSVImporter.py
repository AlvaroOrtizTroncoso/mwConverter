'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import csv
from mwConverter.importer.AbstractImporter import AbstractImporter
from mwConverter.importer.CustomDictReader import CSVRW

class CSVImporter( AbstractImporter ):
    def load(self, path):
        """Load a ';' separated list of entries into an array of OrderedDict. CSV column headers are OrderedDict keys.
        Keeps the order of the columns.
        
        @param: String $path
        @return: array
        """
        response = []
        
        # Open the file to read the headers in the right order
        csvFile = open( path, 'rb' )
        csvReader = csv.DictReader( csvFile, delimiter = ';' )
        sort = csvReader.fieldnames[0]

        # Re-open the file using the ordered reader this time
        orderedReader = CSVRW()
        success, odict = orderedReader.createCsvDict( sort, ';', None, path )
        
        # Compile a list (sequence) of OrderedDicts
        if success:
            for row in odict.values():
                response.append( row )
                
        return response
            