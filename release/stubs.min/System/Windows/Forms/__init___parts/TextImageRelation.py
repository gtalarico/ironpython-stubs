class TextImageRelation(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the position of the text and image relative to each other on a control.
 
 enum TextImageRelation,values: ImageAboveText (1),ImageBeforeText (4),Overlay (0),TextAboveImage (2),TextBeforeImage (8)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return TextImageRelation()

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
 ImageAboveText=None
 ImageBeforeText=None
 Overlay=None
 TextAboveImage=None
 TextBeforeImage=None
 value__=None

