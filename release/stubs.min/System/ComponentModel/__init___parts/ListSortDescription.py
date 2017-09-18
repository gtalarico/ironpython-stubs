class ListSortDescription(object):
 """
 Provides a description of the sort operation applied to a data source.

 

 ListSortDescription(property: PropertyDescriptor,direction: ListSortDirection)
 """
 @staticmethod
 def __new__(self,property,direction):
  """ __new__(cls: type,property: PropertyDescriptor,direction: ListSortDirection) """
  pass
 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the abstract description of a class property associated with this System.ComponentModel.ListSortDescription



Get: PropertyDescriptor(self: ListSortDescription) -> PropertyDescriptor



Set: PropertyDescriptor(self: ListSortDescription)=value

"""

 SortDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the direction of the sort operation associated with this System.ComponentModel.ListSortDescription.



Get: SortDirection(self: ListSortDescription) -> ListSortDirection



Set: SortDirection(self: ListSortDescription)=value

"""


