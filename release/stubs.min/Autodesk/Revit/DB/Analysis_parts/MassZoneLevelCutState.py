class MassZoneLevelCutState(Enum,IComparable,IFormattable,IConvertible):
 """
 The relationship between lower level or upper level and the MassZone.

    The MassZone is not intersected by this level,this level just happens to be the nearest upper or lower level.

    The MassZone was created by cutting its source geometry with this level.  The level cuts through the MassZone geometry.

    One or more faces of the MassZone are coincident with this level and the level does not otherwise cut through or intersect

    the MassZone geometry.

 

 enum MassZoneLevelCutState,values: Cut (1),NotCut (0),NotCutButCoincident (2)
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
 Cut=None
 NotCut=None
 NotCutButCoincident=None
 value__=None

