class ICodeCheckingParameterServer(IExternalServer):
    """ Interface for the code checking parameter server to implement. """
    def PerformCodeChecking(self, data):
        """
        PerformCodeChecking(self: ICodeCheckingParameterServer, data: CodeCheckingParameterServiceData) -> bool
        
            The server's method that will be called when Revit User clicks the Code 
             Checking parameter's button from the properties palette.
        
        
            data: The Code Checking data.
            Returns: Indicates whether the code checking parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

