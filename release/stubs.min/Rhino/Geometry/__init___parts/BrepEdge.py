class BrepEdge(CurveProxy,IDisposable,ISerializable):
 """ Represents a single edge curve in a Brep object. """
 def AdjacentFaces(self):
  """
  AdjacentFaces(self: BrepEdge) -> Array[int]

  

   Gets the indices of all the BrepFaces that use this edge.
  """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Curve,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def GetEdgeParameter(self,trimIndex,trimParameter,edgeParameter):
  """
  GetEdgeParameter(self: BrepEdge,trimIndex: int,trimParameter: float) -> (bool,float)

  

   Get corresponding edge parameter for given trim at given trim parameter.

   Returns: true on success
  """
  pass
 def IsSmoothManifoldEdge(self,angleToleranceRadians):
  """
  IsSmoothManifoldEdge(self: BrepEdge,angleToleranceRadians: float) -> bool

  

   For a manifold,non-boundary edge,decides whether or not the two surfaces

     on 

    either side meet smoothly.

  

  

   angleToleranceRadians: used to decide if surface normals on either side are parallel.

   Returns: true if edge is manifold,has exactly 2 trims,and surface normals on either

     side 

    agree to within angle_tolerance.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: Curve)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def SetEdgeCurve(self,curve3dIndex,subDomain=None):
  """
  SetEdgeCurve(self: BrepEdge,curve3dIndex: int,subDomain: Interval) -> bool

  

   Set 3d curve geometry used by a b-rep edge.

  

   curve3dIndex: index of 3d curve in m_C3[] array

   Returns: true if successful

  SetEdgeCurve(self: BrepEdge,curve3dIndex: int) -> bool

  

   Set 3d curve geometry used by a b-rep edge.

  

   curve3dIndex: index of 3d curve in m_C3[] array

   Returns: true if successful
  """
  pass
 def TrimIndices(self):
  """
  TrimIndices(self: BrepEdge) -> Array[int]

  

   Gets the indices of all trims associated with this edge.

   Returns: Empty array on failure.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Brep that owns this edge.



Get: Brep(self: BrepEdge) -> Brep



"""

 EdgeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of this edge in the Brep.Edges collection.



Get: EdgeIndex(self: BrepEdge) -> int



"""

 EndVertex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """BrepVertex at end of edge



Get: EndVertex(self: BrepEdge) -> BrepVertex



"""

 StartVertex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """BrepVertex at start of edge



Get: StartVertex(self: BrepEdge) -> BrepVertex



"""

 Tolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the accuracy of the edge curve (>=0.0 or RhinoMath.UnsetValue)

    A value of UnsetValue indicates that the tolerance should be computed.

   

    The maximum distance from the edge's 3d curve to any surface of a face

    that has this edge as a portion of its boundary must be <= this tolerance.



Get: Tolerance(self: BrepEdge) -> float



Set: Tolerance(self: BrepEdge)=value

"""

 TrimCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of trim-curves that use this edge.



Get: TrimCount(self: BrepEdge) -> int



"""

 Valence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the topological valency of this edge. The topological valency 

   is defined by how many adjacent faces share this edge.



Get: Valence(self: BrepEdge) -> EdgeAdjacency



"""


