class WireMaterialType(ElementType,IDisposable):
 """ Represents electrical wire material type definition information of wire type. """
 def AddGroundConductorSize(self,ampacity,size):
  """
  AddGroundConductorSize(self: WireMaterialType,ampacity: Int64,size: str) -> GroundConductorSize

  

   Add new electrical ground conductor size type into this material type.

  

   ampacity: Ampacity of ground conductor size to be added.

   size: Size of ground conductor size to be added.

   Returns: New added ground conductor size.
  """
  pass
 def AddTemperatureRatingType(self,name,baseOn):
  """
  AddTemperatureRatingType(self: WireMaterialType,name: str,baseOn: TemperatureRatingType) -> TemperatureRatingType

  

   Add a new temperature rating type into material type.

  

   name: Name of temperature type to be added.

   baseOn: The new temperature rating will be created base on this existing temperature 

    rating type.

  

   Returns: New constructed temperature rating type.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveGroundConductorSize(self,grdConductorSize):
  """
  RemoveGroundConductorSize(self: WireMaterialType,grdConductorSize: GroundConductorSize)

   Remove an existing ground conductor size from this material type.

  

   grdConductorSize: The ground size type to be removed.
  """
  pass
 def RemoveTemperatureRatingType(self,temperatureRating):
  """
  RemoveTemperatureRatingType(self: WireMaterialType,temperatureRating: TemperatureRatingType)

   Remove an existing temperature rating type from this material type.

  

   temperatureRating: The temperature rating type to be removed.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 GroundConductorSizes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all ground conductor size types defined in this wire material type.



Get: GroundConductorSizes(self: WireMaterialType) -> GroundConductorSizeSet



"""

 IsInUse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicate whether the wire material type is in use.



Get: IsInUse(self: WireMaterialType) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get name of wire material type.



Set: Name(self: WireMaterialType)=value

"""

 TemperatureRatings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all temperature rating type definitions defined in this wire material type.



Get: TemperatureRatings(self: WireMaterialType) -> TemperatureRatingTypeSet



"""


