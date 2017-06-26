class MeshFromGeometryOperationIssue(Enum, IComparable, IFormattable, IConvertible):
    """
    Issues, which can be encountered while building a mesh as a
       fallback for geometrical operations.
    
    enum MeshFromGeometryOperationIssue, values: AllFine (0), CurveLoopsWithoutCurvesInInput (4), EmptyCurveLoopsInInput (3), InputCurveLoopProblemWithFallback (6), InputCurveLoopWrongOpenFlag (7), InternalError (12), InternalMissingError (11), InternalUtilityError (10), MissingCurveLoopsInInput (2), MissingCurvesInInputLoop (9), NonContinuousInputCurveLoop (8), NonPlanarProfileLoop (5), NotSetYet (13), NoUsableCurveLoopsInInput (1), NumberOfIssueTypes (14)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllFine = None
    CurveLoopsWithoutCurvesInInput = None
    EmptyCurveLoopsInInput = None
    InputCurveLoopProblemWithFallback = None
    InputCurveLoopWrongOpenFlag = None
    InternalError = None
    InternalMissingError = None
    InternalUtilityError = None
    MissingCurveLoopsInInput = None
    MissingCurvesInInputLoop = None
    NonContinuousInputCurveLoop = None
    NonPlanarProfileLoop = None
    NotSetYet = None
    NoUsableCurveLoopsInInput = None
    NumberOfIssueTypes = None
    value__ = None

