class ViewDisplayDepthCueing(object,IDisposable):
 """ Represents the settings for depth cueing. """
 def Dispose(self):
  """ Dispose(self: ViewDisplayDepthCueing) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ViewDisplayDepthCueing,disposing: bool) """
  pass
 def SetStartEndPercentages(self,startPercentage,endPercentage):
  """
  SetStartEndPercentages(self: ViewDisplayDepthCueing,startPercentage: int,endPercentage: int)

   Sets start and end percentages.

  

   startPercentage: The start percentage defines where depth cueing starts.

   endPercentage: The end percentage defines where depth cueing ends.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 EnableDepthCueing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to enable depth cueing. False to disable it.



Get: EnableDepthCueing(self: ViewDisplayDepthCueing) -> bool



Set: EnableDepthCueing(self: ViewDisplayDepthCueing)=value

"""

 EndPercentage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The end percentage defines where depth cueing ends.

   Values between 0 and 100.



Get: EndPercentage(self: ViewDisplayDepthCueing) -> int



"""

 FadeTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fade to defines the maximum fading in per cent.

   Values between 0 and 100.



Get: FadeTo(self: ViewDisplayDepthCueing) -> int



Set: FadeTo(self: ViewDisplayDepthCueing)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ViewDisplayDepthCueing) -> bool



"""

 StartPercentage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The start percentage defines where depth cueing starts.

   Values between 0 and 100.



Get: StartPercentage(self: ViewDisplayDepthCueing) -> int



"""


