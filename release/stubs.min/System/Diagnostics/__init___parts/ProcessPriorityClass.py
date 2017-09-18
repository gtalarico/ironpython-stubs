class ProcessPriorityClass(Enum,IComparable,IFormattable,IConvertible):
 """
 Indicates the priority that the system associates with a process. This value,together with the priority value of each thread of the process,determines each thread's base priority level.

 

 enum ProcessPriorityClass,values: AboveNormal (32768),BelowNormal (16384),High (128),Idle (64),Normal (32),RealTime (256)
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
 AboveNormal=None
 BelowNormal=None
 High=None
 Idle=None
 Normal=None
 RealTime=None
 value__=None

