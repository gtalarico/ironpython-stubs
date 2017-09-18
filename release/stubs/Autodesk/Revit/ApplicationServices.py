# encoding: utf-8
# module Autodesk.Revit.ApplicationServices calls itself ApplicationServices
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Application(object, IDisposable):
    """ Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings. """
    def CopyModel(self, sourceModelPath, destFilePath, overwrite):
        """
        CopyModel(self: Application, sourceModelPath: ModelPath, destFilePath: str, overwrite: bool)
            Copies an existing model to a new file. Overwriting a file of the same name is 
             allowed.
        
        
            sourceModelPath: The path of the file-based or server-based source model.
            destFilePath: The path of the destination file.
            overwrite: True if the destination file can be overwritten; otherwise, false.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Application) """
        pass

    def ExtractPartAtomFromFamilyFile(self, familyFilePath, xmlFilePath):
        """
        ExtractPartAtomFromFamilyFile(self: Application, familyFilePath: str, xmlFilePath: str)
            Writes a PartAtom XML from the contents of a family file.
        
            familyFilePath: The family file to be processed.
            xmlFilePath: The xml file to be saved.
        """
        pass

    @staticmethod
    def GetFailureDefinitionRegistry():
        """
        GetFailureDefinitionRegistry() -> FailureDefinitionRegistry
        
            Returns the instance of FailureDefinitionRegistry.
            Returns: The instance of FailureDefinitionRegistry.
        """
        pass

    def GetLibraryPaths(self):
        """
        GetLibraryPaths(self: Application) -> IDictionary[str, str]
        
            Returns path information identifying where Revit searches for content.
            Returns: The map of library paths.
        """
        pass

    def GetRevitServerNetworkHosts(self):
        """
        GetRevitServerNetworkHosts(self: Application) -> IList[str]
        
            Gets the list of all Revit Server Network hosts in current session.
            Returns: An array of names of all Revit Server Network hosts in current session.
        """
        pass

    def GetWorksharingCentralGUID(self, serverModelPath):
        """
        GetWorksharingCentralGUID(self: Application, serverModelPath: ServerPath) -> Guid
        
            Gets the worksharing central GUID of the given server-based model.
        
            serverModelPath: The server-based model path.
            Returns: The worksharing central GUID.
        """
        pass

    @staticmethod
    def IsValidThickness(thickness):
        """
        IsValidThickness(thickness: float) -> bool
        
            Checks if the input value is valid to be supplied as a thickness (for an 
             extrusion, or blend, or wall layer, or similar geometric construct).
        
        
            thickness: The input value.
            Returns: True if the input value is valid for thickness; false otherwise.
        """
        pass

    def NewFamilyDocument(self, templateFileName):
        """
        NewFamilyDocument(self: Application, templateFileName: str) -> Document
        
            New family document, including family, titleblock, and annotation symbol
        
            templateFileName: The template file name.
        """
        pass

    def NewProjectDocument(self, *__args):
        """
        NewProjectDocument(self: Application, templateFileName: str) -> Document
        
            New project document
        
            templateFileName: The template file name.
        NewProjectDocument(self: Application, unitSystem: UnitSystem) -> Document
        
            Creates a new project document with no template file specified.
        
            unitSystem: The unit system used for the new document.
            Returns: The newly created document.
        """
        pass

    def NewProjectTemplateDocument(self, templateFilename):
        """
        NewProjectTemplateDocument(self: Application, templateFilename: str) -> Document
        
            New project template document
        
            templateFilename: The template file name.
        """
        pass

    def OpenBuildingComponentDocument(self, fileName):
        """
        OpenBuildingComponentDocument(self: Application, fileName: str) -> Document
        
            Opens a Building Component document from disk.
        
            fileName: The Building Component file to be opened.
        """
        pass

    def OpenDocumentFile(self, *__args):
        """
        OpenDocumentFile(self: Application, modelPath: ModelPath, openOptions: OpenOptions) -> Document
        
            Opens a document from disk.
        
            modelPath: The file to be opened.
            openOptions: Options for opening the file.
            Returns: The opened document.
        OpenDocumentFile(self: Application, fileName: str) -> Document
        
            Opens a document from disk.
        
            fileName: The file to be opened.
            Returns: The opened document.
        """
        pass

    def OpenIFCDocument(self, fileName, importOptions=None):
        """
        OpenIFCDocument(self: Application, fileName: str) -> Document
        
            Opens an IFC document from disk using default options.
        
            fileName: The IFC file to be opened.
            Returns: The newly created document containing the IFC file.
        OpenIFCDocument(self: Application, fileName: str, importOptions: IFCImportOptions) -> Document
        
            Opens an IFC document from disk using custom options.
        
            fileName: The IFC file to be opened.
            importOptions: The options for this import.
            Returns: The newly created document containing the IFC file.
        """
        pass

    def OpenSharedParameterFile(self):
        """
        OpenSharedParameterFile(self: Application) -> DefinitionFile
        
            Enables access to shared parameter groups and definitions that are maintained 
             on disk.
        
            Returns: An object that represents a shared parameters file that exists on disk. Returns 
             ll if the file does not exist.
        """
        pass

    def PurgeReleasedAPIObjects(self):
        """
        PurgeReleasedAPIObjects(self: Application)
            Explicitly purges all API objects that have been released but are still 
             awaiting to be finalized
        """
        pass

    @staticmethod
    def RegisterFailuresProcessor(processor):
        """
        RegisterFailuresProcessor(processor: IFailuresProcessor)
            Registers Revit application-wide instance of Failures Processor.
        
            processor: Instance of Failures Processor to be used by the Revit Application.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Application, disposing: bool) """
        pass

    def SetLibraryPaths(self, paths):
        """ SetLibraryPaths(self: Application, paths: IDictionary[str, str]) """
        pass

    def UpdateRenderAppearanceLibrary(self):
        """
        UpdateRenderAppearanceLibrary(self: Application)
            Updates the stored render appearance library, giving the Revit session access 
             to any new RPC content.
        """
        pass

    def WriteJournalComment(self, comment, timeStamp):
        """
        WriteJournalComment(self: Application, comment: str, timeStamp: bool)
            Writes a comment to the Revit journal file.
        
            comment: Text for journal comment.
            timeStamp: If a time stamp should be included in the journal comment.
        """
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

    ActiveAddInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the Id of the currently running external application.

Get: ActiveAddInId(self: Application) -> AddInId

"""

    AllowNavigationDuringRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the navigation during redraw is enabled, and enable or disable it.

Get: AllowNavigationDuringRedraw(self: Application) -> bool

Set: AllowNavigationDuringRedraw(self: Application) = value
"""

    AllUsersAddinsLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The folder location for .addin files for all users.

Get: AllUsersAddinsLocation(self: Application) -> str

"""

    AngleTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Angle tolerance.

Get: AngleTolerance(self: Application) -> float

"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The background color to use for model views in this session.

Get: BackgroundColor(self: Application) -> Color

Set: BackgroundColor(self: Application) = value
"""

    Cities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a set of all the known city locations within Revit.

Get: Cities(self: Application) -> CitySet

"""

    Create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides an object that can be used to create new instances of Autodesk Revit API objects.

Get: Create(self: Application) -> Application

"""

    CurrentRevitServerAccelerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current Revit Server accelerator.

Get: CurrentRevitServerAccelerator(self: Application) -> str

Set: CurrentRevitServerAccelerator(self: Application) = value
"""

    CurrentUserAddinsLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The folder location for .addin files for the current user.

Get: CurrentUserAddinsLocation(self: Application) -> str

"""

    DefaultIFCProjectTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path to the default template file for new IFC project documents.
   It may be empty, in which case the DefaultProjectTemplate should be used.

Get: DefaultIFCProjectTemplate(self: Application) -> str

"""

    DefaultProjectTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path to the default template file for new project documents.

Get: DefaultProjectTemplate(self: Application) -> str

"""

    DefaultViewDiscipline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view discipline that will be applied to new views by default.

Get: DefaultViewDiscipline(self: Application) -> ViewDiscipline

Set: DefaultViewDiscipline(self: Application) = value
"""

    Documents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a set of documents within Revit.

Get: Documents(self: Application) -> DocumentSet

"""

    ExportIFCCategoryTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path to the file that defines Revit category to IFC entity mappings for IFC export.

Get: ExportIFCCategoryTable(self: Application) -> str

"""

    FamilyTemplatePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default path for family template files.

Get: FamilyTemplatePath(self: Application) -> str

"""

    ImportIFCCategoryTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path to the file that defines IFC entity to Revit category mappings for IFC import.

Get: ImportIFCCategoryTable(self: Application) -> str

"""

    IsArchitectureEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the architecture discipline is enabled, and enable or disable it.

Get: IsArchitectureEnabled(self: Application) -> bool

Set: IsArchitectureEnabled(self: Application) = value
"""

    IsElectricalAnalysisEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not electrical analysis is enabled, and enable or disable it.

Get: IsElectricalAnalysisEnabled(self: Application) -> bool

Set: IsElectricalAnalysisEnabled(self: Application) = value
"""

    IsElectricalEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the electrical discipline is enabled, and enable or disable it.

Get: IsElectricalEnabled(self: Application) -> bool

Set: IsElectricalEnabled(self: Application) = value
"""

    IsEnergyAnalysisEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not energy analysis is enabled, and enable or disable it.

Get: IsEnergyAnalysisEnabled(self: Application) -> bool

Set: IsEnergyAnalysisEnabled(self: Application) = value
"""

    IsMassingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the massing and site tools are enabled, and enable or disable them.

Get: IsMassingEnabled(self: Application) -> bool

Set: IsMassingEnabled(self: Application) = value
"""

    IsMechanicalAnalysisEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not mechanical analysis is enabled, and enable or disable it.

Get: IsMechanicalAnalysisEnabled(self: Application) -> bool

Set: IsMechanicalAnalysisEnabled(self: Application) = value
"""

    IsMechanicalEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the mechanical discipline is enabled, and enable or disable it.

Get: IsMechanicalEnabled(self: Application) -> bool

Set: IsMechanicalEnabled(self: Application) = value
"""

    IsPipingAnalysisEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not piping analysis is enabled, and enable or disable it.

Get: IsPipingAnalysisEnabled(self: Application) -> bool

Set: IsPipingAnalysisEnabled(self: Application) = value
"""

    IsPipingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the piping discipline is enabled, and enable or disable it.

Get: IsPipingEnabled(self: Application) -> bool

Set: IsPipingEnabled(self: Application) = value
"""

    IsStructuralAnalysisEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the structural analysis is enabled, and enable or disable it.

Get: IsStructuralAnalysisEnabled(self: Application) -> bool

Set: IsStructuralAnalysisEnabled(self: Application) = value
"""

    IsStructureEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not the structure discipline is enabled, and enable or disable it.

Get: IsStructureEnabled(self: Application) -> bool

Set: IsStructureEnabled(self: Application) = value
"""

    IsSubscriptionUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this version of Revit is a subscription update.

Get: IsSubscriptionUpdate(self: Application) -> bool

"""

    IsSystemsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks whether or not any systems disciplines (mechanical, electrical, or piping) are enabled.

Get: IsSystemsEnabled(self: Application) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Application) -> bool

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The language used in the current session of Revit.

Get: Language(self: Application) -> LanguageType

"""

    LoginUserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user id of the user currently logged in. The user id will be empty
   if the user is not logged in.

Get: LoginUserId(self: Application) -> str

"""

    PointCloudsRootPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Root path for point cloud files.

Get: PointCloudsRootPath(self: Application) -> str

"""

    Product = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The product type for the current session of Revit.

Get: Product(self: Application) -> ProductType

"""

    RecordingJournalFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the name of the journal file the Revit is currently recording to.

Get: RecordingJournalFilename(self: Application) -> str

"""

    SharedParametersFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains the fully qualified path to a shared parameters file.

Get: SharedParametersFilename(self: Application) -> str

Set: SharedParametersFilename(self: Application) = value
"""

    ShortCurveTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The enforced minimum length for any curve created by Revit.

Get: ShortCurveTolerance(self: Application) -> float

"""

    ShowGraphicalWarningCableTrayConduitDisconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to show the graphical warnings for CTC disconnects.

Get: ShowGraphicalWarningCableTrayConduitDisconnects(self: Application) -> bool

Set: ShowGraphicalWarningCableTrayConduitDisconnects(self: Application) = value
"""

    ShowGraphicalWarningDuctDisconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to show the graphical warnings for duct disconnects.

Get: ShowGraphicalWarningDuctDisconnects(self: Application) -> bool

Set: ShowGraphicalWarningDuctDisconnects(self: Application) = value
"""

    ShowGraphicalWarningElectricalDisconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to show the graphical warnings for Electrical disconnects.

Get: ShowGraphicalWarningElectricalDisconnects(self: Application) -> bool

Set: ShowGraphicalWarningElectricalDisconnects(self: Application) = value
"""

    ShowGraphicalWarningHangerDisconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to show the graphical warnings for Fabrication Hanger disconnects.

Get: ShowGraphicalWarningHangerDisconnects(self: Application) -> bool

Set: ShowGraphicalWarningHangerDisconnects(self: Application) = value
"""

    ShowGraphicalWarningPipeDisconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to show the graphical warnings for Pipe disconnects.

Get: ShowGraphicalWarningPipeDisconnects(self: Application) -> bool

Set: ShowGraphicalWarningPipeDisconnects(self: Application) = value
"""

    Username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user name for the current Revit session.

Get: Username(self: Application) -> str

"""

    VersionBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal build number of the Autodesk Revit application.

Get: VersionBuild(self: Application) -> str

"""

    VersionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the name of the Revit application.

Get: VersionName(self: Application) -> str

"""

    VersionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the primary version of the Revit application.

Get: VersionNumber(self: Application) -> str

"""

    VertexTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertex tolerance.

Get: VertexTolerance(self: Application) -> float

"""


    ApplicationInitialized = None
    DocumentChanged = None
    DocumentClosed = None
    DocumentClosing = None
    DocumentCreated = None
    DocumentCreating = None
    DocumentOpened = None
    DocumentOpening = None
    DocumentPrinted = None
    DocumentPrinting = None
    DocumentSaved = None
    DocumentSavedAs = None
    DocumentSaving = None
    DocumentSavingAs = None
    DocumentSynchronizedWithCentral = None
    DocumentSynchronizingWithCentral = None
    DocumentWorksharingEnabled = None
    ElementTypeDuplicated = None
    ElementTypeDuplicating = None
    FailuresProcessing = None
    FamilyLoadedIntoDocument = None
    FamilyLoadingIntoDocument = None
    FileExported = None
    FileExporting = None
    FileImported = None
    FileImporting = None
    IsLoggedIn = False
    MinimumThickness = 0.0026041666666666665
    ProgressChanged = None
    ViewPrinted = None
    ViewPrinting = None


class ControlledApplication(object):
    """
    Represents the Autodesk Revit Application with no access to documents. It provides options
    and other application wide data and settings for external applications OnStartup/OnShutdown.
    """
    @staticmethod
    def GetFailureDefinitionRegistry():
        """
        GetFailureDefinitionRegistry() -> FailureDefinitionRegistry
        
            Returns the instance of FailureDefinitionRegistry.
            Returns: The instance of FailureDefinitionRegistry.
        """
        pass

    def GetLibraryPaths(self):
        """
        GetLibraryPaths(self: ControlledApplication) -> IDictionary[str, str]
        
            Returns path information identifying where Revit searches for content.
            Returns: The map of library paths.
        """
        pass

    def OpenSharedParameterFile(self):
        """
        OpenSharedParameterFile(self: ControlledApplication) -> DefinitionFile
        
            Enables access to shared parameter groups and definitions that are maintained 
             on disk.
        
            Returns: An object that represents a shared parameters file that exists on disk. Returns 
             ll if the file does not exist.
        """
        pass

    @staticmethod
    def RegisterFailuresProcessor(processor):
        """
        RegisterFailuresProcessor(processor: IFailuresProcessor)
            Registers Revit application-wide instance of Failures Processor.
        
            processor: Instance of Failures Processor to be used by the Revit Application.
        """
        pass

    def SetLibraryPaths(self, paths):
        """ SetLibraryPaths(self: ControlledApplication, paths: IDictionary[str, str]) """
        pass

    def WriteJournalComment(self, comment, timeStamp):
        """
        WriteJournalComment(self: ControlledApplication, comment: str, timeStamp: bool)
            Writes a comment to the Revit journal file.
        
            comment: Text for journal comment
            timeStamp: If a time stamp should be included in the journal comment
        """
        pass

    ActiveAddInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the Id of the currently running external application.

Get: ActiveAddInId(self: ControlledApplication) -> AddInId

"""

    AllUsersAddinsLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The folder location for .addin files for all users.

Get: AllUsersAddinsLocation(self: ControlledApplication) -> str

"""

    Cities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a set of all the known city locations within Revit.

Get: Cities(self: ControlledApplication) -> CitySet

"""

    Create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides an object that can be used to create new instances of Autodesk Revit API objects.

Get: Create(self: ControlledApplication) -> Application

"""

    CurrentUserAddinsLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The folder location for .addin files for the current user.

Get: CurrentUserAddinsLocation(self: ControlledApplication) -> str

"""

    IsLateAddinLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this add-in is loaded on the fly or not. If it is loaded when is Revit starting up, it
is false, otherwise it should be true.

Get: IsLateAddinLoading(self: ControlledApplication) -> bool

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The language used in the current session of Revit.

Get: Language(self: ControlledApplication) -> LanguageType

"""

    Product = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The product type for the current session of Revit.

Get: Product(self: ControlledApplication) -> ProductType

"""

    RecordingJournalFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the name of the journal file the Revit is currently recording to.

Get: RecordingJournalFilename(self: ControlledApplication) -> str

"""

    SharedParametersFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains the fully qualified path to a shared parameters file.

Get: SharedParametersFilename(self: ControlledApplication) -> str

Set: SharedParametersFilename(self: ControlledApplication) = value
"""

    VersionBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal build number of the Autodesk Revit application.

Get: VersionBuild(self: ControlledApplication) -> str

"""

    VersionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the name of the Revit application.

Get: VersionName(self: ControlledApplication) -> str

"""

    VersionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the primary version of the Revit application.

Get: VersionNumber(self: ControlledApplication) -> str

"""


    ApplicationInitialized = None
    DocumentChanged = None
    DocumentClosed = None
    DocumentClosing = None
    DocumentCreated = None
    DocumentCreating = None
    DocumentOpened = None
    DocumentOpening = None
    DocumentPrinted = None
    DocumentPrinting = None
    DocumentSaved = None
    DocumentSavedAs = None
    DocumentSaving = None
    DocumentSavingAs = None
    DocumentSynchronizedWithCentral = None
    DocumentSynchronizingWithCentral = None
    ElementTypeDuplicated = None
    ElementTypeDuplicating = None
    FailuresProcessing = None
    FamilyLoadedIntoDocument = None
    FamilyLoadingIntoDocument = None
    FileExported = None
    FileExporting = None
    FileImported = None
    FileImporting = None
    ProgressChanged = None
    ViewPrinted = None
    ViewPrinting = None


class LanguageType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type containing the supported Revit product languages.
    
    enum LanguageType, values: Brazilian_Portuguese (14), Chinese_Simplified (6), Chinese_Traditional (7), Czech (11), Dutch (5), English_USA (0), French (3), German (1), Hungarian (13), Italian (4), Japanese (8), Korean (9), Polish (12), Russian (10), Spanish (2), Unknown (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Brazilian_Portuguese = None
    Chinese_Simplified = None
    Chinese_Traditional = None
    Czech = None
    Dutch = None
    English_USA = None
    French = None
    German = None
    Hungarian = None
    Italian = None
    Japanese = None
    Korean = None
    Polish = None
    Russian = None
    Spanish = None
    Unknown = None
    value__ = None


class ProductType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type containing the possible Revit product types.
    
    enum ProductType, values: Architecture (0), LT (4), MEP (2), Revit (3), Structure (1), Unknown (5)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Architecture = None
    LT = None
    MEP = None
    Revit = None
    Structure = None
    Unknown = None
    value__ = None


