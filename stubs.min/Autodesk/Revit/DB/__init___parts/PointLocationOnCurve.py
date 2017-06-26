class PointLocationOnCurve(object,IDisposable):
 """
 Defines the measurement parameters necessary to create a point at a specific location on a curve.
 
 PointLocationOnCurve(measType: PointOnCurveMeasurementType,measValue: float,measFrom: PointOnCurveMeasureFrom)
 """
 def Dispose(self):
  """ Dispose(self: PointLocationOnCurve) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PointLocationOnCurve,disposing: bool) """
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
 def __new__(self,measType,measValue,measFrom):
  """ __new__(cls: type,measType: PointOnCurveMeasurementType,measValue: float,measFrom: PointOnCurveMeasureFrom) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointLocationOnCurve) -> bool

"""

 MeasureFrom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The location on the curve from which the measurement is taken.

Get: MeasureFrom(self: PointLocationOnCurve) -> PointOnCurveMeasureFrom

Set: MeasureFrom(self: PointLocationOnCurve)=value
"""

 MeasurementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The measurement type.

Get: MeasurementType(self: PointLocationOnCurve) -> PointOnCurveMeasurementType

Set: MeasurementType(self: PointLocationOnCurve)=value
"""

 MeasurementValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The measurement value.

Get: MeasurementValue(self: PointLocationOnCurve) -> float

Set: MeasurementValue(self: PointLocationOnCurve)=value
"""


