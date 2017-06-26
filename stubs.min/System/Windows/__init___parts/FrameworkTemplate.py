class FrameworkTemplate(DispatcherObject, INameScope, ISealable, IHaveResources, IQueryAmbient):
    """ Enables the instantiation of a tree of System.Windows.FrameworkElement and/or System.Windows.FrameworkContentElement objects. """
    def FindName(self, name, templatedParent):
        """
        FindName(self: FrameworkTemplate, name: str, templatedParent: FrameworkElement) -> object
        
            Finds the element associated with the specified name defined within this template.
        
            name: The string name.
            templatedParent: The context of the System.Windows.FrameworkElement where this template is applied.
            Returns: The element associated with the specified name.
        """
        pass

    def LoadContent(self):
        """
        LoadContent(self: FrameworkTemplate) -> DependencyObject
        
            Loads the content of the template as an instance of an object and returns the root element of the content.
            Returns: The root element of the content. Calling this multiple times returns separate instances.
        """
        pass

    def RegisterName(self, name, scopedElement):
        """
        RegisterName(self: FrameworkTemplate, name: str, scopedElement: object)
            Registers a new name/object pair into the current name scope.
        
            name: The name to register.
            scopedElement: The object to be mapped to the provided name.
        """
        pass

    def Seal(self):
        """
        Seal(self: FrameworkTemplate)
            Locks the template so it cannot be changed.
        """
        pass

    def ShouldSerializeResources(self, manager):
        """
        ShouldSerializeResources(self: FrameworkTemplate, manager: XamlDesignerSerializationManager) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value of the System.Windows.FrameworkTemplate.Resources property on instances of this class.
        
            manager: The System.Windows.Markup.XamlDesignerSerializationManager.
            Returns: true if the System.Windows.FrameworkTemplate.Resources property value should be serialized; otherwise, false.
        """
        pass

    def ShouldSerializeVisualTree(self):
        """
        ShouldSerializeVisualTree(self: FrameworkTemplate) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value of the System.Windows.FrameworkTemplate.VisualTree property on instances of this class.
            Returns: true if the System.Windows.FrameworkTemplate.VisualTree property value should be serialized; otherwise, false.
        """
        pass

    def UnregisterName(self, name):
        """
        UnregisterName(self: FrameworkTemplate, name: str)
            Removes a name/object mapping from the XAML namescope.
        
            name: The name of the mapping to remove.
        """
        pass

    def ValidateTemplatedParent(self, *args): #cannot find CLR method
        """
        ValidateTemplatedParent(self: FrameworkTemplate, templatedParent: FrameworkElement)
            When overridden in a derived class, supplies rules for the element this template is applied to.
        
            templatedParent: The element this template is applied to.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this template has optimized content.

Get: HasContent(self: FrameworkTemplate) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this object is in an immutable state so it cannot be changed.

Get: IsSealed(self: FrameworkTemplate) -> bool

"""

    Resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection of resources that can be used within the scope of this template.

Get: Resources(self: FrameworkTemplate) -> ResourceDictionary

Set: Resources(self: FrameworkTemplate) = value
"""

    Template = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to the object that records or plays the XAML nodes for the template when the template is defined or applied by a writer.

Get: Template(self: FrameworkTemplate) -> TemplateContent

Set: Template(self: FrameworkTemplate) = value
"""

    VisualTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the root node of the template.

Get: VisualTree(self: FrameworkTemplate) -> FrameworkElementFactory

Set: VisualTree(self: FrameworkTemplate) = value
"""


