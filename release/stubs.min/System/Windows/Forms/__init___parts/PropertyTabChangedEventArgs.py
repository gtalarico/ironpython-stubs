class PropertyTabChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.PropertyGrid.PropertyTabChanged event of a System.Windows.Forms.PropertyGrid.

 

 PropertyTabChangedEventArgs(oldTab: PropertyTab,newTab: PropertyTab)
 """
 @staticmethod
 def __new__(self,oldTab,newTab):
  """ __new__(cls: type,oldTab: PropertyTab,newTab: PropertyTab) """
  pass
 NewTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new System.Windows.Forms.Design.PropertyTab selected.



Get: NewTab(self: PropertyTabChangedEventArgs) -> PropertyTab



"""

 OldTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the old System.Windows.Forms.Design.PropertyTab selected.



Get: OldTab(self: PropertyTabChangedEventArgs) -> PropertyTab



"""


