class DpiScale(object):
 """ DpiScale(dpiScaleX: float,dpiScaleY: float) """
 @staticmethod
 def __new__(self,dpiScaleX,dpiScaleY):
  """
  __new__[DpiScale]() -> DpiScale
  
  __new__(cls: type,dpiScaleX: float,dpiScaleY: float)
  """
  pass
 DpiScaleX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DpiScaleX(self: DpiScale) -> float

"""

 DpiScaleY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DpiScaleY(self: DpiScale) -> float

"""

 PixelsPerDip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PixelsPerDip(self: DpiScale) -> float

"""

 PixelsPerInchX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PixelsPerInchX(self: DpiScale) -> float

"""

 PixelsPerInchY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PixelsPerInchY(self: DpiScale) -> float

"""


