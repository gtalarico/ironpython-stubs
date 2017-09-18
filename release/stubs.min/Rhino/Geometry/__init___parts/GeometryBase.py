class GeometryBase(CommonObject,IDisposable,ISerializable):
 """ Provides a common base for most geometric classes. This class is abstract. """
 def ComponentIndex(self):
  """
  ComponentIndex(self: GeometryBase) -> ComponentIndex

  

   If this piece of geometry is a component in something larger,like a BrepEdge

     in a 

    Brep,then this function returns the component index.

  

   Returns: This object's component index.  If this object is not a sub-piece of a larger

     

    geometric entity,then the returned index has 

     m_type=ComponentIndex.InvalidType

  

       and m_index=-1.
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
 def Duplicate(self):
  """
  Duplicate(self: GeometryBase) -> GeometryBase

  

   Constructs a deep (full) copy of this object.

   Returns: An object of the same type as this,with the same properties and behavior.
  """
  pass
 def DuplicateShallow(self):
  """
  DuplicateShallow(self: GeometryBase) -> GeometryBase

  

   Constructs a light copy of this object. By "light",it is meant that the same

     

    underlying data is used until something is done to attempt to change it. For example,

      

      you could have a shallow copy of a very heavy mesh object and the same underlying

     

    data will be used when doing things like inspecting the number of faces on the mesh.

       

     If you modify the location of one of the mesh vertices,the shallow copy will create

      

      a full duplicate of the underlying mesh data and the shallow copy will become a

     

    deep copy.

  

   Returns: An object of the same type as this object.

     This behavior is overridden by 

    implementing classes.
  """
  pass
 def GetBoundingBox(self,*__args):
  """
  GetBoundingBox(self: GeometryBase,plane: Plane) -> BoundingBox

  

   Aligned Boundingbox solver. Gets the plane aligned boundingbox.

  

   plane: Orientation plane for BoundingBox.

   Returns: A BoundingBox in plane coordinates.

  GetBoundingBox(self: GeometryBase,plane: Plane) -> (BoundingBox,Box)

  

   Aligned Boundingbox solver. Gets the plane aligned boundingbox.

  

   plane: Orientation plane for BoundingBox.

   Returns: A BoundingBox in plane coordinates.

  GetBoundingBox(self: GeometryBase,accurate: bool) -> BoundingBox

  

   Boundingbox solver. Gets the world axis aligned boundingbox for the geometry.

  

   accurate: If true,a physically accurate boundingbox will be computed. 

     If not,a boundingbox 

    estimate will be computed. For some geometry types there is no 

     difference between 

    the estimate and the accurate boundingbox. Estimated boundingboxes 

     can be computed 

    much (much) faster than accurate (or "tight") bounding boxes. 

     Estimated bounding 

    boxes are always similar to or larger than accurate bounding boxes.

  

   Returns: The boundingbox of the geometry in world coordinates or BoundingBox.Empty 

     if not 

    bounding box could be found.

  

  GetBoundingBox(self: GeometryBase,xform: Transform) -> BoundingBox

  

   Aligned Boundingbox solver. Gets the world axis aligned boundingbox for the transformed geometry.

  

   xform: Transformation to apply to object prior to the BoundingBox computation. 

     The 

    geometry itself is not modified.

  

   Returns: The accurate boundingbox of the transformed geometry in world coordinates 

     or 

    BoundingBox.Empty if not bounding box could be found.
  """
  pass
 def GetUserString(self,key):
  """
  GetUserString(self: GeometryBase,key: str) -> str

  

   Gets user string from this geometry.

  

   key: id used to retrieve the string.

   Returns: string associated with the key if successful. null if no key was found.
  """
  pass
 def GetUserStrings(self):
  """
  GetUserStrings(self: GeometryBase) -> NameValueCollection

  

   Gets a copy of all (user key string,user value string) pairs attached to this geometry.

   Returns: A new collection.
  """
  pass
 def MakeDeformable(self):
  """
  MakeDeformable(self: GeometryBase) -> bool

  

   If possible,converts the object into a form that can be accurately modified

     with 

    "squishy" transformations like projections,shears,an non-uniform scaling.

  

   Returns: false if object cannot be converted to a deformable object. true if object was

     

    already deformable or was converted into a deformable object.
  """
  pass
 def MemoryEstimate(self):
  """
  MemoryEstimate(self: GeometryBase) -> UInt32

  

   Computes an estimate of the number of bytes that this object is using in memory.

   Returns: An estimated memory footprint.
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
 def Rotate(self,angleRadians,rotationAxis,rotationCenter):
  """
  Rotate(self: GeometryBase,angleRadians: float,rotationAxis: Vector3d,rotationCenter: Point3d) -> bool

  

   Rotates the object about the specified axis. A positive rotation 

     angle results in 

    a counter-clockwise rotation about the axis (right hand rule).

  

  

   angleRadians: Angle of rotation in radians.

   rotationAxis: Direction of the axis of rotation.

   rotationCenter: Point on the axis of rotation.

   Returns: true if geometry successfully rotated.
  """
  pass
 def Scale(self,scaleFactor):
  """
  Scale(self: GeometryBase,scaleFactor: float) -> bool

  

   Scales the object by the specified factor. The scale is centered at the origin.

  

   scaleFactor: The uniform scaling factor.

   Returns: true if geometry successfully scaled.
  """
  pass
 def SetUserString(self,key,value):
  """
  SetUserString(self: GeometryBase,key: str,value: str) -> bool

  

   Attach a user string (key,value combination) to this geometry.

  

   key: id used to retrieve this string.

   value: string associated with key.

   Returns: true on success.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: GeometryBase,xform: Transform) -> bool

  

   Transforms the geometry. If the input Transform has a SimilarityType of

     

    OrientationReversing,you may want to consider flipping the transformed

     geometry 

    after calling this function when it makes sense. For example,

     you may want to call 

    Flip() on a Brep after transforming it.

  

  

   xform: Transformation to apply to geometry.

   Returns: true if geometry successfully transformed.
  """
  pass
 def Translate(self,*__args):
  """
  Translate(self: GeometryBase,x: float,y: float,z: float) -> bool

  

   Translates the object along the specified vector.

  

   x: The X component.

   y: The Y component.

   z: The Z component.

   Returns: true if geometry successfully translated.

  Translate(self: GeometryBase,translationVector: Vector3d) -> bool

  

   Translates the object along the specified vector.

  

   translationVector: A moving vector.

   Returns: true if geometry successfully translated.
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
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,info: SerializationInfo,context: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
 HasBrepForm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if the Brep.TryConvertBrep function will be successful for this object



Get: HasBrepForm(self: GeometryBase) -> bool



"""

 IsDeformable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if object can be accurately modified with "squishy" transformations like

   projections,shears,and non-uniform scaling.



Get: IsDeformable(self: GeometryBase) -> bool



"""

 IsDocumentControlled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true this object may not be modified. Any properties or functions that attempt

   to modify this object when it is set to "IsReadOnly" will throw a NotSupportedException.



Get: IsDocumentControlled(self: GeometryBase) -> bool



"""

 ObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Useful for switch statements that need to differentiate between

   basic object types like points,curves,surfaces,and so on.



Get: ObjectType(self: GeometryBase) -> ObjectType



"""

 UserStringCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of user strings.



Get: UserStringCount(self: GeometryBase) -> int



"""


