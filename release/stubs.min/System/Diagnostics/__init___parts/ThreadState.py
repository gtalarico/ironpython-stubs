class ThreadState(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the current execution state of the thread.

 

 enum ThreadState,values: Initialized (0),Ready (1),Running (2),Standby (3),Terminated (4),Transition (6),Unknown (7),Wait (5)
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
 Initialized=None
 Ready=None
 Running=None
 Standby=None
 Terminated=None
 Transition=None
 Unknown=None
 value__=None
 Wait=None

