class FormattedTextRun(object, IDisposable):
    """ A structure that defines a single run of a formatted text. """
    def Dispose(self):
        """ Dispose(self: FormattedTextRun) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FormattedTextRun, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BaselineStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the style of the text as related to the baseline position.

Get: BaselineStyle(self: FormattedTextRun) -> TextBaselineStyle

"""

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this text run uses Bold text.

Get: Bold(self: FormattedTextRun) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FormattedTextRun) -> bool

"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this text run uses Italic text.

Get: Italic(self: FormattedTextRun) -> bool

"""

    ListStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the style of a paragraph if the paragraph is a list.

Get: ListStyle(self: FormattedTextRun) -> TextListStyle

"""

    NewLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this text run starts on a new line.

Get: NewLine(self: FormattedTextRun) -> bool

"""

    NewParagraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this text run starts a new paragraph.

Get: NewParagraph(self: FormattedTextRun) -> bool

"""

    TabNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a text run that starts at a tab stop, this value indicates the number of the tab stop.

Get: TabNumber(self: FormattedTextRun) -> int

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text segment in this text run.

Get: Text(self: FormattedTextRun) -> str

"""

    Underlined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this text run uses Underlined text.

Get: Underlined(self: FormattedTextRun) -> bool

"""


