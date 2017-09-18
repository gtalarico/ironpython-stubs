class FeatureSupport(object,IFeatureSupport):
 """ Provides static methods for retrieving feature information from the current system. """
 @staticmethod
 def GetVersionPresent(*__args):
  """
  GetVersionPresent(self: FeatureSupport,feature: object) -> Version

  

   When overridden in a derived class,gets the version of the specified feature that is available 

    on the system.

  

  

   feature: The feature whose version is requested.

   Returns: A System.Version representing the version number of the specified feature available on the 

    system; or null if the feature is not installed.

  

  GetVersionPresent(featureClassName: str,featureConstName: str) -> Version

  

   Gets the version of the specified feature that is available on the system.

  

   featureClassName: The fully qualified name of the class to query for information about the specified feature. This 

    class must implement the System.Windows.Forms.IFeatureSupport interface or inherit from a class 

    that implements this interface.

  

   featureConstName: The fully qualified name of the feature to look for.

   Returns: A System.Version with the version number of the specified feature available on the system; or 

    null if the feature is not installed.
  """
  pass
 @staticmethod
 def IsPresent(*__args):
  """
  IsPresent(self: FeatureSupport,feature: object) -> bool

  

   Determines whether any version of the specified feature is installed in the system.

  

   feature: The feature to look for.

   Returns: true if the feature is present; otherwise,false.

  IsPresent(self: FeatureSupport,feature: object,minimumVersion: Version) -> bool

  

   Determines whether the specified or newer version of the specified feature is installed in the 

    system.

  

  

   feature: The feature to look for.

   minimumVersion: A System.Version representing the minimum version number of the feature to look for.

   Returns: true if the feature is present and its version number is greater than or equal to the specified 

    minimum version number; false if the feature is not installed or its version number is below the 

    specified minimum number.

  

  IsPresent(featureClassName: str,featureConstName: str) -> bool

  

   Determines whether any version of the specified feature is installed in the system. This method 

    is static.

  

  

   featureClassName: The fully qualified name of the class to query for information about the specified feature. This 

    class must implement the System.Windows.Forms.IFeatureSupport interface or inherit from a class 

    that implements this interface.

  

   featureConstName: The fully qualified name of the feature to look for.

   Returns: true if the specified feature is present; false if the specified feature is not present or if 

    the product containing the feature is not installed.

  

  IsPresent(featureClassName: str,featureConstName: str,minimumVersion: Version) -> bool

  

   Determines whether the specified or newer version of the specified feature is installed in the 

    system. This method is static.

  

  

   featureClassName: The fully qualified name of the class to query for information about the specified feature. This 

    class must implement the System.Windows.Forms.IFeatureSupport interface or inherit from a class 

    that implements this interface.

  

   featureConstName: The fully qualified name of the feature to look for.

   minimumVersion: A System.Version representing the minimum version number of the feature.

   Returns: true if the feature is present and its version number is greater than or equal to the specified 

    minimum version number; false if the feature is not installed or its version number is below the 

    specified minimum number.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
