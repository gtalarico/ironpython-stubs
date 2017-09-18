class ItemCheckEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.CheckedListBox.ItemCheck event of the System.Windows.Forms.CheckedListBox and System.Windows.Forms.ListView controls.

 

 ItemCheckEventArgs(index: int,newCheckValue: CheckState,currentValue: CheckState)
 """
 @staticmethod
 def __new__(self,index,newCheckValue,currentValue):
  """ __new__(cls: type,index: int,newCheckValue: CheckState,currentValue: CheckState) """
  pass
 CurrentValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the current state of the item's check box.



Get: CurrentValue(self: ItemCheckEventArgs) -> CheckState



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the item to change.



Get: Index(self: ItemCheckEventArgs) -> int



"""

 NewValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to set the check box for the item to be checked,unchecked,or indeterminate.



Get: NewValue(self: ItemCheckEventArgs) -> CheckState



Set: NewValue(self: ItemCheckEventArgs)=value

"""


