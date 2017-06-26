class ActivationContext(object, IDisposable, ISerializable):
    """ Identifies the activation context for the current application. This class cannot be inherited. """
    @staticmethod
    def CreatePartialActivationContext(identity, manifestPaths=None):
        """
        CreatePartialActivationContext(identity: ApplicationIdentity, manifestPaths: Array[str]) -> ActivationContext
        
            Initializes a new instance of the System.ActivationContext class using the specified application identity and array of manifest paths.
        
            identity: An object that identifies an application.
            manifestPaths: A string array of manifest paths for the application.
            Returns: An object with the specified application identity and array of manifest paths.
        CreatePartialActivationContext(identity: ApplicationIdentity) -> ActivationContext
        
            Initializes a new instance of the System.ActivationContext class using the specified application identity.
        
            identity: An object that identifies an application.
            Returns: An object with the specified application identity.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ActivationContext)
            Releases all resources used by the System.ActivationContext.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ApplicationManifestBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ClickOnce application manifest for the current application.

Get: ApplicationManifestBytes(self: ActivationContext) -> Array[Byte]

"""

    DeploymentManifestBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ClickOnce deployment manifest for the current application.

Get: DeploymentManifestBytes(self: ActivationContext) -> Array[Byte]

"""

    Form = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the form, or store context, for the current application.

Get: Form(self: ActivationContext) -> ContextForm

"""

    Identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application identity for the current application.

Get: Identity(self: ActivationContext) -> ApplicationIdentity

"""


    ContextForm = None

