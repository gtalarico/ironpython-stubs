class IExternalResourceUIServer(IExternalServer):
    """ The interface used to provide custom handling of UI operations related to external resources. """
    def GetDBServerId(self):
        """
        GetDBServerId(self: IExternalResourceUIServer) -> Guid
        
            Implement this method to return the id of the server which is associated with 
             this UI server.
        
            Returns: The id of the associated DB server.
        """
        pass

    def HandleBrowseResult(self, resultType, browsingItemPath):
        """
        HandleBrowseResult(self: IExternalResourceUIServer, resultType: ExternalResourceUIBrowseResultType, browsingItemPath: str)
            Implement this method to handle browsing external resources operation result.
        
            resultType: The result of browsing operation.
            browsingItemPath: The absolute path of item which is browsing.
        """
        pass

    def HandleLoadResourceResults(self, document, loadData):
        """ HandleLoadResourceResults(self: IExternalResourceUIServer, document: Document, loadData: IList[ExternalResourceLoadData]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

