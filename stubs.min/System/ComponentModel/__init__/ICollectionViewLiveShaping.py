class ICollectionViewLiveShaping:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanChangeLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveFiltering(self: ICollectionViewLiveShaping) -> bool

"""

    CanChangeLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveGrouping(self: ICollectionViewLiveShaping) -> bool

"""

    CanChangeLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveSorting(self: ICollectionViewLiveShaping) -> bool

"""

    IsLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveFiltering(self: ICollectionViewLiveShaping) -> Nullable[bool]

Set: IsLiveFiltering(self: ICollectionViewLiveShaping) = value
"""

    IsLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveGrouping(self: ICollectionViewLiveShaping) -> Nullable[bool]

Set: IsLiveGrouping(self: ICollectionViewLiveShaping) = value
"""

    IsLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveSorting(self: ICollectionViewLiveShaping) -> Nullable[bool]

Set: IsLiveSorting(self: ICollectionViewLiveShaping) = value
"""

    LiveFilteringProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveFilteringProperties(self: ICollectionViewLiveShaping) -> ObservableCollection[str]

"""

    LiveGroupingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveGroupingProperties(self: ICollectionViewLiveShaping) -> ObservableCollection[str]

"""

    LiveSortingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSortingProperties(self: ICollectionViewLiveShaping) -> ObservableCollection[str]

"""


