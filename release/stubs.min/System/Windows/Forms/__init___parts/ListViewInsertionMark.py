class ListViewInsertionMark(object):
 """ Used to indicate the expected drop location when an item is dragged to a new position in a System.Windows.Forms.ListView control. This functionality is available only on Windows XP and later. """
 def NearestIndex(self,pt):
  """
  NearestIndex(self: ListViewInsertionMark,pt: Point) -> int

  

   Retrieves the index of the item closest to the specified point.

  

   pt: A System.Drawing.Point representing the location from which to find the nearest item.

   Returns: The index of the item closest to the specified point or -1 if the closest item is the item 

    currently being dragged.
  """
  pass
 AppearsAfterItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the insertion mark appears to the right of the item with the index specified by the System.Windows.Forms.ListViewInsertionMark.Index property.



Get: AppearsAfterItem(self: ListViewInsertionMark) -> bool



Set: AppearsAfterItem(self: ListViewInsertionMark)=value

"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding rectangle of the insertion mark.



Get: Bounds(self: ListViewInsertionMark) -> Rectangle



"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the insertion mark.



Get: Color(self: ListViewInsertionMark) -> Color



Set: Color(self: ListViewInsertionMark)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the item next to which the insertion mark appears.



Get: Index(self: ListViewInsertionMark) -> int



Set: Index(self: ListViewInsertionMark)=value

"""


