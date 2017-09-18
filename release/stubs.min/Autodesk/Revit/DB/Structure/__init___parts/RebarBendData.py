class RebarBendData(object,IDisposable):
 """
 The values in this class provide a summary of information taken from the RebarBarType,RebarHookType,and RebarStyle.

 

 RebarBendData(barType: RebarBarType,hookType0: RebarHookType,hookType1: RebarHookType,style: RebarStyle,hookOrient0: RebarHookOrientation,hookOrient1: RebarHookOrientation)

 RebarBendData()
 """
 def Dispose(self):
  """ Dispose(self: RebarBendData) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarBendData,disposing: bool) """
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
 def __new__(self,barType=None,hookType0=None,hookType1=None,style=None,hookOrient0=None,hookOrient1=None):
  """
  __new__(cls: type,barType: RebarBarType,hookType0: RebarHookType,hookType1: RebarHookType,style: RebarStyle,hookOrient0: RebarHookOrientation,hookOrient1: RebarHookOrientation)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BarDiameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The diameter of the bar.



Get: BarDiameter(self: RebarBendData) -> float



Set: BarDiameter(self: RebarBendData)=value

"""

 BendRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The radius of all fillets,except hook fillets,in the Rebar shape.



Get: BendRadius(self: RebarBendData) -> float



Set: BendRadius(self: RebarBendData)=value

"""

 HookAngle0=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The angle of the hook at the start.



Get: HookAngle0(self: RebarBendData) -> int



Set: HookAngle0(self: RebarBendData)=value

"""

 HookAngle1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The angle of the hook at the end.



Get: HookAngle1(self: RebarBendData) -> int



Set: HookAngle1(self: RebarBendData)=value

"""

 HookBendRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The radius of the hook fillets in the Rebar shape.



Get: HookBendRadius(self: RebarBendData) -> float



Set: HookBendRadius(self: RebarBendData)=value

"""

 HookLength0=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The extension length of the hook at the start.



Get: HookLength0(self: RebarBendData) -> float



Set: HookLength0(self: RebarBendData)=value

"""

 HookLength1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The extension length of the hook at the end.



Get: HookLength1(self: RebarBendData) -> float



Set: HookLength1(self: RebarBendData)=value

"""

 HookOrient0=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The orientation of the hook at the start.



Get: HookOrient0(self: RebarBendData) -> RebarHookOrientation



Set: HookOrient0(self: RebarBendData)=value

"""

 HookOrient1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The orientation of the hook at the end.



Get: HookOrient1(self: RebarBendData) -> RebarHookOrientation



Set: HookOrient1(self: RebarBendData)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RebarBendData) -> bool



"""


