class FontFamilyMap(object):
 """
 Defines which System.Windows.Media.FontFamily to use for a specified set of Unicode code points and a culture-specific language.
 
 FontFamilyMap()
 """
 Language=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the culture-specific language for the System.Windows.Media.FontFamilyMap.

Get: Language(self: FontFamilyMap) -> XmlLanguage

Set: Language(self: FontFamilyMap)=value
"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font scale factor for the target System.Windows.Media.FontFamily.

Get: Scale(self: FontFamilyMap) -> float

Set: Scale(self: FontFamilyMap)=value
"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the target font family name for which the Unicode range applies to.

Get: Target(self: FontFamilyMap) -> str

Set: Target(self: FontFamilyMap)=value
"""

 Unicode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string value representing one or more Unicode code point ranges.

Get: Unicode(self: FontFamilyMap) -> str

Set: Unicode(self: FontFamilyMap)=value
"""


