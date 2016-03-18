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
        self.assertTrue( "{{DISPLAYTITLE:LaTeX}}" in markup )
        
    '''
    render the test doc in XML
    '''
    def testRenderMW2( self ):
        # Load test data
        source = "../../../testdata/sample2e.tex"
        parser = LaTeXParser()
        data = parser.load( source )
        
        markup = self.renderer.renderMW( data )
        # Test something was rendered
        self.assertTrue( markup )
        
        # document title
        print markup
        self.assertTrue( "{{DISPLAYTITLE:An Example Document}}" in markup )
        
        # author, date
        self.assertTrue( "Leslie Lamport" in markup )
        self.assertTrue( "January 21, 1994" in markup )
        
        # document sections
        self.assertTrue( "==1 Ordinary Text==" in markup )
        self.assertTrue( "==2 Displayed Text==" in markup )
        
        # Emphasis
        self.assertTrue( "''italic''" in markup )
        
        # quotes
        self.assertTrue( "<blockquote>This is a short quotation." in markup )
        self.assertTrue( "See how it is formatted.</blockquote>" in markup )
        
        # lists
        self.assertTrue( "* This is the first item of an itemized list." in markup )
        self.assertTrue( "# This is the first item of an enumerated" in markup )
        
        #verse
        self.assertTrue( "<blockquote>There is an environment" in markup )
        self.assertTrue( "forced to be terse.</blockquote>" in markup )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()