class BaseLoadOn(Enum,IComparable,IFormattable,IConvertible):
 """
 An enumerated type listing all the possible power load use types for a space object.
 
 enum BaseLoadOn,values: kNoOfBaseLoadOnMethods (3),kUseActualLoad (2),kUseCalculatedLoad (1),kUseDefaultLoad (-1),kUseEnteredLoad (0)
 """
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
 kNoOfBaseLoadOnMethods=None
 kUseActualLoad=None
 kUseCalculatedLoad=None
 kUseDefaultLoad=None
 kUseEnteredLoad=None
 value__=None

