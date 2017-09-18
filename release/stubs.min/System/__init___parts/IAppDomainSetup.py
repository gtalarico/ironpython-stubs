class IAppDomainSetup:
 """ Represents assembly binding information that can be added to an instance of System.AppDomain. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ApplicationBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the directory containing the application.



Get: ApplicationBase(self: IAppDomainSetup) -> str



Set: ApplicationBase(self: IAppDomainSetup)=value

"""

 ApplicationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the application.



Get: ApplicationName(self: IAppDomainSetup) -> str



Set: ApplicationName(self: IAppDomainSetup)=value

"""

 CachePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the name of an area specific to the application where files are shadow copied.



Get: CachePath(self: IAppDomainSetup) -> str



Set: CachePath(self: IAppDomainSetup)=value

"""

 ConfigurationFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the name of the configuration file for an application domain.



Get: ConfigurationFile(self: IAppDomainSetup) -> str



Set: ConfigurationFile(self: IAppDomainSetup)=value

"""

 DynamicBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the directory where dynamically generated files are stored and accessed.



Get: DynamicBase(self: IAppDomainSetup) -> str



Set: DynamicBase(self: IAppDomainSetup)=value

"""

 LicenseFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location of the license file associated with this domain.



Get: LicenseFile(self: IAppDomainSetup) -> str



Set: LicenseFile(self: IAppDomainSetup)=value

"""

 PrivateBinPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the list of directories that is combined with the System.AppDomainSetup.ApplicationBase directory to probe for private assemblies.



Get: PrivateBinPath(self: IAppDomainSetup) -> str



Set: PrivateBinPath(self: IAppDomainSetup)=value

"""

 PrivateBinPathProbe=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the private binary directory path used to locate an application.



Get: PrivateBinPathProbe(self: IAppDomainSetup) -> str



Set: PrivateBinPathProbe(self: IAppDomainSetup)=value

"""

 ShadowCopyDirectories=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the names of the directories containing assemblies to be shadow copied.



Get: ShadowCopyDirectories(self: IAppDomainSetup) -> str



Set: ShadowCopyDirectories(self: IAppDomainSetup)=value

"""

 ShadowCopyFiles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that indicates whether shadow copying is turned on or off.



Get: ShadowCopyFiles(self: IAppDomainSetup) -> str



Set: ShadowCopyFiles(self: IAppDomainSetup)=value

"""


