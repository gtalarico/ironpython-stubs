class ISupportInitializeNotification(ISupportInitialize):
    """ Allows coordination of initialization for a component and its dependent properties. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component is initialized.

Get: IsInitialized(self: ISupportInitializeNotification) -> bool

"""


    Initialized = None

