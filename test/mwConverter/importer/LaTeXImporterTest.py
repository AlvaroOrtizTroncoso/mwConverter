'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
import unittest
from mwConverter.importer.LaTeXImporter import LaTeXImporter


class Test(unittest.TestCase):
    source = "../../../testdata/Test.tex"
    importer = None


    def setUp(self):
        self.importer = LaTeXImporter()



    def tearDown(self):
        pass


    '''
    Test if importer could be instantiated
    '''
    def testInstantiate(self):
        self.assertTrue( self.importer )
        
        
    '''
    Open the testfile. It contains LaTeX markup
    '''
    def testLoadLaTeX(self):
        source = self.importer.load( self.source )
        self.assertTrue( source )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()