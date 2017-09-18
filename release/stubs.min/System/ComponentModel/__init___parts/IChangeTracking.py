class IChangeTracking:
 """ Defines the mechanism for querying the object for changes and resetting of the changed status. """
 def AcceptChanges(self):
  """
  AcceptChanges(self: IChangeTracking)

    """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 IsChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object's changed status.



Get: IsChanged(self: IChangeTracking) -> bool



"""


