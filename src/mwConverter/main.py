'''
Created on 15.03.2016
Import data from a spreadsheet into a wiki page
@author: Alvaro.Ortiz
'''
import ConfigParser
import sys, traceback
import os.path
from mwConverter.Converter import Converter


#Path to configuration file.
# If running from inside Eclipse, the default path is relative to the project root
configPath =  "src/config.ini"

    
if __name__ == "__main__":
    """Import a CSV or LaTeX file into a MediaWiki page
    make sure the CSV is in UTF-8, else convert it, e.g. using Notepad.
    If the wiki page does not exist, it will be created (or re-created)
    If the wiki page exists, nothing will happen.

    The CSV files (.csv) will be converted to a table in MediaWiki markup. 
    LaTeX files (.tex) will be layout as-is
    
    The wiki username, password and endpoint URL are set in an .ini file (for wikis that require authentication).
    Copy example.ini to config.ini and edit before running
    
    Takes two (unnamed) arguments:
    source_file and wiki_page_name
    """
    try:
        # Read the config fle
        config = ConfigParser.ConfigParser()
        config.read( configPath )
        
        #Read the file to import and the page title from the command line arguments
        if len( sys.argv ) != 3: 
            raise IndexError( 'Wrong number of arguments' )
        path = sys.argv[1]
        pageTitle = sys.argv[2]
        
        # Determine the importer and formatter to instantiate, by examining the extension of the filename
        extension = os.path.splitext( path )[1]
        if extension == ".csv":
            from mwConverter.importer.CSVImporter import CSVImporter
            from mwConverter.formatter.TableFormatter import TableFormatter
            importer = CSVImporter()
            formatter = TableFormatter()
            
        elif extension == ".tex":
            from mwConverter.importer.LaTeXImporter import LaTeXImporter
            from mwConverter.formatter.PageFormatter import PageFormatter
            importer = LaTeXImporter()
            formatter = PageFormatter()
            
        else:
            raise ValueError( 'Unsupported file format %s' % extension )
                
        #Instantiate a connector to the wiki
        from mwConverter.connector.MediaWikiApiConnector import MediaWikiApiConnector
        connector = MediaWikiApiConnector( config )
        
        # Instantiate and run the converter
        converter = Converter( importer, formatter, connector )
        converter.run( path, pageTitle )
        
    except:
        traceback.print_exc(file=sys.stdout)

    
