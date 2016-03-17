'''
Created on 16.03.2016

@author: alvaro
'''
import os
from plasTeX.Renderers.Text import Renderer
from mwConverter.renderer.AbstractRenderer import AbstractRenderer

class MwPageRenderer(AbstractRenderer, Renderer):
    _tempDir = None
    
#    def __init__(self, config):
#        self._tempDir = config.get( 'defaults', 'tempDir' )
        
    
    def renderXML(self, data):
        """Format a plasTeX document into XML"""
        if data == None: return ""
        return data.toXML()
    
    
    def renderMW(self, data):
        """Format a plasTeX document into MediaWiki markup"""
        markup = ""
        tempFile = None
        if data == None: return markup
        
        # Render to file
        self.render(data)
        
        # Read the file(s) with the rendered content
        paths = sorted(self.files.values())        
        for path in paths:
            try:
                tempFile = open( path, 'rb' )
                markup = markup + tempFile.read()
                
            except:
                raise
            
            finally:
                if tempFile: 
                    tempFile.close()
                    os.remove( path )
                
        return markup        
    
        
    '''Overrides Text Renderer '''
    def do_maketitle(self, node): 
        output = []
        metadata = node.ownerDocument.userdata
        if 'title' in metadata:
            output.append( "=%s=\n" % metadata['title'] )
            
        return u'\n%s\n' % u'\n'.join(output)
        
        
        
        
             