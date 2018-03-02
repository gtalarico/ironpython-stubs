class BasePoint(object):
 """ BasePoint(id: int,guid: Guid,name: str,description: str,coordinateSystem: str,northSouth: float,eastWest: float,elevation: float,latitude: float,longitude: float,locationInModelX: float,locationInModelY: float,locationInModelZ: float,angleToNorth: float) """
 def GetCompoundPlaneAngleLatitude(self):
  """ GetCompoundPlaneAngleLatitude(self: BasePoint) -> Tuple[bool,int,int,int] """
  pass
 def GetCompoundPlaneAngleLongitude(self):
  """ GetCompoundPlaneAngleLongitude(self: BasePoint) -> Tuple[bool,int,int,int] """
  pass
 def GetCoordinateSystem(self,CoordsysType):
  """ GetCoordinateSystem(self: BasePoint,CoordsysType: CoordinateSystemType) -> CoordinateSystem """
  pass
 @staticmethod
 def __new__(self,id,guid,name,description,coordinateSystem,northSouth,eastWest,elevation,latitude,longitude,locationInModelX,locationInModelY,locationInModelZ,angleToNorth):
  """ __new__(cls: type,id: int,guid: Guid,name: str,description: str,coordinateSystem: str,northSouth: float,eastWest: float,elevation: float,latitude: float,longitude: float,locationInModelX: float,locationInModelY: float,locationInModelZ: float,angleToNorth: float) """
  pass
 AngleToNorth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleToNorth(self: BasePoint) -> float

Set: AngleToNorth(self: BasePoint)=value
"""

 CoordinateSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CoordinateSystem(self: BasePoint) -> str

Set: CoordinateSystem(self: BasePoint)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: BasePoint) -> str

Set: Description(self: BasePoint)=value
"""

 EastWest=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EastWest(self: BasePoint) -> float

Set: EastWest(self: BasePoint)=value
"""

 Elevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Elevation(self: BasePoint) -> float

Set: Elevation(self: BasePoint)=value
"""

 Guid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Guid(self: BasePoint) -> Guid

Set: Guid(self: BasePoint)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: BasePoint) -> int

Set: Id(self: BasePoint)=value
"""

 Latitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Latitude(self: BasePoint) -> float

Set: Latitude(self: BasePoint)=value
"""

 LocationInModelX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationInModelX(self: BasePoint) -> float

Set: LocationInModelX(self: BasePoint)=value
"""

 LocationInModelY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationInModelY(self: BasePoint) -> float

Set: LocationInModelY(self: BasePoint)=value
"""

 LocationInModelZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationInModelZ(self: BasePoint) -> float

Set: LocationInModelZ(self: BasePoint)=value
"""

 Longitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Longitude(self: BasePoint) -> float

Set: Longitude(self: BasePoint)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: BasePoint) -> str

Set: Name(self: BasePoint)=value
"""

 NorthSouth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NorthSouth(self: BasePoint) -> float

Set: NorthSouth(self: BasePoint)=value
"""


 CoordinateSystemType=None

