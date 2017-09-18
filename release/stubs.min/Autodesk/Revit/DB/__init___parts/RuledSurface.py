class RuledSurface(Surface,IDisposable):
 """
 A ruled surface is created by sweeping a line between two profile curves or between a curve and a point (a point and a curve).
    Input curve(s) must be bounded or have natural bounds.
 """
 @staticmethod
 def Create(*__args):
  """
  Create(profileCurve1: Curve,profileCurve2: Curve) -> Surface
  
   Creates a Surface object coincident with the ruled surface joining two bounded 
    generating curves.
  
  
   profileCurve1: The first profile curve; must be bounded and non-degenerate.
   profileCurve2: The second profile curve; must be bounded and non-degenerate.
   Returns: The created surface. Note that this surface may not be of type RuledSurf.
  Create(profileCurve: Curve,point: XYZ) -> Surface
  
   Creates a Surface object coincident with the ruled surface joining a bounded 
    generating curve to a point.
  
  
   profileCurve: The profile curve; must be bounded and non-degenerate.
   point: The point.  Expected to lie within the Revit design limits 
    Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).
  
   Returns: The created surface. Note that this surface may not be of type RuledSurf.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Surface,A_0: bool) """
  pass
 def GetFirstProfileCurve(self):
  """
  GetFirstProfileCurve(self: RuledSurface) -> Curve
  
   Returns a copy of the first profile curve if it is set. If a point was used to 
    define the first profile,this function will return NULL.
  
   Returns: A copy of the first profile curve,if it exists.
  """
  pass
 def GetFirstProfilePoint(self):
  """
  GetFirstProfilePoint(self: RuledSurface) -> XYZ
  
   If a point was used to define the first profile,returns a copy of that point. 
    Otherwise return NULL.
  
   Returns: The first profile point if it was set,NULL otherwise.
  """
  pass
 def GetSecondProfileCurve(self):
  """
  GetSecondProfileCurve(self: RuledSurface) -> Curve
  
   Returns a copy of the second profile curve if it is set. If a point was used to 
    define the second profile,this function will return NULL.
  
   Returns: A copy of the second profile curve,if it exists.
  """
  pass
 def GetSecondProfilePoint(self):
  """
  GetSecondProfilePoint(self: RuledSurface) -> XYZ
  
   If a point was used to define the second profile,returns a copy of that point. 
    Otherwise return NULL.
  
   Returns: The second profile point if it was set,NULL otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Surface,disposing: bool) """
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
