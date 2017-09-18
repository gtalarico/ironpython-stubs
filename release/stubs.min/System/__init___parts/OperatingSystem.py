class OperatingSystem(object,ICloneable,ISerializable):
 """
 Represents information about an operating system,such as the version and platform identifier. This class cannot be inherited.

 

 OperatingSystem(platform: PlatformID,version: Version)
 """
 def Clone(self):
  """
  Clone(self: OperatingSystem) -> object

  

   Creates an System.OperatingSystem object that is identical to this instance.

   Returns: An System.OperatingSystem object that is a copy of this instance.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: OperatingSystem,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo object with the data necessary to 

    deserialize this instance.

  

  

   info: The object to populate with serialization information.

   context: The place to store and retrieve serialized data. Reserved for future use.
  """
  pass
 def ToString(self):
  """
  ToString(self: OperatingSystem) -> str

  

   Converts the value of this System.OperatingSystem object to its equivalent string representation.

   Returns: The string representation of the values returned by the System.OperatingSystem.Platform,

    System.OperatingSystem.Version,and System.OperatingSystem.ServicePack properties.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,platform,version):
  """ __new__(cls: type,platform: PlatformID,version: Version) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Platform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.PlatformID enumeration value that identifies the operating system platform.



Get: Platform(self: OperatingSystem) -> PlatformID



"""

 ServicePack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the service pack version represented by this System.OperatingSystem object.



Get: ServicePack(self: OperatingSystem) -> str



"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Version object that identifies the operating system.



Get: Version(self: OperatingSystem) -> Version



"""

 VersionString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the concatenated string representation of the platform identifier,version,and service pack that are currently installed on the operating system.



Get: VersionString(self: OperatingSystem) -> str



"""


