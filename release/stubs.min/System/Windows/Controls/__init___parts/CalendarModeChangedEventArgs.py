class CalendarModeChangedEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Controls.Calendar.DisplayModeChanged event.

 

 CalendarModeChangedEventArgs(oldMode: CalendarMode,newMode: CalendarMode)
 """
 @staticmethod
 def __new__(self,oldMode,newMode):
  """ __new__(cls: type,oldMode: CalendarMode,newMode: CalendarMode) """
  pass
 NewMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new mode of the System.Windows.Controls.Calendar.



Get: NewMode(self: CalendarModeChangedEventArgs) -> CalendarMode



"""

 OldMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous mode of the System.Windows.Controls.Calendar.



Get: OldMode(self: CalendarModeChangedEventArgs) -> CalendarMode



"""


