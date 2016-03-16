'''
Created on 16.03.2016

@author: Alvaro.Ortiz
'''
import unittest
from mwConverter.importer.CustomDictReader import CustomDictReader, CSVRW


class Test(unittest.TestCase):
    source1 = "../../../testdata/Test.csv"
    source2 = "../../../testdata/Test2.csv"
    source3 = "../../../testdata/Test3.csv"

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRead1(self):
        test = CSVRW()
        success, thedict = test.createCsvDict('profession',';',None, self.source1 )
        self.assertTrue( success )


    def testRead2(self):
        test = CSVRW()
        success, thedict = test.createCsvDict('TBLID',',',None, self.source2 )
        self.assertTrue( success )
        

    def testRead3(self):
        test = CSVRW()
        success, thedict = test.createCsvDict('profession',',',None, self.source3 )
        self.assertTrue( success )
        

if __name__ == "__main__":
    unittest.main()