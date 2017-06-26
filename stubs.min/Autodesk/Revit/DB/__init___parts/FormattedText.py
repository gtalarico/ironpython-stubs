class FormattedText(object, IDisposable):
    """
    FormattedText is used to create, edit and format text in a Autodesk.Revit.DB.TextNote
       or to query the text and format properties of a Autodesk.Revit.DB.TextNode
    
    FormattedText(plainText: str)
    FormattedText()
    """
    def AsTextRange(self):
        """
        AsTextRange(self: FormattedText) -> TextRange
        
            Returns a Autodesk.Revit.DB.TextRange object that represents the entire text.
            Returns: The Autodesk.Revit.DB.TextRange object that represents the entire text.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FormattedText) """
        pass

    def Find(self, searchString, startIndex, matchCase, matchWholeWord):
        """
        Find(self: FormattedText, searchString: str, startIndex: int, matchCase: bool, matchWholeWord: bool) -> TextRange
        
            Returns a text range identifying the first occurrence of the given string 
             within the text,
           starting from a given index.
        
        
            searchString: The text to search for.
            startIndex: The start index to search within the text.
            matchCase: True if the case must match when searching the formatted text, false to search 
             in a case-insensitive manner.
        
            matchWholeWord: True if the match must be a whole word when searching the formatted text, false 
             otherwise.
        
            Returns: The text range identified.
        """
        pass

    def GetAllCapsStatus(self, textRange=None):
        """
        GetAllCapsStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are in all caps.
        
        
            textRange: The given text range.
            Returns: The format status of all caps on characters Autodesk.Revit.DB.FormatStatus.
        GetAllCapsStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are in all caps.
        
            Returns: The format status of all caps on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def GetBoldStatus(self, textRange=None):
        """
        GetBoldStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are bold.
        
        
            textRange: The given text range.
            Returns: The format status of bold on characters Autodesk.Revit.DB.FormatStatus.
        GetBoldStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are bold.
        
            Returns: The format status of bold on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def GetIndentLevel(self, textRange):
        """
        GetIndentLevel(self: FormattedText, textRange: TextRange) -> int
        
            Returns the indent level of the paragraphs in the text range.
        
            textRange: The given text range.
            Returns: The indentation level of the paragraphs in the range.
        """
        pass

    def GetItalicStatus(self, textRange=None):
        """
        GetItalicStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are italic.
        
        
            textRange: The given text range.
            Returns: The format status of italic on characters Autodesk.Revit.DB.FormatStatus.
        GetItalicStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are italic.
        
            Returns: The format status of italic on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def GetListStartNumber(self, textRange):
        """
        GetListStartNumber(self: FormattedText, textRange: TextRange) -> int
        
            Returns the list start number of the paragraphs in a given text range.
        
            textRange: The given text range.
            Returns: The list start number of the text range.
        """
        pass

    def GetListType(self, textRange):
        """
        GetListType(self: FormattedText, textRange: TextRange) -> ListType
        
            Returns the Autodesk.Revit.DB.ListType of a paragraph.
        
            textRange: The given text range.
            Returns: The Autodesk.Revit.DB.ListType of the paragraph.
        """
        pass

    def GetMaximumIndentLevel(self):
        """
        GetMaximumIndentLevel(self: FormattedText) -> int
        
            Returns the maximum allowed indent level
        """
        pass

    def GetMaximumListStartNumber(self):
        """
        GetMaximumListStartNumber(self: FormattedText) -> int
        
            Returns the maximum allowed list start number.
        """
        pass

    def GetMinimumListStartNumber(self):
        """
        GetMinimumListStartNumber(self: FormattedText) -> int
        
            Returns the minumum allowed list start number.
        """
        pass

    def GetPlainText(self, textRange=None):
        """
        GetPlainText(self: FormattedText) -> str
        
            Returns the entire text in a plain text form.
            Returns: The entire text in a plain text form.
        GetPlainText(self: FormattedText, textRange: TextRange) -> str
        
            Returns a substring of the text in a plain text form. The start and end of the 
             substring is identified
           by a given Autodesk.Revit.DB.TextRange.
        
        
            textRange: The given Autodesk.Revit.DB.TextRange.
            Returns: The substring of the text in a plain text form.
        """
        pass

    def GetSubscriptStatus(self, textRange=None):
        """
        GetSubscriptStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are subscripted.
        
        
            textRange: The given text range.
            Returns: The format status of subscript on characters Autodesk.Revit.DB.FormatStatus.
        GetSubscriptStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are subscripted.
        
            Returns: The format status of subscript on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def GetSuperscriptStatus(self, textRange=None):
        """
        GetSuperscriptStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are superscripted.
        
        
            textRange: The given text range.
            Returns: The format status of superscript on characters Autodesk.Revit.DB.FormatStatus.
        GetSuperscriptStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are superscripted.
        
            Returns: The format status of superscript on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def GetUnderlineStatus(self, textRange=None):
        """
        GetUnderlineStatus(self: FormattedText, textRange: TextRange) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             set of characters in a given text range are underlined.
        
        
            textRange: The given text range.
            Returns: The format status of underline on characters Autodesk.Revit.DB.FormatStatus.
        GetUnderlineStatus(self: FormattedText) -> FormatStatus
        
            Returns whether Autodesk.Revit.DB.FormatStatus.All, 
             Autodesk.Revit.DB.FormatStatus.None or a Autodesk.Revit.DB.FormatStatus.Mixed 
             of characters in the entire text are underlined.
        
            Returns: The format status of underline on characters Autodesk.Revit.DB.FormatStatus.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FormattedText, disposing: bool) """
        pass

    def SetAllCapsStatus(self, *__args):
        """
        SetAllCapsStatus(self: FormattedText, textRange: TextRange, isAllCaps: bool)
            Sets the characters in a given text range to be in all caps or not.
        
            textRange: The given text range.
            isAllCaps: The desired all caps status of characters in the given text range.
           True 
             will render all characters in all caps.
           False will revert the characters 
             back to their original mixed case.
        
        SetAllCapsStatus(self: FormattedText, isAllCaps: bool)
            Sets the characters in the entire text to be in all caps or not.
        
            isAllCaps: The desired all caps status of characters in the entire text.
           True to set 
             all capped, false to set not all capped.
        """
        pass

    def SetBoldStatus(self, *__args):
        """
        SetBoldStatus(self: FormattedText, textRange: TextRange, isBold: bool)
            Sets the characters in a given text range to be bold or not bold.
        
            textRange: The given text range.
            isBold: The desired bold status of characters in the given text range.
           True to set 
             bold, false to set not bold.
        
        SetBoldStatus(self: FormattedText, isBold: bool)
            Sets the characters in the entire text to be bold or not bold.
        
            isBold: The desired bold status of characters in the entire text.
           True to set bold, 
             false to set not bold.
        """
        pass

    def SetIndentLevel(self, textRange, level):
        """
        SetIndentLevel(self: FormattedText, textRange: TextRange, level: int)
            Sets the number of tab stops that the paragraph should be indented.
        
            textRange: The given text range.
            level: The level set on the paragraph.
        """
        pass

    def SetItalicStatus(self, *__args):
        """
        SetItalicStatus(self: FormattedText, textRange: TextRange, isItalic: bool)
            Sets the characters in a given text range to be italic or not italic.
        
            textRange: The given text range.
            isItalic: The desired italic status of characters in the given text range.
           True to 
             set italic, false to set not italic.
        
        SetItalicStatus(self: FormattedText, isItalic: bool)
            Sets the characters in the entire text to be italic or not italic.
        
            isItalic: The desired italic status of characters in the entire text.
           True to set 
             italic, false to set not italic.
        """
        pass

    def SetListStartNumber(self, textRange, value):
        """
        SetListStartNumber(self: FormattedText, textRange: TextRange, value: int)
            Sets the list start number on the paragraphs in a given text range.
        
            textRange: The given text range.
            value: The list start number to be set on the text range.
        """
        pass

    def SetListType(self, textRange, listType):
        """
        SetListType(self: FormattedText, textRange: TextRange, listType: ListType)
            Sets the Autodesk.Revit.DB.ListType of a paragraph.
        
            textRange: The given text range.
            listType: The Autodesk.Revit.DB.ListType to set on the paragraph.
        """
        pass

    def SetPlainText(self, *__args):
        """
        SetPlainText(self: FormattedText, plainText: str)
            Sets the entire text with the given text in a plain text form.
        
            plainText: The given text in a plain text form.
        SetPlainText(self: FormattedText, textRange: TextRange, plainText: str)
            Sets the text with the given text in a plain text form in a range.
        
            textRange: The given text range.
            plainText: The given text in a plain text form.
        """
        pass

    def SetSubscriptStatus(self, *__args):
        """
        SetSubscriptStatus(self: FormattedText, textRange: TextRange, isSubscript: bool)
            Sets the characters in a given text range to be subscript or not subscript.
        
            textRange: The given text range.
            isSubscript: The desired subscript status of characters in the given text range.
           True to 
             set subscript, false to set not subscript.
        
        SetSubscriptStatus(self: FormattedText, isSubscript: bool)
            Sets the characters in the entire text to be subscript or not subscript.
        
            isSubscript: The desired subscript status of characters in the entire text.
           True to set 
             subscript, false to set not subscript.
        """
        pass

    def SetSuperscriptStatus(self, *__args):
        """
        SetSuperscriptStatus(self: FormattedText, textRange: TextRange, isSuperscript: bool)
            Sets the characters in a given text range to be superscript or not superscript.
        
            textRange: The given text range.
            isSuperscript: The desired superscript status of characters in the given text range.
           True 
             to set superscript, false to set not superscript.
        
        SetSuperscriptStatus(self: FormattedText, isSuperscript: bool)
            Sets the characters in the entire text to be superscript or not superscript.
        
            isSuperscript: The desired superscript status of characters in the entire text.
           True to 
             set superscript, false to set not superscript.
        """
        pass

    def SetUnderlineStatus(self, *__args):
        """
        SetUnderlineStatus(self: FormattedText, textRange: TextRange, isUnderlined: bool)
            Sets the characters in a given text range to be underlined or not underlined.
        
            textRange: The given text range.
            isUnderlined: The desired underline status of characters in the given text range.
           True to 
             set underlined, false to set not underlined.
        
        SetUnderlineStatus(self: FormattedText, isUnderlined: bool)
            Sets the characters in the entire text to be underlined or not underlined.
        
            isUnderlined: The desired underline status of characters in the entire text.
           True to set 
             underlined, false to set not underlined.
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

    @staticmethod # known case of __new__
    def __new__(self, plainText=None):
        """
        __new__(cls: type, plainText: str)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FormattedText) -> bool

"""


