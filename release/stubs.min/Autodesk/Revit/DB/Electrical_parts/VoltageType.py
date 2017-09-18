class VoltageType(ElementType,IDisposable):
 """
 Represents electrical voltage type. An electrical voltage type define a range of voltages,

 and circuits can be created between components with rated voltages that do not precisely match the voltage definition value.
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetVoltageValue(self,actualValue,minValue,maxValue):
  """
  SetVoltageValue(self: VoltageType,actualValue: float,minValue: float,maxValue: float)

   Assign new values to modify voltage type,all of the unit are volt.
  """
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
 ActualValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get actual voltage value of this voltage definition,the unit is volt.



Get: ActualValue(self: VoltageType) -> float



"""

 IsInUse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this voltage type is in service now,such as by other distribution system.



Get: IsInUse(self: VoltageType) -> bool



"""

 MaxValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get upper boundary of voltage value of this voltage definition,the unit is volt.



Get: MaxValue(self: VoltageType) -> float



"""

 MinValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get lower boundary of voltage value of this voltage definition,the unit is volt.



Get: MinValue(self: VoltageType) -> float



"""


