class IsoStatus(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines enumerated values for isoparametric curve direction on a surface,such as X or Y,

    and curve sides,such as North or West boundary.

    Note: odd values are all x-constant; even values > 0 are all y-constant.

 

 enum IsoStatus,values: East (5),None (0),North (6),South (4),West (3),X (1),Y (2)
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
 East=None
 None=None
 North=None
 South=None
 value__=None
 West=None
 X=None
 Y=None

