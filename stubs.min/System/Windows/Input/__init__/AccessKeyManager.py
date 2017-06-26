class AccessKeyManager(object):
    """ Maintains the registration of all access keys and the handling of interop keyboard commands between Windows Forms, Win32,�and Windows Presentation Foundation (WPF). """
    @staticmethod
    def AddAccessKeyPressedHandler(element, handler):
        """
        AddAccessKeyPressedHandler(element: DependencyObject, handler: AccessKeyPressedEventHandler)
            Adds a handler for the System.Windows.Input.AccessKeyManager.AccessKeyPressed�attached event.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be added.
        """
        pass

    @staticmethod
    def IsKeyRegistered(scope, key):
        """
        IsKeyRegistered(scope: object, key: str) -> bool
        
            Indicates whether the specified key is registered as an access keys in the specified scope.
        
            scope: The presentation source to query for key.
            key: The key to query.
            Returns: true if the key is registered; otherwise, false.
        """
        pass

    @staticmethod
    def ProcessKey(scope, key, isMultiple):
        """
        ProcessKey(scope: object, key: str, isMultiple: bool) -> bool
        
            Processes the specified access keys as if a System.Windows.UIElement.KeyDown event for the key was passed to the System.Windows.Input.AccessKeyManager.
        
            scope: The scope for the access key.
            key: The access key.
            isMultiple: Indicates if key has multiple matches.
            Returns: true if there are more keys that match; otherwise, false.
        """
        pass

    @staticmethod
    def Register(key, element):
        """
        Register(key: str, element: IInputElement)
            Associates the specified access keys with the specified element.
        
            key: The access key.
            element: The element to associate key with.
        """
        pass

    @staticmethod
    def RemoveAccessKeyPressedHandler(element, handler):
        """
        RemoveAccessKeyPressedHandler(element: DependencyObject, handler: AccessKeyPressedEventHandler)
            Removes the specified System.Windows.Input.AccessKeyManager.AccessKeyPressed event handler from the specified object.
        
            element: The System.Windows.UIElement or System.Windows.ContentElement that listens to this event.
            handler: The event handler to be removed.
        """
        pass

    @staticmethod
    def Unregister(key, element):
        """
        Unregister(key: str, element: IInputElement)
            Disassociates the specified access keys from the specified element.
        
            key: The access key.
            element: The element from which to disassociate key.
        """
        pass

    AccessKeyPressedEvent = None

