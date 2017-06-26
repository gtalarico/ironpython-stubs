class MaskInputRejectedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.MaskedTextBox.MaskInputRejected event.
    
    MaskInputRejectedEventArgs(position: int, rejectionHint: MaskedTextResultHint)
    """
    @staticmethod # known case of __new__
    def __new__(self, position, rejectionHint):
        """ __new__(cls: type, position: int, rejectionHint: MaskedTextResultHint) """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position in the mask corresponding to the invalid input character.

Get: Position(self: MaskInputRejectedEventArgs) -> int

"""

    RejectionHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerated value that describes why the input character was rejected.

Get: RejectionHint(self: MaskInputRejectedEventArgs) -> MaskedTextResultHint

"""


