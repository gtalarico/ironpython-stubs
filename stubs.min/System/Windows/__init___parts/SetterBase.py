class SetterBase(object):
 """ Represents the base class for value setters. """
 def CheckSealed(self,*args):
  """
  CheckSealed(self: SetterBase)
   Checks whether this object is read-only and cannot be changed.
  """
  pass
 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this object is in an immutable state.

Get: IsSealed(self: SetterBase) -> bool

"""


