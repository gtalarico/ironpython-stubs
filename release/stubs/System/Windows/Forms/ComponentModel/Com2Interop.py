# encoding: utf-8
# module System.Windows.Forms.ComponentModel.Com2Interop calls itself Com2Interop
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Com2Variant(object):
    """
    Facilitates proper recognition of a variant type.
    
    Com2Variant()
    """

class ICom2PropertyPageDisplayService:
    """ Defines a method that shows the property page for an ActiveX control. """
    def ShowPropertyPage(self, title, component, dispid, pageGuid, parentHandle):
        """
        ShowPropertyPage(self: ICom2PropertyPageDisplayService, title: str, component: object, dispid: int, pageGuid: Guid, parentHandle: IntPtr)
            Shows a property page for the specified object.
        
            title: A string that is the title of the property page.
            component: The object for which the property page is created.
            dispid: The DispID of the property that is highlighted when the property page is created.
            pageGuid: The GUID for the property page.
            parentHandle: A IntPtr that is the handle of the parent control of the property page.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IComPropertyBrowser:
    """ Allows Visual Studio to communicate internally with the System.Windows.Forms.PropertyGrid control. """
    def DropDownDone(self):
        """
        DropDownDone(self: IComPropertyBrowser)
            Closes any open drop-down controls on the System.Windows.Forms.PropertyGrid control.
        """
        pass

    def EnsurePendingChangesCommitted(self):
        """
        EnsurePendingChangesCommitted(self: IComPropertyBrowser) -> bool
        
            Commits all pending changes to the System.Windows.Forms.PropertyGrid control.
            Returns: true if the System.Windows.Forms.PropertyGrid successfully commits changes; otherwise, false.
        """
        pass

    def HandleF4(self):
        """
        HandleF4(self: IComPropertyBrowser)
            Activates the System.Windows.Forms.PropertyGrid control when the user chooses Properties for a 
             control in Design view.
        """
        pass

    def LoadState(self, key):
        """
        LoadState(self: IComPropertyBrowser, key: RegistryKey)
            Loads user states from the registry into the System.Windows.Forms.PropertyGrid control.
        
            key: The registry key that contains the user states.
        """
        pass

    def SaveState(self, key):
        """
        SaveState(self: IComPropertyBrowser, key: RegistryKey)
            Saves user states from the System.Windows.Forms.PropertyGrid control to the registry.
        
            key: The registry key that contains the user states.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    InPropertySet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.PropertyGrid control is currently setting one of the properties of its selected object.

Get: InPropertySet(self: IComPropertyBrowser) -> bool

"""


    ComComponentNameChanged = None


