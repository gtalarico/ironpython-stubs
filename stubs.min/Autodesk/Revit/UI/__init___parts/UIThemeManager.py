class UIThemeManager(object):
    """ Manager object for the UITheme class. """
    @staticmethod
    def GetThemeName(frameTheme):
        """
        GetThemeName(frameTheme: UITheme) -> str
        
            Gets the theme name for the given theme type.
        
            frameTheme: The theme.
            Returns: The name of the theme.
        """
        pass

    CurrentTheme = None
    DefaultTheme = None
    __all__ = [
        'GetThemeName',
    ]

