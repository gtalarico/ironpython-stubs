class LightStyle(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines enumerated values to represent light styles or types,such as directional or spotlight.

 

 enum LightStyle,values: Ambient (10),CameraDirectional (4),CameraPoint (5),CameraSpot (6),None (0),WorldDirectional (7),WorldLinear (11),WorldPoint (8),WorldRectangular (12),WorldSpot (9)
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
 Ambient=None
 CameraDirectional=None
 CameraPoint=None
 CameraSpot=None
 None=None
 value__=None
 WorldDirectional=None
 WorldLinear=None
 WorldPoint=None
 WorldRectangular=None
 WorldSpot=None

