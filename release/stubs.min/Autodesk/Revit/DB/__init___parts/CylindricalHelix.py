class CylindricalHelix(Curve,IDisposable):
 """ A cylindrical helix. """
 @staticmethod
 def Create(basePoint,radius,xVector,zVector,pitch,startAngle,endAngle):
  """
  Create(basePoint: XYZ,radius: float,xVector: XYZ,zVector: XYZ,pitch: float,startAngle: float,endAngle: float) -> CylindricalHelix

  

   Create a cylindrical helix.

  

   basePoint: Base point of the axis. It can be any point in 3d.

   radius: Radius. It should be a positive number.

   xVector: X vector. Should be Non-zero vector.

   zVector: Z vector=axis direction. Should be non-zero and orthogonal to X Vector.

   pitch: Pitch. It should be non-zero number,can be positive or negative.

      

        Positive means right handed and negative means left handed.

  

   startAngle: Start angle. It specifies the start point of the Helix.

   endAngle: End angle. It specifies the end point of the Helix. 

          

    End angle should not be equal to start angle.
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
 BasePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The base point of the axis of the cylindrical helix.



Get: BasePoint(self: CylindricalHelix) -> XYZ



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height of the cylindrical helix.



Get: Height(self: CylindricalHelix) -> float



"""

 IsRightHanded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the helix is right handed,false if the helix is left handed.



Get: IsRightHanded(self: CylindricalHelix) -> bool



"""

 Pitch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The pitch of the cylindrical helix.



Get: Pitch(self: CylindricalHelix) -> float



"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The radius of the cylindrical helix.



Get: Radius(self: CylindricalHelix) -> float



"""

 XVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The X direction vector.



Get: XVector(self: CylindricalHelix) -> XYZ



"""

 YVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Y direction vector.



Get: YVector(self: CylindricalHelix) -> XYZ



"""

 ZVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Z direction vector,which is same as the axis direction vector.



Get: ZVector(self: CylindricalHelix) -> XYZ



"""


