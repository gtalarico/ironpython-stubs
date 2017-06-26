class FrameworkElementFactory(object):
    """
    Supports the creation of templates.
    
    FrameworkElementFactory()
    FrameworkElementFactory(type: Type)
    FrameworkElementFactory(text: str)
    FrameworkElementFactory(type: Type, name: str)
    """
    def AddHandler(self, routedEvent, handler, handledEventsToo=None):
        """
        AddHandler(self: FrameworkElementFactory, routedEvent: RoutedEvent, handler: Delegate, handledEventsToo: bool)
            Adds an event handler for the given routed event to the instances created by this factory, with the option of having the provided handler be invoked even in cases of routed events that had already been 
             marked as handled by another element along the route.
        
        
            routedEvent: Identifier object for the routed event being handled.
            handler: A reference to the handler implementation.
            handledEventsToo: Whether to invoke the handler in cases where the routed event has already been marked as handled in its arguments object. true to invoke the handler even when the routed event is marked handled; otherwise, 
             false. The default is false. Asking to handle already-handled routed events is not common.
        
        AddHandler(self: FrameworkElementFactory, routedEvent: RoutedEvent, handler: Delegate)
            Adds an event handler for the given routed event to the instances created by this factory.
        
            routedEvent: Identifier object for the routed event being handled.
            handler: A reference to the handler implementation.
        """
        pass

    def AppendChild(self, child):
        """
        AppendChild(self: FrameworkElementFactory, child: FrameworkElementFactory)
            Adds a child factory to this factory.
        
            child: The System.Windows.FrameworkElementFactory object to add as a child.
        """
        pass

    def RemoveHandler(self, routedEvent, handler):
        """
        RemoveHandler(self: FrameworkElementFactory, routedEvent: RoutedEvent, handler: Delegate)
            Removes an event handler from the given routed event. This applies to the instances created by this factory.
        
            routedEvent: Identifier object for the routed event.
            handler: The handler to remove.
        """
        pass

    def SetBinding(self, dp, binding):
        """
        SetBinding(self: FrameworkElementFactory, dp: DependencyProperty, binding: BindingBase)
            Sets up data binding on a property.
        
            dp: Identifies the property where the binding should be established.
            binding: Description of the binding.
        """
        pass

    def SetResourceReference(self, dp, name):
        """
        SetResourceReference(self: FrameworkElementFactory, dp: DependencyProperty, name: object)
            Set up a dynamic resource reference on a child property.
        
            dp: The property to which the resource is bound.
            name: The name of the resource.
        """
        pass

    def SetValue(self, dp, value):
        """
        SetValue(self: FrameworkElementFactory, dp: DependencyProperty, value: object)
            Sets the value of a dependency property.
        
            dp: The dependency property identifier of the property to set.
            value: The new value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, text: str)
        __new__(cls: type, type: Type, name: str)
        """
        pass

    FirstChild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first child factory.

Get: FirstChild(self: FrameworkElementFactory) -> FrameworkElementFactory

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this object is in an immutable state.

Get: IsSealed(self: FrameworkElementFactory) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of a template item.

Get: Name(self: FrameworkElementFactory) -> str

Set: Name(self: FrameworkElementFactory) = value
"""

    NextSibling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the next sibling factory.

Get: NextSibling(self: FrameworkElementFactory) -> FrameworkElementFactory

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent System.Windows.FrameworkElementFactory.

Get: Parent(self: FrameworkElementFactory) -> FrameworkElementFactory

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text string to produce.

Get: Text(self: FrameworkElementFactory) -> str

Set: Text(self: FrameworkElementFactory) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the objects this factory produces.

Get: Type(self: FrameworkElementFactory) -> Type

Set: Type(self: FrameworkElementFactory) = value
"""


