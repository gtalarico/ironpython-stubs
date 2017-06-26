class ITransactionFinalizer:
    """
    An interface that may be used to perform a custom action at the end of a transaction.
       A method of the interface will be called when a transaction is either committed or rolled back.
    """
    def OnCommitted(self, document, strTransactionName):
        """
        OnCommitted(self: ITransactionFinalizer, document: Document, strTransactionName: str)
            This method is called at the end of committing a transaction
        
            document: The document associated with the transaction
            strTransactionName: The transaction's name
        """
        pass

    def OnRolledBack(self, document, strTransactionName):
        """
        OnRolledBack(self: ITransactionFinalizer, document: Document, strTransactionName: str)
            This method is called at the end of rolling back a transaction
        
            document: The document associated with the transaction
            strTransactionName: The transaction's name
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

