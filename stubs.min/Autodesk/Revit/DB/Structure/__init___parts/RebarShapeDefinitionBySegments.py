class RebarShapeDefinitionBySegments(RebarShapeDefinition, IDisposable):
    """
    Definition of a shape in terms of one or more straight segments of rebar,
       with arc bends between the segments.
    
    RebarShapeDefinitionBySegments(doc: Document, numberOfSegments: int)
    """
    def AddBendDefaultRadius(self, vertexIndex, turn, angle):
        """
        AddBendDefaultRadius(self: RebarShapeDefinitionBySegments, vertexIndex: int, turn: RebarShapeVertexTurn, angle: RebarShapeBendAngle)
            Specify a default-radius bend.
        
            vertexIndex: Index of the vertex (1 to NumberOfVertices - 2).
            turn: Specify turn direction (RebarShapeVertexTurn::Left or 
             RebarShapeVertexTurn::Right).
        
            angle: Specify whether the bend is acute, obtuse, etc.
        """
        pass

    def AddBendVariableRadius(self, vertexIndex, turn, angle, paramId, measureIncludingBarThickness):
        """
        AddBendVariableRadius(self: RebarShapeDefinitionBySegments, vertexIndex: int, turn: RebarShapeVertexTurn, angle: RebarShapeBendAngle, paramId: ElementId, measureIncludingBarThickness: bool)
            Specify a variable-radius bend.
        
            vertexIndex: Index of the vertex (1 to NumberOfVertices - 2).
            turn: Specify turn direction (RebarShapeVertexTurn::Left or 
             RebarShapeVertexTurn::Right).
        
            angle: Specify whether the bend is acute, obtuse, etc.
            paramId: Id of a parameter driving the radius.
            measureIncludingBarThickness: If true, the radius is measured to the outside of the
           bend; if false, it is 
             measured to the inside.
        """
        pass

    def AddConstraintParallelToSegment(self, iSegment, paramId, measureToOutsideOfBend0, measureToOutsideOfBend1):
        """
        AddConstraintParallelToSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, measureToOutsideOfBend0: bool, measureToOutsideOfBend1: bool)
            Constrain the length of a segment by parameterizing its length.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the constraint. To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            measureToOutsideOfBend0: Choose between two possibilities for the first reference of the length 
             dimension. If false, the reference is at the point where the bend begins; 
             equivalently, at the projection of the bend centerpoint onto the segment. If 
             true, the reference is moved outward by a distance equal to the bend radius 
             plus the bar diameter; if the bend is a right angle or greater, this is 
             equivalent to putting the reference at the outer face of the bend.
        
            measureToOutsideOfBend1: Choose between two possibilities for the second reference of the length 
             dimension.
        """
        pass

    def AddConstraintToSegment(self, iSegment, paramId, constraintDirCoordX, constraintDirCoordY, signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, measureToOutsideOfBend0, measureToOutsideOfBend1):
        """
        AddConstraintToSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, signOfZCoordOfCrossProductOfConstraintDirBySegmentDir: int, measureToOutsideOfBend0: bool, measureToOutsideOfBend1: bool)
            Add a constraint that helps determine the length of a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            signOfZCoordOfCrossProductOfConstraintDirBySegmentDir: Legal values are 1 and -1. For a fixed-direction segment, this value is 
             ignored. For a variable-direction segment, this value is combined with the 
             constraint length (the nonnegative value associated with 'param') to determine 
             the direction of the segment. For example, a segment whose direction vector 
             lies in the upper-right quadrant of the plane, and whose x-axis projected 
             length is A and whose y-axis projected length is B, could be created by 
             calling: AddConstraintToSegment(iSegment, paramA, 1.0, 0.0, 1, ...) 
             AddConstraintToSegment(iSegment, paramB, 0.0, 1.0, -1, ...)
        
            measureToOutsideOfBend0: Choose between two possibilities for the first reference of the length 
             dimension. If false, the reference is at the point where the bend begins; 
             equivalently, at the projection of the bend centerpoint onto the segment. If 
             true, the reference is moved outward by a distance equal to the bend radius 
             plus the bar diameter; if the bend is a right angle or greater, this is 
             equivalent to putting the reference at the outer face of the bend.
        
            measureToOutsideOfBend1: Choose between two possibilities for the second reference of the length 
             dimension.
        """
        pass

    def AddListeningDimensionBendToBend(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iEnd0, iSegment1, iEnd1):
        """
        AddListeningDimensionBendToBend(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iEnd0: int, iSegment1: int, iEnd1: int)
            Specify a dimension between two bends, measured by a read-only parameter.
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iEnd0: End (0 or 1) of the first segment.
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
            iEnd1: End (0 or 1) of the second segment.
        """
        pass

    def AddListeningDimensionSegmentToBend(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1, iEnd1):
        """
        AddListeningDimensionSegmentToBend(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iSegment1: int, iEnd1: int)
            Specify a dimension perpendicular to one fixed-direction segment,
           referring 
             to that segment and some other bend in the shape,
           measured by a read-only 
             parameter.
        
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
            iEnd1: End (0 or 1) of the second segment.
        """
        pass

    def AddListeningDimensionSegmentToSegment(self, paramId, constraintDirCoordX, constraintDirCoordY, iSegment0, iSegment1):
        """
        AddListeningDimensionSegmentToSegment(self: RebarShapeDefinitionBySegments, paramId: ElementId, constraintDirCoordX: float, constraintDirCoordY: float, iSegment0: int, iSegment1: int)
            Specify a dimension perpendicular to two fixed-direction segments, measured by 
             a read-only parameter.
        
        
            paramId: Id of a parameter to report the length of the dimension. The parameter will be 
             read-only
           on Rebar instances.
        
            constraintDirCoordX: The x-coordinate of a 2D vector specifying the constraint direction.
            constraintDirCoordY: The y-coordinate of a 2D vector specifying the constraint direction.
            iSegment0: Index of the first segment (0 to NumberOfSegments - 1).
            iSegment1: Index of the second segment (0 to NumberOfSegments - 1).
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarShapeDefinition, A_0: bool) """
        pass

    def GetSegment(self, segmentIndex):
        """
        GetSegment(self: RebarShapeDefinitionBySegments, segmentIndex: int) -> RebarShapeSegment
        
            Return a reference to one of the segments in the definition.
        
            segmentIndex: Index of the segment (0 to NumberOfSegments - 1).
            Returns: The requested segment.
        """
        pass

    def GetVertex(self, vertexIndex):
        """
        GetVertex(self: RebarShapeDefinitionBySegments, vertexIndex: int) -> RebarShapeVertex
        
            Return a reference to one of the vertices in the definition.
        
            vertexIndex: Index of the vertex (0 to NumberOfVertices - 1).
            Returns: The requested vertex.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeDefinition, disposing: bool) """
        pass

    def RemoveParameterFromSegment(self, iSegment, paramId):
        """
        RemoveParameterFromSegment(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId)
            Remove constraints from a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter driving one or more constraints.
        """
        pass

    def SetSegmentAs180DegreeBend(self, iSegment, paramId=None, measureToOutsideOfBend=None):
        """
        SetSegmentAs180DegreeBend(self: RebarShapeDefinitionBySegments, iSegment: int)
            Indicates that a segment is a "virtual" segment introduced to describe a 
             180-degree bend. The radius of the bend will be taken from the Bar Type.
        
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
        SetSegmentAs180DegreeBend(self: RebarShapeDefinitionBySegments, iSegment: int, paramId: ElementId, measureToOutsideOfBend: bool)
            Indicate that a segment is a "virtual" segment introduced to describe a 
             180-degree bend. The radius of the bend will be driven by radiusParam.
        
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            paramId: Id of a parameter to drive the radius.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            measureToOutsideOfBend: Choose between two possibilities for the references of the radius dimension.
          
              If true, measure to the exterior face of the bar. If false, measure to the 
             interior face.
        """
        pass

    def SetSegmentFixedDirection(self, iSegment, vecCoordX, vecCoordY):
        """
        SetSegmentFixedDirection(self: RebarShapeDefinitionBySegments, iSegment: int, vecCoordX: float, vecCoordY: float)
            Fix the direction of a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
            vecCoordX: The x-coordinate of a 2D vector specifying the segment direction.
            vecCoordY: The y-coordinate of a 2D vector specifying the segment direction.
        """
        pass

    def SetSegmentVariableDirection(self, iSegment):
        """
        SetSegmentVariableDirection(self: RebarShapeDefinitionBySegments, iSegment: int)
            Remove the fixed direction from a segment.
        
            iSegment: Index of the segment (0 to NumberOfSegments - 1).
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

    @staticmethod # known case of __new__
    def __new__(self, doc, numberOfSegments):
        """ __new__(cls: type, doc: Document, numberOfSegments: int) """
        pass

    MajorSegmentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of a segment that can be considered the most important. Revit
   attempts to preserve the orientation of this segment when a Rebar instance
   changes its RebarShape to one with a different number of segments.

Get: MajorSegmentIndex(self: RebarShapeDefinitionBySegments) -> int

Set: MajorSegmentIndex(self: RebarShapeDefinitionBySegments) = value
"""

    NumberOfSegments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of straight segments in this shape.

Get: NumberOfSegments(self: RebarShapeDefinitionBySegments) -> int

"""

    NumberOfVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of vertices in this shape, always equal to NumberOfSegments + 1.

Get: NumberOfVertices(self: RebarShapeDefinitionBySegments) -> int

"""


