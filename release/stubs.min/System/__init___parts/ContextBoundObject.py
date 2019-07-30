class ContextBoundObject(MarshalByRefObject):
 """ Defines the base class for all context-bound classes. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ContextBoundObject()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
