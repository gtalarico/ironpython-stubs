class ViewBase(DependencyObject):
 """ Represents the base class for views that define the appearance of data in a System.Windows.Controls.ListView control. """
 def ClearItem(self,*args):
  """
  ClearItem(self: ViewBase,item: ListViewItem)

   Removes all bindings and styling that are set for an item.

  

   item: The System.Windows.Controls.ListViewItem to remove settings from.
  """
  pass
 def GetAutomationPeer(self,*args):
  """
  GetAutomationPeer(self: ViewBase,parent: ListView) -> IViewAutomationPeer

  

   Is called when a System.Windows.Controls.ListView control creates a 

    System.Windows.Automation.Peers.ListViewAutomationPeer for its 

    System.Windows.Controls.ListView.View.

  

  

   parent: The System.Windows.Controls.ListView control to use to create the 

    System.Windows.Automation.Peers.ListViewAutomationPeer.

  

   Returns: The System.Windows.Automation.Peers.IViewAutomationPeer interface that implements the 

    System.Windows.Automation.Peers.ListViewAutomationPeer for a custom 

    System.Windows.Controls.ListView.View.
  """
  pass
 def PrepareItem(self,*args):
  """
  PrepareItem(self: ViewBase,item: ListViewItem)

   Prepares an item in the view for display,by setting bindings and styles.

  

   item: The item to prepare for display.
  """
  pass
 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object that is associated with the style for the view mode.



"""

 ItemContainerDefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style to use for the items in the view mode.



"""


