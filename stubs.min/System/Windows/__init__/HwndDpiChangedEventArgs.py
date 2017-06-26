class HwndDpiChangedEventArgs(HandledEventArgs):
    # no doc
    NewDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewDpi(self: HwndDpiChangedEventArgs) -> DpiScale

"""

    OldDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldDpi(self: HwndDpiChangedEventArgs) -> DpiScale

"""

    SuggestedRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuggestedRect(self: HwndDpiChangedEventArgs) -> Rect

"""


