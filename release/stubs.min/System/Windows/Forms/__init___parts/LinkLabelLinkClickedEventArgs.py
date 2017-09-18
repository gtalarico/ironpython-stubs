class LinkLabelLinkClickedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.LinkLabel.LinkClicked event.

 

 LinkLabelLinkClickedEventArgs(link: Link)

 LinkLabelLinkClickedEventArgs(link: Link,button: MouseButtons)
 """
 @staticmethod
 def __new__(self,link,button=None):
  """
  __new__(cls: type,link: Link)

  __new__(cls: type,link: Link,button: MouseButtons)
  """
  pass
 Button=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the mouse button that causes the link to be clicked.



Get: Button(self: LinkLabelLinkClickedEventArgs) -> MouseButtons



"""

 Link=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.LinkLabel.Link that was clicked.



Get: Link(self: LinkLabelLinkClickedEventArgs) -> Link



"""


