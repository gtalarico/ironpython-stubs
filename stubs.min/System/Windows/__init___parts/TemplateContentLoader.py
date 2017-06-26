class TemplateContentLoader(XamlDeferringLoader):
    """
    Implements System.Xaml.XamlDeferringLoader in order to defer loading of the XAML content that is defined for a template in WPF XAML.
    
    TemplateContentLoader()
    """
    def Load(self, xamlReader, serviceProvider):
        """
        Load(self: TemplateContentLoader, xamlReader: XamlReader, serviceProvider: IServiceProvider) -> object
        
            Loads XAML content in a deferred mode, based on a System.Xaml.XamlReader and certain required services from a service provider.
        
            xamlReader: The initiating reader that is then returned on calls to System.Windows.TemplateContentLoader.Save(System.Object,System.IServiceProvider).
            serviceProvider: Service provider for required services.
            Returns: The root object for the node stream of the input System.Xaml.XamlReader. Specifically, this is a System.Windows.TemplateContent instance.
        """
        pass

    def Save(self, value, serviceProvider):
        """
        Save(self: TemplateContentLoader, value: object, serviceProvider: IServiceProvider) -> XamlReader
        
            Do not use; always throws an exception. See Remarks.
        
            value: The input value to commit for deferred loading.
            serviceProvider: Service provider for required services.
            Returns: Always throws an exception. See Remarks.
        """
        pass

