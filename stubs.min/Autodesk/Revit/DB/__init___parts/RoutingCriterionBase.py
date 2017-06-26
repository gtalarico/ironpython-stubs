class RoutingCriterionBase(object,IDisposable):
 """ RoutingCriteriaBase is the base class for all routing criteria. """
 def Dispose(self):
  """ Dispose(self: RoutingCriterionBase) """
  pass
 def IsEqual(self,pOther):
  """
  IsEqual(self: RoutingCriterionBase,pOther: RoutingCriterionBase) -> bool
  
   Verify if two criteria are the same.
   Returns: True if the criterion is equal to the other,false otherwise
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RoutingCriterionBase,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RoutingCriterionBase) -> bool

"""


