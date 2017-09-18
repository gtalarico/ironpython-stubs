class DockablePaneProviderData(object):
 """
 Information about a new dockable pane being added to the Revit user interface.
 
 DockablePaneProviderData()
 """
 ContextualHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The contextual help associated with the pane.

Get: ContextualHelp(self: DockablePaneProviderData) -> ContextualHelp

Set: ContextualHelp(self: DockablePaneProviderData)=value
"""

 EditorInteraction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the interaction this pane has with the Active Editor when the pane becomes active.

Get: EditorInteraction(self: DockablePaneProviderData) -> EditorInteraction

Set: EditorInteraction(self: DockablePaneProviderData)=value
"""

 FrameworkElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Windows Presentation Framework object containing the pane's user interface.

Get: FrameworkElement(self: DockablePaneProviderData) -> FrameworkElement

Set: FrameworkElement(self: DockablePaneProviderData)=value
"""

 InitialState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The initial position of the docking pane.

Get: InitialState(self: DockablePaneProviderData) -> DockablePaneState

Set: InitialState(self: DockablePaneProviderData)=value
"""

 VisibleByDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Controls the default visibility of the pane upon the first time
   the pane/plugin is loaded into Revit.

Get: VisibleByDefault(self: DockablePaneProviderData) -> bool

Set: VisibleByDefault(self: DockablePaneProviderData)=value
"""


