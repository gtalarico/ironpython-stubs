class LabelEditEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.BeforeLabelEdit and System.Windows.Forms.ListView.AfterLabelEdit events.

 

 LabelEditEventArgs(item: int)

 LabelEditEventArgs(item: int,label: str)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,label=None):
  """
  __new__(cls: type,item: int)

  __new__(cls: type,item: int,label: str)
  """
  pass
 CancelEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether changes made to the label of the System.Windows.Forms.ListViewItem should be canceled.



Get: CancelEdit(self: LabelEditEventArgs) -> bool



Set: CancelEdit(self: LabelEditEventArgs)=value

"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the System.Windows.Forms.ListViewItem containing the label to edit.



Get: Item(self: LabelEditEventArgs) -> int



"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new text assigned to the label of the System.Windows.Forms.ListViewItem.



Get: Label(self: LabelEditEventArgs) -> str



"""


