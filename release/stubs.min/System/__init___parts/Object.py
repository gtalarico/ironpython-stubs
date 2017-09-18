class Object:
 """
 Supports all classes in the .NET Framework class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all classes in the .NET Framework; it is the root of the type hierarchy.

 

 object()
 """
 def __delattr__(self,*args):
  """
  __delattr__(self: object,name: str)

   Removes an attribute from the provided member
  """
  pass
 def __format__(self,*args):
  """ __format__(self: object,formatSpec: str) -> str """
  pass
 def __getattribute__(self,*args):
  """
  __getattribute__(self: object,name: str) -> object

  

   Gets the specified attribute from the object without running any custom lookup behavior

    

     (__getattr__ and __getattribute__)
  """
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type,**kwargs�: dict,*args�: Array[object]) -> object

  __new__(cls: type,*args�: Array[object]) -> object

  

   Creates a new instance of the type

  __new__(cls: type) -> object

  

   Creates a new instance of the type
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __reduce__(self,*args):
  """ helper for pickle """
  pass
 def __repr__(self,*args):
  """
  __repr__(self: object) -> str

  

   Returns the code representation of the object.  The default implementation returns

     

    a string which consists of the type and a unique numerical identifier.
  """
  pass
 def __setattr__(self,*args):
  """
  __setattr__(self: object,name: str,value: object)

   Sets an attribute on the object without running any custom object defined behavior.
  """
  pass
 def __sizeof__(self,*args):
  """
  __sizeof__(self: object) -> int

  

   Returns the number of bytes of memory required to allocate the object.
  """
  pass
 def __str__(self,*args):
  pass
 def __subclasshook__(self,*args):
  """ __subclasshook__(*args: Array[object]) -> NotImplementedType """
  pass
 __class__=None

