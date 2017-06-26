class ModelCurveNode(RenderNode, IDisposable):
    """ A base class of output nodes that represent various model curves. """
    def Dispose(self):
        """ Dispose(self: RenderNode, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RenderNode, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    LineProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the line (pen) properties of the curve being drawn

Get: LineProperties(self: ModelCurveNode) -> LineProperties

"""


