class TessellatedShapeBuilder(ShapeBuilder,IDisposable):
 """
 A class that permits structured building of geometry or
    a mesh from a collection of connected faces.
    Contains all closed face sets and custom precisions.
 
 TessellatedShapeBuilder()
 """
 def AddFace(self,face):
  """
  AddFace(self: TessellatedShapeBuilder,face: TessellatedFace)
   Adds a face to the currently open connected face set.
  
   face: Face to add. The 'face' parameter can be added only once,as its
     boundary 
    loops will be cleared while adding and 'face' will become unusable.
  """
  pass
 def AreTargetAndFallbackCompatible(self,target,fallback):
  """
  AreTargetAndFallbackCompatible(self: TessellatedShapeBuilder,target: TessellatedShapeBuilderTarget,fallback: TessellatedShapeBuilderFallback) -> bool
  
   Checks whether this combination of fallback and target parameters
     can be 
    used as a valid combination of inputs.
  
  
   target: What kind of geometrical objects should be built.
   fallback: What should be done if a geometrical object described by 'target'
     parameter 
    cannot be built using all data from all stored face sets.
  
   Returns: True if the combination of fallback and target are a valid combination,false
   
      otherwise.
  """
  pass
 def Build(self):
  """
  Build(self: TessellatedShapeBuilder)
   Builds the designated geometrical objects from the stored face sets. Stores the 
    result in this TessellatedShapeBuilder object.
  """
  pass
 def CancelConnectedFaceSet(self):
  """
  CancelConnectedFaceSet(self: TessellatedShapeBuilder)
   Cancels the current face set - i.e.,all data from it will be lost
     and the 
    builder will have no open connected face set anymore.
  """
  pass
 def Clear(self):
  """
  Clear(self: TessellatedShapeBuilder)
   Erases all face set and clears the logs,if any.
  """
  pass
 def CloseConnectedFaceSet(self):
  """
  CloseConnectedFaceSet(self: TessellatedShapeBuilder)
   Closes the currently open connected face set.
  """
  pass
 @staticmethod
 def CreateMeshByExtrusion(profileLoops,extrusionDirection,extrusionDistance,materialId):
  """ CreateMeshByExtrusion(profileLoops: IList[CurveLoop],extrusionDirection: XYZ,extrusionDistance: float,materialId: ElementId) -> MeshFromGeometryOperationResult """
  pass
 def Dispose(self):
  """ Dispose(self: ShapeBuilder,A_0: bool) """
  pass
 def DoesFaceHaveEnoughLoopsAndVertices(self,face):
  """
  DoesFaceHaveEnoughLoopsAndVertices(self: TessellatedShapeBuilder,face: TessellatedFace) -> bool
  
   Checks whether 'face' has enough loops and vertcies to be valid.
  
   face: The face to check.
  """
  pass
 def GetBuildResult(self):
  """
  GetBuildResult(self: TessellatedShapeBuilder) -> TessellatedShapeBuilderResult
  
   Get the built geometry,build status and other data stored in 
    TessellatedShapeBuilderResult. Clears the stored data.
  """
  pass
 def OpenConnectedFaceSet(self,isSolid):
  """
  OpenConnectedFaceSet(self: TessellatedShapeBuilder,isSolid: bool)
   Opens a new connected face set.
  
   isSolid: Whether the face set,which is being open,should be build as a solid or as a 
    void.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ShapeBuilder,disposing: bool) """
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
 Fallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines acceptable fallback if the desired type of geometry can't be built.

Get: Fallback(self: TessellatedShapeBuilder) -> TessellatedShapeBuilderFallback

Set: Fallback(self: TessellatedShapeBuilder)=value
"""

 GraphicsStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Optional - if set,the built geometry will use that graphics style.

Get: GraphicsStyleId(self: TessellatedShapeBuilder) -> ElementId

Set: GraphicsStyleId(self: TessellatedShapeBuilder)=value
"""

 IsFaceSetOpen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Flag whether the current set of connected faces is open and
   additional tessellation faces can be added to it.

Get: IsFaceSetOpen(self: TessellatedShapeBuilder) -> bool

"""

 LogInteger=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Integer value used for logging,if it is performed. Usually
   the number of the face set(s) in the IFC file,from which they
   are imported. Any value is acceptable.

Get: LogInteger(self: TessellatedShapeBuilder) -> int

Set: LogInteger(self: TessellatedShapeBuilder)=value
"""

 LogString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """String used for logging,if any. Usually the name of the file from which
   face sets were imported.

Get: LogString(self: TessellatedShapeBuilder) -> str

Set: LogString(self: TessellatedShapeBuilder)=value
"""

 NumberOfCompletedFaceSets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of completed face sets.

Get: NumberOfCompletedFaceSets(self: TessellatedShapeBuilder) -> int

"""

 OwnerInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """String used for logging,if any. Usually describes the element or object,which
   either defined or will own the geoemtrical objects to be built.

Get: OwnerInfo(self: TessellatedShapeBuilder) -> str

Set: OwnerInfo(self: TessellatedShapeBuilder)=value
"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Requests the type of geometry to be built.

Get: Target(self: TessellatedShapeBuilder) -> TessellatedShapeBuilderTarget

Set: Target(self: TessellatedShapeBuilder)=value
"""


