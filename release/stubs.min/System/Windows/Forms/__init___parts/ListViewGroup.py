class ListViewGroup(object,ISerializable):
 """
 Represents a group of items displayed within a System.Windows.Forms.ListView control.

 

 ListViewGroup()

 ListViewGroup(key: str,headerText: str)

 ListViewGroup(header: str)

 ListViewGroup(header: str,headerAlignment: HorizontalAlignment)
 """
 def ToString(self):
  """
  ToString(self: ListViewGroup) -> str

   Returns: A string that represents the current object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,key: str,headerText: str)

  __new__(cls: type,header: str)

  __new__(cls: type,header: str,headerAlignment: HorizontalAlignment)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header text for the group.



Get: Header(self: ListViewGroup) -> str



Set: Header(self: ListViewGroup)=value

"""

 HeaderAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of the group header text.



Get: HeaderAlignment(self: ListViewGroup) -> HorizontalAlignment



Set: HeaderAlignment(self: ListViewGroup)=value

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing all items associated with this group.



Get: Items(self: ListViewGroup) -> ListViewItemCollection



"""

 ListView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListView control that contains this group.



Get: ListView(self: ListViewGroup) -> ListView



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the group.



Get: Name(self: ListViewGroup) -> str



Set: Name(self: ListViewGroup)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data about the group.



Get: Tag(self: ListViewGroup) -> object



Set: Tag(self: ListViewGroup)=value

"""


