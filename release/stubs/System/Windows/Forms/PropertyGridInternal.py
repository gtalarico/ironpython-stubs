# encoding: utf-8
# module System.Windows.Forms.PropertyGridInternal calls itself PropertyGridInternal
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class IRootGridEntry:
    """ Defines methods and a property that allow filtering on specific attributes. """
    def ResetBrowsableAttributes(self):
        """
        ResetBrowsableAttributes(self: IRootGridEntry)
            Resets the System.Windows.Forms.PropertyGridInternal.IRootGridEntry.BrowsableAttributes property 
             to the default value.
        """
        pass

    def ShowCategories(self, showCategories):
        """
        ShowCategories(self: IRootGridEntry, showCategories: bool)
            Sorts the properties in the property browser.
        
            showCategories: true to group the properties by category; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BrowsableAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the attributes on which the property browser filters.

Get: BrowsableAttributes(self: IRootGridEntry) -> AttributeCollection

Set: BrowsableAttributes(self: IRootGridEntry) = value
"""



class PropertiesTab(PropertyTab, IExtenderProvider):
    """
    Represents the Properties tab on a System.Windows.Forms.PropertyGrid control.
    
    PropertiesTab()
    """
    def Dispose(self):
        """
        Dispose(self: PropertyTab, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.Design.PropertyTab and 
             optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetDefaultProperty(self, obj):
        """
        GetDefaultProperty(self: PropertiesTab, obj: object) -> PropertyDescriptor
            Returns: A System.ComponentModel.PropertyDescriptor that represents the default property.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: PropertiesTab, context: ITypeDescriptorContext, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            context: An System.ComponentModel.ITypeDescriptorContext that indicates the context to retrieve 
             properties from.
        
            component: The component to retrieve properties from.
            attributes: An array of type System.Attribute that indicates the attributes of the properties to retrieve.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties matching the 
             specified context and attributes.
        
        GetProperties(self: PropertiesTab, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            component: The component to retrieve properties from.
            attributes: An array of type System.Attribute that indicates the attributes of the properties to retrieve.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HelpKeyword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help keyword that is to be associated with this tab.

Get: HelpKeyword(self: PropertiesTab) -> str

"""

    TabName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the Properties tab.

Get: TabName(self: PropertiesTab) -> str

"""



class PropertyGridCommands(object):
    """
    Contains a set of menu commands used by the designer in Visual Studio.
    
    PropertyGridCommands()
    """
    Commands = None
    Description = None
    Hide = None
    Reset = None
    wfcMenuCommand = None
    wfcMenuGroup = None


