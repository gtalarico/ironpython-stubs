# encoding: utf-8
# module Microsoft.VisualBasic calls itself VisualBasic
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class VBCodeProvider(CodeDomProvider, IComponent, IDisposable):
    """
    Provides access to instances of the Visual Basic code generator and code compiler.
    
    VBCodeProvider()
    VBCodeProvider(providerOptions: IDictionary[str, str])
    """
    def CreateCompiler(self):
        """
        CreateCompiler(self: VBCodeProvider) -> ICodeCompiler
        
            Gets an instance of the Visual Basic code compiler.
            Returns: An instance of the Visual Basic System.CodeDom.Compiler.ICodeCompiler implementation.
        """
        pass

    def CreateGenerator(self, *__args):
        """
        CreateGenerator(self: VBCodeProvider) -> ICodeGenerator
        
            Gets an instance of the Visual Basic code generator.
            Returns: An instance of the Visual Basic System.CodeDom.Compiler.ICodeGenerator implementation.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GenerateCodeFromMember(self, member, writer, options):
        """
        GenerateCodeFromMember(self: VBCodeProvider, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified class member using the specified text writer and code generator 
             options.
        
        
            member: A System.CodeDom.CodeTypeMember to generate code for.
            writer: The System.IO.TextWriter to write to.
            options: The System.CodeDom.Compiler.CodeGeneratorOptions to use when generating the code.
        """
        pass

    def GetConverter(self, type):
        """
        GetConverter(self: VBCodeProvider, type: Type) -> TypeConverter
        
            Gets a System.ComponentModel.TypeConverter for the specified type of object.
        
            type: The type of object to retrieve a type converter for.
            Returns: A System.ComponentModel.TypeConverter for the specified type.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, providerOptions=None):
        """
        __new__(cls: type)
        __new__(cls: type, providerOptions: IDictionary[str, str])
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file name extension to use when creating source code files.

Get: FileExtension(self: VBCodeProvider) -> str

"""

    LanguageOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a language features identifier.

Get: LanguageOptions(self: VBCodeProvider) -> LanguageOptions

"""



