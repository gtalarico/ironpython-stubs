class GeometryHitTestResult(HitTestResult):
    """
    Returns the results of a hit test that uses a System.Windows.Media.Geometry as a hit test parameter.
    
    GeometryHitTestResult(visualHit: Visual, intersectionDetail: IntersectionDetail)
    """
    @staticmethod # known case of __new__
    def __new__(self, visualHit, intersectionDetail):
        """ __new__(cls: type, visualHit: Visual, intersectionDetail: IntersectionDetail) """
        pass

    IntersectionDetail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.IntersectionDetail value of the hit test.

Get: IntersectionDetail(self: GeometryHitTestResult) -> IntersectionDetail

"""

    VisualHit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual object that is returned from a hit test result.

Get: VisualHit(self: GeometryHitTestResult) -> Visual

"""


