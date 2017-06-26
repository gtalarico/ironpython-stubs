class IMemberForcesServer(IExternalServer):
    """ Interface for the Member Forces server to implement. """
    def MemberForcesUpdate(self, data):
        """
        MemberForcesUpdate(self: IMemberForcesServer, data: MemberForcesServiceData) -> bool
        
            The server's method that will be called when Revit User clicks Member Forces 
             button in the MPP.
        
        
            data: The Moment Forces data.
            Returns: Indicates whether themember forces parameter server is executed successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

