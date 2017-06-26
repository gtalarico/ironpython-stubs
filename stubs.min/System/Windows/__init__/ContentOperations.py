class ContentOperations(object):
    """ Provides static utility methods for getting or setting the position of a System.Windows.ContentElement in an element tree. """
    @staticmethod
    def GetParent(reference):
        """
        GetParent(reference: ContentElement) -> DependencyObject
        
            Gets the parent element of the specified System.Windows.ContentElement.
        
            reference: The System.Windows.ContentElement to get the parent from.
            Returns: The parent element in the current tree.
        """
        pass

    @staticmethod
    def SetParent(reference, parent):
        """
        SetParent(reference: ContentElement, parent: DependencyObject)
            Sets the parent element of the provided System.Windows.ContentElement.
        
            reference: The System.Windows.ContentElement to reparent.
            parent: The new parent element.
        """
        pass

    __all__ = [
        'GetParent',
        'SetParent',
    ]

