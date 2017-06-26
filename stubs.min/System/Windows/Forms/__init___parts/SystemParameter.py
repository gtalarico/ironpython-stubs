class SystemParameter(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the system parameter type.
    
    enum SystemParameter, values: CaretWidthMetric (8), DropShadow (0), FlatMenu (1), FontSmoothingContrastMetric (2), FontSmoothingTypeMetric (3), HorizontalFocusThicknessMetric (10), MenuFadeEnabled (4), SelectionFade (5), ToolTipAnimationMetric (6), UIEffects (7), VerticalFocusThicknessMetric (9)
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

    CaretWidthMetric = None
    DropShadow = None
    FlatMenu = None
    FontSmoothingContrastMetric = None
    FontSmoothingTypeMetric = None
    HorizontalFocusThicknessMetric = None
    MenuFadeEnabled = None
    SelectionFade = None
    ToolTipAnimationMetric = None
    UIEffects = None
    value__ = None
    VerticalFocusThicknessMetric = None

