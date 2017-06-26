class FrameworkRichTextComposition(FrameworkTextComposition):
    """ Represents a composition related to text input. You can use this class to find the text position of the composition or the result string. """
    CompositionEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end position of the current composition text.

Get: CompositionEnd(self: FrameworkRichTextComposition) -> TextPointer

"""

    CompositionStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start position of the current composition text.

Get: CompositionStart(self: FrameworkRichTextComposition) -> TextPointer

"""

    ResultEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end position of the result text of the text input.

Get: ResultEnd(self: FrameworkRichTextComposition) -> TextPointer

"""

    ResultStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start position of the result text of the text input.

Get: ResultStart(self: FrameworkRichTextComposition) -> TextPointer

"""


