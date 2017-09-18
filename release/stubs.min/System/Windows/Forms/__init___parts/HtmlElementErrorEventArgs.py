class HtmlElementErrorEventArgs(EventArgs):
 """ Provides data for the System.Windows.Forms.HtmlWindow.Error event. """
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the descriptive string corresponding to the error.



Get: Description(self: HtmlElementErrorEventArgs) -> str



"""

 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether this error has been handled by the application hosting the document.



Get: Handled(self: HtmlElementErrorEventArgs) -> bool



Set: Handled(self: HtmlElementErrorEventArgs)=value

"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the line of HTML script code on which the error occurred.



Get: LineNumber(self: HtmlElementErrorEventArgs) -> int



"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the document that generated the error.



Get: Url(self: HtmlElementErrorEventArgs) -> Uri



"""


