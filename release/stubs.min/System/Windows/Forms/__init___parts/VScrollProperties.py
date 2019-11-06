class VScrollProperties(ScrollProperties):
 """
 Provides basic properties for the System.Windows.Forms.VScrollBar class.
 
 VScrollProperties(container: ScrollableControl)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return VScrollProperties()

 @staticmethod
 def __new__(self,container):
  """ __new__(cls: type,container: ScrollableControl) """
  pass
 ParentControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control to which this scroll information applies.

"""


