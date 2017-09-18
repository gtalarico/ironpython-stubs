class MeshingParameters(object,IDisposable):
 """
 Represents settings used for creating a mesh representation of a brep or surface.

 

 MeshingParameters()
 """
 def Dispose(self):
  """
  Dispose(self: MeshingParameters)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 @staticmethod
 def DocumentCurrentSetting(doc):
  """
  DocumentCurrentSetting(doc: RhinoDoc) -> MeshingParameters

  

   Gets the MeshingParameters that are currently set for a document.

     These are the 

    same settings that are shown in the DocumentProperties

     "mesh settings" user 

    interface.

  

  

   doc: A Rhino document to query.

   Returns: Meshing parameters of the document.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ComputeCurvature=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether or not surface curvature 

   data will be embedded in the mesh.



Get: ComputeCurvature(self: MeshingParameters) -> bool



Set: ComputeCurvature(self: MeshingParameters)=value

"""

 GridAmplification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the grid amplification factor. 

   Values lower than 1.0 will decrease the number of initial quads,

   values higher than 1.0 will increase the number of initial quads.



Get: GridAmplification(self: MeshingParameters) -> float



Set: GridAmplification(self: MeshingParameters)=value

"""

 GridAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowed angle difference (in radians) 

   for a single sampling quad. The angle pertains to the surface normals.



Get: GridAngle(self: MeshingParameters) -> float



Set: GridAngle(self: MeshingParameters)=value

"""

 GridAspectRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowed aspect ratio of sampling quads.



Get: GridAspectRatio(self: MeshingParameters) -> float



Set: GridAspectRatio(self: MeshingParameters)=value

"""

 GridMaxCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of grid quads in the initial sampling grid.



Get: GridMaxCount(self: MeshingParameters) -> int



Set: GridMaxCount(self: MeshingParameters)=value

"""

 GridMinCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum number of grid quads in the initial sampling grid.



Get: GridMinCount(self: MeshingParameters) -> int



Set: GridMinCount(self: MeshingParameters)=value

"""

 JaggedSeams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether or not the mesh is allowed to have jagged seams. 

   When this flag is set to true,meshes on either side of a Brep Edge will not match up.



Get: JaggedSeams(self: MeshingParameters) -> bool



Set: JaggedSeams(self: MeshingParameters)=value

"""

 MaximumEdgeLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowed mesh edge length.



Get: MaximumEdgeLength(self: MeshingParameters) -> float



Set: MaximumEdgeLength(self: MeshingParameters)=value

"""

 MinimumEdgeLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum allowed mesh edge length.



Get: MinimumEdgeLength(self: MeshingParameters) -> float



Set: MinimumEdgeLength(self: MeshingParameters)=value

"""

 MinimumTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum tolerance.



Get: MinimumTolerance(self: MeshingParameters) -> float



Set: MinimumTolerance(self: MeshingParameters)=value

"""

 RefineAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the mesh parameter refine angle.



Get: RefineAngle(self: MeshingParameters) -> float



Set: RefineAngle(self: MeshingParameters)=value

"""

 RefineGrid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether or not the sampling grid can be refined 

   when certain tolerances are not met.



Get: RefineGrid(self: MeshingParameters) -> bool



Set: RefineGrid(self: MeshingParameters)=value

"""

 RelativeTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the relative tolerance.



Get: RelativeTolerance(self: MeshingParameters) -> float



Set: RelativeTolerance(self: MeshingParameters)=value

"""

 SimplePlanes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether or not planar areas are allowed 

   to be meshed in a simplified manner.



Get: SimplePlanes(self: MeshingParameters) -> bool



Set: SimplePlanes(self: MeshingParameters)=value

"""

 Tolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowed edge deviation. 

   This tolerance is measured between the center of the mesh edge and the surface.



Get: Tolerance(self: MeshingParameters) -> float



Set: Tolerance(self: MeshingParameters)=value

"""


