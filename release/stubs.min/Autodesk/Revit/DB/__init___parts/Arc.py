class Arc(Curve,IDisposable):
 """ A circular arc. """
 @staticmethod
 def Create(*__args):
  """
  Create(center: XYZ,radius: float,startAngle: float,endAngle: float,xAxis: XYZ,yAxis: XYZ) -> Arc

  

   Creates a new geometric arc object based on center,radius,unit vectors,and 

    angles.

  

  

   center: The center of the arc.

   radius: The radius of the arc.

   startAngle: The start angle of the arc (in radians).

   endAngle: The end angle of the arc (in radians).

   xAxis: The x axis to define the arc plane. Must be normalized.

   yAxis: The y axis to define the arc plane. Must be normalized.

   Returns: The new arc.

  Create(plane: Plane,radius: float,startAngle: float,endAngle: float) -> Arc

  

   Creates a new geometric arc object based on plane,radius,and angles.

  

   plane: The plane which the arc resides. The plane's origin is the center of the arc.

   radius: The radius of the arc.

   startAngle: The start angle of the arc (in radians).

   endAngle: The end angle of the arc (in radians).

   Returns: The new arc.

  Create(end0: XYZ,end1: XYZ,pointOnArc: XYZ) -> Arc

  

   Creates a new geometric arc object based on three points.

  

   end0: The start point of the arc.

   end1: The end point of the arc.

   pointOnArc: A point on the arc.

   Returns: The new arc.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
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
 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the center of the arc.



Get: Center(self: Arc) -> XYZ



"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the normal to the plane in which the arc is defined.



Get: Normal(self: Arc) -> XYZ



"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the radius of the arc.



Get: Radius(self: Arc) -> float



"""

 XDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the X direction.



Get: XDirection(self: Arc) -> XYZ



"""

 YDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Y direction.



Get: YDirection(self: Arc) -> XYZ



"""


