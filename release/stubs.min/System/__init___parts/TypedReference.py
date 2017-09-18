class TypedReference(object):
 """ Describes objects that contain both a managed pointer to a location and a runtime representation of the type that may be stored at that location. """
 def Equals(self,o):
  """
  Equals(self: TypedReference,o: object) -> bool

  

   Checks if this object is equal to the specified object.

  

   o: The object with which to compare the current object.

   Returns: true if this object is equal to the specified object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TypedReference) -> int

  

   Returns the hash code of this object.

   Returns: The hash code of this object.
  """
  pass
 @staticmethod
 def GetTargetType(value):
  """
  GetTargetType(value: TypedReference) -> Type

  

   Returns the type of the target of the specified TypedReference.

  

   value: The value whose target's type is to be returned.

   Returns: The type of the target of the specified TypedReference.
  """
  pass
 @staticmethod
 def MakeTypedReference(target,flds):
  """
  MakeTypedReference(target: object,flds: Array[FieldInfo]) -> TypedReference

  

   Makes a TypedReference for a field identified by a specified object and list of field 

    descriptions.

  

  

   target: An object that contains the field described by the first element of flds.

   flds: A list of field descriptions where each element describes a field that contains the field 

    described by the succeeding element. Each described field must be a value type. The field 

    descriptions must be RuntimeFieldInfo objects supplied by the type system.

  

   Returns: A System.TypedReference for the field described by the last element of flds.
  """
  pass
 @staticmethod
 def SetTypedReference(target,value):
  """
  SetTypedReference(target: TypedReference,value: object)

   Converts the specified value to a TypedReference. This method is not supported.

  

   target: The target of the conversion.

   value: The value to be converted.
  """
  pass
 @staticmethod
 def TargetTypeToken(value):
  """
  TargetTypeToken(value: TypedReference) -> RuntimeTypeHandle

  

   Returns the internal metadata type handle for the specified TypedReference.

  

   value: The TypedReference for which the type handle is requested.

   Returns: The internal metadata type handle for the specified TypedReference.
  """
  pass
 @staticmethod
 def ToObject(value):
  """
  ToObject(value: TypedReference) -> object

  

   Converts the specified TypedReference to an Object.

  

   value: The TypedReference to be converted.

   Returns: An System.Object converted from a TypedReference.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
