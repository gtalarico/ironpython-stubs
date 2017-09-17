class DrawingContext(DispatcherObject,IDisposable):
 """ Describes visual content using draw,push,and pop commands. """
 def Close(self):
  """
  Close(self: DrawingContext)
   Closes the System.Windows.Media.DrawingContext and flushes the content. 
    Afterward,the System.Windows.Media.DrawingContext cannot be modified.
  """
  pass
 def DisposeCore(self,*args):
  """
  DisposeCore(self: DrawingContext)
   Releases all resources used by the System.Windows.Media.DrawingContext.
  """
  pass
 def DrawDrawing(self,drawing):
  """
  DrawDrawing(self: DrawingContext,drawing: Drawing)
   Draws the specified System.Windows.Media.Drawing object.
  
   drawing: The drawing to append.
  """
  pass
 def DrawEllipse(self,brush,pen,center,*__args):
  """
  DrawEllipse(self: DrawingContext,brush: Brush,pen: Pen,center: Point,centerAnimations: AnimationClock,radiusX: float,radiusXAnimations: AnimationClock,radiusY: float,radiusYAnimations: AnimationClock)
   Draws an ellipse with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen and applies the specified animation clocks.
  
  
   brush: The brush with which to fill the ellipse.  This is optional,and can be null. 
    If the brush is null,no fill is drawn.
  
   pen: The pen with which to stroke the ellipse.  This is optional,and can be null. 
    If the pen is null,no stroke is drawn.
  
   center: The location of the center of the ellipse.
   centerAnimations: The clock with which to animate the ellipse's center position,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Point objects.
  
   radiusX: The horizontal radius of the ellipse.
   radiusXAnimations: The clock with which to animate the ellipse's x-radius,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate System.Double 
    objects.
  
   radiusY: The vertical radius of the ellipse.
   radiusYAnimations: The clock with which to animate the ellipse's y-radius,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate System.Double 
    objects.
  
  DrawEllipse(self: DrawingContext,brush: Brush,pen: Pen,center: Point,radiusX: float,radiusY: float)
   Draws an ellipse with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen.
  
  
   brush: The brush with which to fill the ellipse.  This is optional,and can be null. 
    If the brush is null,no fill is drawn.
  
   pen: The pen with which to stroke the ellipse.  This is optional,and can be null. 
    If the pen is null,no stroke is drawn.
  
   center: The location of the center of the ellipse.
   radiusX: The horizontal radius of the ellipse.
   radiusY: The vertical radius of the ellipse.
  """
  pass
 def DrawGeometry(self,brush,pen,geometry):
  """
  DrawGeometry(self: DrawingContext,brush: Brush,pen: Pen,geometry: Geometry)
   Draws the specified System.Windows.Media.Geometry using the specified 
    System.Windows.Media.Brush and System.Windows.Media.Pen.
  
  
   brush: The System.Windows.Media.Brush with which to fill the 
    System.Windows.Media.Geometry. This is optional,and can be null. If the brush 
    is null,no fill is drawn.
  
   pen: The System.Windows.Media.Pen with which to stroke the 
    System.Windows.Media.Geometry. This is optional,and can be null. If the pen is 
    null,no stroke is drawn.
  
   geometry: The System.Windows.Media.Geometry to draw.
  """
  pass
 def DrawGlyphRun(self,foregroundBrush,glyphRun):
  """
  DrawGlyphRun(self: DrawingContext,foregroundBrush: Brush,glyphRun: GlyphRun)
   Draws the specified text.
  
   foregroundBrush: The brush used to paint the text.
   glyphRun: The text to draw.
  """
  pass
 def DrawImage(self,imageSource,rectangle,rectangleAnimations=None):
  """
  DrawImage(self: DrawingContext,imageSource: ImageSource,rectangle: Rect,rectangleAnimations: AnimationClock)
   Draws an image into the region defined by the specified System.Windows.Rect and 
    applies the specified animation clock.
  
  
   imageSource: The image to draw.
   rectangle: The region in which to draw bitmapSource.
   rectangleAnimations: The clock with which to animate the rectangle's size and dimensions,or null 
    for no animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Rect objects.
  
  DrawImage(self: DrawingContext,imageSource: ImageSource,rectangle: Rect)
   Draws an image into the region defined by the specified System.Windows.Rect.
  
   imageSource: The image to draw.
   rectangle: The region in which to draw bitmapSource.
  """
  pass
 def DrawLine(self,pen,point0,*__args):
  """
  DrawLine(self: DrawingContext,pen: Pen,point0: Point,point0Animations: AnimationClock,point1: Point,point1Animations: AnimationClock)
   Draws a line between the specified points using the specified 
    System.Windows.Media.Pen and applies the specified animation clocks.
  
  
   pen: The pen to stroke the line.
   point0: The start point of the line.
   point0Animations: The clock with which to animate the start point of the line,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Point objects.
  
   point1: The end point of the line.
   point1Animations: The clock with which to animate the end point of the line,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Point objects.
  
  DrawLine(self: DrawingContext,pen: Pen,point0: Point,point1: Point)
   Draws a line between the specified points using the specified 
    System.Windows.Media.Pen.
  
  
   pen: The pen with which to stroke the line.
   point0: The start point of the line.
   point1: The end point of the line.
  """
  pass
 def DrawRectangle(self,brush,pen,rectangle,rectangleAnimations=None):
  """
  DrawRectangle(self: DrawingContext,brush: Brush,pen: Pen,rectangle: Rect,rectangleAnimations: AnimationClock)
   Draws a rectangle with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen and applies the specified animation clocks.
  
  
   brush: The brush with which to fill the rectangle.  This is optional,and can be null. 
    If the brush is null,no fill is drawn.
  
   pen: The pen with which to stroke the rectangle.  This is optional,and can be null. 
    If the pen is null,no stroke is drawn.
  
   rectangle: The rectangle to draw.
   rectangleAnimations: The clock with which to animate the rectangle's size and dimensions,or null 
    for no animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Rect objects.
  
  DrawRectangle(self: DrawingContext,brush: Brush,pen: Pen,rectangle: Rect)
   Draws a rectangle with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen. The pen and the brush can be null.
  
  
   brush: The brush with which to fill the rectangle.  This is optional,and can be null. 
    If the brush is null,no fill is drawn.
  
   pen: The pen with which to stroke the rectangle.  This is optional,and can be null. 
    If the pen is null,no stroke is drawn.
  
   rectangle: The rectangle to draw.
  """
  pass
 def DrawRoundedRectangle(self,brush,pen,rectangle,*__args):
  """
  DrawRoundedRectangle(self: DrawingContext,brush: Brush,pen: Pen,rectangle: Rect,rectangleAnimations: AnimationClock,radiusX: float,radiusXAnimations: AnimationClock,radiusY: float,radiusYAnimations: AnimationClock)
   Draws a rounded rectangle with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen and applies the specified animation clocks.
  
  
   brush: The brush used to fill the rectangle,or null for no fill.
   pen: The pen used to stroke the rectangle,or null for no stroke.
   rectangle: The rectangle to draw.
   rectangleAnimations: The clock with which to animate the rectangle's size and dimensions,or null 
    for no animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Rect objects.
  
   radiusX: The radius in the X dimension of the rounded corners.  This value will be 
    clamped to the range of 0 to System.Windows.Rect.Width/2
  
   radiusXAnimations: The clock with which to animate the rectangle's radiusX value,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate System.Double 
    values.
  
   radiusY: The radius in the Y dimension of the rounded corners.  This value will be 
    clamped to a value between 0 to System.Windows.Rect.Height/2.
  
   radiusYAnimations: The clock with which to animate the rectangle's radiusY value,or null for no 
    animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate System.Double 
    values.
  
  DrawRoundedRectangle(self: DrawingContext,brush: Brush,pen: Pen,rectangle: Rect,radiusX: float,radiusY: float)
   Draws a rounded rectangle with the specified System.Windows.Media.Brush and 
    System.Windows.Media.Pen.
  
  
   brush: The brush used to fill the rectangle.
   pen: The pen used to stroke the rectangle.
   rectangle: The rectangle to draw.
   radiusX: The radius in the X dimension of the rounded corners.  This value will be 
    clamped to the range of 0 to System.Windows.Rect.Width/2.
  
   radiusY: The radius in the Y dimension of the rounded corners.  This value will be 
    clamped to a value between 0 to System.Windows.Rect.Height/2.
  """
  pass
 def DrawText(self,formattedText,origin):
  """
  DrawText(self: DrawingContext,formattedText: FormattedText,origin: Point)
   Draws formatted text at the specified location.
  
   formattedText: The formatted text to be drawn.
   origin: The location where the text is to be drawn.
  """
  pass
 def DrawVideo(self,player,rectangle,rectangleAnimations=None):
  """
  DrawVideo(self: DrawingContext,player: MediaPlayer,rectangle: Rect,rectangleAnimations: AnimationClock)
   Draws a video into the specified region and applies the specified animation 
    clock.
  
  
   player: The media to draw.
   rectangle: The area in which to draw the media.
   rectangleAnimations: The clock with which to animate the rectangle's size and dimensions,or null 
    for no animation. This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate 
    System.Windows.Rect objects.
  
  DrawVideo(self: DrawingContext,player: MediaPlayer,rectangle: Rect)
   Draws a video into the specified region.
  
   player: The media to draw.
   rectangle: The region in which to draw player.
  """
  pass
 def Pop(self):
  """
  Pop(self: DrawingContext)
   Pops the last opacity mask,opacity,clip,effect,or transform operation that 
    was pushed onto the drawing context.
  """
  pass
 def PushClip(self,clipGeometry):
  """
  PushClip(self: DrawingContext,clipGeometry: Geometry)
   Pushes the specified clip region onto the drawing context.
  
   clipGeometry: The clip region to apply to subsequent drawing commands.
  """
  pass
 def PushEffect(self,effect,effectInput):
  """
  PushEffect(self: DrawingContext,effect: BitmapEffect,effectInput: BitmapEffectInput)
   Pushes the specified System.Windows.Media.Effects.BitmapEffect onto the drawing 
    context.
  
  
   effect: The effect to apply to subsequent drawings.
   effectInput: The area to which the effect is applied,or null if the effect is to be applied 
    to the entire area of subsequent drawings.
  """
  pass
 def PushGuidelineSet(self,guidelines):
  """
  PushGuidelineSet(self: DrawingContext,guidelines: GuidelineSet)
   Pushes the specified System.Windows.Media.GuidelineSet onto the drawing context.
  
   guidelines: The guideline set to apply to subsequent drawing commands.
  """
  pass
 def PushOpacity(self,opacity,opacityAnimations=None):
  """
  PushOpacity(self: DrawingContext,opacity: float,opacityAnimations: AnimationClock)
   Pushes the specified opacity setting onto the drawing context and applies the 
    specified animation clock.
  
  
   opacity: The opacity factor to apply to subsequent drawing commands. This factor is 
    cumulative with previous 
    System.Windows.Media.DrawingContext.PushOpacity(System.Double) operations.
  
   opacityAnimations: The clock with which to animate the opacity value,or null for no animation. 
    This clock must be created from an 
    System.Windows.Media.Animation.AnimationTimeline that can animate System.Double 
    values.
  
  PushOpacity(self: DrawingContext,opacity: float)
   Pushes the specified opacity setting onto the drawing context.
  
   opacity: The opacity factor to apply to subsequent drawing commands. This factor is 
    cumulative with previous 
    System.Windows.Media.DrawingContext.PushOpacity(System.Double) operations.
  """
  pass
 def PushOpacityMask(self,opacityMask):
  """
  PushOpacityMask(self: DrawingContext,opacityMask: Brush)
   Pushes the specified opacity mask onto the drawing context.
  
   opacityMask: The opacity mask to apply to subsequent drawings. The alpha values of this 
    brush determine the opacity of the drawing to which it is applied.
  """
  pass
 def PushTransform(self,transform):
  """
  PushTransform(self: DrawingContext,transform: Transform)
   Pushes the specified System.Windows.Media.Transform onto the drawing context.
  
   transform: The transform to apply to subsequent drawing commands.
  """
  pass
 def VerifyApiNonstructuralChange(self,*args):
  """
  VerifyApiNonstructuralChange(self: DrawingContext)
   This member supports the WPF infrastructure and is not intended to be used 
    directly from your code.
  """
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
