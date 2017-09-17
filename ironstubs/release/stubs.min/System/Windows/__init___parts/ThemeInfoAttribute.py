class ThemeInfoAttribute(Attribute,_Attribute):
 """
 Specifies the location in which theme dictionaries are stored for an assembly.
 
 ThemeInfoAttribute(themeDictionaryLocation: ResourceDictionaryLocation,genericDictionaryLocation: ResourceDictionaryLocation)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,themeDictionaryLocation,genericDictionaryLocation):
  """ __new__(cls: type,themeDictionaryLocation: ResourceDictionaryLocation,genericDictionaryLocation: ResourceDictionaryLocation) """
  pass
 GenericDictionaryLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of generic,not theme specific,resources.

Get: GenericDictionaryLocation(self: ThemeInfoAttribute) -> ResourceDictionaryLocation

"""

 ThemeDictionaryLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location of theme specific resources.

Get: ThemeDictionaryLocation(self: ThemeInfoAttribute) -> ResourceDictionaryLocation

"""


