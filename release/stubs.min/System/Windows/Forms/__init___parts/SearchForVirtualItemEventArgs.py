class SearchForVirtualItemEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.SearchForVirtualItem event.

 

 SearchForVirtualItemEventArgs(isTextSearch: bool,isPrefixSearch: bool,includeSubItemsInSearch: bool,text: str,startingPoint: Point,direction: SearchDirectionHint,startIndex: int)
 """
 @staticmethod
 def __new__(self,isTextSearch,isPrefixSearch,includeSubItemsInSearch,text,startingPoint,direction,startIndex):
  """ __new__(cls: type,isTextSearch: bool,isPrefixSearch: bool,includeSubItemsInSearch: bool,text: str,startingPoint: Point,direction: SearchDirectionHint,startIndex: int) """
  pass
 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction from the current item that the search should take place.



Get: Direction(self: SearchForVirtualItemEventArgs) -> SearchDirectionHint



"""

 IncludeSubItemsInSearch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the search should include subitems of list items.



Get: IncludeSubItemsInSearch(self: SearchForVirtualItemEventArgs) -> bool



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the System.Windows.Forms.ListViewItem found in the System.Windows.Forms.ListView .



Get: Index(self: SearchForVirtualItemEventArgs) -> int



Set: Index(self: SearchForVirtualItemEventArgs)=value

"""

 IsPrefixSearch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the search should return an item if its text starts with the search text.



Get: IsPrefixSearch(self: SearchForVirtualItemEventArgs) -> bool



"""

 IsTextSearch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the search is a text search.



Get: IsTextSearch(self: SearchForVirtualItemEventArgs) -> bool



"""

 StartIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the System.Windows.Forms.ListViewItem where the search starts.



Get: StartIndex(self: SearchForVirtualItemEventArgs) -> int



"""

 StartingPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the starting location of the search.



Get: StartingPoint(self: SearchForVirtualItemEventArgs) -> Point



"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text used to find an item in the System.Windows.Forms.ListView control.



Get: Text(self: SearchForVirtualItemEventArgs) -> str



"""


