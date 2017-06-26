class DpiChangedEventArgs(RoutedEventArgs):
    # no doc
    NewDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewDpi(self: DpiChangedEventArgs) -> DpiScale

"""

    OldDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldDpi(self: DpiChangedEventArgs) -> DpiScale

"""


