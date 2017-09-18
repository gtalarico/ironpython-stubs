class CalendarDateRange(object,INotifyPropertyChanged):
 """
 Represents a range of dates in a System.Windows.Controls.Calendar.

 

 CalendarDateRange()

 CalendarDateRange(day: DateTime)

 CalendarDateRange(start: DateTime,end: DateTime)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,day: DateTime)

  __new__(cls: type,start: DateTime,end: DateTime)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last date in the represented range.



Get: End(self: CalendarDateRange) -> DateTime



Set: End(self: CalendarDateRange)=value

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first date in the represented range.



Get: Start(self: CalendarDateRange) -> DateTime



Set: Start(self: CalendarDateRange)=value

"""


 PropertyChanged=None

