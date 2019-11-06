class DpiChangedEventArgs(CancelEventArgs):
 # no doc
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DpiChangedEventArgs()

 def ToString(self):
  """ ToString(self: DpiChangedEventArgs) -> str """
  pass
 DeviceDpiNew=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeviceDpiNew(self: DpiChangedEventArgs) -> int

"""

 DeviceDpiOld=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeviceDpiOld(self: DpiChangedEventArgs) -> int

"""

 SuggestedRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SuggestedRectangle(self: DpiChangedEventArgs) -> Rectangle

"""


