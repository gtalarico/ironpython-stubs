class ColumnReorderedEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ColumnReordered event.

 

 ColumnReorderedEventArgs(oldDisplayIndex: int,newDisplayIndex: int,header: ColumnHeader)
 """
 @staticmethod
 def __new__(self,oldDisplayIndex,newDisplayIndex,header):
  """ __new__(cls: type,oldDisplayIndex: int,newDisplayIndex: int,header: ColumnHeader) """
  pass
 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ColumnHeader that is being reordered.



Get: Header(self: ColumnReorderedEventArgs) -> ColumnHeader



"""

 NewDisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new display position of the System.Windows.Forms.ColumnHeader



Get: NewDisplayIndex(self: ColumnReorderedEventArgs) -> int



"""

 OldDisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous display position of the System.Windows.Forms.ColumnHeader.



Get: OldDisplayIndex(self: ColumnReorderedEventArgs) -> int



"""


