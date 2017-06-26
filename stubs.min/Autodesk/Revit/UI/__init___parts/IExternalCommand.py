class IExternalCommand:
    """ An interface that should be implemented to provide the implementation for a Revit add-in External Command. """
    def Execute(self, commandData, message, elements):
        """
        Execute(self: IExternalCommand, commandData: ExternalCommandData) -> (Result, str, ElementSet)
        
            Overload this method to implement and external command within Revit.
        
            commandData: An ExternalCommandData object which contains reference to Application and View
        
             needed by external command.
        
            Returns: The result indicates if the execution fails, succeeds, or was canceled by user. 
             If it does not
        succeed, Revit will undo any changes made by the external 
             command.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

