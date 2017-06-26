class SortDescription(object):
 """
 Defines the direction and the property name to be used as the criteria for sorting a collection.
 
 SortDescription(propertyName: str,direction: ListSortDirection)
 """
 def Equals(self,obj):
  """
  Equals(self: SortDescription,obj: object) -> bool
  
   Compares the specified instance and the current instance of 
    System.ComponentModel.SortDescription for value equality.
  
  
   obj: The System.ComponentModel.SortDescription instance to compare.
   Returns: true if obj and this instance of System.ComponentModel.SortDescription have the 
    same values.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SortDescription) -> int
  
   Returns the hash code for this instance of 
    System.ComponentModel.SortDescription.
  
   Returns: The hash code for this instance of System.ComponentModel.SortDescription.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,propertyName,direction):
  """
  __new__(cls: type,propertyName: str,direction: ListSortDirection)
  __new__[SortDescription]() -> SortDescription
  """
  pass
 def __ne__(self,*args):
  pass
 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to sort in ascending or descending order.

Get: Direction(self: SortDescription) -> ListSortDirection

Set: Direction(self: SortDescription)=value
"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this object is in an immutable state.

Get: IsSealed(self: SortDescription) -> bool

"""

 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the property name being used as the sorting criteria.

Get: PropertyName(self: SortDescription) -> str

Set: PropertyName(self: SortDescription)=value
"""


