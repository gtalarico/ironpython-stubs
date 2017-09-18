class BoundingBox(object):
 """
 Represents the value of two points in a bounding box 

    defined by the two extreme corner points.

    This box is therefore aligned to the world X,Y and Z axes.

 

 BoundingBox(min: Point3d,max: Point3d)

 BoundingBox(minX: float,minY: float,minZ: float,maxX: float,maxY: float,maxZ: float)

 BoundingBox(points: IEnumerable[Point3d])
 """
 def ClosestPoint(self,point,includeInterior=None):
  """
  ClosestPoint(self: BoundingBox,point: Point3d,includeInterior: bool) -> Point3d

  

   Finds the closest point on or in the boundingbox.

  

   point: Sample point.

   includeInterior: If false,the point is projected onto the boundary faces only,

     otherwise the 

    interior of the box is also taken into consideration.

  

   Returns: The point on or in the box that is closest to the sample point.

  ClosestPoint(self: BoundingBox,point: Point3d) -> Point3d

  

   Finds the closest point on or in the boundingbox.

  

   point: Sample point.

   Returns: The point on or in the box that is closest to the sample point.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: BoundingBox,box: BoundingBox) -> bool

  

   Determines whether this boundingbox contains another boundingbox.

     This is the same 

    as calling Contains(box,false).

  

  

   box: Box to test.

   Returns: true if the box is on the inside of this boundingbox,or is coincident with the surface of it.

  Contains(self: BoundingBox,box: BoundingBox,strict: bool) -> bool

  

   Determines whether this boundingbox contains another boundingbox.

     The user can 

    choose how to treat boundingboxes with coincidents surfaces.

  

  

   box: Box to test.

   strict: If true,the box needs to be fully on the inside of the boundingbox. 

     I.e. 

    coincident boxes will be considered 'outside'.

  

   Returns: true if the box is (strictly) on the inside of this BoundingBox.

  Contains(self: BoundingBox,point: Point3d) -> bool

  

   Tests a point for boundingbox inclusion. This is the same as calling Contains(point,false)

  

   point: Point to test.

   Returns: true if the point is on the inside of or coincident with this boundingbox; otherwise false.

  Contains(self: BoundingBox,point: Point3d,strict: bool) -> bool

  

   Tests a point for BoundingBox inclusion.

  

   point: Point to test.

   strict: If true,the point needs to be fully on the inside of the BoundingBox. 

     I.e. 

    coincident points will be considered 'outside'.

  

   Returns: If 'strict' is affirmative,true if the point is inside this boundingbox; false if it is on the 

    surface or outside.If 'strict' is negative,true if the point is on the surface or on the inside 

    of the boundingbox; otherwise false.
  """
  pass
 def Corner(self,minX,minY,minZ):
  """
  Corner(self: BoundingBox,minX: bool,minY: bool,minZ: bool) -> Point3d

  

   Gets one of the eight corners of the box.

  

   minX: true for the minimum on the X axis; false for the maximum.

   minY: true for the minimum on the Y axis; false for the maximum.

   minZ: true for the minimum on the Z axis; false for the maximum.

   Returns: The requested point.
  """
  pass
 def FurthestPoint(self,point):
  """
  FurthestPoint(self: BoundingBox,point: Point3d) -> Point3d

  

   Finds the furthest point on the Box.

  

   point: Sample point.

   Returns: The point on the box that is furthest from the sample point.
  """
  pass
 def GetCorners(self):
  """
  GetCorners(self: BoundingBox) -> Array[Point3d]

  

   Gets an array filled with the 8 corner points of this box.

      See remarks for the 

    return order.

  

   Returns: An array of 8 corners.
  """
  pass
 def GetEdges(self):
  """
  GetEdges(self: BoundingBox) -> Array[Line]

  

   Gets an array of the 12 edges of this box.

   Returns: If the boundingbox IsValid,the 12 edges; otherwise,null.
  """
  pass
 def Inflate(self,*__args):
  """
  Inflate(self: BoundingBox,xAmount: float,yAmount: float,zAmount: float)

   Inflate the box with custom amounts in all directions. 

     Inflating with negative 

    amounts may result in decreasing boxes. 

     InValid boxes can not be inflated.

  

  

   xAmount: Amount (in model units) to inflate this box in the x direction.

   yAmount: Amount (in model units) to inflate this box in the y direction.

   zAmount: Amount (in model units) to inflate this box in the z direction.

  Inflate(self: BoundingBox,amount: float)

   Inflates the box with equal amounts in all directions. 

     Inflating with negative 

    amounts may result in decreasing boxes. 

     Invalid boxes can not be inflated.

  

  

   amount: Amount (in model units) to inflate this box in all directions.
  """
  pass
 @staticmethod
 def Intersection(a,b):
  """
  Intersection(a: BoundingBox,b: BoundingBox) -> BoundingBox

  

   Computes the intersection of two bounding boxes.

  

   a: A first bounding box.

   b: A second bounding box.

   Returns: The intersection bounding box.
  """
  pass
 def IsDegenerate(self,tolerance):
  """
  IsDegenerate(self: BoundingBox,tolerance: float) -> int

  

   Determines whether a bounding box is degenerate (flat) in one or more directions.

  

   tolerance: Distances <= tolerance will be considered to be zero.  If tolerance

     is negative 

    (default),then a scale invarient tolerance is used.

  

   Returns: 0=box is not degenerate

     1=box is a rectangle (degenerate in one direction).

     

       2=box is a line (degenerate in two directions).

     3=box is a point 

    (degenerate in three directions)

     4=box is not valid.
  """
  pass
 def MakeValid(self):
  """
  MakeValid(self: BoundingBox) -> bool

  

   Ensures that the box is defined in an increasing fashion along X,Y and Z axes.

     If 

    the Min or Max points are unset,this function will not change the box.

  

   Returns: true if the box was made valid,false if the box could not be made valid.
  """
  pass
 def PointAt(self,tx,ty,tz):
  """
  PointAt(self: BoundingBox,tx: float,ty: float,tz: float) -> Point3d

  

   Evaluates the boundingbox with normalized parameters.

     The box has idealized side 

    length of 1x1x1.

  

  

   tx: Normalized (between 0 and 1 is inside the box) parameter along the X direction.

   ty: Normalized (between 0 and 1 is inside the box) parameter along the Y direction.

   tz: Normalized (between 0 and 1 is inside the box) parameter along the Z direction.

   Returns: The point at the {tx,ty,tz} parameters.
  """
  pass
 def ToBrep(self):
  """
  ToBrep(self: BoundingBox) -> Brep

  

   Constructs a Rhino.Geometry.Brep representation of this boundingbox.

   Returns: If this operation is sucessfull,a Brep representation of this box; otherwise null.
  """
  pass
 def ToString(self):
  """
  ToString(self: BoundingBox) -> str

  

   Constructs the string representation of this aligned boundingbox.

   Returns: Text.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: BoundingBox,xform: Transform) -> bool

  

   Updates this boundingbox to be the smallest axis aligned

     boundingbox that contains 

    the transformed result of its 8 original corner

     points.

  

  

   xform: A transform.

   Returns: true if this operation is sucessfull; otherwise false.
  """
  pass
 def Union(self,*__args):
  """
  Union(a: BoundingBox,b: BoundingBox) -> BoundingBox

  

   Returns a new BoundingBox that represents the union of boxes a and b.

  

   a: First box to include in union.

   b: Second box to include in union.

   Returns: The BoundingBox that contains both a and b.

  Union(box: BoundingBox,point: Point3d) -> BoundingBox

  

   Returns a new BoundingBox that represents the union of a bounding box and a point.

  

   box: Box to include in the union.

   point: Point to include in the union.

   Returns: The BoundingBox that contains both the box and the point.

  Union(self: BoundingBox,other: BoundingBox)

   Updates this BoundingBox to represent the union of itself and another box.

  

   other: Box to include in this union.

  Union(self: BoundingBox,point: Point3d)

   Updates this BoundingBox to represent the union of itself and a point.

  

   point: Point to include in the union.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[BoundingBox]() -> BoundingBox

  

  __new__(cls: type,min: Point3d,max: Point3d)

  __new__(cls: type,minX: float,minY: float,minZ: float,maxX: float,maxY: float,maxZ: float)

  __new__(cls: type,points: IEnumerable[Point3d])
  """
  pass
 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point in the center of the boundingbox.



Get: Center(self: BoundingBox) -> Point3d



"""

 Diagonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the diagonal vector of this BoundingBox. 

   The diagonal connects the Min and Max points.



Get: Diagonal(self: BoundingBox) -> Vector3d



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether or not this boundingbox is valid. 

   Empty boxes are not valid,and neither are boxes with unset points.



Get: IsValid(self: BoundingBox) -> bool



"""

 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the point in the maximal corner.



Get: Max(self: BoundingBox) -> Point3d



Set: Max(self: BoundingBox)=value

"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the point in the minimal corner.



Get: Min(self: BoundingBox) -> Point3d



Set: Min(self: BoundingBox)=value

"""


 Empty=None
 Unset=None

