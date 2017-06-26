class CharacterMetrics(object):
    """
    Represents the metrics used to lay out a character in a device font.
    
    CharacterMetrics()
    CharacterMetrics(metrics: str)
    """
    def Equals(self, obj):
        """
        Equals(self: CharacterMetrics, obj: object) -> bool
        
            Determines whether the specified System.Windows.Media.CharacterMetrics object is equal to the current System.Windows.Media.CharacterMetrics object.
        
            obj: The System.Windows.Media.CharacterMetrics object to compare to the current System.Windows.Media.CharacterMetrics object.
            Returns: true if the objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CharacterMetrics) -> int
        
            Creates a hash code from the metric values of the System.Windows.Media.CharacterMetrics object.
            Returns: A value of type System.Int32.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, metrics=None):
        """
        __new__(cls: type)
        __new__(cls: type, metrics: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Baseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the baseline value for the character.

Get: Baseline(self: CharacterMetrics) -> float

"""

    BlackBoxHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the black box for the character.

Get: BlackBoxHeight(self: CharacterMetrics) -> float

"""

    BlackBoxWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the black box for the character.

Get: BlackBoxWidth(self: CharacterMetrics) -> float

"""

    BottomSideBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the recommended white space below the black box.

Get: BottomSideBearing(self: CharacterMetrics) -> float

"""

    LeftSideBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the recommended white space to the left of the black box.

Get: LeftSideBearing(self: CharacterMetrics) -> float

"""

    Metrics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a comma-delimited string representing metric values.

Get: Metrics(self: CharacterMetrics) -> str

Set: Metrics(self: CharacterMetrics) = value
"""

    RightSideBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the recommended white space to the right of the black box.

Get: RightSideBearing(self: CharacterMetrics) -> float

"""

    TopSideBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the recommended white space above the black box.

Get: TopSideBearing(self: CharacterMetrics) -> float

"""


