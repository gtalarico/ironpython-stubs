class IDataConversionMonitor:
    """
    A base class for an application-specific logger. It should be used to track errors during conversion and/or , track conversion progress, cancel a conversion process if necessary.
       Implementing a logger class is optional, but highly recommended for all but most basic data converters.
       The base class is UI- and language-independent. It is up to the using app to implement UI. Language-specifc data may be used to communicate information to application users.
       English should be used to communicate data of interest to Revit development.
    """
    def GetVerbosity(self):
        """
        GetVerbosity(self: IDataConversionMonitor) -> DataExchangeMessageVerbosity
        
            Reports requested verbosity level
        """
        pass

    def ProcessMessage(self, messageId, messageSeverity, entityIds):
        """ ProcessMessage(self: IDataConversionMonitor, messageId: DataExchangeMessageId, messageSeverity: DataExchangeMessageSeverity, entityIds: IList[str]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

