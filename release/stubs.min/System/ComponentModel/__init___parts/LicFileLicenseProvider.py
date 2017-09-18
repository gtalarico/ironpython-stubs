class LicFileLicenseProvider(LicenseProvider):
 """
 Provides an implementation of a System.ComponentModel.LicenseProvider. The provider works in a similar fashion to the Microsoft .NET Framework standard licensing model.

 

 LicFileLicenseProvider()
 """
 def GetKey(self,*args):
  """
  GetKey(self: LicFileLicenseProvider,type: Type) -> str

  

   Returns a key for the specified type.

  

   type: The object type to return the key.

   Returns: A confirmation that the type parameter is licensed.
  """
  pass
 def GetLicense(self,context,type,instance,allowExceptions):
  """
  GetLicense(self: LicFileLicenseProvider,context: LicenseContext,type: Type,instance: object,allowExceptions: bool) -> License

  

   Returns a license for the instance of the component,if one is available.

  

   context: A System.ComponentModel.LicenseContext that specifies where you can use the licensed object.

   type: A System.Type that represents the component requesting the System.ComponentModel.License.

   instance: An object that requests the System.ComponentModel.License.

   allowExceptions: true if a System.ComponentModel.LicenseException should be thrown when a component cannot be 

    granted a license; otherwise,false.

  

   Returns: A valid System.ComponentModel.License. If this method cannot find a valid 

    System.ComponentModel.License or a valid context parameter,it returns null.
  """
  pass
 def IsKeyValid(self,*args):
  """
  IsKeyValid(self: LicFileLicenseProvider,key: str,type: Type) -> bool

  

   Determines whether the key that the 

    System.ComponentModel.LicFileLicenseProvider.GetLicense(System.ComponentModel.LicenseContext,Syst

    em.Type,System.Object,System.Boolean) method retrieves is valid for the specified type.

  

  

   key: The System.ComponentModel.License.LicenseKey to check.

   type: A System.Type that represents the component requesting the System.ComponentModel.License.

   Returns: true if the key is a valid System.ComponentModel.License.LicenseKey for the specified type; 

    otherwise,false.
  """
  pass
