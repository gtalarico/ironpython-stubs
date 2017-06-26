class Edge(GeometryObject,IDisposable):
 """ An edge of a 3d solid. """
 def AsCurve(self):
  """
  AsCurve(self: Edge) -> Curve
  
   Returns a curve that corresponds to the edge's parametric orientation.
   Returns: It can be an Arc,Line,or HermiteSpline.
  """
  pass
 def AsCurveFollowingFace(self,faceForDir):
  """
  AsCurveFollowingFace(self: Edge,faceForDir: Face) -> Curve
  
   Returns a curve that corresponds to this edge as oriented in its topological 
    direction on the specified face.
  
  
   faceForDir: Specifies the face,on which the curve will follow the topological direction of 
    the edge.
  
   Returns: It can be an Arc,Line,or HermiteSpline.
  """
  pass
 def ComputeDerivatives(self,parameter):
  """
  ComputeDerivatives(self: Edge,parameter: float) -> Transform
  
   Returns the vectors describing the edge at the specified parameter.
  
   parameter: The parameter to be evaluated.
   Returns: The transformation containing a tangent vector,derivative of tangent vector,
    and bi-normal vector.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def Evaluate(self,param):
  """
  Evaluate(self: Edge,param: float) -> XYZ
  
   Evaluates a parameter on the edge.
  
   param: The parameter to be evaluated,in [0,1].
  """
  pass
 def EvaluateOnFace(self,param,face):
  """
  EvaluateOnFace(self: Edge,param: float,face: Face) -> UV
  
   Evaluates a parameter on the edge to produce UV coordinates on the face.
  
   param: The parameter to be evaluated,in [0,1].
   face: The face on which to perform the evaluation. Must belong to the edge.
  """
  pass
 def GetEndPointReference(self,index):
  """
  GetEndPointReference(self: Edge,index: int) -> Reference
  
   Returns a stable reference to the start or the end point of the edge.
  
   index: Use 0 for the start point; 1 for the end point.
   Returns: Reference to the point or ll if reference cannot be obtained.
  """
  pass
 def GetFace(self,index):
  """
  GetFace(self: Edge,index: int) -> Face
  
   Returns one of the two faces that meet at the edge.
  
   index: The index of the face (0 or 1).
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def Tessellate(self):
  """
  Tessellate(self: Edge) -> IList[XYZ]
  
   Returns a polyline approximation to the edge.
  """
  pass
 def TessellateOnFace(self,face):
  """
  TessellateOnFace(self: Edge,face: Face) -> IList[UV]
  
   Returns a polyline approximation to the edge in UV parameters of the face.
  
   face: The face on which to perform the tessellation. Must belong to the edge.
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
 ApproximateLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the approximate length of the edge.

Get: ApproximateLength(self: Edge) -> float

"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a stable reference to the edge.

Get: Reference(self: Edge) -> Reference

"""


