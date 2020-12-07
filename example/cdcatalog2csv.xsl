<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="text"/>
  <xsl:strip-space elements="*"/>
  <xsl:param name="sep" select="','"/>
  <xsl:template match="/">
    <xsl:value-of select="concat('"title"', $sep, '"artist"', $sep, '"country"', $sep, '"company"', $sep, 'price', $sep, 'year', ' ')"/>
    <xsl:for-each select="catalog/cd">
      <xsl:value-of select="concat('"', title, '"', $sep, '"', artist, '"', $sep, '"', country, '"', $sep, '"', company, '"', $sep, price, $sep, year, ' ')"/>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>