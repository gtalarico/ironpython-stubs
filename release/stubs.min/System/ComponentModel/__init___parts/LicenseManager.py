class LicenseManager(object):
 """ Provides properties and methods to add a license to a component and to manage a System.ComponentModel.LicenseProvider. This class cannot be inherited. """
 @staticmethod
 def CreateWithContext(type,creationContext,args=None):
  """
  CreateWithContext(type: Type,creationContext: LicenseContext,args: Array[object]) -> object

  

   Creates an instance of the specified type with the specified arguments,given a context in which 

    you can use the licensed instance.

  

  

   type: A System.Type that represents the type to create.

   creationContext: A System.ComponentModel.LicenseContext that specifies when you can use the licensed instance.

   args: An array of type System.Object that represents the arguments for the type.

   Returns: An instance of the specified type with the given array of arguments.

  CreateWithContext(type: Type,creationContext: LicenseContext) -> object

  

   Creates an instance of the specified type,given a context in which you can use the licensed 

    instance.

  

  

   type: A System.Type that represents the type to create.

   creationContext: A System.ComponentModel.LicenseContext that specifies when you can use the licensed instance.

   Returns: An instance of the specified type.
  """
  pass
 @staticmethod
 def IsLicensed(type):
  """
  IsLicensed(type: Type) -> bool

  

   Returns whether the given type has a valid license.

  

   type: The System.Type to find a valid license for.

   Returns: true if the given type is licensed; otherwise,false.
  """
  pass
 @staticmethod
 def IsValid(type,instance=None,license=None):
  """
  IsValid(type: Type,instance: object) -> (bool,License)

  

   Determines whether a valid license can be granted for the specified instance of the type. This 

    method creates a valid System.ComponentModel.License.

  

  

   type: A System.Type that represents the type of object that requests the license.

   instance: An object of the specified type or a type derived from the specified type.

   Returns: true if a valid System.ComponentModel.License can be granted; otherwise,false.

  IsValid(type: Type) -> bool

  

   Determines whether a valid license can be granted for the specified type.

  

   type: A System.Type that represents the type of object that requests the System.ComponentModel.License.

   Returns: true if a valid license can be granted; otherwise,false.
  """
  pass
 @staticmethod
 def LockContext(contextUser):
  """
  LockContext(contextUser: object)

   Prevents changes being made to the current System.ComponentModel.LicenseContext of the given 

    object.

  

  

   contextUser: The object whose current context you want to lock.
  """
  pass
 @staticmethod
 def UnlockContext(contextUser):
  """
  UnlockContext(contextUser: object)

   Allows changes to be made to the current System.ComponentModel.LicenseContext of the given 

    object.

  

  

   contextUser: The object whose current context you want to unlock.
  """
  pass
 @staticmethod
 def Validate(type,instance=None):
  """
  Validate(type: Type,instance: object) -> License

  

   Determines whether a license can be granted for the instance of the specified type.

  

   type: A System.Type that represents the type of object that requests the license.

   instance: An System.Object of the specified type or a type derived from the specified type.

   Returns: A valid System.ComponentModel.License.

  Validate(type: Type)

   Determines whether a license can be granted for the specified type.

  

   type: A System.Type that represents the type of object that requests the license.
  """
  pass
 CurrentContext=None
 UsageMode=None

