class StylusDeviceCollection(ReadOnlyCollection[StylusDevice], IList[StylusDevice], ICollection[StylusDevice], IEnumerable[StylusDevice], IEnumerable, IList, ICollection, IReadOnlyList[StylusDevice], IReadOnlyCollection[StylusDevice]):
    """ Contains the System.Windows.Input.StylusDevice objects that represent a Tablet PC's stylus devices. """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""


