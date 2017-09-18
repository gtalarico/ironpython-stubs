class GridItem(object):
 """ Implements one row in a System.Windows.Forms.PropertyGrid. """
 def Select(self):
  """
  Select(self: GridItem) -> bool

  

   When overridden in a derived class,selects this System.Windows.Forms.GridItem in the 

    System.Windows.Forms.PropertyGrid.

  

   Returns: true if the selection is successful; otherwise,false.
  """
  pass
 Expandable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the specified property is expandable to show nested properties.



Get: Expandable(self: GridItem) -> bool



"""

 Expanded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets or sets a value indicating whether the System.Windows.Forms.GridItem is in an expanded state.



Get: Expanded(self: GridItem) -> bool



Set: Expanded(self: GridItem)=value

"""

 GridItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the collection of System.Windows.Forms.GridItem objects,if any,associated as a child of this System.Windows.Forms.GridItem.



Get: GridItems(self: GridItem) -> GridItemCollection



"""

 GridItemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the type of this System.Windows.Forms.GridItem.



Get: GridItemType(self: GridItem) -> GridItemType



"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the text of this System.Windows.Forms.GridItem.



Get: Label(self: GridItem) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the parent System.Windows.Forms.GridItem of this System.Windows.Forms.GridItem,if any.



Get: Parent(self: GridItem) -> GridItem



"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the System.ComponentModel.PropertyDescriptor that is associated with this System.Windows.Forms.GridItem.



Get: PropertyDescriptor(self: GridItem) -> PropertyDescriptor



"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets user-defined data about the System.Windows.Forms.GridItem.



Get: Tag(self: GridItem) -> object



Set: Tag(self: GridItem)=value

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the current value of this System.Windows.Forms.GridItem.



Get: Value(self: GridItem) -> object



"""


