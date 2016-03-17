'''
Created on 17.03.2016

@author: Alvaro.Ortiz
'''
import unittest
import ConfigParser
from mwConverter.renderer.MwPageRenderer import MwPageRenderer
from mwConverter.parser.LaTeXParser import LaTeXParser

class Test(unittest.TestCase):
    '''Path to configuration file'''
    configPath =  "../../test.ini"
    config = None
    renderer = None


    def setUp(self):
        # Read the configuration file
        self.config = ConfigParser.ConfigParser()
        self.config.read( self.configPath )
        
        #Instantiate the renderer
        #self.renderer = MwPageRenderer(self.config)
        self.renderer = MwPageRenderer()


    def tearDown(self):
        pass


    '''
    Test if renderer can be instantiated
    '''
    def testInstantiate( self ):
        self.assertTrue( self.renderer )


    '''
    Renderer should be able to format an empty document
    '''
    def testEmptyDoc(self):
        markup = self.renderer.renderMW( None )
        self.assertEquals( 1, len( markup.split( '\n' ) ) )
        
        
    '''
    render the test doc in XML
    '''
    def testRenderXML( self ):
        # Load test data
        source = "../../../testdata/Test.tex"
        parser = LaTeXParser()
        data = parser.load( source )
        
        markup = self.renderer.renderXML( data )
        self.assertTrue( markup )


    '''
    render the test doc in XML
    '''
    def testRenderMW( self ):
        # Load test data
        source = "../../../testdata/Test.tex"
        parser = LaTeXParser()
        data = parser.load( source )
        
        markup = self.renderer.renderMW( data )
        self.assertTrue( markup )
        self.assertTrue( "=LaTeX=" in markup )
        
    '''
    render the test doc in XML
    '''
    def testRenderMW2( self ):
        # Load test data
        source = "../../../testdata/sample2e.tex"
        parser = LaTeXParser()
        data = parser.load( source )
        
        markup = self.renderer.renderMW( data )
        print markup
        self.assertTrue( markup )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()