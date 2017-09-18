class RevolvedSurface(Surface,IDisposable):
 """
 A surface of revolution defined by a profile curve and a local coordinate system.

    The surface is obtained by rotating the curve around Z axis of the local coordinate system.
 """
 @staticmethod
 def Create(*__args):
  """
  Create(axisBasePoint: XYZ,axisDirection: XYZ,profileCurve: Curve,startAngle: float,endAngle: float) -> Surface

  

   Creates a Surface object coincident with the surface of revolution defined by 

    an axis,a profile curve,

     and start and end angles of revolution.

  

  

   axisBasePoint: The base point of the axis of revolution.  Expected to lie within the Revit 

    design limits 

    Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).

  

   axisDirection: The direction of the axis.

   profileCurve: The profile curve,which should satisfy the following conditions:

   It is 

    bounded and non-degenerate.  It is co-planar with the axis of revolution.  It 

    lies on only one side of the axis.  Only the end points of the profile curve 

    can touch the axis.

  

   startAngle: Start angle of rotation.

     The angles are measured around the axis of 

    revolution,using the right-hand rule.

     The profile curve is at the zero 

    angle.

  

   endAngle: End angle of rotation.

     Start angle must be less than end angle and their 

    difference must be less than or equal to two times PI.

  

   Returns: The created surface. Note that this surface may not be of type RevolvedSurface.

  Create(axisBasePoint: XYZ,axisDirection: XYZ,profileCurve: Curve) -> Surface

  

   Creates a Surface object coincident with the surface of revolution defined by 

    an axis and a profile curve.

  

  

   axisBasePoint: The base point of the axis of revolution.  Expected to lie within the Revit 

    design limits 

    Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).

  

   axisDirection: The direction of the axis.

   profileCurve: The profile curve,which should satisfy the following conditions:

   It is 

    bounded and non-degenerate.  It is co-planar with the axis of revolution.  It 

    lies on only one side of the axis.  Only the end points of the profile curve 

    can touch the axis.

  

   Returns: The created surface. Note that this surface may not be of type RevolvedSurface.

  Create(frameOfReference: Frame,profileCurve: Curve,startAngle: float,endAngle: float) -> Surface

  

   Creates a Surface object coincident with the surface of revolution defined by a 

    coordinate frame,a profile curve,

     and start and end angles of revolution.

  

  

   frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 

    for the surface of revolution.

   The frame can be "right-handed" or 

    "left-handed".  The origin of the frame is the base of point of the axis of 

    revolution. The BasisZ of the frame is the direction of the axis.

  

   profileCurve: The profile curve,which should satisfy the following conditions:

   It is 

    bounded and non-degenerate.  It is co-planar with the axis of revolution.  It 

    lies on the xz plane of the frame.  It lies on the right side of the axis.  

    Only the end points of the profile curve can touch the axis.

  

   startAngle: Start angle of rotation.

     The angles are measured around the axis of 

    revolution,using the right-hand rule.

     The profile curve is at the zero 

    angle.

  

   endAngle: End angle of rotation.

     Start angle must be less than end angle and their 

    difference must be less than or equal to two times PI.

  

   Returns: The created surface. Note that this surface may not be of type RevolvedSurface.

  Create(frameOfReference: Frame,profileCurve: Curve) -> Surface

  

   Creates a Surface object coincident with the surface of revolution defined by a 

    coordinate frame and a profile curve.

  

  

   frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 

    for the surface of revolution.

   The frame can be "right-handed" or 

    "left-handed".  The origin of the frame is the base of point of the axis of 

    revolution. The BasisZ of the frame is the direction of the axis.

  

   profileCurve: The profile curve,which should satisfy the following conditions:

   It is 

    bounded and non-degenerate.  It is co-planar with the axis of revolution.  It 

    lies on the xz plane of the frame.  It lies on the right side of the axis.  

    Only the end points of the profile curve can touch the axis.

  

   Returns: The created surface. Note that this surface may not be of type RevolvedSurface.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Surface,A_0: bool) """
  pass
 def GetProfileCurve(self):
  """
  GetProfileCurve(self: RevolvedSurface) -> Curve

  

   Returns a copy of the profile curve expressed in the surface's coordinate 

    system.

  

   Returns: A copy of the profile curve.
  """
  pass
 @staticmethod
 def IsValidProfileCurve(*__args):
  """
  IsValidProfileCurve(axisBasePoint: XYZ,axisDirection: XYZ,profileCurve: Curve) -> bool

  

   Checks if the input profile curve is valid to create a surface of revolution 

    around the given axis.

  

  

   axisBasePoint: The base point of the axis of revolution.

   axisDirection: The direction of the axis.

   profileCurve: The profile curve.

   Returns: True if the profile curve is valid; False otherwise.

  IsValidProfileCurve(frameOfReference: Frame,profileCurve: Curve) -> bool

  

   Checks if the input profile curve is valid to create a surface of revolution in 

    the given frame of reference.

  

  

   frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 

    for the surface of revolution.

   The frame can be "right-handed" or 

    "left-handed".  The origin of the frame is the base of point of the axis of 

    revolution. The BasisZ of the frame is the direction of the axis.

  

   profileCurve: The profile curve.

   Returns: True if the profile curve is valid; False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Surface,disposing: bool) """
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
 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Axis of the revolved surface. This is the Z axis of the local coordinate system associated with this revolved surface.



Get: Axis(self: RevolvedSurface) -> XYZ



"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Center of the circle that defines the base of the revolved surface. This is the origin of the local coordinate system associated with this revolved surface.



Get: Origin(self: RevolvedSurface) -> XYZ



"""

 XDir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """X axis of the local coordinate system associated with this revolved surface.



Get: XDir(self: RevolvedSurface) -> XYZ



"""

 YDir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """X axis of the local coordinate system associated with this revolved surface.



Get: YDir(self: RevolvedSurface) -> XYZ



"""


