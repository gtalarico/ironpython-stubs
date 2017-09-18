class Box(object,IEpsilonComparable[Box]):
 """
 Represents the value of a plane and three intervals in

    an orthogonal,oriented box that is not necessarily parallel to the world Y,X,Z axes.

 

 Box(bbox: BoundingBox)

 Box(basePlane: Plane,xSize: Interval,ySize: Interval,zSize: Interval)

 Box(basePlane: Plane,points: IEnumerable[Point3d])

 Box(basePlane: Plane,geometry: GeometryBase)

 Box(basePlane: Plane,boundingbox: BoundingBox)
 """
 def ClosestPoint(self,point):
  """
  ClosestPoint(self: Box,point: Point3d) -> Point3d

  

   Finds the closest point on or in the Box. The box should be Valid for this to work.

  

   point: Sample point.

   Returns: The point on or in the box that is closest to the sample point.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: Box,box: BoundingBox,strict: bool) -> bool

  

   Test a boundingbox for Box inclusion.

  

   box: Box to test.

   strict: If true,the boundingbox needs to be fully on the inside of this Box. 

     I.e. 

    coincident boxes will be considered 'outside'.

  

   Returns: true if the box is (strictly) on the inside of this Box.

  Contains(self: Box,box: Box) -> bool

  

   Test a box for Box inclusion. This is the same as calling Contains(box,false)

  

   box: Box to test.

   Returns: true if the box is on the inside of or coincident with this Box.

  Contains(self: Box,box: Box,strict: bool) -> bool

  

   Test a box for Box inclusion.

  

   box: Box to test.

   strict: If true,the box needs to be fully on the inside of this Box. 

     I.e. coincident 

    boxes will be considered 'outside'.

  

   Returns: true if the box is (strictly) on the inside of this Box.

  Contains(self: Box,point: Point3d) -> bool

  

   Determines whether a point is included in this box. This is the same as calling 

    Contains(point,false)

  

  

   point: Point to test.

   Returns: true if the point is on the inside of or coincident with this Box.

  Contains(self: Box,point: Point3d,strict: bool) -> bool

  

   Determines whether a point is included in this box.

  

   point: Point to test.

   strict: If true,the point needs to be fully on the inside of the Box. 

     I.e. coincident 

    points will be considered 'outside'.

  

   Returns: true if the point is (strictly) on the inside of this Box.

  Contains(self: Box,box: BoundingBox) -> bool

  

   Test a boundingbox for Box inclusion. This is the same as calling Contains(box,false)

  

   box: Box to test.

   Returns: true if the box is on the inside of or coincident with this Box.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Box,other: Box,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def FurthestPoint(self,point):
  """
  FurthestPoint(self: Box,point: Point3d) -> Point3d

  

   Finds the furthest point on the Box. The Box should be Valid for this to work properly.

  

   point: Sample point.

   Returns: The point on the box that is furthest from the sample point.
  """
  pass
 def GetCorners(self):
  """
  GetCorners(self: Box) -> Array[Point3d]

  

   Gets an array of the 8 corner points of this box.

   Returns: An array of 8 corners.
  """
  pass
 def Inflate(self,*__args):
  """
  Inflate(self: Box,xAmount: float,yAmount: float,zAmount: float)

   Inflates the box by a given offset in each direction.

     Inflating with negative 

    amounts may result in decreasing boxes.

     InValid boxes cannot be inflated.

  

  

   xAmount: Amount (in model units) to inflate this box in the x direction.

   yAmount: Amount (in model units) to inflate this box in the y direction.

   zAmount: Amount (in model units) to inflate this box in the z direction.

  Inflate(self: Box,amount: float)

   Inflates the box by a given offset in each direction.

     Inflating with negative 

    amounts may result in decreasing boxes. 

     InValid boxes cannot be inflated.

  

  

   amount: Amount (in model units) to inflate this box in all directions.
  """
  pass
 def MakeValid(self):
  """
  MakeValid(self: Box) -> bool

  

   Attempts to make the Box valid. This is not always possible.

   Returns: true if the box was made valid,or if it was valid to begin with. 

     false if the box 

    remains in a differently abled state.
  """
  pass
 def PointAt(self,x,y,z):
  """
  PointAt(self: Box,x: float,y: float,z: float) -> Point3d

  

   Evaluates the box volume at the given unitized parameters.

     The box has idealized 

    side length of 1x1x1.

  

  

   x: Unitized parameter (between 0 and 1 is inside the box) along box X direction.

   y: Unitized parameter (between 0 and 1 is inside the box) along box Y direction.

   z: Unitized parameter (between 0 and 1 is inside the box) along box Z direction.

   Returns: The point at (x,y,z).
  """
  pass
 def RepositionBasePlane(self,origin):
  """
  RepositionBasePlane(self: Box,origin: Point3d)

   Repositions the origin of the Base plane for this box without affecting 

     the 

    physical dimensions.

  

  

   origin: The new base plane origin.
  """
  pass
 def ToBrep(self):
  """
  ToBrep(self: Box) -> Brep

  

   Constructs a brep representation of this box.

   Returns: A Brep representation of this box or null.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Box,xform: Transform) -> bool

  

   Transforms this Box using a Transformation matrix. If the Transform does not preserve 

     

    Similarity,the dimensions of the resulting box cannot be trusted.

  

  

   xform: Transformation matrix to apply to this Box.

   Returns: true if the Box was successfully transformed,false if otherwise.
  """
  pass
 def Union(self,point):
  """
  Union(self: Box,point: Point3d)

   Constructs a union between this Box and the given point. 

     This grows the box in 

    directions so it contains the point.

  

  

   point: Point to include.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Box]() -> Box

  

  __new__(cls: type,bbox: BoundingBox)

  __new__(cls: type,basePlane: Plane,xSize: Interval,ySize: Interval,zSize: Interval)

  __new__(cls: type,basePlane: Plane,points: IEnumerable[Point3d])

  __new__(cls: type,basePlane: Plane,geometry: GeometryBase)

  __new__(cls: type,basePlane: Plane,boundingbox: BoundingBox)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total surface area of this box.



Get: Area(self: Box) -> float



"""

 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the world axis aligned Bounding box for this oriented box.



Get: BoundingBox(self: Box) -> BoundingBox



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point that is in the center of the box.



Get: Center(self: Box) -> Point3d



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the validity of this Box. Boxes are invalid when the base plane or any of 

   the dimension intervals are invalid or decreasing.



Get: IsValid(self: Box) -> bool



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the orientation plane for this Box.



Get: Plane(self: Box) -> Plane



Set: Plane(self: Box)=value

"""

 Volume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total volume of this box.



Get: Volume(self: Box) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Interval that describes the dimension of the 

   Box along the orientation plane X-Axis. Otherwise known as the Width of the Box.



Get: X(self: Box) -> Interval



Set: X(self: Box)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Interval that describes the dimension of the 

   Box along the orientation plane Y-Axis. Otherwise known as the Depth of the Box.



Get: Y(self: Box) -> Interval



Set: Y(self: Box)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Interval that describes the dimension of the 

   Box along the orientation plane Z-Axis. Otherwise known as the Height of the Box.



Get: Z(self: Box) -> Interval



Set: Z(self: Box)=value

"""


 Empty=None
 Unset=None

