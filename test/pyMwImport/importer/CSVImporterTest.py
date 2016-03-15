'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import unittest
from pyMwImport.importer.CSVImporter import CSVImporter


class CSVImporterTest(unittest.TestCase):
    source = "../../../testdata/Test.csv"
    importer = None
    
    def setUp(self):
        self.importer = CSVImporter()

    def tearDown(self):
        pass

    '''
    Test if importer could be instantiated
    '''
    def testInstantiate(self):
        self.assertTrue( self.importer )
    
    '''
    Open the testfile. It contains a spreadsheet with a header and 10 data rows
    '''
    def testLoadCSV(self):
        data = self.importer.load( self.source )
        self.assertEqual( 10, len( data ) )

    '''
    Open the spreadsheet. Check if first row contains the right key-value pairs
    {'country (year)': 'USA [1810]', 'remarks': 'material reaches Berlin per F.W.Sieber', 'profession': 'collector', 'name': 'Abbot, John'}
    '''        
    def testRow(self):
        data = self.importer.load( self.source )
        row = data[0]
        self.assertEqual( 'USA [1810]', row[ 'country (year)' ])
        self.assertEqual( 'material reaches Berlin per F.W.Sieber', row[ 'remarks' ])
        self.assertEqual( 'collector', row[ 'profession' ])
        self.assertEqual( 'Abbot, John', row[ 'name' ])
        

if __name__ == "__main__":
    unittest.main()