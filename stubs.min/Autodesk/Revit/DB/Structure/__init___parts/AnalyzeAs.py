class AnalyzeAs(Enum, IComparable, IFormattable, IConvertible):
    """
    Analyze As has various functions within the Analytical Model, and is Element-dependent.
       "Not for Analysis" usually means that there will not be an Analytical Model generated.
       The others indicate how the Analytical Model behavior will treat the Element in question.
       For instance "Hanger" columns have different support expectations than "Gravity" columns.
    
    enum AnalyzeAs, values: Gravity (1), GravityLateral (10), Hanger (0), Lateral (2), Mat (4), NotApplicable (8), NotForAnalysis (7), SlabOneWay (3), SlabOnGrade (5), SlabTwoWay (9)
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

    Gravity = None
    GravityLateral = None
    Hanger = None
    Lateral = None
    Mat = None
    NotApplicable = None
    NotForAnalysis = None
    SlabOneWay = None
    SlabOnGrade = None
    SlabTwoWay = None
    value__ = None

