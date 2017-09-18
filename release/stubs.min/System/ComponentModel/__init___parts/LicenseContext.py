class LicenseContext(object,IServiceProvider):
 """
 Specifies when you can use a licensed object and provides a way of obtaining additional services needed to support licenses running within its domain.

 

 LicenseContext()
 """
 def GetSavedLicenseKey(self,type,resourceAssembly):
  """
  GetSavedLicenseKey(self: LicenseContext,type: Type,resourceAssembly: Assembly) -> str

  

   When overridden in a derived class,returns a saved license key for the specified type,from the 

    specified resource assembly.

  

  

   type: A System.Type that represents the type of component.

   resourceAssembly: An System.Reflection.Assembly with the license key.

   Returns: The System.ComponentModel.License.LicenseKey for the specified type. This method returns null 

    unless you override it.
  """
  pass
 def GetService(self,type):
  """
  GetService(self: LicenseContext,type: Type) -> object

  

   Gets the requested service,if it is available.

  

   type: The type of service to retrieve.

   Returns: An instance of the service,or null if the service cannot be found.
  """
  pass
 def SetSavedLicenseKey(self,type,key):
  """
  SetSavedLicenseKey(self: LicenseContext,type: Type,key: str)

   When overridden in a derived class,sets a license key for the specified type.

  

   type: A System.Type that represents the component associated with the license key.

   key: The System.ComponentModel.License.LicenseKey to save for the type of component.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 UsageMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value that specifies when you can use a license.



Get: UsageMode(self: LicenseContext) -> LicenseUsageMode



"""


