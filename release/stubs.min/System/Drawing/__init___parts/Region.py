class Region(MarshalByRefObject,IDisposable):
 """
 Describes the interior of a graphics shape composed of rectangles and paths. This class cannot be inherited.

 

 Region()

 Region(rect: Rectangle)

 Region(path: GraphicsPath)

 Region(rect: RectangleF)

 Region(rgnData: RegionData)
 """
 def Clone(self):
  """
  Clone(self: Region) -> Region

  

   Creates an exact copy of this System.Drawing.Region.

   Returns: The System.Drawing.Region that this method creates.
  """
  pass
 def Complement(self,*__args):
  """
  Complement(self: Region,path: GraphicsPath)

   Updates this System.Drawing.Region to contain the portion of the specified 

    System.Drawing.Drawing2D.GraphicsPath that does not intersect with this System.Drawing.Region.

  

  

   path: The System.Drawing.Drawing2D.GraphicsPath to complement this System.Drawing.Region.

  Complement(self: Region,region: Region)

   Updates this System.Drawing.Region to contain the portion of the specified System.Drawing.Region 

    that does not intersect with this System.Drawing.Region.

  

  

   region: The System.Drawing.Region object to complement this System.Drawing.Region object.

  Complement(self: Region,rect: RectangleF)

   Updates this System.Drawing.Region to contain the portion of the specified 

    System.Drawing.RectangleF structure that does not intersect with this System.Drawing.Region.

  

  

   rect: The System.Drawing.RectangleF structure to complement this System.Drawing.Region.

  Complement(self: Region,rect: Rectangle)

   Updates this System.Drawing.Region to contain the portion of the specified 

    System.Drawing.Rectangle structure that does not intersect with this System.Drawing.Region.

  

  

   rect: The System.Drawing.Rectangle structure to complement this System.Drawing.Region.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Region)

   Releases all resources used by this System.Drawing.Region.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Region,region: Region,g: Graphics) -> bool

  

   Tests whether the specified System.Drawing.Region is identical to this System.Drawing.Region on 

    the specified drawing surface.

  

  

   region: The System.Drawing.Region to test.

   g: A System.Drawing.Graphics that represents a drawing surface.

   Returns: true if the interior of region is identical to the interior of this region when the 

    transformation associated with the g parameter is applied; otherwise,false.
  """
  pass
 def Exclude(self,*__args):
  """
  Exclude(self: Region,path: GraphicsPath)

   Updates this System.Drawing.Region to contain only the portion of its interior that does not 

    intersect with the specified System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: The System.Drawing.Drawing2D.GraphicsPath to exclude from this System.Drawing.Region.

  Exclude(self: Region,region: Region)

   Updates this System.Drawing.Region to contain only the portion of its interior that does not 

    intersect with the specified System.Drawing.Region.

  

  

   region: The System.Drawing.Region to exclude from this System.Drawing.Region.

  Exclude(self: Region,rect: Rectangle)

   Updates this System.Drawing.Region to contain only the portion of its interior that does not 

    intersect with the specified System.Drawing.Rectangle structure.

  

  

   rect: The System.Drawing.Rectangle structure to exclude from this System.Drawing.Region.

  Exclude(self: Region,rect: RectangleF)

   Updates this System.Drawing.Region to contain only the portion of its interior that does not 

    intersect with the specified System.Drawing.RectangleF structure.

  

  

   rect: The System.Drawing.RectangleF structure to exclude from this System.Drawing.Region.
  """
  pass
 @staticmethod
 def FromHrgn(hrgn):
  """
  FromHrgn(hrgn: IntPtr) -> Region

  

   Initializes a new System.Drawing.Region from a handle to the specified existing GDI region.

  

   hrgn: A handle to an existing System.Drawing.Region.

   Returns: The new System.Drawing.Region.
  """
  pass
 def GetBounds(self,g):
  """
  GetBounds(self: Region,g: Graphics) -> RectangleF

  

   Gets a System.Drawing.RectangleF structure that represents a rectangle that bounds this 

    System.Drawing.Region on the drawing surface of a System.Drawing.Graphics object.

  

  

   g: The System.Drawing.Graphics on which this System.Drawing.Region is drawn.

   Returns: A System.Drawing.RectangleF structure that represents the bounding rectangle for this 

    System.Drawing.Region on the specified drawing surface.
  """
  pass
 def GetHrgn(self,g):
  """
  GetHrgn(self: Region,g: Graphics) -> IntPtr

  

   Returns a Windows handle to this System.Drawing.Region in the specified graphics context.

  

   g: The System.Drawing.Graphics on which this System.Drawing.Region is drawn.

   Returns: A Windows handle to this System.Drawing.Region.
  """
  pass
 def GetRegionData(self):
  """
  GetRegionData(self: Region) -> RegionData

  

   Returns a System.Drawing.Drawing2D.RegionData that represents the information that describes 

    this System.Drawing.Region.

  

   Returns: A System.Drawing.Drawing2D.RegionData that represents the information that describes this 

    System.Drawing.Region.
  """
  pass
 def GetRegionScans(self,matrix):
  """
  GetRegionScans(self: Region,matrix: Matrix) -> Array[RectangleF]

  

   Returns an array of System.Drawing.RectangleF structures that approximate this 

    System.Drawing.Region after the specified matrix transformation is applied.

  

  

   matrix: A System.Drawing.Drawing2D.Matrix that represents a geometric transformation to apply to the 

    region.

  

   Returns: An array of System.Drawing.RectangleF structures that approximate this System.Drawing.Region 

    after the specified matrix transformation is applied.
  """
  pass
 def Intersect(self,*__args):
  """
  Intersect(self: Region,rect: Rectangle)

   Updates this System.Drawing.Region to the intersection of itself with the specified 

    System.Drawing.Rectangle structure.

  

  

   rect: The System.Drawing.Rectangle structure to intersect with this System.Drawing.Region.

  Intersect(self: Region,path: GraphicsPath)

   Updates this System.Drawing.Region to the intersection of itself with the specified 

    System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: The System.Drawing.Drawing2D.GraphicsPath to intersect with this System.Drawing.Region.

  Intersect(self: Region,region: Region)

   Updates this System.Drawing.Region to the intersection of itself with the specified 

    System.Drawing.Region.

  

  

   region: The System.Drawing.Region to intersect with this System.Drawing.Region.

  Intersect(self: Region,rect: RectangleF)

   Updates this System.Drawing.Region to the intersection of itself with the specified 

    System.Drawing.RectangleF structure.

  

  

   rect: The System.Drawing.RectangleF structure to intersect with this System.Drawing.Region.
  """
  pass
 def IsEmpty(self,g):
  """
  IsEmpty(self: Region,g: Graphics) -> bool

  

   Tests whether this System.Drawing.Region has an empty interior on the specified drawing surface.

  

   g: A System.Drawing.Graphics that represents a drawing surface.

   Returns: true if the interior of this System.Drawing.Region is empty when the transformation associated 

    with g is applied; otherwise,false.
  """
  pass
 def IsInfinite(self,g):
  """
  IsInfinite(self: Region,g: Graphics) -> bool

  

   Tests whether this System.Drawing.Region has an infinite interior on the specified drawing 

    surface.

  

  

   g: A System.Drawing.Graphics that represents a drawing surface.

   Returns: true if the interior of this System.Drawing.Region is infinite when the transformation 

    associated with g is applied; otherwise,false.
  """
  pass
 def IsVisible(self,*__args):
  """
  IsVisible(self: Region,point: Point,g: Graphics) -> bool

  

   Tests whether the specified System.Drawing.Point structure is contained within this 

    System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   point: The System.Drawing.Point structure to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,point: Point) -> bool

  

   Tests whether the specified System.Drawing.Point structure is contained within this 

    System.Drawing.Region.

  

  

   point: The System.Drawing.Point structure to test.

   Returns: true when point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: int,y: int,g: Graphics) -> bool

  

   Tests whether the specified point is contained within this System.Drawing.Region object when 

    drawn using the specified System.Drawing.Graphics object.

  

  

   x: The x-coordinate of the point to test.

   y: The y-coordinate of the point to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when the specified point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: int,y: int,width: int,height: int) -> bool

  

   Tests whether any portion of the specified rectangle is contained within this 

    System.Drawing.Region.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test.

   y: The y-coordinate of the upper-left corner of the rectangle to test.

   width: The width of the rectangle to test.

   height: The height of the rectangle to test.

   Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 

    otherwise,false.

  

  IsVisible(self: Region,rect: Rectangle,g: Graphics) -> bool

  

   Tests whether any portion of the specified System.Drawing.Rectangle structure is contained 

    within this System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   rect: The System.Drawing.Rectangle structure to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when any portion of the rect is contained within this System.Drawing.Region; otherwise,

    false.

  

  IsVisible(self: Region,x: int,y: int,width: int,height: int,g: Graphics) -> bool

  

   Tests whether any portion of the specified rectangle is contained within this 

    System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test.

   y: The y-coordinate of the upper-left corner of the rectangle to test.

   width: The width of the rectangle to test.

   height: The height of the rectangle to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 

    otherwise,false.

  

  IsVisible(self: Region,rect: Rectangle) -> bool

  

   Tests whether any portion of the specified System.Drawing.Rectangle structure is contained 

    within this System.Drawing.Region.

  

  

   rect: The System.Drawing.Rectangle structure to test.

   Returns: This method returns true when any portion of rect is contained within this 

    System.Drawing.Region; otherwise,false.

  

  IsVisible(self: Region,rect: RectangleF,g: Graphics) -> bool

  

   Tests whether any portion of the specified System.Drawing.RectangleF structure is contained 

    within this System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   rect: The System.Drawing.RectangleF structure to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when rect is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: Single,y: Single,g: Graphics) -> bool

  

   Tests whether the specified point is contained within this System.Drawing.Region when drawn 

    using the specified System.Drawing.Graphics.

  

  

   x: The x-coordinate of the point to test.

   y: The y-coordinate of the point to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when the specified point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,point: PointF) -> bool

  

   Tests whether the specified System.Drawing.PointF structure is contained within this 

    System.Drawing.Region.

  

  

   point: The System.Drawing.PointF structure to test.

   Returns: true when point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: Single,y: Single) -> bool

  

   Tests whether the specified point is contained within this System.Drawing.Region.

  

   x: The x-coordinate of the point to test.

   y: The y-coordinate of the point to test.

   Returns: true when the specified point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,point: PointF,g: Graphics) -> bool

  

   Tests whether the specified System.Drawing.PointF structure is contained within this 

    System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   point: The System.Drawing.PointF structure to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when point is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: Single,y: Single,width: Single,height: Single,g: Graphics) -> bool

  

   Tests whether any portion of the specified rectangle is contained within this 

    System.Drawing.Region when drawn using the specified System.Drawing.Graphics.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test.

   y: The y-coordinate of the upper-left corner of the rectangle to test.

   width: The width of the rectangle to test.

   height: The height of the rectangle to test.

   g: A System.Drawing.Graphics that represents a graphics context.

   Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 

    otherwise,false.

  

  IsVisible(self: Region,rect: RectangleF) -> bool

  

   Tests whether any portion of the specified System.Drawing.RectangleF structure is contained 

    within this System.Drawing.Region.

  

  

   rect: The System.Drawing.RectangleF structure to test.

   Returns: true when any portion of rect is contained within this System.Drawing.Region; otherwise,false.

  IsVisible(self: Region,x: Single,y: Single,width: Single,height: Single) -> bool

  

   Tests whether any portion of the specified rectangle is contained within this 

    System.Drawing.Region.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test.

   y: The y-coordinate of the upper-left corner of the rectangle to test.

   width: The width of the rectangle to test.

   height: The height of the rectangle to test.

   Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region 

    object; otherwise,false.
  """
  pass
 def MakeEmpty(self):
  """
  MakeEmpty(self: Region)

   Initializes this System.Drawing.Region to an empty interior.
  """
  pass
 def MakeInfinite(self):
  """
  MakeInfinite(self: Region)

   Initializes this System.Drawing.Region object to an infinite interior.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def ReleaseHrgn(self,regionHandle):
  """
  ReleaseHrgn(self: Region,regionHandle: IntPtr)

   Releases the handle of the System.Drawing.Region.

  

   regionHandle: The handle to the System.Drawing.Region.
  """
  pass
 def Transform(self,matrix):
  """
  Transform(self: Region,matrix: Matrix)

   Transforms this System.Drawing.Region by the specified System.Drawing.Drawing2D.Matrix.

  

   matrix: The System.Drawing.Drawing2D.Matrix by which to transform this System.Drawing.Region.
  """
  pass
 def Translate(self,dx,dy):
  """
  Translate(self: Region,dx: int,dy: int)

   Offsets the coordinates of this System.Drawing.Region by the specified amount.

  

   dx: The amount to offset this System.Drawing.Region horizontally.

   dy: The amount to offset this System.Drawing.Region vertically.

  Translate(self: Region,dx: Single,dy: Single)

   Offsets the coordinates of this System.Drawing.Region by the specified amount.

  

   dx: The amount to offset this System.Drawing.Region horizontally.

   dy: The amount to offset this System.Drawing.Region vertically.
  """
  pass
 def Union(self,*__args):
  """
  Union(self: Region,path: GraphicsPath)

   Updates this System.Drawing.Region to the union of itself and the specified 

    System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: The System.Drawing.Drawing2D.GraphicsPath to unite with this System.Drawing.Region.

  Union(self: Region,region: Region)

   Updates this System.Drawing.Region to the union of itself and the specified 

    System.Drawing.Region.

  

  

   region: The System.Drawing.Region to unite with this System.Drawing.Region.

  Union(self: Region,rect: Rectangle)

   Updates this System.Drawing.Region to the union of itself and the specified 

    System.Drawing.Rectangle structure.

  

  

   rect: The System.Drawing.Rectangle structure to unite with this System.Drawing.Region.

  Union(self: Region,rect: RectangleF)

   Updates this System.Drawing.Region to the union of itself and the specified 

    System.Drawing.RectangleF structure.

  

  

   rect: The System.Drawing.RectangleF structure to unite with this System.Drawing.Region.
  """
  pass
 def Xor(self,*__args):
  """
  Xor(self: Region,path: GraphicsPath)

   Updates this System.Drawing.Region to the union minus the intersection of itself with the 

    specified System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: The System.Drawing.Drawing2D.GraphicsPath to erload:System.Drawing.Region.Xor with this 

    System.Drawing.Region.

  

  Xor(self: Region,region: Region)

   Updates this System.Drawing.Region to the union minus the intersection of itself with the 

    specified System.Drawing.Region.

  

  

   region: The System.Drawing.Region to erload:System.Drawing.Region.Xor with this System.Drawing.Region.

  Xor(self: Region,rect: RectangleF)

   Updates this System.Drawing.Region to the union minus the intersection of itself with the 

    specified System.Drawing.RectangleF structure.

  

  

   rect: The System.Drawing.RectangleF structure to 

    System.Drawing.Region.Xor(System.Drawing.Drawing2D.GraphicsPath) with this 

    System.Drawing.Region.

  

  Xor(self: Region,rect: Rectangle)

   Updates this System.Drawing.Region to the union minus the intersection of itself with the 

    specified System.Drawing.Rectangle structure.

  

  

   rect: The System.Drawing.Rectangle structure to erload:System.Drawing.Region.Xor with this 

    System.Drawing.Region.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
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
  __new__(cls: type)

  __new__(cls: type,rect: RectangleF)

  __new__(cls: type,rect: Rectangle)

  __new__(cls: type,path: GraphicsPath)

  __new__(cls: type,rgnData: RegionData)
  """
  pass
