'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import csv
from mwConverter.parser.AbstractParser import AbstractParser
from mwConverter.parser.CustomDictReader import CSVRW

class CSVParser( AbstractParser ):
    def load(self, path):
        """Load a ';' separated list of entries into an array of OrderedDict. CSV column headers are OrderedDict keys.
        Keeps the order of the columns.
        
        @param: String $path
        @return: array
        """
        response = []
        csvFile = None
        
        try:
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
        
        except:
            raise
        
        finally:
            if csvFile: csvFile.close()
            