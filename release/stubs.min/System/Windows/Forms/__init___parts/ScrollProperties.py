class ScrollProperties(object):
 """ Encapsulates properties related to scrolling. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,container: ScrollableControl) """
  pass
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the scroll bar can be used on the container.



Get: Enabled(self: ScrollProperties) -> bool



Set: Enabled(self: ScrollProperties)=value

"""

 LargeChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance to move a scroll bar in response to a large scroll command.



Get: LargeChange(self: ScrollProperties) -> int



Set: LargeChange(self: ScrollProperties)=value

"""

 Maximum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the upper limit of the scrollable range.



Get: Maximum(self: ScrollProperties) -> int



Set: Maximum(self: ScrollProperties)=value

"""

 Minimum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lower limit of the scrollable range.



Get: Minimum(self: ScrollProperties) -> int



Set: Minimum(self: ScrollProperties)=value

"""

 ParentControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control to which this scroll information applies.



"""

 SmallChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance to move a scroll bar in response to a small scroll command.



Get: SmallChange(self: ScrollProperties) -> int



Set: SmallChange(self: ScrollProperties)=value

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a numeric value that represents the current position of the scroll bar box.



Get: Value(self: ScrollProperties) -> int



Set: Value(self: ScrollProperties)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the scroll bar can be seen by the user.



Get: Visible(self: ScrollProperties) -> bool



Set: Visible(self: ScrollProperties)=value

"""


