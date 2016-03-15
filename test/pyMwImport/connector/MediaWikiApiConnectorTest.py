'''
Created on 15.03.2016

@author: Alvaro.Ortiz
'''
import unittest
import ConfigParser

class Test(unittest.TestCase):
    '''Path to configuration file'''
    configPath =  "../../test.ini"
    config = None

    def setUp(self):
        # Read the config fle
        self.config = ConfigParser.ConfigParser()
        self.config.read( self.configPath )


    def tearDown(self):
        pass


    def testReadConfigFile(self):
        self.assertEqual( 'http://test.biowikifarm.net', self.config.get( 'defaults', 'baseURL' ) )


if __name__ == "__main__":
    unittest.main()