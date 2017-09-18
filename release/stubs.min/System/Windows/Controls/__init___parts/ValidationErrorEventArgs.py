class ValidationErrorEventArgs(RoutedEventArgs):
 """ Provides information for the System.Windows.Controls.Validation.Error�attached event. """
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the error is a new error or an existing error that has now been cleared.



Get: Action(self: ValidationErrorEventArgs) -> ValidationErrorEventAction



"""

 Error=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the error that caused this System.Windows.Controls.Validation.Error event.



Get: Error(self: ValidationErrorEventArgs) -> ValidationError



"""


