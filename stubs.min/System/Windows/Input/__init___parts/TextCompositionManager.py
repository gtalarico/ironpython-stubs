class TextCompositionManager(DispatcherObject):
    """ Provides facilities for managing events related to input and text compositions. """
    @staticmethod
    def AddPreviewTextInputHandler(element, handler):
        """
        AddPreviewTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInput � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddPreviewTextInputStartHandler(element, handler):
        """
        AddPreviewTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputStart � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddPreviewTextInputUpdateHandler(element, handler):
        """
        AddPreviewTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputUpdate � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputHandler(element, handler):
        """
        AddTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInput � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputStartHandler(element, handler):
        """
        AddTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def AddTextInputUpdateHandler(element, handler):
        """
        AddTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Adds a handler for the System.Windows.Input.TextCompositionManager.TextInputUpdate � attached event.
        
            element: A dependency object to add the event handler to.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to add.
        """
        pass

    @staticmethod
    def CompleteComposition(composition):
        """
        CompleteComposition(composition: TextComposition) -> bool
        
            Completes a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to complete.
            Returns: true if the text composition was successfully completed; otherwise, false.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputHandler(element, handler):
        """
        RemovePreviewTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInput � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputStartHandler(element, handler):
        """
        RemovePreviewTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemovePreviewTextInputUpdateHandler(element, handler):
        """
        RemovePreviewTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.PreviewTextInputUpdate � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputHandler(element, handler):
        """
        RemoveTextInputHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInput � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputStartHandler(element, handler):
        """
        RemoveTextInputStartHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputStart � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def RemoveTextInputUpdateHandler(element, handler):
        """
        RemoveTextInputUpdateHandler(element: DependencyObject, handler: TextCompositionEventHandler)
            Removes a handler for the System.Windows.Input.TextCompositionManager.TextInputUpdate � attached event.
        
            element: A dependency object to remove the event handler from.  The dependency object must be a System.Windows.UIElement or a System.Windows.ContentElement.
            handler: A delegate that designates the handler to remove.
        """
        pass

    @staticmethod
    def StartComposition(composition):
        """
        StartComposition(composition: TextComposition) -> bool
        
            Starts a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to start.
            Returns: true if the text composition was successfully started; otherwise, false.
        """
        pass

    @staticmethod
    def UpdateComposition(composition):
        """
        UpdateComposition(composition: TextComposition) -> bool
        
            Updates a specified text composition.
        
            composition: A System.Windows.Input.TextComposition object to update.
            Returns: true if the text composition was successfully updated; otherwise, false.
        """
        pass

    PreviewTextInputEvent = None
    PreviewTextInputStartEvent = None
    PreviewTextInputUpdateEvent = None
    TextInputEvent = None
    TextInputStartEvent = None
    TextInputUpdateEvent = None

