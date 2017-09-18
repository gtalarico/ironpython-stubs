class ScrollEventArgs(EventArgs):
 """
 Provides data for the Scroll event.

 

 ScrollEventArgs(type: ScrollEventType,newValue: int)

 ScrollEventArgs(type: ScrollEventType,newValue: int,scroll: ScrollOrientation)

 ScrollEventArgs(type: ScrollEventType,oldValue: int,newValue: int)

 ScrollEventArgs(type: ScrollEventType,oldValue: int,newValue: int,scroll: ScrollOrientation)
 """
 @staticmethod
 def __new__(self,type,*__args):
  """
  __new__(cls: type,type: ScrollEventType,newValue: int)

  __new__(cls: type,type: ScrollEventType,newValue: int,scroll: ScrollOrientation)

  __new__(cls: type,type: ScrollEventType,oldValue: int,newValue: int)

  __new__(cls: type,type: ScrollEventType,oldValue: int,newValue: int,scroll: ScrollOrientation)
  """
  pass
 NewValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the new System.Windows.Forms.ScrollBar.Value of the scroll bar.



Get: NewValue(self: ScrollEventArgs) -> int



Set: NewValue(self: ScrollEventArgs)=value

"""

 OldValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the old System.Windows.Forms.ScrollBar.Value of the scroll bar.



Get: OldValue(self: ScrollEventArgs) -> int



"""

 ScrollOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scroll bar orientation that raised the Scroll event.



Get: ScrollOrientation(self: ScrollEventArgs) -> ScrollOrientation



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of scroll event that occurred.



Get: Type(self: ScrollEventArgs) -> ScrollEventType



"""


