class ListViewItem(object,ICloneable,ISerializable):
 """
 Represents an item in a System.Windows.Forms.ListView control.

 

 ListViewItem()

 ListViewItem(text: str)

 ListViewItem(text: str,imageIndex: int)

 ListViewItem(items: Array[str])

 ListViewItem(items: Array[str],imageIndex: int)

 ListViewItem(items: Array[str],imageIndex: int,foreColor: Color,backColor: Color,font: Font)

 ListViewItem(subItems: Array[ListViewSubItem],imageIndex: int)

 ListViewItem(group: ListViewGroup)

 ListViewItem(text: str,group: ListViewGroup)

 ListViewItem(text: str,imageIndex: int,group: ListViewGroup)

 ListViewItem(items: Array[str],group: ListViewGroup)

 ListViewItem(items: Array[str],imageIndex: int,group: ListViewGroup)

 ListViewItem(items: Array[str],imageIndex: int,foreColor: Color,backColor: Color,font: Font,group: ListViewGroup)

 ListViewItem(subItems: Array[ListViewSubItem],imageIndex: int,group: ListViewGroup)

 ListViewItem(text: str,imageKey: str)

 ListViewItem(items: Array[str],imageKey: str)

 ListViewItem(items: Array[str],imageKey: str,foreColor: Color,backColor: Color,font: Font)

 ListViewItem(subItems: Array[ListViewSubItem],imageKey: str)

 ListViewItem(text: str,imageKey: str,group: ListViewGroup)

 ListViewItem(items: Array[str],imageKey: str,group: ListViewGroup)

 ListViewItem(items: Array[str],imageKey: str,foreColor: Color,backColor: Color,font: Font,group: ListViewGroup)

 ListViewItem(subItems: Array[ListViewSubItem],imageKey: str,group: ListViewGroup)
 """
 def BeginEdit(self):
  """
  BeginEdit(self: ListViewItem)

   Places the item text into edit mode.
  """
  pass
 def Clone(self):
  """
  Clone(self: ListViewItem) -> object

  

   Creates an identical copy of the item.

   Returns: An object that represents an item that has the same text,image,and subitems associated with it 

    as the cloned item.
  """
  pass
 def Deserialize(self,*args):
  """
  Deserialize(self: ListViewItem,info: SerializationInfo,context: StreamingContext)

   Deserializes the item.

  

   info: A System.Runtime.Serialization.SerializationInfo that holds the data needed to deserialize the 

    item.

  

   context: A System.Runtime.Serialization.StreamingContext that represents the source and destination of 

    the stream being deserialized.
  """
  pass
 def EnsureVisible(self):
  """
  EnsureVisible(self: ListViewItem)

   Ensures that the item is visible within the control,scrolling the contents of the control,if 

    necessary.
  """
  pass
 def FindNearestItem(self,searchDirection):
  """
  FindNearestItem(self: ListViewItem,searchDirection: SearchDirectionHint) -> ListViewItem

  

   Finds the next item from the System.Windows.Forms.ListViewItem,searching in the specified 

    direction.

  

  

   searchDirection: One of the System.Windows.Forms.SearchDirectionHint values.

   Returns: The System.Windows.Forms.ListViewItem that is closest to the given coordinates,searching in the 

    specified direction.
  """
  pass
 def GetBounds(self,portion):
  """
  GetBounds(self: ListViewItem,portion: ItemBoundsPortion) -> Rectangle

  

   Retrieves the specified portion of the bounding rectangle for the item.

  

   portion: One of the System.Windows.Forms.ItemBoundsPortion values that represents a portion of the item 

    for which to retrieve the bounding rectangle.

  

   Returns: A System.Drawing.Rectangle that represents the bounding rectangle for the specified portion of 

    the item.
  """
  pass
 def GetSubItemAt(self,x,y):
  """
  GetSubItemAt(self: ListViewItem,x: int,y: int) -> ListViewSubItem

  

   Returns the subitem of the System.Windows.Forms.ListViewItem at the specified coordinates.

  

   x: The x-coordinate.

   y: The y-coordinate.

   Returns: The System.Windows.Forms.ListViewItem.ListViewSubItem at the specified x- and y-coordinates.
  """
  pass
 def Remove(self):
  """
  Remove(self: ListViewItem)

   Removes the item from its associated System.Windows.Forms.ListView control.
  """
  pass
 def Serialize(self,*args):
  """
  Serialize(self: ListViewItem,info: SerializationInfo,context: StreamingContext)

   Serializes the item.

  

   info: A System.Runtime.Serialization.SerializationInfo that holds the data needed to serialize the 

    item.

  

   context: A System.Runtime.Serialization.StreamingContext that represents the source and destination of 

    the stream being serialized.
  """
  pass
 def ToString(self):
  """
  ToString(self: ListViewItem) -> str

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

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type,text: str)

  __new__(cls: type,text: str,imageIndex: int)

  __new__(cls: type,items: Array[str])

  __new__(cls: type,items: Array[str],imageIndex: int)

  __new__(cls: type,items: Array[str],imageIndex: int,foreColor: Color,backColor: Color,font: Font)

  __new__(cls: type,subItems: Array[ListViewSubItem],imageIndex: int)

  __new__(cls: type,group: ListViewGroup)

  __new__(cls: type,text: str,group: ListViewGroup)

  __new__(cls: type,text: str,imageIndex: int,group: ListViewGroup)

  __new__(cls: type,items: Array[str],group: ListViewGroup)

  __new__(cls: type,items: Array[str],imageIndex: int,group: ListViewGroup)

  __new__(cls: type,items: Array[str],imageIndex: int,foreColor: Color,backColor: Color,font: Font,group: ListViewGroup)

  __new__(cls: type,subItems: Array[ListViewSubItem],imageIndex: int,group: ListViewGroup)

  __new__(cls: type,text: str,imageKey: str)

  __new__(cls: type,items: Array[str],imageKey: str)

  __new__(cls: type,items: Array[str],imageKey: str,foreColor: Color,backColor: Color,font: Font)

  __new__(cls: type,subItems: Array[ListViewSubItem],imageKey: str)

  __new__(cls: type,text: str,imageKey: str,group: ListViewGroup)

  __new__(cls: type,items: Array[str],imageKey: str,group: ListViewGroup)

  __new__(cls: type,items: Array[str],imageKey: str,foreColor: Color,backColor: Color,font: Font,group: ListViewGroup)

  __new__(cls: type,subItems: Array[ListViewSubItem],imageKey: str,group: ListViewGroup)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the item's text.



Get: BackColor(self: ListViewItem) -> Color



Set: BackColor(self: ListViewItem)=value

"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding rectangle of the item,including subitems.



Get: Bounds(self: ListViewItem) -> Rectangle



"""

 Checked=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is checked.



Get: Checked(self: ListViewItem) -> bool



Set: Checked(self: ListViewItem)=value

"""

 Focused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item has focus within the System.Windows.Forms.ListView control.



Get: Focused(self: ListViewItem) -> bool



Set: Focused(self: ListViewItem)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text displayed by the item.



Get: Font(self: ListViewItem) -> Font



Set: Font(self: ListViewItem)=value

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the item's text.



Get: ForeColor(self: ListViewItem) -> Color



Set: ForeColor(self: ListViewItem)=value

"""

 Group=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the group to which the item is assigned.



Get: Group(self: ListViewItem) -> ListViewGroup



Set: Group(self: ListViewItem)=value

"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the image that is displayed for the item.



Get: ImageIndex(self: ListViewItem) -> int



Set: ImageIndex(self: ListViewItem)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key for the image that is displayed for the item.



Get: ImageKey(self: ListViewItem) -> str



Set: ImageKey(self: ListViewItem)=value

"""

 ImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ImageList that contains the image displayed with the item.



Get: ImageList(self: ListViewItem) -> ImageList



"""

 IndentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of small image widths by which to indent the System.Windows.Forms.ListViewItem.



Get: IndentCount(self: ListViewItem) -> int



Set: IndentCount(self: ListViewItem)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the item within the System.Windows.Forms.ListView control.



Get: Index(self: ListViewItem) -> int



"""

 ListView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListView control that contains the item.



Get: ListView(self: ListViewItem) -> ListView



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name associated with this System.Windows.Forms.ListViewItem.



Get: Name(self: ListViewItem) -> str



Set: Name(self: ListViewItem)=value

"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position of the upper-left corner of the System.Windows.Forms.ListViewItem.



Get: Position(self: ListViewItem) -> Point



Set: Position(self: ListViewItem)=value

"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the item is selected.



Get: Selected(self: ListViewItem) -> bool



Set: Selected(self: ListViewItem)=value

"""

 StateImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the state image (an image such as a selected or cleared check box that indicates the state of the item) that is displayed for the item.



Get: StateImageIndex(self: ListViewItem) -> int



Set: StateImageIndex(self: ListViewItem)=value

"""

 SubItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing all subitems of the item.



Get: SubItems(self: ListViewItem) -> ListViewSubItemCollection



"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data to associate with the item.



Get: Tag(self: ListViewItem) -> object



Set: Tag(self: ListViewItem)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the item.



Get: Text(self: ListViewItem) -> str



Set: Text(self: ListViewItem)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text shown when the mouse pointer rests on the System.Windows.Forms.ListViewItem.



Get: ToolTipText(self: ListViewItem) -> str



Set: ToolTipText(self: ListViewItem)=value

"""

 UseItemStyleForSubItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListViewItem.Font,System.Windows.Forms.ListViewItem.ForeColor,and System.Windows.Forms.ListViewItem.BackColor properties for the item are used for all its subitems.



Get: UseItemStyleForSubItems(self: ListViewItem) -> bool



Set: UseItemStyleForSubItems(self: ListViewItem)=value

"""


 ListViewSubItem=None
 ListViewSubItemCollection=None

