class LostFocusEventManager(WeakEventManager):
    """ Provides a System.Windows.WeakEventManager implementation so that you can use the "weak event listener" pattern to attach listeners for the System.Windows.UIElement.LostFocus or System.Windows.ContentElement.LostFocus events. """
    @staticmethod
    def AddHandler(source, handler):
        """ AddHandler(source: DependencyObject, handler: EventHandler[RoutedEventArgs]) """
        pass

    @staticmethod
    def AddListener(source, listener):
        """
        AddListener(source: DependencyObject, listener: IWeakEventListener)
            Adds the provided listener to the list of listeners on the provided source.
        
            source: The object with the event.
            listener: The object to add as a listener.
        """
        pass

    @staticmethod
    def RemoveHandler(source, handler):
        """ RemoveHandler(source: DependencyObject, handler: EventHandler[RoutedEventArgs]) """
        pass

    @staticmethod
    def RemoveListener(source, listener):
        """
        RemoveListener(source: DependencyObject, listener: IWeakEventListener)
            Removes the specified listener from the list of listeners on the provided source.
        
            source: The object to remove the listener from.
            listener: The listener to remove.
        """
        pass

    ReadLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a read-lock on the underlying data table, and returns an System.IDisposable.

"""

    WriteLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a write-lock on the underlying data table, and returns an System.IDisposable.

"""


