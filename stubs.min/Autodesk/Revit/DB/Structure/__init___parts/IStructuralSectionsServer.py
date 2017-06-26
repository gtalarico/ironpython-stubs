class IStructuralSectionsServer(IExternalServer):
    """ Interface for the section type parameter server to implement. """
    def StructuralSectionsUpdate(self, data):
        """
        StructuralSectionsUpdate(self: IStructuralSectionsServer, data: StructuralSectionsServiceData) -> bool
        
            The server's method that will be called when Revit User clicks the Section Type 
             parameter's button in the family dialog.
        
        
            data: The Section Type data.
            Returns: Indicates whether the section type parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

