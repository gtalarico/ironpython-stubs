class MaterialRefs(object,IDictionary[Guid,MaterialRef],ICollection[KeyValuePair[Guid,MaterialRef]],IEnumerable[KeyValuePair[Guid,MaterialRef]],IEnumerable):
 """
 If you are developing a high quality plug-in renderer,and a user is

    assigning a custom render material to this object,then add rendering

    material information to the MaterialRefs dictionary.

    

    Note to developers:

     As soon as the MaterialRefs dictionary contains items rendering

     material queries slow down.  Do not populate the MaterialRefs

    dictionary when setting the MaterialIndex will take care of your needs.
 """
 def Add(self,*__args):
  """
  Add(self: MaterialRefs,key: Guid,value: MaterialRef)

   Add or replace an element with the provided key and value to this dictionary.

  

   key: The plug-in associated with this MaterialRef

   value: MaterialRef to add to this dictionary

  Add(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef])
  """
  pass
 def Clear(self):
  """
  Clear(self: MaterialRefs)

   Removes all items from this dictionary.
  """
  pass
 def Contains(self,item):
  """ Contains(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef]) -> bool """
  pass
 def ContainsKey(self,key):
  """
  ContainsKey(self: MaterialRefs,key: Guid) -> bool

  

   Determines whether this dictionary contains an MaterialRef with the

     specified 

    plug-in id.

  

  

   key: The plug-in Id used to locate a MaterialRef in this dictionary.

   Returns: true if this dictionary contains an element with the specified plug-in

     Id; 

    otherwise,false.
  """
  pass
 def CopyTo(self,array,arrayIndex):
  """ CopyTo(self: MaterialRefs,array: Array[KeyValuePair[Guid,MaterialRef]],arrayIndex: int) """
  pass
 def Create(self,createParams):
  """
  Create(self: MaterialRefs,createParams: MaterialRefCreateParams) -> MaterialRef

  

   Call this method to create a MaterialRef which can be used when calling

     one of the 

    Add methods.

  

  

   createParams: Values used to initialize the MaterialRef

   Returns: A temporary MaterialRef object,the caller is responsible for disposing

     of this 

    object.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: MaterialRefs) -> IEnumerator[KeyValuePair[Guid,MaterialRef]]

  

   Returns an enumerator that iterates through this dictionary.

   Returns: A IEnumerator that can be used to iterate this dictionary.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: MaterialRefs,key: Guid) -> bool

  

   Removes the MaterialRef with the specified plug-in Id from this

     dictionary.

  

   key: The plug-in Id for the MaterialRef to remove.

   Returns: true if the MaterialRef is successfully removed; otherwise,false. This

     method also 

    returns false if key was not found in the original dictionary.

  

  Remove(self: MaterialRefs,item: KeyValuePair[Guid,MaterialRef]) -> bool
  """
  pass
 def TryGetValue(self,key,value):
  """
  TryGetValue(self: MaterialRefs,key: Guid) -> (bool,MaterialRef)

  

   Gets the value associated with the specified key.

  

   key: The plug-in Id whose MaterialRef to get.

   Returns: true if this dictionary contains a MaterialRef with the specified key;

     otherwise,

    false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__(self: IDictionary[Guid,MaterialRef],key: Guid) -> bool """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of elements contained in this dictionary



Get: Count(self: MaterialRefs) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """IDictionary required property,always returns false for this dictionary.



Get: IsReadOnly(self: MaterialRefs) -> bool



"""

 Keys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an ICollection containing the plug-in Id's in this dictionary.



Get: Keys(self: MaterialRefs) -> ICollection[Guid]



"""

 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an ICollection containing the MaterialRef objects in this

   dictionary.



Get: Values(self: MaterialRefs) -> ICollection[MaterialRef]



"""


