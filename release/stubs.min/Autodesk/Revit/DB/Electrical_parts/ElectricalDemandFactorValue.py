class ElectricalDemandFactorValue(object,IDisposable):
 """
 This class represents values used by a particular demand factor definition.  Each instance

    corresponds to a row in a table of values.  These values are part of the ElectricalDemandFactorDefinition

    class.

 

 ElectricalDemandFactorValue(minRange: float,maxRange: float,factor: float)

 ElectricalDemandFactorValue()
 """
 def Dispose(self):
  """ Dispose(self: ElectricalDemandFactorValue) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElectricalDemandFactorValue,disposing: bool) """
  pass
 def SetMaxRangeToUnlimited(self):
  """
  SetMaxRangeToUnlimited(self: ElectricalDemandFactorValue)

   Sets the max range on the value to unlimited
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
 @staticmethod
 def __new__(self,minRange=None,maxRange=None,factor=None):
  """
  __new__(cls: type,minRange: float,maxRange: float,factor: float)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Factor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The demand factor for this demand factor value.  For example,objects 1 to 3 can have 100% demand factor.

   In the example above,the demand factor will be 1.0.



Get: Factor(self: ElectricalDemandFactorValue) -> float



Set: Factor(self: ElectricalDemandFactorValue)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ElectricalDemandFactorValue) -> bool



"""

 MaxRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum range for this demand factor value.  For example,objects 1 to 3 can have 100% demand factor.

   In the example above,the maximum range will be 3.



Get: MaxRange(self: ElectricalDemandFactorValue) -> float



Set: MaxRange(self: ElectricalDemandFactorValue)=value

"""

 MinRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum range for this demand factor value.  For example,objects 1 to 3 can have 100% demand factor.

   In the example above,the minimum range will be 1.



Get: MinRange(self: ElectricalDemandFactorValue) -> float



Set: MinRange(self: ElectricalDemandFactorValue)=value

"""


