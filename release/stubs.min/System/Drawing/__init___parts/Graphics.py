class Graphics(MarshalByRefObject,IDisposable,IDeviceContext):
 """ Encapsulates a GDI+ drawing surface. This class cannot be inherited. """
 def AddMetafileComment(self,data):
  """
  AddMetafileComment(self: Graphics,data: Array[Byte])

   Adds a comment to the current System.Drawing.Imaging.Metafile.

  

   data: Array of bytes that contains the comment.
  """
  pass
 def BeginContainer(self,dstrect=None,srcrect=None,unit=None):
  """
  BeginContainer(self: Graphics,dstrect: Rectangle,srcrect: Rectangle,unit: GraphicsUnit) -> GraphicsContainer

  

   Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 

    uses a new graphics container with the specified scale transformation.

  

  

   dstrect: System.Drawing.Rectangle structure that,together with the srcrect parameter,specifies a scale 

    transformation for the container.

  

   srcrect: System.Drawing.Rectangle structure that,together with the dstrect parameter,specifies a scale 

    transformation for the container.

  

   unit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the unit of measure for the 

    container.

  

   Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 

    this System.Drawing.Graphics at the time of the method call.

  

  BeginContainer(self: Graphics,dstrect: RectangleF,srcrect: RectangleF,unit: GraphicsUnit) -> GraphicsContainer

  

   Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 

    uses a new graphics container with the specified scale transformation.

  

  

   dstrect: System.Drawing.RectangleF structure that,together with the srcrect parameter,specifies a scale 

    transformation for the new graphics container.

  

   srcrect: System.Drawing.RectangleF structure that,together with the dstrect parameter,specifies a scale 

    transformation for the new graphics container.

  

   unit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the unit of measure for the 

    container.

  

   Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 

    this System.Drawing.Graphics at the time of the method call.

  

  BeginContainer(self: Graphics) -> GraphicsContainer

  

   Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 

    uses a new graphics container.

  

   Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 

    this System.Drawing.Graphics at the time of the method call.
  """
  pass
 def Clear(self,color):
  """
  Clear(self: Graphics,color: Color)

   Clears the entire drawing surface and fills it with the specified background color.

  

   color: System.Drawing.Color structure that represents the background color of the drawing surface.
  """
  pass
 def CopyFromScreen(self,*__args):
  """
  CopyFromScreen(self: Graphics,upperLeftSource: Point,upperLeftDestination: Point,blockRegionSize: Size,copyPixelOperation: CopyPixelOperation)

   Performs a bit-block transfer of color data,corresponding to a rectangle of pixels,from the 

    screen to the drawing surface of the System.Drawing.Graphics.

  

  

   upperLeftSource: The point at the upper-left corner of the source rectangle.

   upperLeftDestination: The point at the upper-left corner of the destination rectangle.

   blockRegionSize: The size of the area to be transferred.

   copyPixelOperation: One of the System.Drawing.CopyPixelOperation values.

  CopyFromScreen(self: Graphics,sourceX: int,sourceY: int,destinationX: int,destinationY: int,blockRegionSize: Size,copyPixelOperation: CopyPixelOperation)

   Performs a bit-block transfer of the color data,corresponding to a rectangle of pixels,from 

    the screen to the drawing surface of the System.Drawing.Graphics.

  

  

   sourceX: The x-coordinate of the point at the upper-left corner of the source rectangle.

   sourceY: The y-coordinate of the point at the upper-left corner of the source rectangle

   destinationX: The x-coordinate of the point at the upper-left corner of the destination rectangle.

   destinationY: The y-coordinate of the point at the upper-left corner of the destination rectangle.

   blockRegionSize: The size of the area to be transferred.

   copyPixelOperation: One of the System.Drawing.CopyPixelOperation values.

  CopyFromScreen(self: Graphics,upperLeftSource: Point,upperLeftDestination: Point,blockRegionSize: Size)

   Performs a bit-block transfer of color data,corresponding to a rectangle of pixels,from the 

    screen to the drawing surface of the System.Drawing.Graphics.

  

  

   upperLeftSource: The point at the upper-left corner of the source rectangle.

   upperLeftDestination: The point at the upper-left corner of the destination rectangle.

   blockRegionSize: The size of the area to be transferred.

  CopyFromScreen(self: Graphics,sourceX: int,sourceY: int,destinationX: int,destinationY: int,blockRegionSize: Size)

   Performs a bit-block transfer of the color data,corresponding to a rectangle of pixels,from 

    the screen to the drawing surface of the System.Drawing.Graphics.

  

  

   sourceX: The x-coordinate of the point at the upper-left corner of the source rectangle.

   sourceY: The y-coordinate of the point at the upper-left corner of the source rectangle.

   destinationX: The x-coordinate of the point at the upper-left corner of the destination rectangle.

   destinationY: The y-coordinate of the point at the upper-left corner of the destination rectangle.

   blockRegionSize: The size of the area to be transferred.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Graphics)

   Releases all resources used by this System.Drawing.Graphics.
  """
  pass
 def DrawArc(self,pen,*__args):
  """
  DrawArc(self: Graphics,pen: Pen,x: int,y: int,width: int,height: int,startAngle: int,sweepAngle: int)

   Draws an arc representing a portion of an ellipse specified by a pair of coordinates,a width,

    and a height.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the arc.

   x: The x-coordinate of the upper-left corner of the rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the rectangle that defines the ellipse.

   width: Width of the rectangle that defines the ellipse.

   height: Height of the rectangle that defines the ellipse.

   startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.

  DrawArc(self: Graphics,pen: Pen,rect: Rectangle,startAngle: Single,sweepAngle: Single)

   Draws an arc representing a portion of an ellipse specified by a System.Drawing.Rectangle 

    structure.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the arc.

   rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.

   startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.

  DrawArc(self: Graphics,pen: Pen,x: Single,y: Single,width: Single,height: Single,startAngle: Single,sweepAngle: Single)

   Draws an arc representing a portion of an ellipse specified by a pair of coordinates,a width,

    and a height.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the arc.

   x: The x-coordinate of the upper-left corner of the rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the rectangle that defines the ellipse.

   width: Width of the rectangle that defines the ellipse.

   height: Height of the rectangle that defines the ellipse.

   startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.

  DrawArc(self: Graphics,pen: Pen,rect: RectangleF,startAngle: Single,sweepAngle: Single)

   Draws an arc representing a portion of an ellipse specified by a System.Drawing.RectangleF 

    structure.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the arc.

   rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.

   startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.
  """
  pass
 def DrawBezier(self,pen,*__args):
  """
  DrawBezier(self: Graphics,pen: Pen,pt1: Point,pt2: Point,pt3: Point,pt4: Point)

   Draws a B�zier spline defined by four System.Drawing.Point structures.

  

   pen: System.Drawing.Pen structure that determines the color,width,and style of the curve.

   pt1: System.Drawing.Point structure that represents the starting point of the curve.

   pt2: System.Drawing.Point structure that represents the first control point for the curve.

   pt3: System.Drawing.Point structure that represents the second control point for the curve.

   pt4: System.Drawing.Point structure that represents the ending point of the curve.

  DrawBezier(self: Graphics,pen: Pen,pt1: PointF,pt2: PointF,pt3: PointF,pt4: PointF)

   Draws a B�zier spline defined by four System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the curve.

   pt1: System.Drawing.PointF structure that represents the starting point of the curve.

   pt2: System.Drawing.PointF structure that represents the first control point for the curve.

   pt3: System.Drawing.PointF structure that represents the second control point for the curve.

   pt4: System.Drawing.PointF structure that represents the ending point of the curve.

  DrawBezier(self: Graphics,pen: Pen,x1: Single,y1: Single,x2: Single,y2: Single,x3: Single,y3: Single,x4: Single,y4: Single)

   Draws a B�zier spline defined by four ordered pairs of coordinates that represent points.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the curve.

   x1: The x-coordinate of the starting point of the curve.

   y1: The y-coordinate of the starting point of the curve.

   x2: The x-coordinate of the first control point of the curve.

   y2: The y-coordinate of the first control point of the curve.

   x3: The x-coordinate of the second control point of the curve.

   y3: The y-coordinate of the second control point of the curve.

   x4: The x-coordinate of the ending point of the curve.

   y4: The y-coordinate of the ending point of the curve.
  """
  pass
 def DrawBeziers(self,pen,points):
  """
  DrawBeziers(self: Graphics,pen: Pen,points: Array[Point])

   Draws a series of B�zier splines from an array of System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the curve.

   points: Array of System.Drawing.Point structures that represent the points that determine the curve. The 

    number of points in the array should be a multiple of 3 plus 1,such as 4,7,or 10.

  

  DrawBeziers(self: Graphics,pen: Pen,points: Array[PointF])

   Draws a series of B�zier splines from an array of System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the curve.

   points: Array of System.Drawing.PointF structures that represent the points that determine the curve. 

    The number of points in the array should be a multiple of 3 plus 1,such as 4,7,or 10.
  """
  pass
 def DrawClosedCurve(self,pen,points,tension=None,fillmode=None):
  """
  DrawClosedCurve(self: Graphics,pen: Pen,points: Array[Point])

   Draws a closed cardinal spline defined by an array of System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.Point structures that define the spline.

  DrawClosedCurve(self: Graphics,pen: Pen,points: Array[Point],tension: Single,fillmode: FillMode)

   Draws a closed cardinal spline defined by an array of System.Drawing.Point structures using a 

    specified tension.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.Point structures that define the spline.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled. This parameter is required but ignored.

  

  DrawClosedCurve(self: Graphics,pen: Pen,points: Array[PointF])

   Draws a closed cardinal spline defined by an array of System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that define the spline.

  DrawClosedCurve(self: Graphics,pen: Pen,points: Array[PointF],tension: Single,fillmode: FillMode)

   Draws a closed cardinal spline defined by an array of System.Drawing.PointF structures using a 

    specified tension.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that define the spline.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled. This parameter is required but is ignored.
  """
  pass
 def DrawCurve(self,pen,points,*__args):
  """
  DrawCurve(self: Graphics,pen: Pen,points: Array[Point])

   Draws a cardinal spline through a specified array of System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.Point structures that define the spline.

  DrawCurve(self: Graphics,pen: Pen,points: Array[Point],tension: Single)

   Draws a cardinal spline through a specified array of System.Drawing.Point structures using a 

    specified tension.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.Point structures that define the spline.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

  DrawCurve(self: Graphics,pen: Pen,points: Array[Point],offset: int,numberOfSegments: int,tension: Single)

   Draws a cardinal spline through a specified array of System.Drawing.Point structures using a 

    specified tension.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.Point structures that define the spline.

   offset: Offset from the first element in the array of the points parameter to the starting point in the 

    curve.

  

   numberOfSegments: Number of segments after the starting point to include in the curve.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

  DrawCurve(self: Graphics,pen: Pen,points: Array[PointF],offset: int,numberOfSegments: int,tension: Single)

   Draws a cardinal spline through a specified array of System.Drawing.PointF structures using a 

    specified tension. The drawing begins offset from the beginning of the array.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that define the spline.

   offset: Offset from the first element in the array of the points parameter to the starting point in the 

    curve.

  

   numberOfSegments: Number of segments after the starting point to include in the curve.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

  DrawCurve(self: Graphics,pen: Pen,points: Array[PointF])

   Draws a cardinal spline through a specified array of System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that define the spline.

  DrawCurve(self: Graphics,pen: Pen,points: Array[PointF],tension: Single)

   Draws a cardinal spline through a specified array of System.Drawing.PointF structures using a 

    specified tension.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that represent the points that define the curve.

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

  DrawCurve(self: Graphics,pen: Pen,points: Array[PointF],offset: int,numberOfSegments: int)

   Draws a cardinal spline through a specified array of System.Drawing.PointF structures. The 

    drawing begins offset from the beginning of the array.

  

  

   pen: System.Drawing.Pen that determines the color,width,and height of the curve.

   points: Array of System.Drawing.PointF structures that define the spline.

   offset: Offset from the first element in the array of the points parameter to the starting point in the 

    curve.

  

   numberOfSegments: Number of segments after the starting point to include in the curve.
  """
  pass
 def DrawEllipse(self,pen,*__args):
  """
  DrawEllipse(self: Graphics,pen: Pen,rect: Rectangle)

   Draws an ellipse specified by a bounding System.Drawing.Rectangle structure.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the ellipse.

   rect: System.Drawing.Rectangle structure that defines the boundaries of the ellipse.

  DrawEllipse(self: Graphics,pen: Pen,x: int,y: int,width: int,height: int)

   Draws an ellipse defined by a bounding rectangle specified by coordinates for the upper-left 

    corner of the rectangle,a height,and a width.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the ellipse.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   width: Width of the bounding rectangle that defines the ellipse.

   height: Height of the bounding rectangle that defines the ellipse.

  DrawEllipse(self: Graphics,pen: Pen,rect: RectangleF)

   Draws an ellipse defined by a bounding System.Drawing.RectangleF.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the ellipse.

   rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.

  DrawEllipse(self: Graphics,pen: Pen,x: Single,y: Single,width: Single,height: Single)

   Draws an ellipse defined by a bounding rectangle specified by a pair of coordinates,a height,

    and a width.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the ellipse.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   width: Width of the bounding rectangle that defines the ellipse.

   height: Height of the bounding rectangle that defines the ellipse.
  """
  pass
 def DrawIcon(self,icon,*__args):
  """
  DrawIcon(self: Graphics,icon: Icon,targetRect: Rectangle)

   Draws the image represented by the specified System.Drawing.Icon within the area specified by a 

    System.Drawing.Rectangle structure.

  

  

   icon: System.Drawing.Icon to draw.

   targetRect: System.Drawing.Rectangle structure that specifies the location and size of the resulting image 

    on the display surface. The image contained in the icon parameter is scaled to the dimensions of 

    this rectangular area.

  

  DrawIcon(self: Graphics,icon: Icon,x: int,y: int)

   Draws the image represented by the specified System.Drawing.Icon at the specified coordinates.

  

   icon: System.Drawing.Icon to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.
  """
  pass
 def DrawIconUnstretched(self,icon,targetRect):
  """
  DrawIconUnstretched(self: Graphics,icon: Icon,targetRect: Rectangle)

   Draws the image represented by the specified System.Drawing.Icon without scaling the image.

  

   icon: System.Drawing.Icon to draw.

   targetRect: System.Drawing.Rectangle structure that specifies the location and size of the resulting image. 

    The image is not scaled to fit this rectangle,but retains its original size. If the image is 

    larger than the rectangle,it is clipped to fit inside it.
  """
  pass
 def DrawImage(self,image,*__args):
  """
  DrawImage(self: Graphics,image: Image,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit,imageAttr: ImageAttributes,callback: DrawImageAbort,callbackData: int)DrawImage(self: Graphics,image: Image,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.Point structures that define a parallelogram.

   srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit,imageAttr: ImageAttributes)

   Draws the specified portion of the specified System.Drawing.Image at the specified location.

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.Point structures that define a parallelogram.

   srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

   imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 

    image object.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit,imageAttr: ImageAttributes,callback: DrawImageAbort)DrawImage(self: Graphics,image: Image,destRect: RectangleF,srcRect: RectangleF,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.RectangleF structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.

   srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit,imageAttr: ImageAttributes)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.

   srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

   imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 

    image object.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit,imageAttr: ImageAttributes,callback: DrawImageAbort)DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: Single,srcY: Single,srcWidth: Single,srcHeight: Single,srcUnit: GraphicsUnit,imageAttrs: ImageAttributes,callback: DrawImageAbort,callbackData: IntPtr)DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: int,srcY: int,srcWidth: int,srcHeight: int,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.

   srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.

   srcWidth: Width of the portion of the source image to draw.

   srcHeight: Height of the portion of the source image to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    to determine the source rectangle.

  

  DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: int,srcY: int,srcWidth: int,srcHeight: int,srcUnit: GraphicsUnit,imageAttr: ImageAttributes,callback: DrawImageAbort)DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: Single,srcY: Single,srcWidth: Single,srcHeight: Single,srcUnit: GraphicsUnit,imageAttrs: ImageAttributes,callback: DrawImageAbort)DrawImage(self: Graphics,image: Image,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit,imageAttr: ImageAttributes,callback: DrawImageAbort,callbackData: int)DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: Single,srcY: Single,srcWidth: Single,srcHeight: Single,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.

   srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.

   srcWidth: Width of the portion of the source image to draw.

   srcHeight: Height of the portion of the source image to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    to determine the source rectangle.

  

  DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: Single,srcY: Single,srcWidth: Single,srcHeight: Single,srcUnit: GraphicsUnit,imageAttrs: ImageAttributes)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.

   srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.

   srcWidth: Width of the portion of the source image to draw.

   srcHeight: Height of the portion of the source image to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    to determine the source rectangle.

  

   imageAttrs: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 

    image object.

  

  DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: int,srcY: int,srcWidth: int,srcHeight: int,srcUnit: GraphicsUnit,imageAttr: ImageAttributes)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.

   srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.

   srcWidth: Width of the portion of the source image to draw.

   srcHeight: Height of the portion of the source image to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    to determine the source rectangle.

  

   imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 

    image object.

  

  DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcX: int,srcY: int,srcWidth: int,srcHeight: int,srcUnit: GraphicsUnit,imageAttrs: ImageAttributes,callback: DrawImageAbort,callbackData: IntPtr)DrawImage(self: Graphics,image: Image,point: PointF)

   Draws the specified System.Drawing.Image,using its original physical size,at the specified 

    location.

  

  

   image: System.Drawing.Image to draw.

   point: System.Drawing.PointF structure that represents the upper-left corner of the drawn image.

  DrawImage(self: Graphics,image: Image,destRect: Rectangle,srcRect: Rectangle,srcUnit: GraphicsUnit)

   Draws the specified portion of the specified System.Drawing.Image at the specified location and 

    with the specified size.

  

  

   image: System.Drawing.Image to draw.

   destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 

    image is scaled to fit the rectangle.

  

   srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,x: int,y: int)

   Draws the specified image,using its original physical size,at the location specified by a 

    coordinate pair.

  

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

  DrawImage(self: Graphics,image: Image,rect: Rectangle)

   Draws the specified System.Drawing.Image at the specified location and with the specified size.

  

   image: System.Drawing.Image to draw.

   rect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image.

  DrawImage(self: Graphics,image: Image,x: int,y: int,width: int,height: int)

   Draws the specified System.Drawing.Image at the specified location and with the specified size.

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

   width: Width of the drawn image.

   height: Height of the drawn image.

  DrawImage(self: Graphics,image: Image,x: Single,y: Single)

   Draws the specified System.Drawing.Image,using its original physical size,at the specified 

    location.

  

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

  DrawImage(self: Graphics,image: Image,destPoints: Array[Point])

   Draws the specified System.Drawing.Image at the specified location and with the specified shape 

    and size.

  

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.Point structures that define a parallelogram.

  DrawImage(self: Graphics,image: Image,x: Single,y: Single,srcRect: RectangleF,srcUnit: GraphicsUnit)

   Draws a portion of an image at a specified location.

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

   srcRect: System.Drawing.RectangleF structure that specifies the portion of the System.Drawing.Image to 

    draw.

  

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,x: int,y: int,srcRect: Rectangle,srcUnit: GraphicsUnit)

   Draws a portion of an image at a specified location.

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

   srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.

   srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 

    by the srcRect parameter.

  

  DrawImage(self: Graphics,image: Image,destPoints: Array[PointF])

   Draws the specified System.Drawing.Image at the specified location and with the specified shape 

    and size.

  

  

   image: System.Drawing.Image to draw.

   destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.

  DrawImage(self: Graphics,image: Image,rect: RectangleF)

   Draws the specified System.Drawing.Image at the specified location and with the specified size.

  

   image: System.Drawing.Image to draw.

   rect: System.Drawing.RectangleF structure that specifies the location and size of the drawn image.

  DrawImage(self: Graphics,image: Image,x: Single,y: Single,width: Single,height: Single)

   Draws the specified System.Drawing.Image at the specified location and with the specified size.

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

   width: Width of the drawn image.

   height: Height of the drawn image.

  DrawImage(self: Graphics,image: Image,point: Point)

   Draws the specified System.Drawing.Image,using its original physical size,at the specified 

    location.

  

  

   image: System.Drawing.Image to draw.

   point: System.Drawing.Point structure that represents the location of the upper-left corner of the 

    drawn image.
  """
  pass
 def DrawImageUnscaled(self,image,*__args):
  """
  DrawImageUnscaled(self: Graphics,image: Image,rect: Rectangle)

   Draws a specified image using its original physical size at a specified location.

  

   image: System.Drawing.Image to draw.

   rect: System.Drawing.Rectangle that specifies the upper-left corner of the drawn image. The X and Y 

    properties of the rectangle specify the upper-left corner. The Width and Height properties are 

    ignored.

  

  DrawImageUnscaled(self: Graphics,image: Image,x: int,y: int,width: int,height: int)

   Draws a specified image using its original physical size at a specified location.

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.

   width: Not used.

   height: Not used.

  DrawImageUnscaled(self: Graphics,image: Image,point: Point)

   Draws a specified image using its original physical size at a specified location.

  

   image: System.Drawing.Image to draw.

   point: System.Drawing.Point structure that specifies the upper-left corner of the drawn image.

  DrawImageUnscaled(self: Graphics,image: Image,x: int,y: int)

   Draws the specified image using its original physical size at the location specified by a 

    coordinate pair.

  

  

   image: System.Drawing.Image to draw.

   x: The x-coordinate of the upper-left corner of the drawn image.

   y: The y-coordinate of the upper-left corner of the drawn image.
  """
  pass
 def DrawImageUnscaledAndClipped(self,image,rect):
  """
  DrawImageUnscaledAndClipped(self: Graphics,image: Image,rect: Rectangle)

   Draws the specified image without scaling and clips it,if necessary,to fit in the specified 

    rectangle.

  

  

   image: The System.Drawing.Image to draw.

   rect: The System.Drawing.Rectangle in which to draw the image.
  """
  pass
 def DrawLine(self,pen,*__args):
  """
  DrawLine(self: Graphics,pen: Pen,pt1: PointF,pt2: PointF)

   Draws a line connecting two System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line.

   pt1: System.Drawing.PointF structure that represents the first point to connect.

   pt2: System.Drawing.PointF structure that represents the second point to connect.

  DrawLine(self: Graphics,pen: Pen,pt1: Point,pt2: Point)

   Draws a line connecting two System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line.

   pt1: System.Drawing.Point structure that represents the first point to connect.

   pt2: System.Drawing.Point structure that represents the second point to connect.

  DrawLine(self: Graphics,pen: Pen,x1: int,y1: int,x2: int,y2: int)

   Draws a line connecting the two points specified by the coordinate pairs.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line.

   x1: The x-coordinate of the first point.

   y1: The y-coordinate of the first point.

   x2: The x-coordinate of the second point.

   y2: The y-coordinate of the second point.

  DrawLine(self: Graphics,pen: Pen,x1: Single,y1: Single,x2: Single,y2: Single)

   Draws a line connecting the two points specified by the coordinate pairs.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line.

   x1: The x-coordinate of the first point.

   y1: The y-coordinate of the first point.

   x2: The x-coordinate of the second point.

   y2: The y-coordinate of the second point.
  """
  pass
 def DrawLines(self,pen,points):
  """
  DrawLines(self: Graphics,pen: Pen,points: Array[Point])

   Draws a series of line segments that connect an array of System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line segments.

   points: Array of System.Drawing.Point structures that represent the points to connect.

  DrawLines(self: Graphics,pen: Pen,points: Array[PointF])

   Draws a series of line segments that connect an array of System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the line segments.

   points: Array of System.Drawing.PointF structures that represent the points to connect.
  """
  pass
 def DrawPath(self,pen,path):
  """
  DrawPath(self: Graphics,pen: Pen,path: GraphicsPath)

   Draws a System.Drawing.Drawing2D.GraphicsPath.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the path.

   path: System.Drawing.Drawing2D.GraphicsPath to draw.
  """
  pass
 def DrawPie(self,pen,*__args):
  """
  DrawPie(self: Graphics,pen: Pen,rect: Rectangle,startAngle: Single,sweepAngle: Single)

   Draws a pie shape defined by an ellipse specified by a System.Drawing.Rectangle structure and 

    two radial lines.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the pie shape.

   rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 

    ellipse from which the pie shape comes.

  

   startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.

   sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 

    shape.

  

  DrawPie(self: Graphics,pen: Pen,x: int,y: int,width: int,height: int,startAngle: int,sweepAngle: int)

   Draws a pie shape defined by an ellipse specified by a coordinate pair,a width,a height,and 

    two radial lines.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the pie shape.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie shape comes.

  

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie shape comes.

  

   width: Width of the bounding rectangle that defines the ellipse from which the pie shape comes.

   height: Height of the bounding rectangle that defines the ellipse from which the pie shape comes.

   startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.

   sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 

    shape.

  

  DrawPie(self: Graphics,pen: Pen,rect: RectangleF,startAngle: Single,sweepAngle: Single)

   Draws a pie shape defined by an ellipse specified by a System.Drawing.RectangleF structure and 

    two radial lines.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the pie shape.

   rect: System.Drawing.RectangleF structure that represents the bounding rectangle that defines the 

    ellipse from which the pie shape comes.

  

   startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.

   sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 

    shape.

  

  DrawPie(self: Graphics,pen: Pen,x: Single,y: Single,width: Single,height: Single,startAngle: Single,sweepAngle: Single)

   Draws a pie shape defined by an ellipse specified by a coordinate pair,a width,a height,and 

    two radial lines.

  

  

   pen: System.Drawing.Pen that determines the color,width,and style of the pie shape.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie shape comes.

  

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie shape comes.

  

   width: Width of the bounding rectangle that defines the ellipse from which the pie shape comes.

   height: Height of the bounding rectangle that defines the ellipse from which the pie shape comes.

   startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.

   sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 

    shape.
  """
  pass
 def DrawPolygon(self,pen,points):
  """
  DrawPolygon(self: Graphics,pen: Pen,points: Array[Point])

   Draws a polygon defined by an array of System.Drawing.Point structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the polygon.

   points: Array of System.Drawing.Point structures that represent the vertices of the polygon.

  DrawPolygon(self: Graphics,pen: Pen,points: Array[PointF])

   Draws a polygon defined by an array of System.Drawing.PointF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the polygon.

   points: Array of System.Drawing.PointF structures that represent the vertices of the polygon.
  """
  pass
 def DrawRectangle(self,pen,*__args):
  """
  DrawRectangle(self: Graphics,pen: Pen,x: int,y: int,width: int,height: int)

   Draws a rectangle specified by a coordinate pair,a width,and a height.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the rectangle.

   x: The x-coordinate of the upper-left corner of the rectangle to draw.

   y: The y-coordinate of the upper-left corner of the rectangle to draw.

   width: Width of the rectangle to draw.

   height: Height of the rectangle to draw.

  DrawRectangle(self: Graphics,pen: Pen,x: Single,y: Single,width: Single,height: Single)

   Draws a rectangle specified by a coordinate pair,a width,and a height.

  

   pen: A System.Drawing.Pen that determines the color,width,and style of the rectangle.

   x: The x-coordinate of the upper-left corner of the rectangle to draw.

   y: The y-coordinate of the upper-left corner of the rectangle to draw.

   width: The width of the rectangle to draw.

   height: The height of the rectangle to draw.

  DrawRectangle(self: Graphics,pen: Pen,rect: Rectangle)

   Draws a rectangle specified by a System.Drawing.Rectangle structure.

  

   pen: A System.Drawing.Pen that determines the color,width,and style of the rectangle.

   rect: A System.Drawing.Rectangle structure that represents the rectangle to draw.
  """
  pass
 def DrawRectangles(self,pen,rects):
  """
  DrawRectangles(self: Graphics,pen: Pen,rects: Array[Rectangle])

   Draws a series of rectangles specified by System.Drawing.Rectangle structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the outlines of the rectangles.

   rects: Array of System.Drawing.Rectangle structures that represent the rectangles to draw.

  DrawRectangles(self: Graphics,pen: Pen,rects: Array[RectangleF])

   Draws a series of rectangles specified by System.Drawing.RectangleF structures.

  

   pen: System.Drawing.Pen that determines the color,width,and style of the outlines of the rectangles.

   rects: Array of System.Drawing.RectangleF structures that represent the rectangles to draw.
  """
  pass
 def DrawString(self,s,font,brush,*__args):
  """
  DrawString(self: Graphics,s: str,font: Font,brush: Brush,point: PointF)

   Draws the specified text string at the specified location with the specified 

    System.Drawing.Brush and System.Drawing.Font objects.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   point: System.Drawing.PointF structure that specifies the upper-left corner of the drawn text.

  DrawString(self: Graphics,s: str,font: Font,brush: Brush,x: Single,y: Single,format: StringFormat)

   Draws the specified text string at the specified location with the specified 

    System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 

    specified System.Drawing.StringFormat.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   x: The x-coordinate of the upper-left corner of the drawn text.

   y: The y-coordinate of the upper-left corner of the drawn text.

   format: System.Drawing.StringFormat that specifies formatting attributes,such as line spacing and 

    alignment,that are applied to the drawn text.

  

  DrawString(self: Graphics,s: str,font: Font,brush: Brush,point: PointF,format: StringFormat)

   Draws the specified text string at the specified location with the specified 

    System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 

    specified System.Drawing.StringFormat.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   point: System.Drawing.PointF structure that specifies the upper-left corner of the drawn text.

   format: System.Drawing.StringFormat that specifies formatting attributes,such as line spacing and 

    alignment,that are applied to the drawn text.

  

  DrawString(self: Graphics,s: str,font: Font,brush: Brush,x: Single,y: Single)

   Draws the specified text string at the specified location with the specified 

    System.Drawing.Brush and System.Drawing.Font objects.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   x: The x-coordinate of the upper-left corner of the drawn text.

   y: The y-coordinate of the upper-left corner of the drawn text.

  DrawString(self: Graphics,s: str,font: Font,brush: Brush,layoutRectangle: RectangleF)

   Draws the specified text string in the specified rectangle with the specified 

    System.Drawing.Brush and System.Drawing.Font objects.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   layoutRectangle: System.Drawing.RectangleF structure that specifies the location of the drawn text.

  DrawString(self: Graphics,s: str,font: Font,brush: Brush,layoutRectangle: RectangleF,format: StringFormat)

   Draws the specified text string in the specified rectangle with the specified 

    System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 

    specified System.Drawing.StringFormat.

  

  

   s: String to draw.

   font: System.Drawing.Font that defines the text format of the string.

   brush: System.Drawing.Brush that determines the color and texture of the drawn text.

   layoutRectangle: System.Drawing.RectangleF structure that specifies the location of the drawn text.

   format: System.Drawing.StringFormat that specifies formatting attributes,such as line spacing and 

    alignment,that are applied to the drawn text.
  """
  pass
 def EndContainer(self,container):
  """
  EndContainer(self: Graphics,container: GraphicsContainer)

   Closes the current graphics container and restores the state of this System.Drawing.Graphics to 

    the state saved by a call to the System.Drawing.Graphics.BeginContainer method.

  

  

   container: System.Drawing.Drawing2D.GraphicsContainer that represents the container this method restores.
  """
  pass
 def EnumerateMetafile(self,metafile,*__args):
  """ EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,srcRect: Rectangle,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,srcRect: RectangleF,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,srcRect: RectangleF,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],srcRect: RectangleF,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],srcRect: Rectangle,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,srcRect: Rectangle,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],srcRect: RectangleF,srcUnit: GraphicsUnit,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,srcRect: Rectangle,unit: GraphicsUnit,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: RectangleF,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: Point,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoint: PointF,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[Point],callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,callback: EnumerateMetafileProc,callbackData: IntPtr)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destPoints: Array[PointF],callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics,metafile: Metafile,destRect: Rectangle,callback: EnumerateMetafileProc,callbackData: IntPtr,imageAttr: ImageAttributes) """
  pass
 def ExcludeClip(self,*__args):
  """
  ExcludeClip(self: Graphics,rect: Rectangle)

   Updates the clip region of this System.Drawing.Graphics to exclude the area specified by a 

    System.Drawing.Rectangle structure.

  

  

   rect: System.Drawing.Rectangle structure that specifies the rectangle to exclude from the clip region.

  ExcludeClip(self: Graphics,region: Region)

   Updates the clip region of this System.Drawing.Graphics to exclude the area specified by a 

    System.Drawing.Region.

  

  

   region: System.Drawing.Region that specifies the region to exclude from the clip region.
  """
  pass
 def FillClosedCurve(self,brush,points,fillmode=None,tension=None):
  """
  FillClosedCurve(self: Graphics,brush: Brush,points: Array[Point])

   Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 

    structures.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.Point structures that define the spline.

  FillClosedCurve(self: Graphics,brush: Brush,points: Array[Point],fillmode: FillMode)

   Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 

    structures using the specified fill mode.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.Point structures that define the spline.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled.

  

  FillClosedCurve(self: Graphics,brush: Brush,points: Array[Point],fillmode: FillMode,tension: Single)

   Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 

    structures using the specified fill mode and tension.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.Point structures that define the spline.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled.

  

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.

  FillClosedCurve(self: Graphics,brush: Brush,points: Array[PointF])

   Fills the interior of a closed cardinal spline curve defined by an array of 

    System.Drawing.PointF structures.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.PointF structures that define the spline.

  FillClosedCurve(self: Graphics,brush: Brush,points: Array[PointF],fillmode: FillMode)

   Fills the interior of a closed cardinal spline curve defined by an array of 

    System.Drawing.PointF structures using the specified fill mode.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.PointF structures that define the spline.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled.

  

  FillClosedCurve(self: Graphics,brush: Brush,points: Array[PointF],fillmode: FillMode,tension: Single)

   Fills the interior of a closed cardinal spline curve defined by an array of 

    System.Drawing.PointF structures using the specified fill mode and tension.

  

  

   brush: A System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.PointF structures that define the spline.

   fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 

    filled.

  

   tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
  """
  pass
 def FillEllipse(self,brush,*__args):
  """
  FillEllipse(self: Graphics,brush: Brush,rect: Rectangle)

   Fills the interior of an ellipse defined by a bounding rectangle specified by a 

    System.Drawing.Rectangle structure.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 

    ellipse.

  

  FillEllipse(self: Graphics,brush: Brush,x: int,y: int,width: int,height: int)

   Fills the interior of an ellipse defined by a bounding rectangle specified by a pair of 

    coordinates,a width,and a height.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   width: Width of the bounding rectangle that defines the ellipse.

   height: Height of the bounding rectangle that defines the ellipse.

  FillEllipse(self: Graphics,brush: Brush,x: Single,y: Single,width: Single,height: Single)

   Fills the interior of an ellipse defined by a bounding rectangle specified by a pair of 

    coordinates,a width,and a height.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.

   width: Width of the bounding rectangle that defines the ellipse.

   height: Height of the bounding rectangle that defines the ellipse.

  FillEllipse(self: Graphics,brush: Brush,rect: RectangleF)

   Fills the interior of an ellipse defined by a bounding rectangle specified by a 

    System.Drawing.RectangleF structure.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rect: System.Drawing.RectangleF structure that represents the bounding rectangle that defines the 

    ellipse.
  """
  pass
 def FillPath(self,brush,path):
  """
  FillPath(self: Graphics,brush: Brush,path: GraphicsPath)

   Fills the interior of a System.Drawing.Drawing2D.GraphicsPath.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   path: System.Drawing.Drawing2D.GraphicsPath that represents the path to fill.
  """
  pass
 def FillPie(self,brush,*__args):
  """
  FillPie(self: Graphics,brush: Brush,x: int,y: int,width: int,height: int,startAngle: int,sweepAngle: int)

   Fills the interior of a pie section defined by an ellipse specified by a pair of coordinates,a 

    width,a height,and two radial lines.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie section comes.

  

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie section comes.

  

   width: Width of the bounding rectangle that defines the ellipse from which the pie section comes.

   height: Height of the bounding rectangle that defines the ellipse from which the pie section comes.

   startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 

    section.

  

  FillPie(self: Graphics,brush: Brush,x: Single,y: Single,width: Single,height: Single,startAngle: Single,sweepAngle: Single)

   Fills the interior of a pie section defined by an ellipse specified by a pair of coordinates,a 

    width,a height,and two radial lines.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie section comes.

  

   y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 

    from which the pie section comes.

  

   width: Width of the bounding rectangle that defines the ellipse from which the pie section comes.

   height: Height of the bounding rectangle that defines the ellipse from which the pie section comes.

   startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 

    section.

  

  FillPie(self: Graphics,brush: Brush,rect: Rectangle,startAngle: Single,sweepAngle: Single)

   Fills the interior of a pie section defined by an ellipse specified by a 

    System.Drawing.RectangleF structure and two radial lines.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 

    ellipse from which the pie section comes.

  

   startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.

   sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 

    section.
  """
  pass
 def FillPolygon(self,brush,points,fillMode=None):
  """
  FillPolygon(self: Graphics,brush: Brush,points: Array[PointF],fillMode: FillMode)

   Fills the interior of a polygon defined by an array of points specified by System.Drawing.PointF 

    structures using the specified fill mode.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.PointF structures that represent the vertices of the polygon to fill.

   fillMode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines the style of the 

    fill.

  

  FillPolygon(self: Graphics,brush: Brush,points: Array[Point],fillMode: FillMode)

   Fills the interior of a polygon defined by an array of points specified by System.Drawing.Point 

    structures using the specified fill mode.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.Point structures that represent the vertices of the polygon to fill.

   fillMode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines the style of the 

    fill.

  

  FillPolygon(self: Graphics,brush: Brush,points: Array[Point])

   Fills the interior of a polygon defined by an array of points specified by System.Drawing.Point 

    structures.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.Point structures that represent the vertices of the polygon to fill.

  FillPolygon(self: Graphics,brush: Brush,points: Array[PointF])

   Fills the interior of a polygon defined by an array of points specified by System.Drawing.PointF 

    structures.

  

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   points: Array of System.Drawing.PointF structures that represent the vertices of the polygon to fill.
  """
  pass
 def FillRectangle(self,brush,*__args):
  """
  FillRectangle(self: Graphics,brush: Brush,x: int,y: int,width: int,height: int)

   Fills the interior of a rectangle specified by a pair of coordinates,a width,and a height.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the rectangle to fill.

   y: The y-coordinate of the upper-left corner of the rectangle to fill.

   width: Width of the rectangle to fill.

   height: Height of the rectangle to fill.

  FillRectangle(self: Graphics,brush: Brush,rect: RectangleF)

   Fills the interior of a rectangle specified by a System.Drawing.RectangleF structure.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rect: System.Drawing.RectangleF structure that represents the rectangle to fill.

  FillRectangle(self: Graphics,brush: Brush,x: Single,y: Single,width: Single,height: Single)

   Fills the interior of a rectangle specified by a pair of coordinates,a width,and a height.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   x: The x-coordinate of the upper-left corner of the rectangle to fill.

   y: The y-coordinate of the upper-left corner of the rectangle to fill.

   width: Width of the rectangle to fill.

   height: Height of the rectangle to fill.

  FillRectangle(self: Graphics,brush: Brush,rect: Rectangle)

   Fills the interior of a rectangle specified by a System.Drawing.Rectangle structure.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rect: System.Drawing.Rectangle structure that represents the rectangle to fill.
  """
  pass
 def FillRectangles(self,brush,rects):
  """
  FillRectangles(self: Graphics,brush: Brush,rects: Array[RectangleF])

   Fills the interiors of a series of rectangles specified by System.Drawing.RectangleF structures.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rects: Array of System.Drawing.RectangleF structures that represent the rectangles to fill.

  FillRectangles(self: Graphics,brush: Brush,rects: Array[Rectangle])

   Fills the interiors of a series of rectangles specified by System.Drawing.Rectangle structures.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   rects: Array of System.Drawing.Rectangle structures that represent the rectangles to fill.
  """
  pass
 def FillRegion(self,brush,region):
  """
  FillRegion(self: Graphics,brush: Brush,region: Region)

   Fills the interior of a System.Drawing.Region.

  

   brush: System.Drawing.Brush that determines the characteristics of the fill.

   region: System.Drawing.Region that represents the area to fill.
  """
  pass
 def Flush(self,intention=None):
  """
  Flush(self: Graphics,intention: FlushIntention)

   Forces execution of all pending graphics operations with the method waiting or not waiting,as 

    specified,to return before the operations finish.

  

  

   intention: Member of the System.Drawing.Drawing2D.FlushIntention enumeration that specifies whether the 

    method returns immediately or waits for any existing operations to finish.

  

  Flush(self: Graphics)

   Forces execution of all pending graphics operations and returns immediately without waiting for 

    the operations to finish.
  """
  pass
 @staticmethod
 def FromHdc(hdc,hdevice=None):
  """
  FromHdc(hdc: IntPtr,hdevice: IntPtr) -> Graphics

  

   Creates a new System.Drawing.Graphics from the specified handle to a device context and handle 

    to a device.

  

  

   hdc: Handle to a device context.

   hdevice: Handle to a device.

   Returns: This method returns a new System.Drawing.Graphics for the specified device context and device.

  FromHdc(hdc: IntPtr) -> Graphics

  

   Creates a new System.Drawing.Graphics from the specified handle to a device context.

  

   hdc: Handle to a device context.

   Returns: This method returns a new System.Drawing.Graphics for the specified device context.
  """
  pass
 @staticmethod
 def FromHdcInternal(hdc):
  """
  FromHdcInternal(hdc: IntPtr) -> Graphics

  

   Returns a System.Drawing.Graphics for the specified device context.

  

   hdc: Handle to a device context.

   Returns: A System.Drawing.Graphics for the specified device context.
  """
  pass
 @staticmethod
 def FromHwnd(hwnd):
  """
  FromHwnd(hwnd: IntPtr) -> Graphics

  

   Creates a new System.Drawing.Graphics from the specified handle to a window.

  

   hwnd: Handle to a window.

   Returns: This method returns a new System.Drawing.Graphics for the specified window handle.
  """
  pass
 @staticmethod
 def FromHwndInternal(hwnd):
  """
  FromHwndInternal(hwnd: IntPtr) -> Graphics

  

   Creates a new System.Drawing.Graphics for the specified windows handle.

  

   hwnd: Handle to a window.

   Returns: A System.Drawing.Graphics for the specified window handle.
  """
  pass
 @staticmethod
 def FromImage(image):
  """
  FromImage(image: Image) -> Graphics

  

   Creates a new System.Drawing.Graphics from the specified System.Drawing.Image.

  

   image: System.Drawing.Image from which to create the new System.Drawing.Graphics.

   Returns: This method returns a new System.Drawing.Graphics for the specified System.Drawing.Image.
  """
  pass
 def GetContextInfo(self):
  """
  GetContextInfo(self: Graphics) -> object

  

   Gets the cumulative graphics context.

   Returns: An System.Object representing the cumulative graphics context.
  """
  pass
 @staticmethod
 def GetHalftonePalette():
  """
  GetHalftonePalette() -> IntPtr

  

   Gets a handle to the current Windows halftone palette.

   Returns: Internal pointer that specifies the handle to the palette.
  """
  pass
 def GetHdc(self):
  """
  GetHdc(self: Graphics) -> IntPtr

  

   Gets the handle to the device context associated with this System.Drawing.Graphics.

   Returns: Handle to the device context associated with this System.Drawing.Graphics.
  """
  pass
 def GetNearestColor(self,color):
  """
  GetNearestColor(self: Graphics,color: Color) -> Color

  

   Gets the nearest color to the specified System.Drawing.Color structure.

  

   color: System.Drawing.Color structure for which to find a match.

   Returns: A System.Drawing.Color structure that represents the nearest color to the one specified with the 

    color parameter.
  """
  pass
 def IntersectClip(self,*__args):
  """
  IntersectClip(self: Graphics,region: Region)

   Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 

    region and the specified System.Drawing.Region.

  

  

   region: System.Drawing.Region to intersect with the current region.

  IntersectClip(self: Graphics,rect: RectangleF)

   Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 

    region and the specified System.Drawing.RectangleF structure.

  

  

   rect: System.Drawing.RectangleF structure to intersect with the current clip region.

  IntersectClip(self: Graphics,rect: Rectangle)

   Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 

    region and the specified System.Drawing.Rectangle structure.

  

  

   rect: System.Drawing.Rectangle structure to intersect with the current clip region.
  """
  pass
 def IsVisible(self,*__args):
  """
  IsVisible(self: Graphics,x: int,y: int,width: int,height: int) -> bool

  

   Indicates whether the rectangle specified by a pair of coordinates,a width,and a height is 

    contained within the visible clip region of this System.Drawing.Graphics.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test for visibility.

   y: The y-coordinate of the upper-left corner of the rectangle to test for visibility.

   width: Width of the rectangle to test for visibility.

   height: Height of the rectangle to test for visibility.

   Returns: true if the rectangle defined by the x,y,width,and height parameters is contained within the 

    visible clip region of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,point: PointF) -> bool

  

   Indicates whether the specified System.Drawing.PointF structure is contained within the visible 

    clip region of this System.Drawing.Graphics.

  

  

   point: System.Drawing.PointF structure to test for visibility.

   Returns: true if the point specified by the point parameter is contained within the visible clip region 

    of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,rect: RectangleF) -> bool

  

   Indicates whether the rectangle specified by a System.Drawing.RectangleF structure is contained 

    within the visible clip region of this System.Drawing.Graphics.

  

  

   rect: System.Drawing.RectangleF structure to test for visibility.

   Returns: true if the rectangle specified by the rect parameter is contained within the visible clip 

    region of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,x: Single,y: Single,width: Single,height: Single) -> bool

  

   Indicates whether the rectangle specified by a pair of coordinates,a width,and a height is 

    contained within the visible clip region of this System.Drawing.Graphics.

  

  

   x: The x-coordinate of the upper-left corner of the rectangle to test for visibility.

   y: The y-coordinate of the upper-left corner of the rectangle to test for visibility.

   width: Width of the rectangle to test for visibility.

   height: Height of the rectangle to test for visibility.

   Returns: true if the rectangle defined by the x,y,width,and height parameters is contained within the 

    visible clip region of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,x: int,y: int) -> bool

  

   Indicates whether the point specified by a pair of coordinates is contained within the visible 

    clip region of this System.Drawing.Graphics.

  

  

   x: The x-coordinate of the point to test for visibility.

   y: The y-coordinate of the point to test for visibility.

   Returns: true if the point defined by the x and y parameters is contained within the visible clip region 

    of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,rect: Rectangle) -> bool

  

   Indicates whether the rectangle specified by a System.Drawing.Rectangle structure is contained 

    within the visible clip region of this System.Drawing.Graphics.

  

  

   rect: System.Drawing.Rectangle structure to test for visibility.

   Returns: true if the rectangle specified by the rect parameter is contained within the visible clip 

    region of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,x: Single,y: Single) -> bool

  

   Indicates whether the point specified by a pair of coordinates is contained within the visible 

    clip region of this System.Drawing.Graphics.

  

  

   x: The x-coordinate of the point to test for visibility.

   y: The y-coordinate of the point to test for visibility.

   Returns: true if the point defined by the x and y parameters is contained within the visible clip region 

    of this System.Drawing.Graphics; otherwise,false.

  

  IsVisible(self: Graphics,point: Point) -> bool

  

   Indicates whether the specified System.Drawing.Point structure is contained within the visible 

    clip region of this System.Drawing.Graphics.

  

  

   point: System.Drawing.Point structure to test for visibility.

   Returns: true if the point specified by the point parameter is contained within the visible clip region 

    of this System.Drawing.Graphics; otherwise,false.
  """
  pass
 def MeasureCharacterRanges(self,text,font,layoutRect,stringFormat):
  """
  MeasureCharacterRanges(self: Graphics,text: str,font: Font,layoutRect: RectangleF,stringFormat: StringFormat) -> Array[Region]

  

   Gets an array of System.Drawing.Region objects,each of which bounds a range of character 

    positions within the specified string.

  

  

   text: String to measure.

   font: System.Drawing.Font that defines the text format of the string.

   layoutRect: System.Drawing.RectangleF structure that specifies the layout rectangle for the string.

   stringFormat: System.Drawing.StringFormat that represents formatting information,such as line spacing,for 

    the string.

  

   Returns: This method returns an array of System.Drawing.Region objects,each of which bounds a range of 

    character positions within the specified string.
  """
  pass
 def MeasureString(self,text,font,*__args):
  """
  MeasureString(self: Graphics,text: str,font: Font,origin: PointF,stringFormat: StringFormat) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font and formatted 

    with the specified System.Drawing.StringFormat.

  

  

   text: String to measure.

   font: System.Drawing.Font defines the text format of the string.

   origin: System.Drawing.PointF structure that represents the upper-left corner of the string.

   stringFormat: System.Drawing.StringFormat that represents formatting information,such as line spacing,for 

    the string.

  

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified by the text 

    parameter as drawn with the font parameter and the stringFormat parameter.

  

  MeasureString(self: Graphics,text: str,font: Font,layoutArea: SizeF) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font within the 

    specified layout area.

  

  

   text: String to measure.

   font: System.Drawing.Font defines the text format of the string.

   layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified by the text 

    parameter as drawn with the font parameter.

  

  MeasureString(self: Graphics,text: str,font: Font,width: int) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font.

  

   text: String to measure.

   font: System.Drawing.Font that defines the format of the string.

   width: Maximum width of the string in pixels.

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified in the text 

    parameter as drawn with the font parameter.

  

  MeasureString(self: Graphics,text: str,font: Font,layoutArea: SizeF,stringFormat: StringFormat) -> (SizeF,int,int)

  

   Measures the specified string when drawn with the specified System.Drawing.Font and formatted 

    with the specified System.Drawing.StringFormat.

  

  

   text: String to measure.

   font: System.Drawing.Font that defines the text format of the string.

   layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.

   stringFormat: System.Drawing.StringFormat that represents formatting information,such as line spacing,for 

    the string.

  

   Returns: This method returns a System.Drawing.SizeF structure that represents the size of the string,in 

    the units specified by the System.Drawing.Graphics.PageUnit property,of the text parameter as 

    drawn with the font parameter and the stringFormat parameter.

  

  MeasureString(self: Graphics,text: str,font: Font,layoutArea: SizeF,stringFormat: StringFormat) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font and formatted 

    with the specified System.Drawing.StringFormat.

  

  

   text: String to measure.

   font: System.Drawing.Font defines the text format of the string.

   layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.

   stringFormat: System.Drawing.StringFormat that represents formatting information,such as line spacing,for 

    the string.

  

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified in the text 

    parameter as drawn with the font parameter and the stringFormat parameter.

  

  MeasureString(self: Graphics,text: str,font: Font) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font.

  

   text: String to measure.

   font: System.Drawing.Font that defines the text format of the string.

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified by the text 

    parameter as drawn with the font parameter.

  

  MeasureString(self: Graphics,text: str,font: Font,width: int,format: StringFormat) -> SizeF

  

   Measures the specified string when drawn with the specified System.Drawing.Font and formatted 

    with the specified System.Drawing.StringFormat.

  

  

   text: String to measure.

   font: System.Drawing.Font that defines the text format of the string.

   width: Maximum width of the string.

   format: System.Drawing.StringFormat that represents formatting information,such as line spacing,for 

    the string.

  

   Returns: This method returns a System.Drawing.SizeF structure that represents the size,in the units 

    specified by the System.Drawing.Graphics.PageUnit property,of the string specified in the text 

    parameter as drawn with the font parameter and the stringFormat parameter.
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
 def MultiplyTransform(self,matrix,order=None):
  """
  MultiplyTransform(self: Graphics,matrix: Matrix,order: MatrixOrder)

   Multiplies the world transformation of this System.Drawing.Graphics and specified the 

    System.Drawing.Drawing2D.Matrix in the specified order.

  

  

   matrix: 4x4 System.Drawing.Drawing2D.Matrix that multiplies the world transformation.

   order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that determines the order of the 

    multiplication.

  

  MultiplyTransform(self: Graphics,matrix: Matrix)

   Multiplies the world transformation of this System.Drawing.Graphics and specified the 

    System.Drawing.Drawing2D.Matrix.

  

  

   matrix: 4x4 System.Drawing.Drawing2D.Matrix that multiplies the world transformation.
  """
  pass
 def ReleaseHdc(self,hdc=None):
  """
  ReleaseHdc(self: Graphics)

   Releases a device context handle obtained by a previous call to the 

    System.Drawing.Graphics.GetHdc method of this System.Drawing.Graphics.

  

  ReleaseHdc(self: Graphics,hdc: IntPtr)

   Releases a device context handle obtained by a previous call to the 

    System.Drawing.Graphics.GetHdc method of this System.Drawing.Graphics.

  

  

   hdc: Handle to a device context obtained by a previous call to the System.Drawing.Graphics.GetHdc 

    method of this System.Drawing.Graphics.
  """
  pass
 def ReleaseHdcInternal(self,hdc):
  """
  ReleaseHdcInternal(self: Graphics,hdc: IntPtr)

   Releases a handle to a device context.

  

   hdc: Handle to a device context.
  """
  pass
 def ResetClip(self):
  """
  ResetClip(self: Graphics)

   Resets the clip region of this System.Drawing.Graphics to an infinite region.
  """
  pass
 def ResetTransform(self):
  """
  ResetTransform(self: Graphics)

   Resets the world transformation matrix of this System.Drawing.Graphics to the identity matrix.
  """
  pass
 def Restore(self,gstate):
  """
  Restore(self: Graphics,gstate: GraphicsState)

   Restores the state of this System.Drawing.Graphics to the state represented by a 

    System.Drawing.Drawing2D.GraphicsState.

  

  

   gstate: System.Drawing.Drawing2D.GraphicsState that represents the state to which to restore this 

    System.Drawing.Graphics.
  """
  pass
 def RotateTransform(self,angle,order=None):
  """
  RotateTransform(self: Graphics,angle: Single,order: MatrixOrder)

   Applies the specified rotation to the transformation matrix of this System.Drawing.Graphics in 

    the specified order.

  

  

   angle: Angle of rotation in degrees.

   order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 

    rotation is appended or prepended to the matrix transformation.

  

  RotateTransform(self: Graphics,angle: Single)

   Applies the specified rotation to the transformation matrix of this System.Drawing.Graphics.

  

   angle: Angle of rotation in degrees.
  """
  pass
 def Save(self):
  """
  Save(self: Graphics) -> GraphicsState

  

   Saves the current state of this System.Drawing.Graphics and identifies the saved state with a 

    System.Drawing.Drawing2D.GraphicsState.

  

   Returns: This method returns a System.Drawing.Drawing2D.GraphicsState that represents the saved state of 

    this System.Drawing.Graphics.
  """
  pass
 def ScaleTransform(self,sx,sy,order=None):
  """
  ScaleTransform(self: Graphics,sx: Single,sy: Single,order: MatrixOrder)

   Applies the specified scaling operation to the transformation matrix of this 

    System.Drawing.Graphics in the specified order.

  

  

   sx: Scale factor in the x direction.

   sy: Scale factor in the y direction.

   order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 

    scaling operation is prepended or appended to the transformation matrix.

  

  ScaleTransform(self: Graphics,sx: Single,sy: Single)

   Applies the specified scaling operation to the transformation matrix of this 

    System.Drawing.Graphics by prepending it to the object's transformation matrix.

  

  

   sx: Scale factor in the x direction.

   sy: Scale factor in the y direction.
  """
  pass
 def SetClip(self,*__args):
  """
  SetClip(self: Graphics,rect: RectangleF,combineMode: CombineMode)

   Sets the clipping region of this System.Drawing.Graphics to the result of the specified 

    operation combining the current clip region and the rectangle specified by a 

    System.Drawing.RectangleF structure.

  

  

   rect: System.Drawing.RectangleF structure to combine.

   combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 

    operation to use.

  

  SetClip(self: Graphics,rect: RectangleF)

   Sets the clipping region of this System.Drawing.Graphics to the rectangle specified by a 

    System.Drawing.RectangleF structure.

  

  

   rect: System.Drawing.RectangleF structure that represents the new clip region.

  SetClip(self: Graphics,path: GraphicsPath,combineMode: CombineMode)

   Sets the clipping region of this System.Drawing.Graphics to the result of the specified 

    operation combining the current clip region and the specified 

    System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: System.Drawing.Drawing2D.GraphicsPath to combine.

   combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 

    operation to use.

  

  SetClip(self: Graphics,path: GraphicsPath)

   Sets the clipping region of this System.Drawing.Graphics to the specified 

    System.Drawing.Drawing2D.GraphicsPath.

  

  

   path: System.Drawing.Drawing2D.GraphicsPath that represents the new clip region.

  SetClip(self: Graphics,rect: Rectangle,combineMode: CombineMode)

   Sets the clipping region of this System.Drawing.Graphics to the result of the specified 

    operation combining the current clip region and the rectangle specified by a 

    System.Drawing.Rectangle structure.

  

  

   rect: System.Drawing.Rectangle structure to combine.

   combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 

    operation to use.

  

  SetClip(self: Graphics,region: Region,combineMode: CombineMode)

   Sets the clipping region of this System.Drawing.Graphics to the result of the specified 

    operation combining the current clip region and the specified System.Drawing.Region.

  

  

   region: System.Drawing.Region to combine.

   combineMode: Member from the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 

    operation to use.

  

  SetClip(self: Graphics,rect: Rectangle)

   Sets the clipping region of this System.Drawing.Graphics to the rectangle specified by a 

    System.Drawing.Rectangle structure.

  

  

   rect: System.Drawing.Rectangle structure that represents the new clip region.

  SetClip(self: Graphics,g: Graphics,combineMode: CombineMode)

   Sets the clipping region of this System.Drawing.Graphics to the result of the specified 

    combining operation of the current clip region and the System.Drawing.Graphics.Clip property of 

    the specified System.Drawing.Graphics.

  

  

   g: System.Drawing.Graphics that specifies the clip region to combine.

   combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 

    operation to use.

  

  SetClip(self: Graphics,g: Graphics)

   Sets the clipping region of this System.Drawing.Graphics to the Clip property of the specified 

    System.Drawing.Graphics.

  

  

   g: System.Drawing.Graphics from which to take the new clip region.
  """
  pass
 def TransformPoints(self,destSpace,srcSpace,pts):
  """
  TransformPoints(self: Graphics,destSpace: CoordinateSpace,srcSpace: CoordinateSpace,pts: Array[Point])

   Transforms an array of points from one coordinate space to another using the current world and 

    page transformations of this System.Drawing.Graphics.

  

  

   destSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the 

    destination coordinate space.

  

   srcSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the source 

    coordinate space.

  

   pts: Array of System.Drawing.Point structures that represents the points to transformation.

  TransformPoints(self: Graphics,destSpace: CoordinateSpace,srcSpace: CoordinateSpace,pts: Array[PointF])

   Transforms an array of points from one coordinate space to another using the current world and 

    page transformations of this System.Drawing.Graphics.

  

  

   destSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the 

    destination coordinate space.

  

   srcSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the source 

    coordinate space.

  

   pts: Array of System.Drawing.PointF structures that represent the points to transform.
  """
  pass
 def TranslateClip(self,dx,dy):
  """
  TranslateClip(self: Graphics,dx: Single,dy: Single)

   Translates the clipping region of this System.Drawing.Graphics by specified amounts in the 

    horizontal and vertical directions.

  

  

   dx: The x-coordinate of the translation.

   dy: The y-coordinate of the translation.

  TranslateClip(self: Graphics,dx: int,dy: int)

   Translates the clipping region of this System.Drawing.Graphics by specified amounts in the 

    horizontal and vertical directions.

  

  

   dx: The x-coordinate of the translation.

   dy: The y-coordinate of the translation.
  """
  pass
 def TranslateTransform(self,dx,dy,order=None):
  """
  TranslateTransform(self: Graphics,dx: Single,dy: Single,order: MatrixOrder)

   Changes the origin of the coordinate system by applying the specified translation to the 

    transformation matrix of this System.Drawing.Graphics in the specified order.

  

  

   dx: The x-coordinate of the translation.

   dy: The y-coordinate of the translation.

   order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 

    translation is prepended or appended to the transformation matrix.

  

  TranslateTransform(self: Graphics,dx: Single,dy: Single)

   Changes the origin of the coordinate system by prepending the specified translation to the 

    transformation matrix of this System.Drawing.Graphics.

  

  

   dx: The x-coordinate of the translation.

   dy: The y-coordinate of the translation.
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
 Clip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Drawing.Region that limits the drawing region of this System.Drawing.Graphics.



Get: Clip(self: Graphics) -> Region



Set: Clip(self: Graphics)=value

"""

 ClipBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Drawing.RectangleF structure that bounds the clipping region of this System.Drawing.Graphics.



Get: ClipBounds(self: Graphics) -> RectangleF



"""

 CompositingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies how composited images are drawn to this System.Drawing.Graphics.



Get: CompositingMode(self: Graphics) -> CompositingMode



Set: CompositingMode(self: Graphics)=value

"""

 CompositingQuality=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rendering quality of composited images drawn to this System.Drawing.Graphics.



Get: CompositingQuality(self: Graphics) -> CompositingQuality



Set: CompositingQuality(self: Graphics)=value

"""

 DpiX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal resolution of this System.Drawing.Graphics.



Get: DpiX(self: Graphics) -> Single



"""

 DpiY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical resolution of this System.Drawing.Graphics.



Get: DpiY(self: Graphics) -> Single



"""

 InterpolationMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the interpolation mode associated with this System.Drawing.Graphics.



Get: InterpolationMode(self: Graphics) -> InterpolationMode



Set: InterpolationMode(self: Graphics)=value

"""

 IsClipEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the clipping region of this System.Drawing.Graphics is empty.



Get: IsClipEmpty(self: Graphics) -> bool



"""

 IsVisibleClipEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the visible clipping region of this System.Drawing.Graphics is empty.



Get: IsVisibleClipEmpty(self: Graphics) -> bool



"""

 PageScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scaling between world units and page units for this System.Drawing.Graphics.



Get: PageScale(self: Graphics) -> Single



Set: PageScale(self: Graphics)=value

"""

 PageUnit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the unit of measure used for page coordinates in this System.Drawing.Graphics.



Get: PageUnit(self: Graphics) -> GraphicsUnit



Set: PageUnit(self: Graphics)=value

"""

 PixelOffsetMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or set a value specifying how pixels are offset during rendering of this System.Drawing.Graphics.



Get: PixelOffsetMode(self: Graphics) -> PixelOffsetMode



Set: PixelOffsetMode(self: Graphics)=value

"""

 RenderingOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rendering origin of this System.Drawing.Graphics for dithering and for hatch brushes.



Get: RenderingOrigin(self: Graphics) -> Point



Set: RenderingOrigin(self: Graphics)=value

"""

 SmoothingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rendering quality for this System.Drawing.Graphics.



Get: SmoothingMode(self: Graphics) -> SmoothingMode



Set: SmoothingMode(self: Graphics)=value

"""

 TextContrast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the gamma correction value for rendering text.



Get: TextContrast(self: Graphics) -> int



Set: TextContrast(self: Graphics)=value

"""

 TextRenderingHint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rendering mode for text associated with this System.Drawing.Graphics.



Get: TextRenderingHint(self: Graphics) -> TextRenderingHint



Set: TextRenderingHint(self: Graphics)=value

"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a copy of the geometric world transformation for this System.Drawing.Graphics.



Get: Transform(self: Graphics) -> Matrix



Set: Transform(self: Graphics)=value

"""

 VisibleClipBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding rectangle of the visible clipping region of this System.Drawing.Graphics.



Get: VisibleClipBounds(self: Graphics) -> RectangleF



"""


 DrawImageAbort=None
 EnumerateMetafileProc=None

