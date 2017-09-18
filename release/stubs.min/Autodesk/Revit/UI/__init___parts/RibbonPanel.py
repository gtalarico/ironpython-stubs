class RibbonPanel(object):
 """ Represents a panel added by an External Application or External Command into the Add-Ins tab. """
 def AddItem(self,itemData):
  """
  AddItem(self: RibbonPanel,itemData: RibbonItemData) -> RibbonItem

  

   Adds a Ribbon item to the panel.

  

   itemData: Data containing information about the new item.

   Returns: The added Ribbon item.
  """
  pass
 def AddSeparator(self):
  """
  AddSeparator(self: RibbonPanel)

   Adds a new Separator to the panel.
  """
  pass
 def AddSlideOut(self):
  """
  AddSlideOut(self: RibbonPanel)

   Adds a slideout to the current panel.
  """
  pass
 def AddStackedItems(self,item1,item2,item3=None):
  """
  AddStackedItems(self: RibbonPanel,item1: RibbonItemData,item2: RibbonItemData) -> IList[RibbonItem]

  

   Adds two stacked items to the panel.

  

   item1: Data containing information about the first item. This data must be of type 

    PushButtonData,PulldownButtonData,SplitButtonData,ComboBoxData,or 

    TextBoxData.

  

   item2: Data containing information about the second item. This data must be of type 

    PushButtonData,PulldownButtonData,SplitButtonData,ComboBoxData,or 

    TextBoxData.

  

   Returns: A collection containing the added items.

  AddStackedItems(self: RibbonPanel,item1: RibbonItemData,item2: RibbonItemData,item3: RibbonItemData) -> IList[RibbonItem]

  

   Adds three stacked items to the panel.

  

   item1: Data containing information about the first item. This data must be of type 

    PushButtonData,PulldownButtonData,SplitButtonData,ComboBoxData,or 

    TextBoxData.

  

   item2: Data containing information about the second item. This data must be of type 

    PushButtonData,PulldownButtonData,SplitButtonData,ComboBoxData,or 

    TextBoxData.

  

   item3: Data containing information about the third item. This data must be of type 

    PushButtonData,PulldownButtonData,SplitButtonData,ComboBoxData,or 

    TextBoxData.

  

   Returns: A collection containing the added items.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: RibbonPanel,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.Object.

  

  

   obj: Another panel object.
  """
  pass
 def GetItems(self):
  """
  GetItems(self: RibbonPanel) -> IList[RibbonItem]

  

   Gets a copy of the collection of RibbonItems assigned to the RibbonPanel.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the RibbonPanel can respond to user interaction.



Get: Enabled(self: RibbonPanel) -> bool



Set: Enabled(self: RibbonPanel)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the RibbonPanel.



Get: Name(self: RibbonPanel) -> str



Set: Name(self: RibbonPanel)=value

"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the RibbonPanel.



Get: Title(self: RibbonPanel) -> str



Set: Title(self: RibbonPanel)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the RibbonPanel is displayed.



Get: Visible(self: RibbonPanel) -> bool



Set: Visible(self: RibbonPanel)=value

"""


