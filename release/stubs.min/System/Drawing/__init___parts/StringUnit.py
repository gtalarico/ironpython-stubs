class StringUnit(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the units of measure for a text string.
 
 enum StringUnit,values: Display (1),Document (5),Em (32),Inch (4),Millimeter (6),Pixel (2),Point (3),World (0)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return StringUnit()

 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Display=None
 Document=None
 Em=None
 Inch=None
 Millimeter=None
 Pixel=None
 Point=None
 value__=None
 World=None

