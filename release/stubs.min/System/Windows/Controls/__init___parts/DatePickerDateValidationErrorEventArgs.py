class DatePickerDateValidationErrorEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DatePicker.DateValidationError event.

 

 DatePickerDateValidationErrorEventArgs(exception: Exception,text: str)
 """
 @staticmethod
 def __new__(self,exception,text):
  """ __new__(cls: type,exception: Exception,text: str) """
  pass
 Exception=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the initial exception associated with the System.Windows.Controls.DatePicker.DateValidationError event.



Get: Exception(self: DatePickerDateValidationErrorEventArgs) -> Exception



"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that caused the System.Windows.Controls.DatePicker.DateValidationError event.



Get: Text(self: DatePickerDateValidationErrorEventArgs) -> str



"""

 ThrowException=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether System.Windows.Controls.DatePickerDateValidationErrorEventArgs.Exception should be thrown.



Get: ThrowException(self: DatePickerDateValidationErrorEventArgs) -> bool



Set: ThrowException(self: DatePickerDateValidationErrorEventArgs)=value

"""


