class AssemblyLoadEventArgs(EventArgs):
    """
    Provides data for the System.AppDomain.AssemblyLoad event.
    
    AssemblyLoadEventArgs(loadedAssembly: Assembly)
    """
    @staticmethod # known case of __new__
    def __new__(self, loadedAssembly):
        """ __new__(cls: type, loadedAssembly: Assembly) """
        pass

    LoadedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Reflection.Assembly that represents the currently loaded assembly.

Get: LoadedAssembly(self: AssemblyLoadEventArgs) -> Assembly

"""


