class RevitLinkInstance(Instance, IDisposable):
    """ Represents an instance of a RevitLinkType. """
    @staticmethod
    def Create(document, revitLinkTypeId):
        """
        Create(document: Document, revitLinkTypeId: ElementId) -> RevitLinkInstance
        
            Creates a new instance of a linked Revit project (RevitLinkType).
        
            document: The document in which the new instance should be created.
            revitLinkTypeId: The element id of the RevitLinkType.
            Returns: The newly-created RevitLinkInstance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetLinkDocument(self):
        """
        GetLinkDocument(self: RevitLinkInstance) -> Document
        
            The document associated with the Revit link.
        """
        pass

    def MoveBasePointToHostBasePoint(self, resetToOriginalRotation):
        """
        MoveBasePointToHostBasePoint(self: RevitLinkInstance, resetToOriginalRotation: bool)
            Moves this link instance so that the base point in
           the linked document is 
             aligned to the base point in the
           host document. This is a one-time movement 
             and does not
           set up any shared coordinates relationship.  If the rotation 
             angle of this link instance was changed after insertion,
           the rotation angle 
             can be preserved or reset to the original insertion angle.
        
        
            resetToOriginalRotation: Sets to true if:  restoring the original insertion angle of the link instance 
             after it is moved
           if there was a rotation \ mirror transform on the link 
             instance.  there was no a rotation \ mirror transform on the link instance.  
             Sets to false to retain the current angle of the link instance after it is 
             moved
           if there was a rotation \ mirror transform on the link instance.
        """
        pass

    def MoveOriginToHostOrigin(self, resetToOriginalRotation):
        """
        MoveOriginToHostOrigin(self: RevitLinkInstance, resetToOriginalRotation: bool)
            Moves this link instance so that the internal origin
           of the linked document 
             is aligned to the internal origin
           of the host document. This is a one-time 
             movement and does not
           set up any shared coordinates relationship.  If the 
             rotation angle of the link instance was changed after insertion,
           the 
             rotation angle can be preserved or reset to the original insertion angle.
        
        
            resetToOriginalRotation: Sets to true if:  restoring the original insertion angle of the link instance 
             after it is moved
           if there was a rotation \ mirror transform on the link 
             instance.  there was no a rotation \ mirror transform on the link instance.  
             Sets to false to retain the current angle of the link instance after it is 
             moved
           if there was a rotation \ mirror transform on the link instance.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

