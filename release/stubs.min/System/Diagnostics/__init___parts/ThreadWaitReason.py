class ThreadWaitReason(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the reason a thread is waiting.

 

 enum ThreadWaitReason,values: EventPairHigh (7),EventPairLow (8),ExecutionDelay (4),Executive (0),FreePage (1),LpcReceive (9),LpcReply (10),PageIn (2),PageOut (12),Suspended (5),SystemAllocation (3),Unknown (13),UserRequest (6),VirtualMemory (11)
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
 EventPairHigh=None
 EventPairLow=None
 ExecutionDelay=None
 Executive=None
 FreePage=None
 LpcReceive=None
 LpcReply=None
 PageIn=None
 PageOut=None
 Suspended=None
 SystemAllocation=None
 Unknown=None
 UserRequest=None
 value__=None
 VirtualMemory=None

