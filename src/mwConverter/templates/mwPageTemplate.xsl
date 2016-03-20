<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:plastex="http://plastex.sf.net/"> 
<xsl:output method="text"/>

<xsl:template match="/">
    <xsl:apply-templates select="dom-document"/>
</xsl:template>

<xsl:template match="dom-document">
    {{DISPLAYTITLE:<xsl:value-of select="normalize-space(title)"/>}}
    ''<xsl:value-of select="normalize-space(author)"/>, <xsl:value-of select="normalize-space(date)"/>''
    <xsl:apply-templates select="document"/>
</xsl:template>

<xsl:template match="document">
    <xsl:apply-templates select="par"/>
    <xsl:apply-templates select="section"/>
</xsl:template>

<xsl:template match="section">
    ==<xsl:value-of select="title"/>==
    <xsl:apply-templates select="par"/>
</xsl:template>

<xsl:template match="par">
    <xsl:value-of select="."/>
</xsl:template>


</xsl:stylesheet>