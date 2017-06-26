class FrameworkTextComposition(TextComposition):
    """ Represents a composition during the text input events of a System.Windows.Controls.TextBox. """
    def Complete(self):
        """
        Complete(self: FrameworkTextComposition)
            Finalizes the composition.
        """
        pass

    CompositionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the current composition in Unicode symbols.

Get: CompositionLength(self: FrameworkTextComposition) -> int

"""

    CompositionOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position at which the composition text occurs in the System.Windows.Controls.TextBox.

Get: CompositionOffset(self: FrameworkTextComposition) -> int

"""

    ResultLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the finalized text in Unicode symbols when the System.Windows.Input.TextCompositionManager.TextInput event occurs.

Get: ResultLength(self: FrameworkTextComposition) -> int

"""

    ResultOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset of the finalized text when the System.Windows.Input.TextCompositionManager.TextInput event occurs.

Get: ResultOffset(self: FrameworkTextComposition) -> int

"""


