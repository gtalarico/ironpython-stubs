class TextPointer(ContentPosition, ITextPointer):
    """ Represents a position within a System.Windows.Documents.FlowDocument or System.Windows.Controls.TextBlock. """
    def CompareTo(self, position):
        """
        CompareTo(self: TextPointer, position: TextPointer) -> int
        
            Performs an ordinal comparison between the positions specified by the current System.Windows.Documents.TextPointer and a second specified System.Windows.Documents.TextPointer.
        
            position: A System.Windows.Documents.TextPointer that specifies a position to compare to the current position.
                """
        pass

    def DeleteTextInRun(self, count):
        """
        DeleteTextInRun(self: TextPointer, count: int) -> int
        
            Deletes the specified number of characters from the position indicated by the current System.Windows.Documents.TextPointer.
        
            count: The number of characters to delete, starting at the current position. Specify a positive value to delete characters that follow the current position; specify a negative value to delete characters that 
             precede the current position.
        
            Returns: The number of characters actually deleted.
        """
        pass

    def GetAdjacentElement(self, direction):
        """
        GetAdjacentElement(self: TextPointer, direction: LogicalDirection) -> DependencyObject
        
            Returns the element, if any, that borders the current System.Windows.Documents.TextPointer in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to search for an adjacent element.
            Returns: The adjacent element in the specified direction, or null if no adjacent element exists.
        """
        pass

    def GetCharacterRect(self, direction):
        """
        GetCharacterRect(self: TextPointer, direction: LogicalDirection) -> Rect
        
            Returns a bounding box (System.Windows.Rect) for content that borders the current System.Windows.Documents.TextPointer in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to find a content bounding box.
            Returns: A bounding box for content that borders the current System.Windows.Documents.TextPointer in the specified direction, or System.Windows.Rect.Empty if current, valid layout information is unavailable.
        """
        pass

    def GetInsertionPosition(self, direction):
        """
        GetInsertionPosition(self: TextPointer, direction: LogicalDirection) -> TextPointer
        
            Returns a System.Windows.Documents.TextPointer to the closest insertion position in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to search for the closest insertion position.
            Returns: A System.Windows.Documents.TextPointer to the closest insertion position in the specified direction.
        """
        pass

    def GetLineStartPosition(self, count, actualCount=None):
        """
        GetLineStartPosition(self: TextPointer, count: int) -> (TextPointer, int)
        
            Returns a System.Windows.Documents.TextPointer to the beginning of a line that is specified relative to the current System.Windows.Documents.TextPointer, and reports how many lines were skipped.
        
            count: The number of start-of-line markers to skip when determining the line for which to return the starting position. Negative values specify preceding lines, 0 specifies the current line, and positive values 
             specify following lines.
        
            Returns: A System.Windows.Documents.TextPointer pointing to the beginning of the specified line (with the System.Windows.Documents.TextPointer.LogicalDirection set to 
             System.Windows.Documents.LogicalDirection.Forward), or to the beginning of the line closest to the specified line if the specified line is out of range.
        
        GetLineStartPosition(self: TextPointer, count: int) -> TextPointer
        
            Returns a System.Windows.Documents.TextPointer to the beginning of a line that is specified relative to the current System.Windows.Documents.TextPointer.
        
            count: The number of start-of-line markers to skip when determining the line for which to return the starting position. Negative values specify preceding lines, 0 specifies the current line, and positive values 
             specify following lines.
        
            Returns: A System.Windows.Documents.TextPointer pointing to the beginning of the specified line (with the System.Windows.Documents.TextPointer.LogicalDirection set to 
             System.Windows.Documents.LogicalDirection.Forward), or null if the specified line is out of range or otherwise cannot be located.
        """
        pass

    def GetNextContextPosition(self, direction):
        """
        GetNextContextPosition(self: TextPointer, direction: LogicalDirection) -> TextPointer
        
            Returns a pointer to the next symbol in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to search for the next symbol.
            Returns: A System.Windows.Documents.TextPointer to the next symbol in the requested direction, or null if the current System.Windows.Documents.TextPointer borders the start or end of content.
        """
        pass

    def GetNextInsertionPosition(self, direction):
        """
        GetNextInsertionPosition(self: TextPointer, direction: LogicalDirection) -> TextPointer
        
            Returns a System.Windows.Documents.TextPointer to the next insertion position in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to search for the next insertion position.
            Returns: A System.Windows.Documents.TextPointer that identifies the next insertion position in the requested direction, or null if no next insertion position can be found.
        """
        pass

    def GetOffsetToPosition(self, position):
        """
        GetOffsetToPosition(self: TextPointer, position: TextPointer) -> int
        
            Returns the count of symbols between the current System.Windows.Documents.TextPointer and a second specified System.Windows.Documents.TextPointer.
        
            position: A System.Windows.Documents.TextPointer that specifies a position to find the distance (in symbols) to.
            Returns: The relative number of symbols between the current System.Windows.Documents.TextPointer and position.  A negative value indicates that the current System.Windows.Documents.TextPointer follows the position 
             specified by position, 0 indicates that the positions are equal, and a positive value indicates that the current System.Windows.Documents.TextPointer precedes the position specified by position.
        """
        pass

    def GetPointerContext(self, direction):
        """
        GetPointerContext(self: TextPointer, direction: LogicalDirection) -> TextPointerContext
        
            Returns a category indicator for the content adjacent to the current System.Windows.Documents.TextPointer in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to determine the category for adjacent content.
            Returns: One of the System.Windows.Documents.TextPointerContext values that indicates the category for adjacent content in the specified logical direction.
        """
        pass

    def GetPositionAtOffset(self, offset, direction=None):
        """
        GetPositionAtOffset(self: TextPointer, offset: int, direction: LogicalDirection) -> TextPointer
        
            Returns a System.Windows.Documents.TextPointer to the position indicated by the specified offset, in symbols, from the beginning of the current System.Windows.Documents.TextPointer and in the specified 
             direction.
        
        
            offset: An offset, in symbols, for which to calculate and return the position.  If the offset is negative, the returned System.Windows.Documents.TextPointer precedes the current 
             System.Windows.Documents.TextPointer; otherwise, it follows.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction of the returned System.Windows.Documents.TextPointer.
            Returns: A System.Windows.Documents.TextPointer to the position indicated by the specified offset, or null if the offset extends past the end of the content.
        GetPositionAtOffset(self: TextPointer, offset: int) -> TextPointer
        
            Returns a System.Windows.Documents.TextPointer to the position indicated by the specified offset, in symbols, from the beginning of the current System.Windows.Documents.TextPointer.
        
            offset: An offset, in symbols, for which to calculate and return the position.  If the offset is negative, the position is calculated in the logical direction opposite of that indicated by the 
             System.Windows.Documents.TextPointer.LogicalDirection property.
        
            Returns: A System.Windows.Documents.TextPointer to the position indicated by the specified offset, or null if no corresponding position can be found.
        """
        pass

    def GetTextInRun(self, direction, textBuffer=None, startIndex=None, count=None):
        """
        GetTextInRun(self: TextPointer, direction: LogicalDirection) -> str
        
            Returns a string containing any text adjacent to the current System.Windows.Documents.TextPointer in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to find and return any adjacent text.
            Returns: A string containing any adjacent text in the specified logical direction, or System.String.Empty if no adjacent text can be found.
        GetTextInRun(self: TextPointer, direction: LogicalDirection, textBuffer: Array[Char], startIndex: int, count: int) -> int
        
            Copies the specified maximum number of characters from any adjacent text in the specified direction into a caller-supplied character array.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to find and copy any adjacent text.
            textBuffer: A buffer into which any text is copied.
            startIndex: An index into textBuffer at which to begin writing copied text.
            count: The maximum number of characters to copy.
            Returns: The number of characters actually copied into textBuffer.
        """
        pass

    def GetTextRunLength(self, direction):
        """
        GetTextRunLength(self: TextPointer, direction: LogicalDirection) -> int
        
            Returns the number of Unicode characters between the current System.Windows.Documents.TextPointer and the next non-text symbol, in the specified logical direction.
        
            direction: One of the System.Windows.Documents.LogicalDirection values that specifies the logical direction in which to count the number of characters.
            Returns: The number of Unicode characters between the current System.Windows.Documents.TextPointer and the next non-text symbol.  This number may be 0 if there is no adjacent text.
        """
        pass

    def InsertLineBreak(self):
        """
        InsertLineBreak(self: TextPointer) -> TextPointer
        
            Inserts a line break at the current position.
            Returns: A System.Windows.Documents.TextPointer positioned immediately after the System.Windows.Documents.LineBreak element inserted by this method.
        """
        pass

    def InsertParagraphBreak(self):
        """
        InsertParagraphBreak(self: TextPointer) -> TextPointer
        
            Inserts a paragraph break at the current position.
            Returns: A System.Windows.Documents.TextPointer to the beginning (System.Windows.Documents.TextElement.ContentStart) of the new paragraph.
        """
        pass

    def InsertTextInRun(self, textData):
        """
        InsertTextInRun(self: TextPointer, textData: str)
            Inserts the specified text into the text System.Windows.Documents.Run at the current position.
        
            textData: The text to insert.
        """
        pass

    def IsInSameDocument(self, textPosition):
        """
        IsInSameDocument(self: TextPointer, textPosition: TextPointer) -> bool
        
            Indicates whether the specified position is in the same text container as the current position.
        
            textPosition: A System.Windows.Documents.TextPointer that specifies a position to compare to the current position.
            Returns: true if textPosition indicates a position that is in the same text container as the current position; otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: TextPointer) -> str
        
            This type or member supports the Windows Presentation Foundation (WPF)�infrastructure and is not intended to be used directly from your code.
            Returns: The string that represents the object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DocumentEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Documents.TextPointer at the end of content in the text container associated with the current position.

Get: DocumentEnd(self: TextPointer) -> TextPointer

"""

    DocumentStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Documents.TextPointer at the beginning of content in the text container associated with the current position.

Get: DocumentStart(self: TextPointer) -> TextPointer

"""

    HasValidLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the text container associated with the current position has a valid (up-to-date) layout.

Get: HasValidLayout(self: TextPointer) -> bool

"""

    IsAtInsertionPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the current position is an insertion position.

Get: IsAtInsertionPosition(self: TextPointer) -> bool

"""

    IsAtLineStartPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the current position is at the beginning of a line.

Get: IsAtLineStartPosition(self: TextPointer) -> bool

"""

    LogicalDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical direction associated with the current position which is used to disambiguate content associated with the current position.

Get: LogicalDirection(self: TextPointer) -> LogicalDirection

"""

    Paragraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paragraph that scopes the current position, if any.

Get: Paragraph(self: TextPointer) -> Paragraph

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical parent that scopes the current position.

Get: Parent(self: TextPointer) -> DependencyObject

"""


