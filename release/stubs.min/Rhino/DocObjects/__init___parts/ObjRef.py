class ObjRef(object,IDisposable):
 """
 Represents a reference to a Rhino object.

 

 ObjRef(id: Guid)

 ObjRef(rhinoObject: RhinoObject)

 ObjRef(rhinoObject: RhinoObject,pickContext: PickContext)
 """
 def Brep(self):
  """
  Brep(self: ObjRef) -> Brep

  

   Gets the brep if this reference geometry is one.

   Returns: A boundary representation; or null on error.
  """
  pass
 def ClippingPlaneSurface(self):
  """
  ClippingPlaneSurface(self: ObjRef) -> ClippingPlaneSurface

  

   Gets the clipping plane surface if this reference targeted one.

   Returns: A clipping plane surface,or null if this reference targeted something else.
  """
  pass
 def Curve(self):
  """
  Curve(self: ObjRef) -> Curve

  

   Gets the curve if this reference targeted one.

   Returns: A curve,or null if this reference targeted something else.
  """
  pass
 def CurveParameter(self,parameter):
  """
  CurveParameter(self: ObjRef) -> (Curve,float)

  

   If the reference geometry is a curve or edge with a selection

     point,then this gets 

    the parameter of the selection point.

  

   Returns: If the selection point was on a curve or edge,then the

     curve/edge is returned,

    otherwise null.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ObjRef)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def Edge(self):
  """
  Edge(self: ObjRef) -> BrepEdge

  

   Gets the edge if this reference geometry is one.

   Returns: A boundary representation edge; or null on error.
  """
  pass
 def Face(self):
  """
  Face(self: ObjRef) -> BrepFace

  

   If the referenced geometry is a brep face,a brep with one face,or

     a surface,this 

    returns the brep face.

  

   Returns: A boundary representation face; or null on error.
  """
  pass
 def Geometry(self):
  """
  Geometry(self: ObjRef) -> GeometryBase

  

   Gets the geometry linked to the object targeted by this reference.

   Returns: The geometry.
  """
  pass
 def Hatch(self):
  """
  Hatch(self: ObjRef) -> Hatch

  

   Gets the hatch if the referenced geometry is one.

   Returns: A hatch; or null if the referenced object is not a hatch
  """
  pass
 def Light(self):
  """
  Light(self: ObjRef) -> Light

  

   Gets the light if the referenced geometry is one.

   Returns: A light; or null if the referenced object is not a light,or on error.
  """
  pass
 def Mesh(self):
  """
  Mesh(self: ObjRef) -> Mesh

  

   Gets the mesh if the referenced geometry is one.

   Returns: A mesh; or null if the referenced object is not a mesh,or on error.
  """
  pass
 def Object(self):
  """
  Object(self: ObjRef) -> RhinoObject

  

   Returns the referenced Rhino object.
  """
  pass
 def Point(self):
  """
  Point(self: ObjRef) -> Point

  

   Gets the point if the referenced geometry is one.

   Returns: A point; or null if the referenced object is not a point,or on error.
  """
  pass
 def PointCloud(self):
  """
  PointCloud(self: ObjRef) -> PointCloud

  

   Gets the point cloud if the referenced geometry is one.

   Returns: A point cloud; or null if the referenced object is not a point cloud,or on error.
  """
  pass
 def SelectionMethod(self):
  """
  SelectionMethod(self: ObjRef) -> SelectionMethod

  

   Gets the method used to select this object.

   Returns: The method used to select this object.
  """
  pass
 def SelectionPoint(self):
  """
  SelectionPoint(self: ObjRef) -> Point3d

  

   If the object was selected by picking a point on it,then

     SelectionPoint() returns 

    the point where the selection

     occured,otherwise it returns Point3d.Unset.

  

   Returns: The point where the selection occured or Point3d.Unset on failure.
  """
  pass
 def SetSelectionComponent(self,componentIndex):
  """
  SetSelectionComponent(self: ObjRef,componentIndex: ComponentIndex)

   When an object is selected by picking a sub-object,SetSelectionComponent

     may be 

    used to identify the sub-object.
  """
  pass
 def Surface(self):
  """
  Surface(self: ObjRef) -> Surface

  

   Gets the surface if the referenced geometry is one.

   Returns: A surface; or null if the referenced object is not a surface,or on error.
  """
  pass
 def SurfaceParameter(self,u,v):
  """
  SurfaceParameter(self: ObjRef) -> (Surface,float,float)

  

   If the reference geometry is a surface,brep with one face,

     or surface edge with a 

    selection point,then this gets the 

     surface paramters of the selection point.

  

   Returns: If the selection point was on a surface,then the surface is returned.
  """
  pass
 def TextDot(self):
  """
  TextDot(self: ObjRef) -> TextDot

  

   Gets the text dot if the referenced geometry is one.

   Returns: A text dot; or null if the referenced object is not a text dot,or on error.
  """
  pass
 def TextEntity(self):
  """
  TextEntity(self: ObjRef) -> TextEntity

  

   Gets the text entity if the referenced geometry is one.

   Returns: A text entity; or null if the referenced object is not a text entity,or on error.
  """
  pass
 def Trim(self):
  """
  Trim(self: ObjRef) -> BrepTrim

  

   If the referenced geometry is an edge of a surface,

     this returns the associated 

    brep trim.

  

   Returns: A boundary representation trim; or null on error
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
 def __new__(self,*__args):
  """
  __new__(cls: type,id: Guid)

  __new__(cls: type,rhinoObject: RhinoObject)

  __new__(cls: type,rhinoObject: RhinoObject,pickContext: PickContext)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 GeometryComponentIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the component index of the referenced (sub) geometry.

   Some objects have subobjects that are valid pieces of geometry. For

   example,breps have edges and faces that are valid curves and surfaces.

   Each subobject has a component index that is > 0. The parent

   geometry has a component index=-1.



Get: GeometryComponentIndex(self: ObjRef) -> ComponentIndex



"""

 ObjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the id of the referenced Rhino object.



Get: ObjectId(self: ObjRef) -> Guid



"""

 RuntimeSerialNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If > 0,then this is the value of a Rhino object's serial number field.

   The serial number is used instead of the pointer to prevent crashes in

   cases when the RhinoObject is deleted but an ObjRef continues to reference

   the Rhino object. The value of RuntimeSerialNumber is not saved in archives

   because it generally changes if you save and reload an archive.



Get: RuntimeSerialNumber(self: ObjRef) -> UInt32



"""


