class FormattableString(object,IFormattable):
 # no doc
 def GetArgument(self,index):
  """ GetArgument(self: FormattableString,index: int) -> object """
  pass
 def GetArguments(self):
  """ GetArguments(self: FormattableString) -> Array[object] """
  pass
 @staticmethod
 def Invariant(formattable):
  """ Invariant(formattable: FormattableString) -> str """
  pass
 def ToString(self,formatProvider=None):
  """
  ToString(self: FormattableString) -> str

  ToString(self: FormattableString,formatProvider: IFormatProvider) -> str
  """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 ArgumentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ArgumentCount(self: FormattableString) -> int



"""

 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Format(self: FormattableString) -> str



"""


