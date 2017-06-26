class AdornerHitTestResult(PointHitTestResult):
    """ Represents data returned from calling the System.Windows.Documents.AdornerLayer.AdornerHitTest(System.Windows.Point) method. """
    Adorner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual that was hit.

Get: Adorner(self: AdornerHitTestResult) -> Adorner

"""


