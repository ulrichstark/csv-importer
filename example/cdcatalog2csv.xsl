<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="text"/>
  <xsl:strip-space elements="*"/>
  <xsl:param name="sep" select="','"/>
  
  <xsl:template match="/">
    <xsl:value-of select="concat('&quot;title&quot;', $sep, '&quot;artist&quot;', $sep, '&quot;country&quot;', $sep, '&quot;company&quot;', $sep, 'price', $sep, 'year', '&#10;')"/>
    <xsl:for-each select="catalog/cd">
      <xsl:value-of select="concat('&quot;', title, '&quot;', $sep, '&quot;', artist, '&quot;', $sep, '&quot;',
country, '&quot;', $sep, '&quot;', company, '&quot;', $sep, price, $sep, year, '&#10;')"/>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>