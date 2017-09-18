# encoding: utf-8
# module Rhino.Render.UI calls itself UI
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class IUserInterfaceSection:
    """
    Implement this interface in your user control to get UserInterfaceSection
                event notification.
    """
    def OnUserInterfaceSectionExpanding(self, userInterfaceSection, expanding):
        """
        OnUserInterfaceSectionExpanding(self: IUserInterfaceSection, userInterfaceSection: UserInterfaceSection, expanding: bool)
            The UserInterfaceSection object that called this interface method.
        
            userInterfaceSection: The UserInterfaceSection object that called this interface method.
            expanding: Will be true if the control has been createExpanded or false if it was
                    collapsed.
        """
        pass

    def UserInterfaceDisplayData(self, userInterfaceSection, renderContentList):
        """
        UserInterfaceDisplayData(self: IUserInterfaceSection, userInterfaceSection: UserInterfaceSection, renderContentList: Array[RenderContent])
            Called by UserInterfaceSection when the selected content changes or a
                    content field 
             property value changes.
        
        
            userInterfaceSection: The UserInterfaceSection object that called this interface method.
            renderContentList: The currently selected list of content items to edit.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UserInterfaceSection(object):
    """ Custom user interface section manager """
    def Expand(self, expand):
        """
        Expand(self: UserInterfaceSection, expand: bool)
            Expand or collapse this content section.
        
            expand: If true then expand the content section otherwise collapse it.
        """
        pass

    @staticmethod
    def FromWindow(window):
        """
        FromWindow(window: IWin32Window) -> UserInterfaceSection
        
            Find the UserInterfaceSection that created the specified instance of a
                    window.
        
            window: If window is not null then look for the UserInterfaceSection that
                    created the 
             window.
        
            Returns: If a UserInterfaceSection object is found containing a reference to
                    the requested 
             window then return the object otherwise return null.
        """
        pass

    def GetContentList(self):
        """
        GetContentList(self: UserInterfaceSection) -> Array[RenderContent]
        
            Returns a list of currently selected content items to be edited.
            Returns: Returns a list of currently selected content items to be edited.
        """
        pass

    def GetSibling(self, id):
        """
        GetSibling(self: UserInterfaceSection, id: Guid) -> UserInterfaceSection
        
            Look for a UI section in the same container with the specified class Id.
        
            id: The class Id of the section to search for.
            Returns: Returns the first section in this sections container whose window class
                    Id matches 
             the specified Id or null if no match is found.
        """
        pass

    def GetSiblings(self):
        """
        GetSiblings(self: UserInterfaceSection) -> Array[UserInterfaceSection]
        
            Get a list of the RhinoCommon added content sections associated with
                    this sections 
             container.
        
            Returns: Returns a list of the RhinoCommon added content sections associated
                    with this 
             sections container.
        """
        pass

    def Show(self, visible):
        """
        Show(self: UserInterfaceSection, visible: bool)
            Show or hide this content section.
        
            visible: If true then show the content section otherwise hide it.
        """
        pass

    RenderContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RenderContent object that created this user interface object.

Get: RenderContent(self: UserInterfaceSection) -> RenderContent

"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user control associated with this user interface object.

Get: Window(self: UserInterfaceSection) -> IWin32Window

"""



