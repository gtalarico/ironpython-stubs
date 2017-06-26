class CanExecuteChangedEventManager(WeakEventManager):
    # no doc
    @staticmethod
    def AddHandler(source, handler):
        """ AddHandler(source: ICommand, handler: EventHandler[EventArgs]) """
        pass

    @staticmethod
    def RemoveHandler(source, handler):
        """ RemoveHandler(source: ICommand, handler: EventHandler[EventArgs]) """
        pass

    ReadLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a read-lock on the underlying data table, and returns an System.IDisposable.

"""

    WriteLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a write-lock on the underlying data table, and returns an System.IDisposable.

"""


