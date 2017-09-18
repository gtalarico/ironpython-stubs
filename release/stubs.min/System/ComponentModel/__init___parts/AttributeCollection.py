class AttributeCollection(object,ICollection,IEnumerable):
 """
 Represents a collection of attributes.

 

 AttributeCollection(*attributes: Array[Attribute])
 """
 def Contains(self,*__args):
  """
  Contains(self: AttributeCollection,attributes: Array[Attribute]) -> bool

  

   Determines whether this attribute collection contains all the specified attributes in the 

    attribute array.

  

  

   attributes: An array of type System.Attribute to find in the collection.

   Returns: true if the collection contains all the attributes; otherwise,false.

  Contains(self: AttributeCollection,attribute: Attribute) -> bool

  

   Determines whether this collection of attributes has the specified attribute.

  

   attribute: An System.Attribute to find in the collection.

   Returns: true if the collection contains the attribute or is the default attribute for the type of 

    attribute; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: AttributeCollection,array: Array,index: int)

   Copies the collection to an array,starting at the specified index.

  

   array: The System.Array to copy the collection to.

   index: The index to start from.
  """
  pass
 @staticmethod
 def FromExisting(existing,newAttributes):
  """
  FromExisting(existing: AttributeCollection,*newAttributes: Array[Attribute]) -> AttributeCollection

  

   Creates a new System.ComponentModel.AttributeCollection from an existing 

    System.ComponentModel.AttributeCollection.

  

  

   existing: An System.ComponentModel.AttributeCollection from which to create the copy.

   newAttributes: An array of type System.Attribute that provides the attributes for this collection. Can be null.

   Returns: A new System.ComponentModel.AttributeCollection that is a copy of existing.
  """
  pass
 def GetDefaultAttribute(self,*args):
  """
  GetDefaultAttribute(self: AttributeCollection,attributeType: Type) -> Attribute

  

   Returns the default System.Attribute of a given System.Type.

  

   attributeType: The System.Type of the attribute to retrieve.

   Returns: An System.Attribute.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: AttributeCollection) -> IEnumerator

  

   Gets an enumerator for this collection.

   Returns: An enumerator of type System.Collections.IEnumerator.
  """
  pass
 def Matches(self,*__args):
  """
  Matches(self: AttributeCollection,attributes: Array[Attribute]) -> bool

  

   Determines whether the attributes in the specified array are the same as the attributes in the 

    collection.

  

  

   attributes: An array of System.CodeDom.MemberAttributes to compare with the attributes in this collection.

   Returns: true if all the attributes in the array are contained in the collection and have the same values 

    as the attributes in the collection; otherwise,false.

  

  Matches(self: AttributeCollection,attribute: Attribute) -> bool

  

   Determines whether a specified attribute is the same as an attribute in the collection.

  

   attribute: An instance of System.Attribute to compare with the attributes in this collection.

   Returns: true if the attribute is contained within the collection and has the same value as the attribute 

    in the collection; otherwise,false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 @staticmethod
 def __new__(self,attributes):
  """
  __new__(cls: type,*attributes: Array[Attribute])

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the attribute collection.



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of attributes.



Get: Count(self: AttributeCollection) -> int



"""


 Empty=None

