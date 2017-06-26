class LayoutSettings(object):
    """ Provides a base class for collecting layout scheme characteristics. """
    LayoutEngine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current table layout engine.

Get: LayoutEngine(self: LayoutSettings) -> LayoutEngine

"""


