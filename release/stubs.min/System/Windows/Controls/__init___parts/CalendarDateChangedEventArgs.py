class CalendarDateChangedEventArgs(RoutedEventArgs):
 """ Provides data for the System.Windows.Controls.Calendar.DisplayDateChanged event. """
 AddedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the date to be newly displayed.



Get: AddedDate(self: CalendarDateChangedEventArgs) -> Nullable[DateTime]



"""

 RemovedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the date that was previously displayed.



Get: RemovedDate(self: CalendarDateChangedEventArgs) -> Nullable[DateTime]



"""


