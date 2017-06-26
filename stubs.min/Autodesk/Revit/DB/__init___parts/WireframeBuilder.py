class WireframeBuilder(ShapeBuilder,IDisposable):
 """
 Constructs a shape representation consisting of points and curves. That shape would typically be stored in a DirectShape or a DirectShapeType object.
 
 WireframeBuilder()
 """
 def AddCurve(self,GCurve):
  """
  AddCurve(self: WireframeBuilder,GCurve: Curve)
   Add a curve to the shape representation stored in this WireframeBuilder.
  
   GCurve: The curve to be added.
  """
  pass
 def AddPoint(self,GPoint):
  """
  AddPoint(self: WireframeBuilder,GPoint: Point)
   Add a point to the shape representation stored in this WireframeBuilder.
  
   GPoint: The point to be added.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ShapeBuilder,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ShapeBuilder,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: WireframeBuilder)
   Clears the accumulated geometry.
  """
  pass
 @staticmethod
 def ValidateCurve(GCurve):
  """
  ValidateCurve(GCurve: Curve) -> bool
  
   Validates curve to be added to the wireframe shape being constructed. Used by 
    addCurve to validate input.
     This function may be used to pre-validate the 
    geometry being added to avoid an exception from AddCurve().
  
  
   GCurve: Curve object to be validated.
   Returns: True is %GCurve% is acceptable as a part of a wireframe shape representation 
    being built.
  """
  pass
 @staticmethod
 def ValidatePoint(GPoint):
  """
  ValidatePoint(GPoint: Point) -> bool
  
   Validates the point object to be added to the wireframe shape being 
    constructed. Used by AddPoint() to validate input.
  
  
   GPoint: Point object to be validated.
   Returns: True is %GPoint% is acceptable as a part of a wireframe shape representation 
    being built.
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
