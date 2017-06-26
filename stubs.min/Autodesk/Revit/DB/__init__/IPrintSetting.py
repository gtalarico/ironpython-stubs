class IPrintSetting:
    """ An interface which represents the Print Setup (Application Menu->Print->Print Setup) within Autodesk Revit. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PrintParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Parameters of Print Setup.

Get: PrintParameters(self: IPrintSetting) -> PrintParameters

"""


