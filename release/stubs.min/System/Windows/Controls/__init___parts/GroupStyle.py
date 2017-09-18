class GroupStyle(object,INotifyPropertyChanged):
 """
 Defines how you want the group to look at each level.

 

 GroupStyle()
 """
 def add_PropertyChanged(self,*args):
  """ add_PropertyChanged(self: GroupStyle,value: PropertyChangedEventHandler) """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: GroupStyle,e: PropertyChangedEventArgs)

   Raises the System.Windows.Controls.GroupStyle.PropertyChanged event using the provided arguments.

  

   e: Arguments of the event being raised.
  """
  pass
 def remove_PropertyChanged(self,*args):
  """ remove_PropertyChanged(self: GroupStyle,value: PropertyChangedEventHandler) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AlternationCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of alternating System.Windows.Controls.GroupItem objects.



Get: AlternationCount(self: GroupStyle) -> int



Set: AlternationCount(self: GroupStyle)=value

"""

 ContainerStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is applied to the System.Windows.Controls.GroupItem generated for each item.



Get: ContainerStyle(self: GroupStyle) -> Style



Set: ContainerStyle(self: GroupStyle)=value

"""

 ContainerStyleSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Enables the application writer to provide custom selection logic for a style to apply to each generated System.Windows.Controls.GroupItem.



Get: ContainerStyleSelector(self: GroupStyle) -> StyleSelector



Set: ContainerStyleSelector(self: GroupStyle)=value

"""

 HeaderStringFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a composite string that specifies how to format the header if it is displayed as a string.



Get: HeaderStringFormat(self: GroupStyle) -> str



Set: HeaderStringFormat(self: GroupStyle)=value

"""

 HeaderTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template that is used to display the group header.



Get: HeaderTemplate(self: GroupStyle) -> DataTemplate



Set: HeaderTemplate(self: GroupStyle)=value

"""

 HeaderTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Enables the application writer to provide custom selection logic for a template that is used to display the group header.



Get: HeaderTemplateSelector(self: GroupStyle) -> DataTemplateSelector



Set: HeaderTemplateSelector(self: GroupStyle)=value

"""

 HidesIfEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether items corresponding to empty groups should be displayed.



Get: HidesIfEmpty(self: GroupStyle) -> bool



Set: HidesIfEmpty(self: GroupStyle)=value

"""

 Panel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a template that creates the panel used to layout the items.



Get: Panel(self: GroupStyle) -> ItemsPanelTemplate



Set: Panel(self: GroupStyle)=value

"""


 Default=None
 DefaultGroupPanel=None

