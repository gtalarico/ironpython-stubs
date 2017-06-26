class PresentationSource(DispatcherObject):
    """ Provides an abstract base for classes that present content from another technology as part of an interoperation scenario. In addition, this class provides static methods for working with these sources, as well as the basic visual-layer presentation architecture. """
    def AddSource(self, *args): #cannot find CLR method
        """
        AddSource(self: PresentationSource)
            Adds a System.Windows.PresentationSource derived class instance to the list of known presentation sources.
        """
        pass

    @staticmethod
    def AddSourceChangedHandler(element, handler):
        """
        AddSourceChangedHandler(element: IInputElement, handler: SourceChangedEventHandler)
            Adds a handler for the SourceChanged event to the provided element.
        
            element: The element to add the handler to.
            handler: The hander implementation to add.
        """
        pass

    def ClearContentRenderedListeners(self, *args): #cannot find CLR method
        """
        ClearContentRenderedListeners(self: PresentationSource)
            Sets the list of listeners for the System.Windows.PresentationSource.ContentRendered event to null.
        """
        pass

    @staticmethod
    def FromDependencyObject(dependencyObject):
        """
        FromDependencyObject(dependencyObject: DependencyObject) -> PresentationSource
        
            Returns the source in which a provided System.Windows.DependencyObject is presented.
        
            dependencyObject: The System.Windows.DependencyObject to find the source for.
            Returns: The System.Windows.PresentationSource in which the dependency object is being presented.
        """
        pass

    @staticmethod
    def FromVisual(visual):
        """
        FromVisual(visual: Visual) -> PresentationSource
        
            Returns the source in which a provided System.Windows.Media.Visual is presented.
        
            visual: The System.Windows.Media.Visual to find the source for.
            Returns: The System.Windows.PresentationSource in which the visual is being presented, or null if visual is disposed.
        """
        pass

    def GetCompositionTargetCore(self, *args): #cannot find CLR method
        """
        GetCompositionTargetCore(self: PresentationSource) -> CompositionTarget
        
            When overridden in a derived class, returns a visual target for the given source.
            Returns: Returns a System.Windows.Media.CompositionTarget that is target for rendering the visual.
        """
        pass

    def RemoveSource(self, *args): #cannot find CLR method
        """
        RemoveSource(self: PresentationSource)
            Removes a System.Windows.PresentationSource derived class instance from the list of known presentation sources.
        """
        pass

    @staticmethod
    def RemoveSourceChangedHandler(e, handler):
        """
        RemoveSourceChangedHandler(e: IInputElement, handler: SourceChangedEventHandler)
            Removes a handler for the SourceChanged event from the provided element.
        
            e: The element to remove the handler from.
            handler: The handler implementation to remove.
        """
        pass

    def RootChanged(self, *args): #cannot find CLR method
        """
        RootChanged(self: PresentationSource, oldRoot: Visual, newRoot: Visual)
            Provides notification that the root System.Windows.Media.Visual has changed.
        
            oldRoot: The old root System.Windows.Media.Visual.
            newRoot: The new root System.Windows.Media.Visual.
        """
        pass

    CompositionTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual target for the visuals being presented in the source.

Get: CompositionTarget(self: PresentationSource) -> CompositionTarget

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value that declares whether the object is disposed.

Get: IsDisposed(self: PresentationSource) -> bool

"""

    RootVisual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets or sets the root visual being presented in the source.

Get: RootVisual(self: PresentationSource) -> Visual

Set: RootVisual(self: PresentationSource) = value
"""


    ContentRendered = None
    CurrentSources = None

