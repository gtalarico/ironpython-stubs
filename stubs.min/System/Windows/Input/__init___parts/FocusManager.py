class FocusManager(object):
    """ Provides a set of static methods, attached properties, and events for determining and setting focus scopes and for setting the focused element within the scope. """
    @staticmethod
    def AddGotFocusHandler(element, handler):
        """ AddGotFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def AddLostFocusHandler(element, handler):
        """ AddLostFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def GetFocusedElement(element):
        """
        GetFocusedElement(element: DependencyObject) -> IInputElement
        
            Gets the element with logical focus within the specified focus scope.
        
            element: The element with logical focus in the specified focus scope.
            Returns: The element in the specified focus scope with logical focus.
        """
        pass

    @staticmethod
    def GetFocusScope(element):
        """
        GetFocusScope(element: DependencyObject) -> DependencyObject
        
            Determines the closest ancestor of the specified element that has System.Windows.Input.FocusManager.IsFocusScope set to true.
        
            element: The element to get the closest focus scope for.
            Returns: The focus scope for the specified element.
        """
        pass

    @staticmethod
    def GetIsFocusScope(element):
        """
        GetIsFocusScope(element: DependencyObject) -> bool
        
            Determines whether the specified System.Windows.DependencyObject is a focus scope.
        
            element: The element from which to read the attached property.
            Returns: true if System.Windows.Input.FocusManager.IsFocusScope is set to true on the specified element; otherwise, false.
        """
        pass

    @staticmethod
    def RemoveGotFocusHandler(element, handler):
        """ RemoveGotFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def RemoveLostFocusHandler(element, handler):
        """ RemoveLostFocusHandler(element: DependencyObject, handler: RoutedEventHandler) """
        pass

    @staticmethod
    def SetFocusedElement(element, value):
        """
        SetFocusedElement(element: DependencyObject, value: IInputElement)
            Sets logical focus on the specified element.
        
            element: The focus scope in which to make the specified element the System.Windows.Input.FocusManager.FocusedElement.
            value: The element to give logical focus to.
        """
        pass

    @staticmethod
    def SetIsFocusScope(element, value):
        """
        SetIsFocusScope(element: DependencyObject, value: bool)
            Sets the specified System.Windows.DependencyObject as a focus scope.
        
            element: The element to make a focus scope.
            value: true if element is a focus scope; otherwise, false.
        """
        pass

    FocusedElementProperty = None
    GotFocusEvent = None
    IsFocusScopeProperty = None
    LostFocusEvent = None
    __all__ = [
        'AddGotFocusHandler',
        'AddLostFocusHandler',
        'FocusedElementProperty',
        'GetFocusedElement',
        'GetFocusScope',
        'GetIsFocusScope',
        'GotFocusEvent',
        'IsFocusScopeProperty',
        'LostFocusEvent',
        'RemoveGotFocusHandler',
        'RemoveLostFocusHandler',
        'SetFocusedElement',
        'SetIsFocusScope',
    ]

