class DateBoldEventArgs(EventArgs):
 """ Provides data for events that are internal to the System.Windows.Forms.MonthCalendar control. """
 DaysToBold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets dates that are bold.



Get: DaysToBold(self: DateBoldEventArgs) -> Array[int]



Set: DaysToBold(self: DateBoldEventArgs)=value

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of dates that are bold.



Get: Size(self: DateBoldEventArgs) -> int



"""

 StartDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first date that is bold.



Get: StartDate(self: DateBoldEventArgs) -> DateTime



"""


