class Extrusion(Surface,IDisposable,ISerializable):
 """
 Represents an extrusion,or objects such as beams or linearly extruded elements,

    that can be represented by profile curves and two miter planes at the extremes.

 

 Extrusion()
 """
 def AddInnerProfile(self,innerProfile):
  """
  AddInnerProfile(self: Extrusion,innerProfile: Curve) -> bool

  

   Adds an inner profile.

  

   innerProfile: Closed curve in the XY plane or a 2d curve.

   Returns: true if the profile was set.
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
 @staticmethod
 def Create(planarCurve,height,cap):
  """
  Create(planarCurve: Curve,height: float,cap: bool) -> Extrusion

  

   Creates an extrusion of a 3d curve (which must be planar) and a height.

  

   planarCurve: Planar curve used as profile

   height: If the height > 0,the bottom of the extrusion will be in plane and

     the top will be 

    height units above the plane.

     If the height < 0,the top of the extrusion will be 

    in plane and

     the bottom will be height units below the plane.

     The 

    plane used is the one that is returned from the curve's TryGetPlane function.

  

   cap: If the curve is closed and cap is true,then the resulting extrusion is capped.

   Returns: If the input is valid,then a new extrusion is returned. Otherwise null is returned
  """
  pass
 @staticmethod
 def CreateCylinderExtrusion(cylinder,capBottom,capTop):
  """
  CreateCylinderExtrusion(cylinder: Cylinder,capBottom: bool,capTop: bool) -> Extrusion

  

   Gets an extrusion form of a cylinder.

  

   cylinder: IsFinite must be true.

   capBottom: If true,the end at cylinder.Height1 will be capped.

   capTop: If true,the end at cylinder.Height2 will be capped.

   Returns: Extrusion on success. null on failure.
  """
  pass
 @staticmethod
 def CreatePipeExtrusion(cylinder,otherRadius,capTop,capBottom):
  """
  CreatePipeExtrusion(cylinder: Cylinder,otherRadius: float,capTop: bool,capBottom: bool) -> Extrusion

  

   Gets an extrusion form of a pipe.

  

   cylinder: IsFinite must be true.

   otherRadius: If cylinder.Radius is less than other radius,then the cylinder will be the inside

     

    of the pipe.

  

   capTop: If true,the end at cylinder.Height2 will be capped.

   capBottom: If true,the end at cylinder.Height1 will be capped.

   Returns: Extrusion on success. null on failure.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

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
 def GetMesh(self,meshType):
  """
  GetMesh(self: Extrusion,meshType: MeshType) -> Mesh

  

   Obtains a reference to a specified type of mesh for this extrusion.

  

   meshType: The mesh type.

   Returns: A mesh.
  """
  pass
 def GetPathPlane(self,s):
  """
  GetPathPlane(self: Extrusion,s: float) -> Plane

  

   Gets the 3D plane perpendicular to the path at a normalized path parameter.

  

   s: 0.0=starting profile

     1.0=ending profile.

   Returns: A plane. The plane is Invalid on failure.
  """
  pass
 def GetProfilePlane(self,s):
  """
  GetProfilePlane(self: Extrusion,s: float) -> Plane

  

   Gets the 3D plane containing the profile curve at a normalized path parameter.

  

   s: 0.0=starting profile

     1.0=ending profile.

   Returns: A plane. The plane is Invalid on failure.
  """
  pass
 def GetProfileTransformation(self,s):
  """
  GetProfileTransformation(self: Extrusion,s: float) -> Transform

  

   Gets the transformation that maps the xy profile curve to its 3d location.

  

   s: 0.0=starting profile

     1.0=ending profile.

   Returns: A Transformation. The transform is Invalid on failure.
  """
  pass
 def GetWireframe(self):
  """
  GetWireframe(self: Extrusion) -> Array[Curve]

  

   Constructs all the Wireframe curves for this Extrusion.

   Returns: An array of Wireframe curves.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

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
 def PathLineCurve(self):
  """
  PathLineCurve(self: Extrusion) -> LineCurve

  

   Gets the line-like curve that is the conceptual axis of the extrusion.

   Returns: The path as a line curve.
  """
  pass
 def Profile3d(self,*__args):
  """
  Profile3d(self: Extrusion,ci: ComponentIndex) -> Curve

  

   Gets one of the profiles.

  

   ci: The index of this profile.

   Returns: The profile.

  Profile3d(self: Extrusion,profileIndex: int,s: float) -> Curve

  

   Gets a transversal isocurve of the extruded profile.

  

   profileIndex: 0 <= profileIndex < ProfileCount

     The outer profile has index 0.

   s: 0.0 <= s <= 1.0

     A relative parameter controling which profile is returned.

    

     0=bottom profile and 1=top profile.

  

   Returns: The profile.
  """
  pass
 def ProfileIndex(self,profileParameter):
  """
  ProfileIndex(self: Extrusion,profileParameter: float) -> int

  

   Gets the index of the profile curve at a domain related to a parameter.

  

   profileParameter: Parameter on profile curve.

   Returns: -1 if profileParameter does not correspond to a point on the profile curve.

     When 

    the profileParameter corresponds to the end of one profile and the

     beginning of the 

    next profile,the index of the next profile is returned.
  """
  pass
 def SetOuterProfile(self,outerProfile,cap):
  """
  SetOuterProfile(self: Extrusion,outerProfile: Curve,cap: bool) -> bool

  

   Sets the outer profile of the extrusion.

  

   outerProfile: curve in the XY plane or a 2D curve.

   cap: If outerProfile is a closed curve,then cap determines if the extrusion

     has end 

    caps. If outerProfile is an open curve,cap is ignored.

  

   Returns: true if the profile was set. If the outer profile is closed,then the

     extrusion may 

    also have inner profiles. If the outer profile is open,

     the extrusion may not have 

    inner profiles. If the extrusion already

     has a profile,the set will fail.
  """
  pass
 def SetPathAndUp(self,a,b,up):
  """
  SetPathAndUp(self: Extrusion,a: Point3d,b: Point3d,up: Vector3d) -> bool

  

   Allows to set the two points at the extremes and the up vector.

  

   a: The start point.

   b: The end point.

   up: The up vector.

   Returns: true if the operation succeeded; otherwise false.

     Setting up=a-b will make the 

    operation fail.
  """
  pass
 def ToBrep(self,splitKinkyFaces=None):
  """
  ToBrep(self: Extrusion,splitKinkyFaces: bool) -> Brep

  

   Constructs a brep form of the extrusion. The outer profile is always the first face of the brep.


    
     If there are inner profiles,additional brep faces are created for each profile. If 

    the

     outer profile is closed,then end caps are added as the last two faces of the 

    brep.

  

  

   splitKinkyFaces: If true and the profiles have kinks,then the faces corresponding to those profiles are split

    

        so they will be G1.

  

   Returns: A brep with a similar shape like this extrustion,or null on error.
  """
  pass
 def WallEdge(self,ci):
  """
  WallEdge(self: Extrusion,ci: ComponentIndex) -> Curve

  

   Gets one of the longitudinal curves along the beam or extrusion.

  

   ci: The index of this profile.

   Returns: The profile.
  """
  pass
 def WallSurface(self,ci):
  """
  WallSurface(self: Extrusion,ci: ComponentIndex) -> Surface

  

   Gets one of the longitudinal surfaces of the extrusion.

  

   ci: The index specifying which precise item to retrieve.

   Returns: The surface.
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 CapCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of capping surfaces.



Get: CapCount(self: Extrusion) -> int



"""

 IsCappedAtBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the surface that fills the bottom profile is existing.



Get: IsCappedAtBottom(self: Extrusion) -> bool



"""

 IsCappedAtTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the surface that fills the top profile is existing.



Get: IsCappedAtTop(self: Extrusion) -> bool



"""

 IsMiteredAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a miter plane at the end is defined.



Get: IsMiteredAtEnd(self: Extrusion) -> bool



"""

 IsMiteredAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a value indicating whether a miter plane at start is defined.



Get: IsMiteredAtStart(self: Extrusion) -> bool



"""

 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether there is no gap among all surfaces constructing this object.



Get: IsSolid(self: Extrusion) -> bool



"""

 MiterPlaneNormalAtEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the normal of the miter plane at the end in profile coordinates.

   In profile coordinates,0,0,1 always maps to the extrusion axis



Get: MiterPlaneNormalAtEnd(self: Extrusion) -> Vector3d



Set: MiterPlaneNormalAtEnd(self: Extrusion)=value

"""

 MiterPlaneNormalAtStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the normal of the miter plane at the start in profile coordinates.

   In profile coordinates,0,0,1 always maps to the extrusion axis



Get: MiterPlaneNormalAtStart(self: Extrusion) -> Vector3d



Set: MiterPlaneNormalAtStart(self: Extrusion)=value

"""

 PathEnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the end point of the path.



Get: PathEnd(self: Extrusion) -> Point3d



"""

 PathStart=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the start point of the path.



Get: PathStart(self: Extrusion) -> Point3d



"""

 PathTangent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the up vector of the path.



Get: PathTangent(self: Extrusion) -> Vector3d



"""

 ProfileCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of profile curves.



Get: ProfileCount(self: Extrusion) -> int



"""


