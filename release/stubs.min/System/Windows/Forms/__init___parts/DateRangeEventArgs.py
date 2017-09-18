class DateRangeEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.MonthCalendar.DateChanged or System.Windows.Forms.MonthCalendar.DateSelected events of the System.Windows.Forms.MonthCalendar control.

 

 DateRangeEventArgs(start: DateTime,end: DateTime)
 """
 @staticmethod
 def __new__(self,start,end):
  """ __new__(cls: type,start: DateTime,end: DateTime) """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last date/time value in the range that the user has selected.



Get: End(self: DateRangeEventArgs) -> DateTime



"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first date/time value in the range that the user has selected.



Get: Start(self: DateRangeEventArgs) -> DateTime



"""


