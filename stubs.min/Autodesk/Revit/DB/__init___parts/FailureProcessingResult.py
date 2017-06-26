class FailureProcessingResult(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type representing the result achieved by any of the available types of failure handlers:
       FailuresPreprocessor, the handler of FailuresProcessing event or a FailuresProcessor.
    
    enum FailureProcessingResult, values: Continue (0), ProceedWithCommit (1), ProceedWithRollBack (2), WaitForUserInput (3)
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

    Continue = None
    ProceedWithCommit = None
    ProceedWithRollBack = None
    value__ = None
    WaitForUserInput = None

