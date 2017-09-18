class RetrieveVirtualItemEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.RetrieveVirtualItem event.

 

 RetrieveVirtualItemEventArgs(itemIndex: int)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,itemIndex):
  """ __new__(cls: type,itemIndex: int) """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the item retrieved from the cache.



Get: Item(self: RetrieveVirtualItemEventArgs) -> ListViewItem



Set: Item(self: RetrieveVirtualItemEventArgs)=value

"""

 ItemIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the item to retrieve from the cache.



Get: ItemIndex(self: RetrieveVirtualItemEventArgs) -> int



"""


