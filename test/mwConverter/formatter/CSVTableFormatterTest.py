'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import unittest
from mwConverter.formatter.TableFormatter import TableFormatter
from mwConverter.importer.CSVImporter import CSVImporter

class Test( unittest.TestCase ):
    formatter = None

    def setUp( self ):
        self.formatter = TableFormatter()


    def tearDown( self ):
        pass

    '''
    Test if formatter can be instantiated
    '''
    def testInstantiate( self ):
        self.assertTrue( self.formatter )
        
    '''
    Formatter should be able to format an empty array
    3 rows of markup are expected for an empty table
    plus one at the end of the file
    '''
    def testEmptyTable(self):
        markup = self.formatter.format( [] )
        self.assertEquals( 4, len( markup.split( '\n' ) ) )
    
    '''
    The test spreadsheet has 10 rows of data in 4 columns
    '''
    def testFilledTable( self ):
        # Load test data
        source = "../../../testdata/Test.csv"
        importer = CSVImporter()
        data = importer.load( source )
        
        markup = self.formatter.format( data )
        # 4 Rows table header and footer
        # 4 Rows column headers + 1 line separator
        # 10 rows x (4 columns of data + 1 line separator per row)
        self.assertEquals( 59, len( markup.split( '\n' ) ) )


if __name__ == "__main__":
    unittest.main()