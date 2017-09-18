class SourceLevels(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the levels of trace messages filtered by the source switch and event type filter.

 

 enum (flags) SourceLevels,values: ActivityTracing (65280),All (-1),Critical (1),Error (3),Information (15),Off (0),Verbose (31),Warning (7)
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
 ActivityTracing=None
 All=None
 Critical=None
 Error=None
 Information=None
 Off=None
 value__=None
 Verbose=None
 Warning=None

