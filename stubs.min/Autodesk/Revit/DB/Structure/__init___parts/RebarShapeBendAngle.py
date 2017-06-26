class RebarShapeBendAngle(Enum,IComparable,IFormattable,IConvertible):
 """
 A bend in a rebar shape has an angular range
    specified by one of these values. The angles refer to
    the angle swept out by one segment as it is bent
    relative to another. That is,an "Obtuse" bend results
    in two segments that meet at an angle that is less
    than 90 degrees when measured internally. Put another
    way,to create an equilateral triangle,you would need
    two "Obtuse" bends.
 
 enum RebarShapeBendAngle,values: Acute (1),Obtuse (3),Right (2)
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
 Acute=None
 Obtuse=None
 Right=None
 value__=None

