class TransactionStatus(Enum,IComparable,IFormattable,IConvertible):
 """
 An enumerated type listing the possible statuses associated with a Transaction,TransactionGroup,or SubTransaction,
    or the result of a particular method call on one of those objects.
 
 enum TransactionStatus,values: Committed (3),Error (5),Pending (4),Proceed (6),RolledBack (2),Started (1),Uninitialized (0)
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
 Committed=None
 Error=None
 Pending=None
 Proceed=None
 RolledBack=None
 Started=None
 Uninitialized=None
 value__=None

