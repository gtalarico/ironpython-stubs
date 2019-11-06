class HScrollProperties(ScrollProperties):
 """
 Provides basic properties for the System.Windows.Forms.HScrollBar
 
 HScrollProperties(container: ScrollableControl)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return HScrollProperties()

 @staticmethod
 def __new__(self,container):
  """ __new__(cls: type,container: ScrollableControl) """
  pass
 ParentControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control to which this scroll information applies.

"""


