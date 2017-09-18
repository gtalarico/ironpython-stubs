class LinkClickedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.RichTextBox.LinkClicked event.

 

 LinkClickedEventArgs(linkText: str)
 """
 @staticmethod
 def __new__(self,linkText):
  """ __new__(cls: type,linkText: str) """
  pass
 LinkText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text of the link being clicked.



Get: LinkText(self: LinkClickedEventArgs) -> str



"""


