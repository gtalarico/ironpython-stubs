class PresentationTraceSources(object):
    """ Provides debug tracing support that is specifically targeted for Windows Presentation Foundation (WPF) applications. """
    @staticmethod
    def GetTraceLevel(element):
        """
        GetTraceLevel(element: object) -> PresentationTraceLevel
        
            Gets the value of the System.Diagnostics.PresentationTraceSources.TraceLevel�attached property for a specified element.
        
            element: The element from which the property value is read.
            Returns: The System.Diagnostics.PresentationTraceSources.TraceLevel property value for the element.
        """
        pass

    @staticmethod
    def Refresh():
        """
        Refresh()
            Refreshes trace sources, by forcing the app.config file to be re-read.
        """
        pass

    @staticmethod
    def SetTraceLevel(element, traceLevel):
        """
        SetTraceLevel(element: object, traceLevel: PresentationTraceLevel)
            Sets the value of the System.Diagnostics.PresentationTraceSources.TraceLevel�attached property to a specified element.
        
            element: The element to which the attached property is written.
            traceLevel: The needed System.Diagnostics.PresentationTraceLevel value.
        """
        pass

    AnimationSource = None
    DataBindingSource = None
    DependencyPropertySource = None
    DocumentsSource = None
    FreezableSource = None
    HwndHostSource = None
    MarkupSource = None
    NameScopeSource = None
    ResourceDictionarySource = None
    RoutedEventSource = None
    ShellSource = None
    TraceLevelProperty = None
    __all__ = [
        'GetTraceLevel',
        'Refresh',
        'SetTraceLevel',
        'TraceLevelProperty',
    ]

