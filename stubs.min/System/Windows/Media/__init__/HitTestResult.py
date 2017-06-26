class HitTestResult(object):
    """ Provides the base class for several derived classes that represents the return value from a hit test. """
    VisualHit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual object that was hit.

Get: VisualHit(self: HitTestResult) -> DependencyObject

"""


