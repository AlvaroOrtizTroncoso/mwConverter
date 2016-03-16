'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
import unittest
from mwConverter.parser.LaTeXParser import LaTeXParser


class Test(unittest.TestCase):
    source = "../../../testdata/Test.tex"
    parser = None


    def setUp(self):
        self.parser = LaTeXParser()



    def tearDown(self):
        pass


    '''
    Test if parser could be instantiated
    '''
    def testInstantiate(self):
        self.assertTrue( self.parser )
        
        
    '''
    Open the testfile. It contains LaTeX markup
    '''
    def testLoadLaTeX(self):
        source = self.parser.load( self.source )
        self.assertTrue( source )


if __name__ == "__main__":
    unittest.main()