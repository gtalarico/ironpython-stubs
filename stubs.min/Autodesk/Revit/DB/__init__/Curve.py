class Curve(GeometryObject, IDisposable):
    """ A parametric curve. """
    def Clone(self):
        """
        Clone(self: Curve) -> Curve
        
            Returns a copy of this curve.
            Returns: A copy of this curve.
        """
        pass

    def ComputeDerivatives(self, parameter, normalized):
        """
        ComputeDerivatives(self: Curve, parameter: float, normalized: bool) -> Transform
        
            Returns the vectors describing the curve at the specified parameter.
        
            parameter: The parameter to be evaluated.
            normalized: If false, param is interpreted as natural parameterization of the curve.
           If 
             true, param is expected to be in [0,1] interval mapped to the bounds of the 
             curve. Setting to true is valid only if the curve is bound.
        
            Returns: The transformation containing the point on the curve, the tangent vector, 
             derivative of tangent vector, and bi-normal vector.
        """
        pass

    def ComputeNormalizedParameter(self, rawParameter):
        """
        ComputeNormalizedParameter(self: Curve, rawParameter: float) -> float
        
            Computes the normalized curve parameter from the raw parameter.
        
            rawParameter: The raw parameter.
            Returns: The real number equal to the normalized curve parameter.
        """
        pass

    def ComputeRawParameter(self, normalizedParameter):
        """
        ComputeRawParameter(self: Curve, normalizedParameter: float) -> float
        
            Computes the raw parameter from the normalized parameter.
        
            normalizedParameter: The normalized parameter.
            Returns: The real number equal to the raw curve parameter.
        """
        pass

    def CreateOffset(self, offsetDist, referenceVector):
        """
        CreateOffset(self: Curve, offsetDist: float, referenceVector: XYZ) -> Curve
        
            Creates a new curve that is an offset of the existing curve.
        
            offsetDist: The signed distance that controls the offset.
            referenceVector: A reference vector to define the offset direction.
            Returns: The new curve.
        """
        pass

    def CreateReversed(self):
        """
        CreateReversed(self: Curve) -> Curve
        
            Creates a new curve with the opposite orientation of the existing curve.
            Returns: The new curve.
        """
        pass

    def CreateTransformed(self, transform):
        """
        CreateTransformed(self: Curve, transform: Transform) -> Curve
        
            Crates a new instance of a curve as a transformation of this curve.
        
            transform: The transform to apply.
            Returns: The new curve.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def Distance(self, point):
        """
        Distance(self: Curve, point: XYZ) -> float
        
            Returns the shortest distance from the specified point to this curve.
        
            point: The specified point.
            Returns: The real number equal to the shortest distance.
        """
        pass

    def Evaluate(self, parameter, normalized):
        """
        Evaluate(self: Curve, parameter: float, normalized: bool) -> XYZ
        
            Evaluates and returns the point that matches a parameter along the curve.
        
            parameter: The parameter to be evaluated.
            normalized: If false, param is interpreted as natural parameterization of the curve.
           If 
             true, param is expected to be in [0,1] interval mapped to the bounds of the 
             curve. Setting to true is valid only if the curve is bound.
        
            Returns: The point evaluated along the curve.
        """
        pass

    def GetEndParameter(self, index):
        """
        GetEndParameter(self: Curve, index: int) -> float
        
            Returns the raw parameter value at the start or end of this curve.
        
            index: 0 for the start or 1 for end of the curve.
            Returns: The parameter.
        """
        pass

    def GetEndPoint(self, index):
        """
        GetEndPoint(self: Curve, index: int) -> XYZ
        
            Returns the 3D point at the start or end of this curve.
        
            index: 0 for the start or 1 for end of the curve.
            Returns: The curve endpoint.
        """
        pass

    def GetEndPointReference(self, index):
        """
        GetEndPointReference(self: Curve, index: int) -> Reference
        
            Returns a stable reference to the start point or the end point of the curve.
        
            index: Use 0 for the start point; 1 for the end point.
            Returns: Reference to the point or ll if reference cannot be obtained.
        """
        pass

    def Intersect(self, curve, resultArray=None):
        """
        Intersect(self: Curve, curve: Curve) -> SetComparisonResult
        
            Calculates the intersection of this curve with the specified curve.
        
            curve: The specified curve to intersect with this curve.
            Returns: SetComparisonResult.Overlap - One or more intersections were encountered. 
             SetComparisonResult.Subset - The inputs are parallel lines with only one common 
             intersection point, or 
        the curve used to invoke the intersection check is a 
             line entirely within the unbound line passed as argument 
             curve.SetComparisonResult.Superset - The input curve is entirely within the 
             unbound line used to invoke the intersection check.SetComparisonResult.Disjoint 
             - There is no intersection found between the two 
             curves.SetComparisonResult.Equal - The two curves are identical.
        
        Intersect(self: Curve, curve: Curve) -> (SetComparisonResult, IntersectionResultArray)
        
            Calculates the intersection of this curve with the specified curve and returns 
             the intersection results.
        
        
            curve: The specified curve to intersect with this curve.
            Returns: SetComparisonResult.Overlap - One or more intersections were encountered.  The 
             output argument has the details.SetComparisonResult.Subset - The inputs are 
             parallel lines with only one common intersection point, or 
        the curve used to 
             invoke the intersection check is a line entirely within the unbound line passed 
             as argument curve.
        If the former, the output argument has the details of the 
             intersection point.SetComparisonResult.Superset - The input curve is entirely 
             within the unbound line used to invoke the intersection 
             check.SetComparisonResult.Disjoint - There is no intersection found between the 
             two curves.SetComparisonResult.Equal - The two curves are identical.
        """
        pass

    def IsInside(self, parameter, end=None):
        """
        IsInside(self: Curve, parameter: float) -> bool
        
            Indicates whether the specified parameter value is within this curve's bounds.
        
            parameter: The raw curve parameter to be evaluated.
            Returns: True if the parameter is within the bounds, otherwise false.
        IsInside(self: Curve, parameter: float) -> (bool, int)
        
            Indicates whether the specified parameter value is within this curve's bounds 
             and outputs the end index.
        
        
            parameter: The raw curve parameter to be evaluated.
            Returns: True if the parameter is within the curve's bounds, otherwise false.
        """
        pass

    def MakeBound(self, startParameter, endParameter):
        """
        MakeBound(self: Curve, startParameter: float, endParameter: float)
            Changes the bounds of this curve to the specified values.
        
            startParameter: The new parameter of the start point.
            endParameter: The new parameter of the end point.
        """
        pass

    def MakeUnbound(self):
        """
        MakeUnbound(self: Curve)
            Makes this curve unbound.
        """
        pass

    def Project(self, point):
        """
        Project(self: Curve, point: XYZ) -> IntersectionResult
        
            Projects the specified point on this curve.
        
            point: The point to be projected.
            Returns: Geometric information if projection is successful.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GeometryObject) """
        pass

    def SetGraphicsStyleId(self, id):
        """
        SetGraphicsStyleId(self: Curve, id: ElementId)
            Sets the graphics style id for this curve.
        
            id: The id of the GraphicsStyle element from which to apply the curve properties.
        """
        pass

    def Tessellate(self):
        """
        Tessellate(self: Curve) -> IList[XYZ]
        
            Valid only if the curve is bound. Returns a polyline approximation to the curve.
        """
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

    ApproximateLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The approximate length of the curve.

Get: ApproximateLength(self: Curve) -> float

"""

    IsBound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes whether the parameter of the curve is restricted to a particular interval.

Get: IsBound(self: Curve) -> bool

"""

    IsCyclic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boolean value that indicates whether this curve is cyclic.

Get: IsCyclic(self: Curve) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The exact length of the curve.

Get: Length(self: Curve) -> float

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The period of this curve.

Get: Period(self: Curve) -> float

"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a stable reference to the curve.

Get: Reference(self: Curve) -> Reference

"""


