'''
Created on 15.03.2016
Import data from a spreadsheet into a wiki page
See README.md for usage
@author: Alvaro.Ortiz
'''
import ConfigParser
import sys, traceback
import os.path
from mwConverter.formatter.TableFormatter import TableFormatter
from mwConverter.connector.MediaWikiApiConnector import MediaWikiApiConnector

'''Path to configuration file'''
configPath =  "../config.ini"

def run():
    try:
        # Read the config fle
        config = ConfigParser.ConfigParser()
        config.read( configPath )
        
        #Read the file to import from the command line arguments
        if len( sys.argv ) == 1: 
            raise IndexError( 'Wrong number of arguments' )
        source = sys.argv[1]
        
        # Determine the importer to instantiate, by examining the extension of the filename
        extension = os.path.splitext( source )[1]
        if extension == ".csv":
            from mwConverter.importer.CSVImporter import CSVImporter
            importer = CSVImporter()
            
        else:
            raise ValueError( 'Unsupported file format' )
        
        #Load data into an array of dicts
        data = importer.load()
        
        #Format data into a table
        formatter = TableFormatter()
        table = formatter.format( data )
        
        #Connect to the wiki
        connector = MediaWikiApiConnector( config )
        
    except:
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    run()