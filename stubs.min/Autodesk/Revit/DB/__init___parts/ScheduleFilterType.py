class ScheduleFilterType(Enum,IComparable,IFormattable,IConvertible):
 """
 Type of schedule filter.
 
 enum ScheduleFilterType,values: BeginsWith (10),Contains (8),EndsWith (12),Equal (2),GreaterThan (4),GreaterThanOrEqual (5),HasParameter (1),Invalid (0),IsAssociatedWithGlobalParameter (14),IsNotAssociatedWithGlobalParameter (15),LessThan (6),LessThanOrEqual (7),NotBeginsWith (11),NotContains (9),NotEndsWith (13),NotEqual (3)
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
 BeginsWith=None
 Contains=None
 EndsWith=None
 Equal=None
 GreaterThan=None
 GreaterThanOrEqual=None
 HasParameter=None
 Invalid=None
 IsAssociatedWithGlobalParameter=None
 IsNotAssociatedWithGlobalParameter=None
 LessThan=None
 LessThanOrEqual=None
 NotBeginsWith=None
 NotContains=None
 NotEndsWith=None
 NotEqual=None
 value__=None

