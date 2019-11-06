class ItemChangedEventArgs(EventArgs):
 """ Provides data for the System.Windows.Forms.CurrencyManager.ItemChanged event. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return ItemChangedEventArgs()

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the position of the item being changed within the list.

Get: Index(self: ItemChangedEventArgs) -> int

"""


