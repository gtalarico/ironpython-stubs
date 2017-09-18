class IFeatureSupport:
 """ Specifies a standard interface for retrieving feature information from the current system. """
 def GetVersionPresent(self,feature):
  """
  GetVersionPresent(self: IFeatureSupport,feature: object) -> Version

  

   Retrieves the version of the specified feature.

  

   feature: The feature whose version is requested.

   Returns: A System.Version representing the version number of the specified feature; or null if the 

    feature is not installed.
  """
  pass
 def IsPresent(self,feature,minimumVersion=None):
  """
  IsPresent(self: IFeatureSupport,feature: object,minimumVersion: Version) -> bool

  

   Determines whether the specified or newer version of the specified feature is currently 

    available on the system.

  

  

   feature: The feature to look for.

   minimumVersion: A System.Version representing the minimum version number of the feature to look for.

   Returns: true if the requested version of the feature is present; otherwise,false.

  IsPresent(self: IFeatureSupport,feature: object) -> bool

  

   Determines whether any version of the specified feature is currently available on the system.

  

   feature: The feature to look for.

   Returns: true if the feature is present; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
