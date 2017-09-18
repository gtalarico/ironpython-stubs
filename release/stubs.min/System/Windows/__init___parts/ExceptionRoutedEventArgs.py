class ExceptionRoutedEventArgs(RoutedEventArgs):
 """ Provides data for the  System.Windows.Controls.Image and System.Windows.Controls.MediaElement failed events. """
 ErrorException=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the exception that caused the error condition.

Get: ErrorException(self: ExceptionRoutedEventArgs) -> Exception

"""


