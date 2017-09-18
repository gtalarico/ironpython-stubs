class ListViewHitTestInfo(object):
 """
 Contains information about an area of a System.Windows.Forms.ListView control or a System.Windows.Forms.ListViewItem.

 

 ListViewHitTestInfo(hitItem: ListViewItem,hitSubItem: ListViewSubItem,hitLocation: ListViewHitTestLocations)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,hitItem,hitSubItem,hitLocation):
  """ __new__(cls: type,hitItem: ListViewItem,hitSubItem: ListViewSubItem,hitLocation: ListViewHitTestLocations) """
  pass
 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListViewItem at the position indicated by a hit test on a System.Windows.Forms.ListView.



Get: Item(self: ListViewHitTestInfo) -> ListViewItem



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of a hit test on a System.Windows.Forms.ListView control,in relation to the System.Windows.Forms.ListView and the items it contains.



Get: Location(self: ListViewHitTestInfo) -> ListViewHitTestLocations



"""

 SubItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListViewItem.ListViewSubItem at the position indicated by a hit test on a System.Windows.Forms.ListView.



Get: SubItem(self: ListViewHitTestInfo) -> ListViewSubItem



"""


