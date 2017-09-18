class OSFeature(FeatureSupport,IFeatureSupport):
 """ Provides operating-system specific feature queries. """
 def GetVersionPresent(self,feature):
  """
  GetVersionPresent(self: OSFeature,feature: object) -> Version

  

   Retrieves the version of the specified feature currently available on the system.

  

   feature: The feature whose version is requested,either System.Windows.Forms.OSFeature.LayeredWindows or 

    System.Windows.Forms.OSFeature.Themes.

  

   Returns: A System.Version representing the version of the specified operating system feature currently 

    available on the system; or null if the feature cannot be found.
  """
  pass
 @staticmethod
 def IsPresent(*__args):
  """
  IsPresent(enumVal: SystemParameter) -> bool

  

   Retrieves a value indicating whether the operating system supports the specified feature or 

    metric.

  

  

   enumVal: A System.Windows.Forms.SystemParameter representing the feature to search for.

   Returns: true if the feature is available on the system; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Feature=None
 LayeredWindows=None
 Themes=None

