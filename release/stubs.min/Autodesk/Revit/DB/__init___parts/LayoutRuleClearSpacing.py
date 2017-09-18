class LayoutRuleClearSpacing(LayoutRule,IDisposable):
 """
 This class indicate the layout rule of a Beam System is Clear-Spacing.

 

 LayoutRuleClearSpacing(spacing: float,justifyType: BeamSystemJustifyType)
 """
 def Dispose(self):
  """ Dispose(self: LayoutRuleClearSpacing,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 def __new__(self,spacing,justifyType):
  """ __new__(cls: type,spacing: float,justifyType: BeamSystemJustifyType) """
  pass
 JustifyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the type of justification.



Get: JustifyType(self: LayoutRuleClearSpacing) -> BeamSystemJustifyType



Set: JustifyType(self: LayoutRuleClearSpacing)=value

"""

 Spacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or set the spacing of the beam system.



Get: Spacing(self: LayoutRuleClearSpacing) -> float



Set: Spacing(self: LayoutRuleClearSpacing)=value

"""


