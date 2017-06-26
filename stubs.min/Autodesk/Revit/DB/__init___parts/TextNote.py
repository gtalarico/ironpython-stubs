class TextNote(TextElement, IDisposable):
    """ A class representing text note annotations in Revit. """
    def AddLeader(self, leaderType):
        """
        AddLeader(self: TextNote, leaderType: TextNoteLeaderTypes) -> Leader
        
            Adds a leader to the text note.
        
            leaderType: Type of the leader being added.
            Returns: The newly added leader.
        """
        pass

    @staticmethod
    def Create(document, viewId, position, *__args):
        """
        Create(document: Document, viewId: ElementId, position: XYZ, text: str, options: TextNoteOptions) -> TextNote
        
            Creates a new unwrapped text note element with the given properties.
        
            document: A valid Revit document that is currently modifiable (i.e. with an open 
             transaction).
        
            viewId: Id of the graphic view in which the note is to be created.
            position: A model position of the new note.
           Note that the position's relation to the 
             text's bounding box depends on the requested text alignment
           (set via the 
             Options argument). It will be the box' top-left corner for a left-aligned text,
             
           the top-right corner for a right-aligned text, and middle-top point if the 
             text is to be centered.
        
            text: Text to populate the text note with.
            options: Options to control behavior and appearance of the text note.
            Returns: The newly created text note.
        Create(document: Document, viewId: ElementId, position: XYZ, text: str, typeId: ElementId) -> TextNote
        
            Creates a new unwrapped TextNote element with the given properties.
        
            document: A valid Revit document that is currently modifiable (i.e. with an open 
             transaction).
        
            viewId: Id of the graphic view in which the note is to be created.
            position: A model position of the new note.
           For a left-aligned text (default), the 
             origin is set at the top-left corner of the note's bounding box.
        
            text: Text to populate the text note with.
            typeId: Id of the text type to use for the new text note.
            Returns: The newly created text note.
        Create(document: Document, viewId: ElementId, position: XYZ, width: float, text: str, options: TextNoteOptions) -> TextNote
        
            Creates a new line-wrapping text note element of the given width and properties.
        
            document: A valid Revit document that is currently modifiable (i.e. with an open 
             transaction).
        
            viewId: Id of the graphic view in which the note is to be created.
            position: A model position of the new note.
           Note that the position's relation to the 
             text's bounding box depends on the requested text alignment
           (set via the 
             Options argument). It will be the box' top-left corner for a left-aligned text,
             
           the top-right corner for a right-aligned text, and middle-top point if the 
             text is to be centered.
        
            width: Width [ft] of the text in paper space (i.e. as it is measured when printed.)
          
              If a line of text is longer than the given specified Width, the text will be 
             automatically wrapped.
           If a a zero Width is supplied then this method will 
             create an unwrapped text note element.
        
            text: Text to populate the text note with.
            options: Options to control behavior and appearance of the text note.
            Returns: The newly created text note.
        Create(document: Document, viewId: ElementId, position: XYZ, width: float, text: str, typeId: ElementId) -> TextNote
        
            Creates a new line-wrapping text note element of the given width and properties.
        
            document: A valid Revit document that is currently modifiable (i.e. with an open 
             transaction).
        
            viewId: Id of the graphic view in which the note is to be created.
            position: A model position of the new note.
           For a left-aligned text (default), the 
             origin is set at the top-left corner of the note's bounding box.
        
            width: Width [ft] of the text in paper space (i.e. as it is measured when printed.)
          
              If a line of text is longer than the specified Width, the text will be 
             automatically wrapped.
           If a a zero Width is supplied then this method will 
             create an unwrapped text note element.
        
            text: Text to populate the text note with.
            typeId: Id of the text type to use for the new text note.
            Returns: The newly created text note.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFormattedText(self):
        """
        GetFormattedText(self: TextNote) -> FormattedText
        
            Returns an object that contains text and associated formatting of this note.
            Returns: The object that contains the text and associated formatting of of the text in 
             this text note.
        """
        pass

    def GetLeaders(self):
        """
        GetLeaders(self: TextNote) -> IList[Leader]
        
            Returns a collection of leaders currently attached to the text note.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveLeaders(self):
        """
        RemoveLeaders(self: TextNote)
            Removes all leaders currently attached to the text note.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetFormattedText(self, formattedText):
        """
        SetFormattedText(self: TextNote, formattedText: FormattedText)
            Sets the text and associated formatting of the text of in this text note with
         
               a given FormattedText object.
        
        
            formattedText: The FormattedText object containing the text and associated formatting of the 
             text.
        """
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

    LeaderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of leader objects currently attached to the text note.

Get: LeaderCount(self: TextNote) -> int

"""

    LeaderLeftAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Attachment position of leaders on the left side of the text note.

Get: LeaderLeftAttachment(self: TextNote) -> LeaderAtachement

Set: LeaderLeftAttachment(self: TextNote) = value
"""

    LeaderRightAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Attachment position of leaders on the right side of the text note.

Get: LeaderRightAttachment(self: TextNote) -> LeaderAtachement

Set: LeaderRightAttachment(self: TextNote) = value
"""

    TextNoteType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access the type of the TextNote object.

Get: TextNoteType(self: TextNote) -> TextNoteType

Set: TextNoteType(self: TextNote) = value
"""


