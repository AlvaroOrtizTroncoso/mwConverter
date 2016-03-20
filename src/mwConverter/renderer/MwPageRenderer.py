'''
Created on 16.03.2016

@author: alvaro
'''
import os, re
from plasTeX.Renderers.Text import Renderer
from mwConverter.renderer.AbstractRenderer import AbstractRenderer

class MwPageRenderer(AbstractRenderer, Renderer):
    """Renders MediaWiki markup from Latex
    Supports:
    * page title (displaytitle MediaWiki extension has to be enabled)
    * section titles
    * paragraphs
    * italics (LaTeX emph)
    * bold (LaTex em)
    * non-breaking spaces
    * blockquotes
    * ordered and unordered lists
    """    
    
    
    def renderMW(self, data):
        """Format a plasTeX document into MediaWiki markup"""
        markup = ""
        tempFile = None
        if data == None: return markup
        
        # Render to file
        self.render( data )
        
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
                    
        # Done reading files, return the cleaned-up markup
        return self._postMarkup(markup)


    def _stripNode(self, node):
        """Get the text content of a node as a clean unicode string"""
        return unicode(node).strip()
    
    
    def _postMarkup(self, markup):
        """"Remove lines starting with spaces
        (use blockquotes or pre if you need preformatted text)
        """
        markup = re.sub( r"\n\s+", "\n\n",  markup )
        return markup
        
    
    '''Overrides Text Renderer '''
    def do_maketitle(self, node): 
        """Page title"""
        metadata = node.ownerDocument.userdata
        displayTitle = 'Page Title'
        if 'title' in metadata:
            # Use the displaytitle extension to change the page title
            displayTitle = self._stripNode(metadata['title'])

        displayAuthor = []          
        if 'author' in metadata:
            for author in metadata['author']:
                if [a for a in author if getattr(a,'macroName','') == '\\']:
                    for a in author:
                        if getattr(a,'macroName','') == '\\':
                            continue
                        displayAuthor.append( self._stripNode( a ) )
                else:
                    displayAuthor.append( self._stripNode( author ) )
        
        displayDate = ''            
        if 'date' in metadata:
            displayDate = self._stripNode( metadata['date'] )
            
        return u"{{DISPLAYTITLE:%s}}\n''%s''. ''%s''\n\n" % ( displayTitle, ", ".join(displayAuthor), displayDate )
        
    
    def do_section(self, node):
        """Section titles and text"""
        output = []
        # Title
        if node.fullTitle:
            output.append( '\n==%s==\n' % self._stripNode( node.fullTitle ) )
        #Text
        output.append( '\n%s' % self._stripNode(node) )
        
        return u'\n%s\n' % u'\n'.join(output)
    
    do_part = do_chapter = do_subsection = do_subsubsection = do_section
    do_paragraph = do_subparagraph = do_subsubparagraph = do_section
    
        
    def do_emph(self, node):
        """Italics"""
        return u"''%s''" % self._stripNode(node)

    
    def do_em(self, node):
        """Bold"""
        return u"'''%s'''" % self._stripNode(node)

    
    def do_quote(self, node):
        """Blockquote, single line"""
        content = self._stripNode(node).replace( '\\', '\r\r' )
        return u"<blockquote>%s</blockquote>" % content
    
    do_quotation = do_verse = do_quote

    
    def do_itemize(self, node):
        """Unordered lists (not nested)"""
        output = []
        for item in node:
            output.append( "* %s" % self._stripNode( item ).replace( "\n", "" ))
        return self.addBlock(u'\n'.join(output))

    
    def do_enumerate(self, node):
        """Ordered lists (not nested)"""
        output = []
        for item in node:
            output.append( "# %s" % self._stripNode( item ).replace( "\n", "" ) )
        return u'\r' + self.addBlock(u'\n'.join(output))

    
    def do__tilde(self, node):
        """Non-breaking spaces"""
        return u'&nbsp;'
    
    #MATH
    def do_math(self, node):
        response = self._stripNode(node.source)
        response = re.sub(r'\s*_{(\S+)}\s*', r'<sub>\1</sub>', response)
        response = re.sub(r'\s*\^{(\S+)}\s*', r'<sup>\1</sup>', response)
        response = re.sub(r'^\$\s*(.+)\$$', r'<code>\1</code>', response)
        return response
    
    do_ensuremath = do_math
    
