class Form(GenericForm, IDisposable):
    """ An object that represents a Form within the Autodesk Revit Massing Family. """
    def AddEdge(self, *__args):
        """
        AddEdge(self: Form, faceReference: Reference, point: XYZ)
            Add an edge to the form, connecting two edges on different profiles, by a 
             specified face of the form and a point on face.
        
        
            faceReference: The geometry reference of face
            point: A point on the face, defining the position of edge to be created.
        AddEdge(self: Form, startEdgeReference: Reference, startParam: float, endEdgeReference: Reference, endParam: float)
            Add an edge to the form, connecting two edges on same/different profile, by a 
             pair of specified edge/param.
        
        
            startEdgeReference: The geometry reference of start edge
            startParam: The param on start edge to specify the location.
            endEdgeReference: The geometry reference of end edge
            endParam: The param on end edge to specify the location.
        AddEdge(self: Form, startPointReference: Reference, endPointReference: Reference)
            Add an edge to the form, connecting two edges on same/different profile, by a 
             pair of specified points.
        
        
            startPointReference: The geometry reference of start point
            endPointReference: The geometry reference of end point
        """
        pass

    def AddProfile(self, edgeReference, param):
        """
        AddProfile(self: Form, edgeReference: Reference, param: float) -> int
        
            Add a profile into the form, by a specified edge/param.
        
            edgeReference: The geometry reference of edge.
            param: The param on edge to specify the location.
            Returns: Index of newly created profile.
        """
        pass

    def CanManipulateProfile(self, profileIndex):
        """
        CanManipulateProfile(self: Form, profileIndex: int) -> bool
        
            Tell if a profile can be deleted/moved/rotated.
        
            profileIndex: Index to specify the profile.
        """
        pass

    def CanManipulateSubElement(self, subElementReference):
        """
        CanManipulateSubElement(self: Form, subElementReference: Reference) -> bool
        
            Tell if a sub element can be deleted/moved/rotated/scaled.
        
            subElementReference: The geometry reference of face/edge/curve/vertex
        """
        pass

    def ConstrainProfiles(self, masterProfileIndex):
        """
        ConstrainProfiles(self: Form, masterProfileIndex: int)
            Constrain form profiles using the specified profile as master. This is an 
             advanced version of property "AreProfilesConstrained", allowing specify the 
             master profile.
        
        
            masterProfileIndex: Index to specify the profile used as master profile.
        """
        pass

    def DeleteProfile(self, profileIndex):
        """
        DeleteProfile(self: Form, profileIndex: int)
            Delete a profile of the form.
        
            profileIndex: Index to specify the profile.
        """
        pass

    def DeleteSubElement(self, subElementReference):
        """
        DeleteSubElement(self: Form, subElementReference: Reference)
            Delete a face/edge/curve/vertex of the form, specified by a reference.
        
            subElementReference: The geometry reference of face/edge/curve/vertex
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetControlPoints(self, curveOrEdgeOrFaceReference):
        """
        GetControlPoints(self: Form, curveOrEdgeOrFaceReference: Reference) -> ReferenceArray
        
            Given an edge or a curve or a face, return all control points lying on it (in 
             form of geometry references).
        
        
            curveOrEdgeOrFaceReference: The reference of an edge or curve or face.
            Returns: Reference array containing all control points lying on it.
        """
        pass

    def GetCurvesAndEdgesReference(self, pointReference):
        """
        GetCurvesAndEdgesReference(self: Form, pointReference: Reference) -> ReferenceArray
        
            Given a point, return all edges and curves that it is lying on.
        
            pointReference: The reference of a point.
            Returns: Reference array containing all edges and curves that the point is lying on.
        """
        pass

    def GetPathCurveIndexByCurveReference(self, curveReference):
        """
        GetPathCurveIndexByCurveReference(self: Form, curveReference: Reference) -> int
        
            Given a reference to certain curve in the path, return its index.
        
            curveReference: Reference to the curve in path
        """
        pass

    def GetProfileAndCurveLoopIndexFromReference(self, curveOrEdgeReference, profileIndex, curveLoopIndex):
        """
        GetProfileAndCurveLoopIndexFromReference(self: Form, curveOrEdgeReference: Reference, profileIndex: int, curveLoopIndex: int) -> (int, int)
        
            Given a reference to certain curve or edge, get the index of its profile and 
             curve loop respectively.
        
        
            curveOrEdgeReference: Reference to a curve/edge that is part of one profile
            profileIndex: Profile index for output
            curveLoopIndex: Curve loop index for output
        """
        pass

    def IsAutoCreaseEdge(self, edgeReference):
        """
        IsAutoCreaseEdge(self: Form, edgeReference: Reference) -> bool
        
            Tell if an edge is an auto-crease on a top/bottom cap face.
        
            edgeReference: The reference of the edge to be checked.
        """
        pass

    def IsBeginningFace(self, faceReference):
        """
        IsBeginningFace(self: Form, faceReference: Reference) -> bool
        
            Given a face, tell if it is a beginning cap face.
        
            faceReference: The reference of the  face to be checked.
        """
        pass

    def IsConnectingEdge(self, edgeReference):
        """
        IsConnectingEdge(self: Form, edgeReference: Reference) -> bool
        
            Tell if an edge is a connecting edge on a side face. Connecting edges connect 
             vertices on different profiles.
        
        
            edgeReference: The reference of the edge to be checked.
        """
        pass

    def IsCurveReference(self, curveReference):
        """
        IsCurveReference(self: Form, curveReference: Reference) -> bool
        
            Tell if the pick is the reference to a curve of the form.
        
            curveReference: Reference to be checked.
        """
        pass

    def IsEdgeReference(self, edgeReference):
        """
        IsEdgeReference(self: Form, edgeReference: Reference) -> bool
        
            Tell if the pick is the reference to an edge of the form.
        
            edgeReference: Reference to be checked.
        """
        pass

    def IsEndFace(self, faceReference):
        """
        IsEndFace(self: Form, faceReference: Reference) -> bool
        
            Given a face, tell if it is an end cap face.
        
            faceReference: The reference of the face to be checked.
        """
        pass

    def IsFaceReference(self, faceReference):
        """
        IsFaceReference(self: Form, faceReference: Reference) -> bool
        
            Tell if the pick is the reference to a face of the form.
        
            faceReference: Reference to be checked.
        """
        pass

    def IsProfileEdge(self, curveOrEdgeReference):
        """
        IsProfileEdge(self: Form, curveOrEdgeReference: Reference) -> bool
        
            Tell if an edge or curve is generated from a profile.
        
            curveOrEdgeReference: The reference of the edge or curve to be checked.
        """
        pass

    def IsReferenceOnlyProfile(self, profileIndex):
        """
        IsReferenceOnlyProfile(self: Form, profileIndex: int) -> bool
        
            Tell if the profile is made by referencing existing geometry in the Revit model.
        
            profileIndex: Index to specify the profile to be checked.
        """
        pass

    def IsSideFace(self, faceReference):
        """
        IsSideFace(self: Form, faceReference: Reference) -> bool
        
            Given a face, tell if it is a side face.
        
            faceReference: The reference of the  face to be checked.
        """
        pass

    def IsVertexReference(self, vertexReference):
        """
        IsVertexReference(self: Form, vertexReference: Reference) -> bool
        
            Tell if the pick is the reference to a vertex of the form.
        
            vertexReference: Reference to be checked.
        """
        pass

    def MoveProfile(self, profileIndex, offset):
        """
        MoveProfile(self: Form, profileIndex: int, offset: XYZ)
            Move a profile of the form, specified by a reference, and an offset vector.
        
            profileIndex: Index to specify the profile.
            offset: The vector by which the element is to be moved.
        """
        pass

    def MoveSubElement(self, subElementReference, offset):
        """
        MoveSubElement(self: Form, subElementReference: Reference, offset: XYZ)
            Move a face/edge/curve/vertex of the form, specified by a reference, and an 
             offset vector.
        
        
            subElementReference: The geometry reference of face/edge/curve/vertex
            offset: The vector by which the element is to be moved.
        """
        pass

    def Rehost(self, *__args):
        """
        Rehost(self: Form, hostRef: Reference, location: XYZ)
            Rehost Form to edge, face or curve.
        
            hostRef: The geometry reference on which to rehost the form.
            location: The location to which to Rehost the form.
        Rehost(self: Form, sketchPlane: SketchPlane, location: XYZ)
            Rehost Form to sketch plane
        
            sketchPlane: The sketch plane on which to rehost the form.
            location: The location to which to Rehost the form.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RotateProfile(self, profileIndex, axis, angle):
        """
        RotateProfile(self: Form, profileIndex: int, axis: Line, angle: float)
            Rotate a profile of the form, by a specified angle around a given axis.
        
            profileIndex: Index to specify the profile.
            axis: An unbounded line that represents the axis of rotation.
            angle: The angle, in radians, by which the element is to be rotated around the 
             specified axis.
        """
        pass

    def RotateSubElement(self, subElementReference, axis, angle):
        """
        RotateSubElement(self: Form, subElementReference: Reference, axis: Line, angle: float)
            Rotate a face/edge/curve/vertex of the form, by a specified angle around a 
             given axis.
        
        
            subElementReference: The geometry reference of face/edge/curve/vertex
            axis: An unbounded line that represents the axis of rotation.
            angle: The angle, in radians, by which the element is to be rotated around the 
             specified axis.
        """
        pass

    def ScaleProfile(self, profileIndex, factor, origin):
        """
        ScaleProfile(self: Form, profileIndex: int, factor: float, origin: XYZ)
            Scale a profile of the form, by a specified origin and scale factor.
        
            profileIndex: Index to specify the profile.
            factor: The scale factor, it should be large than zero.
            origin: The origin where scale happens.
        """
        pass

    def ScaleSubElement(self, subElementReference, factor, origin):
        """
        ScaleSubElement(self: Form, subElementReference: Reference, factor: float, origin: XYZ)
            Scale a face/edge/curve/vertex of the form, by a specified origin and scale 
             factor.
        
        
            subElementReference: The geometry reference of face/edge/curve/vertex
            factor: The scale factor, it should be large than zero.
            origin: The origin where scale happens.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    AreProfilesConstrained = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set if the form's profiles are constrained.

Get: AreProfilesConstrained(self: Form) -> bool

Set: AreProfilesConstrained(self: Form) = value
"""

    BaseOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve/set the base offset of the form object. It is only valid for locked form.

Get: BaseOffset(self: Form) -> float

Set: BaseOffset(self: Form) = value
"""

    HasOneOrMoreReferenceProfiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tell if the form has any reference profile.

Get: HasOneOrMoreReferenceProfiles(self: Form) -> bool

"""

    HasOpenGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tell if the form has an open geometry.

Get: HasOpenGeometry(self: Form) -> bool

"""

    IsInXRayMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set if the form is in X-Ray mode.

Get: IsInXRayMode(self: Form) -> bool

Set: IsInXRayMode(self: Form) = value
"""

    PathCurveCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of curves in the form path.

Get: PathCurveCount(self: Form) -> int

"""

    ProfileCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of profiles in the form.

Get: ProfileCount(self: Form) -> int

"""

    TopOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve/set the top offset of the form object. It is only valid for locked form.

Get: TopOffset(self: Form) -> float

Set: TopOffset(self: Form) = value
"""


