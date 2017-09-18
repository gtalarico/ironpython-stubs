class AppDomainSetup(object,IAppDomainSetup):
 """
 Represents assembly binding information that can be added to an instance of System.AppDomain.

 

 AppDomainSetup()

 AppDomainSetup(activationContext: ActivationContext)

 AppDomainSetup(activationArguments: ActivationArguments)
 """
 def GetConfigurationBytes(self):
  """
  GetConfigurationBytes(self: AppDomainSetup) -> Array[Byte]

  

   Returns the XML configuration information set by the 

    System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method,which overrides the 

    application's XML configuration information.

  

   Returns: An array that contains the XML configuration information that was set by the 

    System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method,or null if the 

    System.AppDomainSetup.SetConfigurationBytes(System.Byte[]) method has not been called.
  """
  pass
 def SetCompatibilitySwitches(self,switches):
  """ SetCompatibilitySwitches(self: AppDomainSetup,switches: IEnumerable[str]) """
  pass
 def SetConfigurationBytes(self,value):
  """
  SetConfigurationBytes(self: AppDomainSetup,value: Array[Byte])

   Provides XML configuration information for the application domain,overriding the application's 

    XML configuration information.

  

  

   value: An array that contains the XML configuration information to be used for the application domain.
  """
  pass
 def SetNativeFunction(self,functionName,functionVersion,functionPointer):
  """ SetNativeFunction(self: AppDomainSetup,functionName: str,functionVersion: int,functionPointer: IntPtr) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,activationContext: ActivationContext)

  __new__(cls: type,activationArguments: ActivationArguments)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ActivationArguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets data about the activation of an application domain.



Get: ActivationArguments(self: AppDomainSetup) -> ActivationArguments



Set: ActivationArguments(self: AppDomainSetup)=value

"""

 AppDomainInitializer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.AppDomainInitializer delegate,which represents a callback method that is invoked when the application domain is initialized.



Get: AppDomainInitializer(self: AppDomainSetup) -> AppDomainInitializer



Set: AppDomainInitializer(self: AppDomainSetup)=value

"""

 AppDomainInitializerArguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the arguments passed to the callback method represented by the System.AppDomainInitializer delegate. The callback method is invoked when the application domain is initialized.



Get: AppDomainInitializerArguments(self: AppDomainSetup) -> Array[str]



Set: AppDomainInitializerArguments(self: AppDomainSetup)=value

"""

 AppDomainManagerAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display name of the assembly that provides the type of the application domain manager for application domains created using this System.AppDomainSetup object.



Get: AppDomainManagerAssembly(self: AppDomainSetup) -> str



Set: AppDomainManagerAssembly(self: AppDomainSetup)=value

"""

 AppDomainManagerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the full name of the type that provides the application domain manager for application domains created using this System.AppDomainSetup object.



Get: AppDomainManagerType(self: AppDomainSetup) -> str



Set: AppDomainManagerType(self: AppDomainSetup)=value

"""

 ApplicationBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the directory containing the application.



Get: ApplicationBase(self: AppDomainSetup) -> str



Set: ApplicationBase(self: AppDomainSetup)=value

"""

 ApplicationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the application.



Get: ApplicationName(self: AppDomainSetup) -> str



Set: ApplicationName(self: AppDomainSetup)=value

"""

 ApplicationTrust=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object containing security and trust information.



Get: ApplicationTrust(self: AppDomainSetup) -> ApplicationTrust



Set: ApplicationTrust(self: AppDomainSetup)=value

"""

 CachePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of an area specific to the application where files are shadow copied.



Get: CachePath(self: AppDomainSetup) -> str



Set: CachePath(self: AppDomainSetup)=value

"""

 ConfigurationFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the configuration file for an application domain.



Get: ConfigurationFile(self: AppDomainSetup) -> str



Set: ConfigurationFile(self: AppDomainSetup)=value

"""

 DisallowApplicationBaseProbing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the application base path and private binary path are probed when searching for assemblies to load.



Get: DisallowApplicationBaseProbing(self: AppDomainSetup) -> bool



Set: DisallowApplicationBaseProbing(self: AppDomainSetup)=value

"""

 DisallowBindingRedirects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether an application domain allows assembly binding redirection.



Get: DisallowBindingRedirects(self: AppDomainSetup) -> bool



Set: DisallowBindingRedirects(self: AppDomainSetup)=value

"""

 DisallowCodeDownload=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether HTTP download of assemblies is allowed for an application domain.



Get: DisallowCodeDownload(self: AppDomainSetup) -> bool



Set: DisallowCodeDownload(self: AppDomainSetup)=value

"""

 DisallowPublisherPolicy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the <publisherPolicy> section of the configuration file is applied to an application domain.



Get: DisallowPublisherPolicy(self: AppDomainSetup) -> bool



Set: DisallowPublisherPolicy(self: AppDomainSetup)=value

"""

 DynamicBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base directory where the directory for dynamically generated files is located.



Get: DynamicBase(self: AppDomainSetup) -> str



Set: DynamicBase(self: AppDomainSetup)=value

"""

 LicenseFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location of the license file associated with this domain.



Get: LicenseFile(self: AppDomainSetup) -> str



Set: LicenseFile(self: AppDomainSetup)=value

"""

 LoaderOptimization=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the optimization policy used to load an executable.



Get: LoaderOptimization(self: AppDomainSetup) -> LoaderOptimization



Set: LoaderOptimization(self: AppDomainSetup)=value

"""

 PartialTrustVisibleAssemblies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a list of assemblies marked with the System.Security.PartialTrustVisibilityLevel.NotVisibleByDefault flag that are made visible to partial-trust code running in a sandboxed application domain.



Get: PartialTrustVisibleAssemblies(self: AppDomainSetup) -> Array[str]



Set: PartialTrustVisibleAssemblies(self: AppDomainSetup)=value

"""

 PrivateBinPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the list of directories under the application base directory that are probed for private assemblies.



Get: PrivateBinPath(self: AppDomainSetup) -> str



Set: PrivateBinPath(self: AppDomainSetup)=value

"""

 PrivateBinPathProbe=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string value that includes or excludes System.AppDomainSetup.ApplicationBase from the search path for the application,and searches only System.AppDomainSetup.PrivateBinPath.



Get: PrivateBinPathProbe(self: AppDomainSetup) -> str



Set: PrivateBinPathProbe(self: AppDomainSetup)=value

"""

 SandboxInterop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether interface caching is disabled for interop calls in the application domain,so that a QueryInterface is performed on each call.



Get: SandboxInterop(self: AppDomainSetup) -> bool



Set: SandboxInterop(self: AppDomainSetup)=value

"""

 ShadowCopyDirectories=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the names of the directories containing assemblies to be shadow copied.



Get: ShadowCopyDirectories(self: AppDomainSetup) -> str



Set: ShadowCopyDirectories(self: AppDomainSetup)=value

"""

 ShadowCopyFiles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that indicates whether shadow copying is turned on or off.



Get: ShadowCopyFiles(self: AppDomainSetup) -> str



Set: ShadowCopyFiles(self: AppDomainSetup)=value

"""

 TargetFrameworkName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TargetFrameworkName(self: AppDomainSetup) -> str



Set: TargetFrameworkName(self: AppDomainSetup)=value

"""


