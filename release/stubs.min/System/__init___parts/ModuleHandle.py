class ModuleHandle(object):
 """ Represents a runtime handle for a module. """
 def Equals(self,*__args):
  """
  Equals(self: ModuleHandle,handle: ModuleHandle) -> bool

  

   Returns a System.Boolean value indicating whether the specified System.ModuleHandle structure is 

    equal to the current System.ModuleHandle.

  

  

   handle: The System.ModuleHandle structure to be compared with the current System.ModuleHandle.

   Returns: true if handle is equal to the current System.ModuleHandle structure; otherwise false.

  Equals(self: ModuleHandle,obj: object) -> bool

  

   Returns a System.Boolean value indicating whether the specified object is a System.ModuleHandle 

    structure,and equal to the current System.ModuleHandle.

  

  

   obj: The object to be compared with the current System.ModuleHandle structure.

   Returns: true if obj is a System.ModuleHandle structure,and is equal to the current System.ModuleHandle 

    structure; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: ModuleHandle) -> int """
  pass
 def GetRuntimeFieldHandleFromMetadataToken(self,fieldToken):
  """
  GetRuntimeFieldHandleFromMetadataToken(self: ModuleHandle,fieldToken: int) -> RuntimeFieldHandle

  

   Returns a runtime handle for the field identified by the specified metadata token.

  

   fieldToken: A metadata token that identifies a field in the module.

   Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.
  """
  pass
 def GetRuntimeMethodHandleFromMetadataToken(self,methodToken):
  """
  GetRuntimeMethodHandleFromMetadataToken(self: ModuleHandle,methodToken: int) -> RuntimeMethodHandle

  

   Returns a runtime method handle for the method or constructor identified by the specified 

    metadata token.

  

  

   methodToken: A metadata token that identifies a method or constructor in the module.

   Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.
  """
  pass
 def GetRuntimeTypeHandleFromMetadataToken(self,typeToken):
  """
  GetRuntimeTypeHandleFromMetadataToken(self: ModuleHandle,typeToken: int) -> RuntimeTypeHandle

  

   Returns a runtime type handle for the type identified by the specified metadata token.

  

   typeToken: A metadata token that identifies a type in the module.

   Returns: A System.RuntimeTypeHandle for the type identified by typeToken.
  """
  pass
 def ResolveFieldHandle(self,fieldToken,typeInstantiationContext=None,methodInstantiationContext=None):
  """
  ResolveFieldHandle(self: ModuleHandle,fieldToken: int,typeInstantiationContext: Array[RuntimeTypeHandle],methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeFieldHandle

  

   Returns a runtime field handle for the field identified by the specified metadata token,

    specifying the generic type arguments of the type and method where the token is in scope.

  

  

   fieldToken: A metadata token that identifies a field in the module.

   typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the 

    type where the token is in scope,or null if that type is not generic.

  

   methodInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the 

    method where the token is in scope,or null if that method is not generic.

  

   Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.

  ResolveFieldHandle(self: ModuleHandle,fieldToken: int) -> RuntimeFieldHandle

  

   Returns a runtime handle for the field identified by the specified metadata token.

  

   fieldToken: A metadata token that identifies a field in the module.

   Returns: A System.RuntimeFieldHandle for the field identified by fieldToken.
  """
  pass
 def ResolveMethodHandle(self,methodToken,typeInstantiationContext=None,methodInstantiationContext=None):
  """
  ResolveMethodHandle(self: ModuleHandle,methodToken: int,typeInstantiationContext: Array[RuntimeTypeHandle],methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeMethodHandle

  

   Returns a runtime method handle for the method or constructor identified by the specified 

    metadata token,specifying the generic type arguments of the type and method where the token is 

    in scope.

  

  

   methodToken: A metadata token that identifies a method or constructor in the module.

   typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the 

    type where the token is in scope,or null if that type is not generic.

  

   methodInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the 

    method where the token is in scope,or null if that method is not generic.

  

   Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.

  ResolveMethodHandle(self: ModuleHandle,methodToken: int) -> RuntimeMethodHandle

  

   Returns a runtime method handle for the method or constructor identified by the specified 

    metadata token.

  

  

   methodToken: A metadata token that identifies a method or constructor in the module.

   Returns: A System.RuntimeMethodHandle for the method or constructor identified by methodToken.
  """
  pass
 def ResolveTypeHandle(self,typeToken,typeInstantiationContext=None,methodInstantiationContext=None):
  """
  ResolveTypeHandle(self: ModuleHandle,typeToken: int,typeInstantiationContext: Array[RuntimeTypeHandle],methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeTypeHandle

  

   Returns a runtime type handle for the type identified by the specified metadata token,

    specifying the generic type arguments of the type and method where the token is in scope.

  

  

   typeToken: A metadata token that identifies a type in the module.

   typeInstantiationContext: An array of System.RuntimeTypeHandle structures representing the generic type arguments of the 

    type where the token is in scope,or null if that type is not generic.

  

   methodInstantiationContext: An array of System.RuntimeTypeHandle structures objects representing the generic type arguments 

    of the method where the token is in scope,or null if that method is not generic.

  

   Returns: A System.RuntimeTypeHandle for the type identified by typeToken.

  ResolveTypeHandle(self: ModuleHandle,typeToken: int) -> RuntimeTypeHandle

  

   Returns a runtime type handle for the type identified by the specified metadata token.

  

   typeToken: A metadata token that identifies a type in the module.

   Returns: A System.RuntimeTypeHandle for the type identified by typeToken.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 MDStreamVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the metadata stream version.



Get: MDStreamVersion(self: ModuleHandle) -> int



"""


 EmptyHandle=None

