class MEPFamilyConnectorInfo(MEPConnectorInfo, IDisposable):
    """ MEP family connector information. """
    def Dispose(self):
        """ Dispose(self: MEPConnectorInfo, A_0: bool) """
        pass

    def GetAssociateFamilyParameterId(self, connectorParameterId):
        """
        GetAssociateFamilyParameterId(self: MEPFamilyConnectorInfo, connectorParameterId: ElementId) -> ElementId
        
            Gets the associate family parameter id of the specified connector parameter id.
        
            connectorParameterId: connectorParameterId is defined in the family connector element.
            Returns: Returns valid ElementId if the connectorParameterId associates to one family 
             parameter; otherwise returns invalid ElementId.
        """
        pass

    def GetConnectorParameterValue(self, connectorParameterId):
        """
        GetConnectorParameterValue(self: MEPFamilyConnectorInfo, connectorParameterId: ElementId) -> ParameterValue
        
            Gets the parameter value of the specified connector parameter id.
        
            connectorParameterId: connectorParameterId is defined in the family connector element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MEPConnectorInfo, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

