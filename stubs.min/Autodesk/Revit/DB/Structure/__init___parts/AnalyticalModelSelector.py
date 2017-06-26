class AnalyticalModelSelector(object,IDisposable):
 """
 Defines a portion of an Analytical Model for an Element.
 
 AnalyticalModelSelector(curve: Curve)
 AnalyticalModelSelector(curve: Curve,inCurveSelector: AnalyticalCurveSelector)
 AnalyticalModelSelector()
 AnalyticalModelSelector(inCurveSelector: AnalyticalCurveSelector)
 """
 def Dispose(self):
  """ Dispose(self: AnalyticalModelSelector) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalyticalModelSelector,disposing: bool) """
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,curve: Curve)
  __new__(cls: type,curve: Curve,inCurveSelector: AnalyticalCurveSelector)
  __new__(cls: type)
  __new__(cls: type,inCurveSelector: AnalyticalCurveSelector)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CurveSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The portion of the curve to be selected.

Get: CurveSelector(self: AnalyticalModelSelector) -> AnalyticalCurveSelector

Set: CurveSelector(self: AnalyticalModelSelector)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalyticalModelSelector) -> bool

"""


