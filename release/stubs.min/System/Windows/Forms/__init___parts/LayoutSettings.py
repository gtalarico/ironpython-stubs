class LayoutSettings(object):
 """ Provides a base class for collecting layout scheme characteristics. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return LayoutSettings()

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current table layout engine.

Get: LayoutEngine(self: LayoutSettings) -> LayoutEngine

"""


