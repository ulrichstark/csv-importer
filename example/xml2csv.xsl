<?xml version="1.0" encoding="UTF-8"?>
<!-- XSLT-Programm zur Transformation von XML-Dateien ins das csv 
  Dieses Stylesheet transformiert aus beliebigen XML-Dateien Elemente aus 
  Tiefe 3 in csv-Spalten und verwendet die Elementnamen dieser Ebene als 
  Spaltenüberschrift in der 1. Zeile.
  Parameter:
  q=Quotierungszeichen für die Spaltenwerte, 
  lf=Zeilentrennzeichen/-string
  sep=Spaltentrennzeichen/-string 
  (C) 2020-12-07 u.schaefer@oth-aw.de -->
  
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text"/>
  <xsl:strip-space elements="*"/>
  <xsl:param name="sep" select="','"/>
  <xsl:param name="q" select="'&quot;'"/>
  <xsl:param name="lf" select="'&#10;'"/>

  <xsl:template match="/">
    <xsl:for-each select="*/*[1]/*">
      <xsl:value-of select="concat($q, name(), $q)"/>
      <xsl:if test="position()!=last()"><xsl:value-of select="$sep"/></xsl:if>
    </xsl:for-each>
    <xsl:value-of select="$lf"/>
    <xsl:apply-templates select="*/*"/>
  </xsl:template>

  <xsl:template match="*">
    <xsl:for-each select="*">
      <xsl:value-of select="concat($q, text(), $q)"/>
      <xsl:if test="position()!=last()"><xsl:value-of select="$sep"/></xsl:if>
    </xsl:for-each>
    <xsl:value-of select="$lf"/>
  </xsl:template>

</xsl:stylesheet>

