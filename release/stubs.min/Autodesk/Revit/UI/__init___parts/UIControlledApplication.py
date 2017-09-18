class UIControlledApplication(object):
 """
 Represents the Autodesk Revit user interface,providing access to

 UI customization methods and events.
 """
 def CreateAddInCommandBinding(self,revitCommandId):
  """
  CreateAddInCommandBinding(self: UIControlledApplication,revitCommandId: RevitCommandId) -> AddInCommandBinding

  

   Creates a new AddInCommandBinding.

  

   revitCommandId: The Revit command id to identify the command handler you want to replace.
  """
  pass
 def CreateRibbonPanel(self,*__args):
  """
  CreateRibbonPanel(self: UIControlledApplication,tabName: str,panelName: str) -> RibbonPanel

  

   Create a new RibbonPanel on the specified tab.

  

   tabName: The name of the tab,on which the new panel will be created.

   panelName: The name of the panel to be created.

  CreateRibbonPanel(self: UIControlledApplication,panelName: str) -> RibbonPanel

  

   Create a new RibbonPanel on the Add-Ins tab.

  

   panelName: The name of the panel to be created.

  CreateRibbonPanel(self: UIControlledApplication,tab: Tab,panelName: str) -> RibbonPanel

  

   Create a new RibbonPanel on the designated standard Revit tab.

  

   tab: The target tab,on which the new panel will be created.

   panelName: The name of the panel to be created.
  """
  pass
 def CreateRibbonTab(self,tabName):
  """
  CreateRibbonTab(self: UIControlledApplication,tabName: str)

   Creates a new tab on the Revit user interface.

  

   tabName: The name of the tab to be created.
  """
  pass
 def GetDockablePane(self,id):
  """
  GetDockablePane(self: UIControlledApplication,id: DockablePaneId) -> DockablePane

  

   Gets a DockablePane object by its ID.

  

   id: Unique identifier for the new pane.
  """
  pass
 def GetRibbonPanels(self,*__args):
  """
  GetRibbonPanels(self: UIControlledApplication) -> List[RibbonPanel]

  

   Get all the custom Panels on Add-Ins tab of Revit.

  GetRibbonPanels(self: UIControlledApplication,tab: Tab) -> List[RibbonPanel]

  

   Get all the custom Panels on a designated standard Revit tab.

  

   tab: The tab on which the panels are located.

  GetRibbonPanels(self: UIControlledApplication,tabName: str) -> List[RibbonPanel]

  

   Get all the custom Panels on a designated Revit tab.

  

   tabName: The name of the tab on which the panels are located.
  """
  pass
 def LoadAddIn(self,fileName):
  """
  LoadAddIn(self: UIControlledApplication,fileName: str)

   Loads add-ins from the given manifest file.

  

   fileName: The name of the add-in manifest file including the extension is to identify the 

    

  manifest file which contains Revit add-ins.
  """
  pass
 def LoadPackageContents(self,packageContentsPath):
  """
  LoadPackageContents(self: UIControlledApplication,packageContentsPath: str)

   Loads add-ins from the given packageContents.xml file.

  

   packageContentsPath: The name of package contents file
  """
  pass
 def RegisterDockablePane(self,id,title,provider):
  """
  RegisterDockablePane(self: UIControlledApplication,id: DockablePaneId,title: str,provider: IDockablePaneProvider)

   Adds a new dockable pane to the Revit user interface.

  

   id: Unique identifier for the new pane.

   title: String to use for the pane caption.

   provider: Your add-in's implementation of the IDockablePaneProvider interface.
  """
  pass
 def RemoveAddInCommandBinding(self,revitCommandId):
  """
  RemoveAddInCommandBinding(self: UIControlledApplication,revitCommandId: RevitCommandId)

   Removes an AddInCommandBinding.

  

   revitCommandId: The Revit command id to identify the command handler you want to remove the 

    binding.
  """
  pass
 ActiveAddInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get current active external application or external command id.



Get: ActiveAddInId(self: UIControlledApplication) -> AddInId



"""

 ControlledApplication=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the database level ControlledApplication represented by this UI-level ControlledApplication.



Get: ControlledApplication(self: UIControlledApplication) -> ControlledApplication



"""

 IsLateAddinLoading=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this add-in is loaded on the fly or not. If it is loaded when Revit is starting up,it

is false,otherwise it should be true.



Get: IsLateAddinLoading(self: UIControlledApplication) -> bool



"""

 LoadedApplications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns an array of successfully loaded external applications.



Get: LoadedApplications(self: UIControlledApplication) -> ExternalApplicationArray



"""


 ApplicationClosing=None
 DialogBoxShowing=None
 DisplayingOptionsDialog=None
 DockableFrameFocusChanged=None
 DockableFrameVisibilityChanged=None
 FabricationPartBrowserChanged=None
 Idling=None
 ViewActivated=None
 ViewActivating=None

