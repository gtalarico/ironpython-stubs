class LicenseProvider(object):
 """ Provides the abstract base class for implementing a license provider. """
 def GetLicense(self,context,type,instance,allowExceptions):
  """
  GetLicense(self: LicenseProvider,context: LicenseContext,type: Type,instance: object,allowExceptions: bool) -> License

  

   When overridden in a derived class,gets a license for an instance or type of component,when 

    given a context and whether the denial of a license throws an exception.

  

  

   context: A System.ComponentModel.LicenseContext that specifies where you can use the licensed object.

   type: A System.Type that represents the component requesting the license.

   instance: An object that is requesting the license.

   allowExceptions: true if a System.ComponentModel.LicenseException should be thrown when the component cannot be 

    granted a license; otherwise,false.

  

   Returns: A valid System.ComponentModel.License.
  """
  pass
