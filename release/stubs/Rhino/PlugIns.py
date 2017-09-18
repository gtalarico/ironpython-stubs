# encoding: utf-8
# module Rhino.PlugIns calls itself PlugIns
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CustomRenderSaveFileTypes(object):
    # no doc
    def RegisterFileType(self, extensions, description, saveFileHandler):
        """ RegisterFileType(self: CustomRenderSaveFileTypes, extensions: IEnumerable[str], description: str, saveFileHandler: SaveFileHandler) """
        pass

    SaveFileHandler = None


class DescriptionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DescriptionType, values: Address (1), Country (2), Email (5), Fax (7), Organization (0), Phone (3), UpdateUrl (6), WebSite (4) """
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

    Address = None
    Country = None
    Email = None
    Fax = None
    Organization = None
    Phone = None
    UpdateUrl = None
    value__ = None
    WebSite = None


class PlugIn(object):
    # no doc
    def AskUserForLicense(self, productBuildType, standAlone, textMask, parent, validateDelegate):
        """ AskUserForLicense(self: PlugIn, productBuildType: LicenseBuildType, standAlone: bool, textMask: str, parent: IWin32Window, validateDelegate: ValidateProductKeyDelegate) -> bool """
        pass

    def CommandSettings(self, name):
        """ CommandSettings(self: PlugIn, name: str) -> PersistentSettings """
        pass

    def CreateCommands(self, *args): #cannot find CLR method
        """
        CreateCommands(self: PlugIn)
            Called right after plug-in is created and is responsible for creating
                    all of the 
             commands in a given plug-in.  The base class implementation
                    Constructs an instance 
             of every publicly exported command class in your
                    plug-in's assembly.
        """
        pass

    def DocumentPropertiesDialogPages(self, *args): #cannot find CLR method
        """ DocumentPropertiesDialogPages(self: PlugIn, doc: RhinoDoc, pages: List[OptionsDialogPage]) """
        pass

    @staticmethod
    def Find(*__args):
        """
        Find(plugInId: Guid) -> PlugIn
        
            Finds the plug-in instance that was loaded from a given plug-in Id.
        
            plugInId: The plug-in Id.
            Returns: The plug-in instance if successful. Otherwise, null.
        Find(pluginAssembly: Assembly) -> PlugIn
        
            Finds the plug-in instance that was loaded from a given assembly.
        
            pluginAssembly: The plug-in assembly.
                    You can get the assembly instance at runtime with the 
             System.Type.Assembly instance property.
        
            Returns: The assembly plug-in instance if successful. Otherwise, null.
        """
        pass

    def GetCommands(self):
        """
        GetCommands(self: PlugIn) -> Array[Command]
        
            All of the commands associated with this plug-in.
        """
        pass

    @staticmethod
    def GetEnglishCommandNames(pluginId):
        """
        GetEnglishCommandNames(pluginId: Guid) -> Array[str]
        
            Gets names of all "non-test" commands for a given plug-in.
        
            pluginId: The plug-in ID.
            Returns: An array with all plug-in names. This can be empty, but not null.
        """
        pass

    @staticmethod
    def GetInstalledPlugInFolders():
        """ GetInstalledPlugInFolders() -> Array[str] """
        pass

    @staticmethod
    def GetInstalledPlugInNames(typeFilter=None, loaded=None, unloaded=None):
        """
        GetInstalledPlugInNames(typeFilter: PlugInType, loaded: bool, unloaded: bool) -> Array[str]
        
            Gets a list of installed plug-in names.  The list can be restricted by some filters.
        
            typeFilter: The enumeration flags that determine which types of plug-ins are included.
            loaded: true if loaded plug-ins are returned.
            unloaded: true if unloaded plug-ins are returned.
            Returns: An array of installed plug-in names. This can be empty, but not null.
        GetInstalledPlugInNames() -> Array[str]
        """
        pass

    @staticmethod
    def GetInstalledPlugIns():
        """ GetInstalledPlugIns() -> Dictionary[Guid, str] """
        pass

    def GetLicense(self, *__args):
        """
        GetLicense(self: PlugIn, licenseCapabilities: LicenseCapabilities, textMask: str, validateDelegate: ValidateProductKeyDelegate) -> bool
        
            Verifies that there is a valid product license for your plug-in, using
                    the Rhino 
             licensing system. If the plug-in is installed as a standalone
                    node, the locally 
             installed license will be validated. If the plug-in
                    is installed as a network node, 
             a loaner license will be requested by
                    the system's assigned Zoo server. If the Zoo 
             server finds and returns 
                    a license, then this license will be validated. If no 
             license is found,
                    then the user will be prompted to provide a license key, which 
             will be
                    validated.
        
        
            licenseCapabilities: In the event that a license was not found, or if the user wants to change
                    the way 
             your plug-in is licenses, then provide what capabilities your
                    license has by using 
             this enumeration flag.
        
            textMask: In the event that the user needs to be asked for a license, then you can
                    provide a 
             text mask, which helps the user to distinguish between proper
                    and improper user 
             input of your license code. Note, if you do not want
                    to use a text mask, then pass 
             in a null value for this parameter.
                    For more information on text masks, search MSDN 
             for the System.Windows.Forms.MaskedTextBox class.
        
            validateDelegate: Since the Rhino licensing system knows nothing about your product license,
                    you will 
             need to validate the product license provided by the Rhino 
                    licensing system. This 
             is done by supplying a callback function, or delegate,
                    that can be called to 
             perform the validation.
        
            Returns: true if a valid license was found. false otherwise.
        GetLicense(self: PlugIn, productBuildType: LicenseBuildType, validateDelegate: ValidateProductKeyDelegate) -> bool
        
            Verifies that there is a valid product license for your plug-in, using
                    the Rhino 
             licensing system. If the plug-in is installed as a standalone
                    node, the locally 
             installed license will be validated. If the plug-in
                    is installed as a network node, 
             a loaner license will be requested by
                    the system's assigned Zoo server. If the Zoo 
             server finds and returns 
                    a license, then this license will be validated. If no 
             license is found,
                    then the user will be prompted to provide a license key, which 
             will be
                    validated.
        
        
            productBuildType: The product build contentType required by your plug-in.
            validateDelegate: Since the Rhino licensing system knows nothing about your product license,
                    you will 
             need to validate the product license provided by the Rhino 
                    licensing system. This 
             is done by supplying a callback function, or delegate,
                    that can be called to 
             perform the validation.
        
            Returns: true if a valid license was found. false otherwise.
        """
        pass

    def GetLicenseOwner(self, registeredOwner, registeredOrganization):
        """
        GetLicenseOwner(self: PlugIn) -> (bool, str, str)
        
            Get the customer name and organization used when entering the product
                    license.
        """
        pass

    @staticmethod
    def GetLoadProtection(pluginId, loadSilently):
        """
        GetLoadProtection(pluginId: Guid) -> (bool, bool)
        
            Get load protection state for a plug-in
        """
        pass

    def GetPlugInObject(self):
        """ GetPlugInObject(self: PlugIn) -> object """
        pass

    @staticmethod
    def IdFromName(pluginName):
        """ IdFromName(pluginName: str) -> Guid """
        pass

    @staticmethod
    def IdFromPath(pluginPath):
        """ IdFromPath(pluginPath: str) -> Guid """
        pass

    @staticmethod
    def LoadPlugIn(pluginId):
        """ LoadPlugIn(pluginId: Guid) -> bool """
        pass

    @staticmethod
    def NameFromPath(pluginPath):
        """
        NameFromPath(pluginPath: str) -> str
        
            Gets a plug-in name for an installed plug-in given the path to that plug-in.
        
            pluginPath: The path of the plug-in.
            Returns: The plug-in name.
        """
        pass

    def ObjectPropertiesPages(self, *args): #cannot find CLR method
        """ ObjectPropertiesPages(self: PlugIn, pages: List[ObjectPropertiesPage]) """
        pass

    def OnLoad(self, *args): #cannot find CLR method
        """
        OnLoad(self: PlugIn, errorMessage: str) -> (LoadReturnCode, str)
        
            Is called when the plug-in is being loaded.
        
            errorMessage: If a load error is returned and this string is set. This string is the 
                    error 
             message that will be reported back to the user.
        
            Returns: An appropriate load return code.
                    The default implementation returns 
             Rhino.PlugIns.LoadReturnCode.Success.
        """
        pass

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: PlugIn) """
        pass

    def OptionsDialogPages(self, *args): #cannot find CLR method
        """ OptionsDialogPages(self: PlugIn, pages: List[OptionsDialogPage]) """
        pass

    @staticmethod
    def PathFromId(pluginId):
        """
        PathFromId(pluginId: Guid) -> str
        
            Gets the path to an installed plug-in given the id of that plug-in
        """
        pass

    @staticmethod
    def PathFromName(pluginName):
        """
        PathFromName(pluginName: str) -> str
        
            Gets the path to an installed plug-in given the name of that plug-in
        """
        pass

    @staticmethod
    def PlugInExists(id, loaded, loadProtected):
        """ PlugInExists(id: Guid) -> (bool, bool, bool) """
        pass

    def ReadDocument(self, *args): #cannot find CLR method
        """
        ReadDocument(self: PlugIn, doc: RhinoDoc, archive: BinaryArchiveReader, options: FileReadOptions)
            Called whenever a Rhino document is being loaded and plug-in user data was
                    
             encountered written by a plug-in with this plug-in's GUID.
        
        
            doc: A Rhino document that is being loaded.
            archive: OpenNURBS file archive object Rhino is using to read this file.
                    Use 
             BinaryArchiveReader.Read*() functions to read plug-in data.
                    
                    If any 
             BinaryArchive.Read*() functions throws an exception then
                    archive.ReadErrorOccurve 
             will be true and you should immediately return.
        
            options: Describes what is being written.
        """
        pass

    def RegisterCommand(self, *args): #cannot find CLR method
        """ RegisterCommand(self: PlugIn, command: Command) -> bool """
        pass

    def ReturnLicense(self):
        """
        ReturnLicense(self: PlugIn) -> bool
        
            Returns, or releases, a product license that was obtained from the Rhino
                    licensing 
             system. Note, most plug-ins do not need to call this as the
                    Rhino licensing system 
             will return all licenses when Rhino shuts down.
        """
        pass

    @staticmethod
    def SetLoadProtection(pluginId, loadSilently):
        """
        SetLoadProtection(pluginId: Guid, loadSilently: bool)
            Set load protection state for a certain plug-in
        """
        pass

    def ShouldCallWriteDocument(self, *args): #cannot find CLR method
        """
        ShouldCallWriteDocument(self: PlugIn, options: FileWriteOptions) -> bool
        
            Called whenever a Rhino is about to save a .3dm file.
                    If you want to save plug-in 
             document data when a model is 
                    saved in a version 5 .3dm file, then you must 
             override this
                    function to return true and you must override WriteDocument().
        
        
            options: The file write options, such as "include preview image" and "include render meshes".
            Returns: true if the plug-in wants to save document user data in the
                    version 5 .3dm file.  
             The default returns false.
        """
        pass

    def WriteDocument(self, *args): #cannot find CLR method
        """
        WriteDocument(self: PlugIn, doc: RhinoDoc, archive: BinaryArchiveWriter, options: FileWriteOptions)
            Called when Rhino is saving a .3dm file to allow the plug-in
                    to save document user 
             data.
        
        
            doc: The Rhino document instance that is being saved.
            archive: OpenNURBS file archive object Rhino is using to write the file.
                    Use 
             BinaryArchiveWriter.Write*() functions to write plug-in data.
                    OR use the 
             ArchivableDictionary
                    
                    If any BinaryArchiveWriter.Write*() functions 
             throw an exception, 
                    then archive.WriteErrorOccured will be true and you should 
             immediately return.
                    Setting archive.WriteErrorOccured to true will cause Rhino to 
             stop saving the file.
        
            options: The file write options, such as "include preview image" and "include render meshes".
        """
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Source assembly for this plug-in.

Get: Assembly(self: PlugIn) -> Assembly

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PlugIn) -> Guid

"""

    LoadAtStartup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadAtStartup(self: PlugIn) -> bool

"""

    LoadTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plug-ins are typically loaded on demand when they are first needed. You can change
            this behavior to load the plug-in at during different stages in time by overriding
            this property.

Get: LoadTime(self: PlugIn) -> PlugInLoadTime

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PlugIn) -> str

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: PlugIn) -> PersistentSettings

"""

    SettingsDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SettingsDirectory(self: PlugIn) -> str

"""

    SettingsDirectoryAllUsers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SettingsDirectoryAllUsers(self: PlugIn) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: PlugIn) -> str

"""



class DigitizerPlugIn(PlugIn):
    # no doc
    def EnableDigitizer(self, *args): #cannot find CLR method
        """
        EnableDigitizer(self: DigitizerPlugIn, enable: bool) -> bool
        
            Called by Rhino to enable/disable input from the digitizer.
                    If enable is true and 
             EnableDigitizer() returns false, then
                    Rhino will not calibrate the digitizer.
        
        
            enable: If true, enable the digitizer. If false, disable the digitizer.
            Returns: true if the operation succeeded; otherwise, false.
        """
        pass

    def SendPoint(self, point, mousebuttons, shiftKey, controlKey):
        """
        SendPoint(self: DigitizerPlugIn, point: Point3d, mousebuttons: MouseButtons, shiftKey: bool, controlKey: bool)
            If the digitizer is enabled, call this function to send a point to Rhino.
                    Call this 
             function as much as you like.  The digitizers that Rhino currently
                    supports send a 
             point every 15 milliseconds or so. This function should be
                    called when users press 
             or release any digitizer button.
        
        
            point: 3d point in digitizer coordinates.
            mousebuttons: corresponding digitizer button is down.
            shiftKey: true if the Shift keyboard key was pressed. Otherwise, false.
            controlKey: true if the Control keyboard key was pressed. Otherwise, false.
        """
        pass

    def SendRay(self, ray, mousebuttons, shiftKey, controlKey):
        """ SendRay(self: DigitizerPlugIn, ray: Ray3d, mousebuttons: MouseButtons, shiftKey: bool, controlKey: bool) """
        pass

    DigitizerUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit system of the points the digitizer passes to SendPoint().
            Rhino uses this value when it calibrates a digitizer.
            This unit system must be not change.

"""

    PointTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point tolerance is the distance the digitizer must move 
            (in digitizer coordinates) for a new point to be considered
            real rather than noise. Small desktop digitizer arms have
            values like 0.001 inches and 0.01 millimeters.  This value
            should never be smaller than the accuracy of the digitizing
            device.

"""



class FileExportPlugIn(PlugIn):
    # no doc
    def AddFileTypes(self, *args): #cannot find CLR method
        """ AddFileTypes(self: FileExportPlugIn, options: FileWriteOptions) -> FileTypeList """
        pass

    def WriteFile(self, *args): #cannot find CLR method
        """ WriteFile(self: FileExportPlugIn, filename: str, index: int, doc: RhinoDoc, options: FileWriteOptions) -> WriteFileResult """
        pass


class FileImportPlugIn(PlugIn):
    # no doc
    def AddFileTypes(self, *args): #cannot find CLR method
        """ AddFileTypes(self: FileImportPlugIn, options: FileReadOptions) -> FileTypeList """
        pass

    def MakeReferenceTableName(self, *args): #cannot find CLR method
        """ MakeReferenceTableName(self: FileImportPlugIn, nameToPrefix: str) -> str """
        pass

    def ReadFile(self, *args): #cannot find CLR method
        """ ReadFile(self: FileImportPlugIn, filename: str, index: int, doc: RhinoDoc, options: FileReadOptions) -> bool """
        pass


class FileTypeList(object):
    """ FileTypeList() """
    def AddFileType(self, description, *__args):
        """
        AddFileType(self: FileTypeList, description: str, extensions: IEnumerable[str]) -> int
        AddFileType(self: FileTypeList, description: str, extension1: str, extension2: str) -> int
        AddFileType(self: FileTypeList, description: str, extension: str) -> int
        """
        pass


class LicenseBuildType(Enum, IComparable, IFormattable, IConvertible):
    """
    License build contentType enumerations.
    
    enum LicenseBuildType, values: Beta (300), Evaluation (200), Release (100), Unspecified (0)
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

    Beta = None
    Evaluation = None
    Release = None
    Unspecified = None
    value__ = None


class LicenseCapabilities(Enum, IComparable, IFormattable, IConvertible):
    """
    Controls the buttons that will appear on the license notification window
                that is displayed if a license for the requesting product is not found.
                Note, the "Close" button will always be displayed.
    
    enum (flags) LicenseCapabilities, values: CanBeEvaluated (4), CanBePurchased (1), CanBeSpecified (2), EvaluationIsExpired (8), NoCapabilities (0)
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

    CanBeEvaluated = None
    CanBePurchased = None
    CanBeSpecified = None
    EvaluationIsExpired = None
    NoCapabilities = None
    value__ = None


class LicenseData(object):
    """
    Zoo plugin license data.
    
    LicenseData()
    LicenseData(productLicense: str, serialNumber: str, licenseTitle: str)
    LicenseData(productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType)
    LicenseData(productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int)
    LicenseData(productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable[DateTime])
    LicenseData(productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable[DateTime], productIcon: Icon)
    """
    def Dispose(self):
        """ Dispose(self: LicenseData) """
        pass

    @staticmethod
    def IsNotValid(data):
        """
        IsNotValid(data: LicenseData) -> bool
        
            Indicates whether a LicenseData object is either null or invalid.
        """
        pass

    def IsValid(self, data=None):
        """
        IsValid(data: LicenseData) -> bool
        
            Indicates whether a LicenseData object is not null and valid.
        IsValid(self: LicenseData) -> bool
        
            Public validator.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, productLicense=None, serialNumber=None, licenseTitle=None, buildType=None, licenseCount=None, expirationDate=None, productIcon=None):
        """
        __new__(cls: type)
        __new__(cls: type, productLicense: str, serialNumber: str, licenseTitle: str)
        __new__(cls: type, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType)
        __new__(cls: type, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int)
        __new__(cls: type, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable[DateTime])
        __new__(cls: type, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable[DateTime], productIcon: Icon)
        """
        pass

    BuildType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The build of the product that this license work with.
            When your product requests a license from the Zoo, it
            will specify one of these build types.

Get: BuildType(self: LicenseData) -> LicenseBuildType

Set: BuildType(self: LicenseData) = value
"""

    DateToExpire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time the license is set to expire.
            This is provided by the plugin that validated the license.
            This time value should be in Coordinated Universal Time (UTC).

Get: DateToExpire(self: LicenseData) -> Nullable[DateTime]

Set: DateToExpire(self: LicenseData) = value
"""

    LicenseCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of instances supported by this license.
            This is provided by the plugin that validated the license.

Get: LicenseCount(self: LicenseData) -> int

Set: LicenseCount(self: LicenseData) = value
"""

    LicenseTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title of the license.
            This is provided by the plugin that validated the license.
            (e.g. "Rhinoceros 5.0 Commercial")

Get: LicenseTitle(self: LicenseData) -> str

Set: LicenseTitle(self: LicenseData) = value
"""

    ProductIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The product's icon. This will displayed in the "license"
            page in the Options dialog. Note, this can be null.
            Note, LicenseData creates it's own copy of the icon.

Get: ProductIcon(self: LicenseData) -> Icon

Set: ProductIcon(self: LicenseData) = value
"""

    ProductLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual product license. 
            This is provided by the plugin that validated the license.

Get: ProductLicense(self: LicenseData) -> str

Set: ProductLicense(self: LicenseData) = value
"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The "for display only" product license.
            This is provided by the plugin that validated the license.

Get: SerialNumber(self: LicenseData) -> str

Set: SerialNumber(self: LicenseData) = value
"""



class LicenseStatus(object):
    """
    LicenseStatus class.
    
    LicenseStatus()
    """
    BuildType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The build contentType of the product, where:
              100 = A release build, either commercical, education, nfr, etc.
              200 = A evaluation build
              300 = A beta build, such as a wip.

Get: BuildType(self: LicenseStatus) -> LicenseBuildType

Set: BuildType(self: LicenseStatus) = value
"""

    CheckOutExpirationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time the checked out license will expire.
            Note, this is only set if m_license_type = LicenceType.Standalone
            and if "limited license checkout" was enabled on the Zoo server.
            Note, date and time is in local time coordinates.

Get: CheckOutExpirationDate(self: LicenseStatus) -> Nullable[DateTime]

Set: CheckOutExpirationDate(self: LicenseStatus) = value
"""

    ExpirationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time the license will expire.
            This value can be null if:
              1.) The license contentType is "Standalone" and the license does not expire.
              2.) The license contentType is "Network".
              3.) The license contentType is "NetworkCheckedOut" and the checkout does not expire
            Note, date and time is in local time coordinates.

Get: ExpirationDate(self: LicenseStatus) -> Nullable[DateTime]

Set: ExpirationDate(self: LicenseStatus) = value
"""

    LicenseTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title of the license. (e.g. "Rhinoceros 5.0 Commercial")

Get: LicenseTitle(self: LicenseStatus) -> str

Set: LicenseTitle(self: LicenseStatus) = value
"""

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The license contentType. (e.g. Standalone, Network, etc.)

Get: LicenseType(self: LicenseStatus) -> LicenseType

Set: LicenseType(self: LicenseStatus) = value
"""

    ProductIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The product's icon. Note, this can be null.

Get: ProductIcon(self: LicenseStatus) -> Icon

Set: ProductIcon(self: LicenseStatus) = value
"""

    ProductId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the product or plugin.

Get: ProductId(self: LicenseStatus) -> Guid

Set: ProductId(self: LicenseStatus) = value
"""

    RegisteredOrganization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The registered organization of the product (e.g. "Robert McNeel and Associates")

Get: RegisteredOrganization(self: LicenseStatus) -> str

Set: RegisteredOrganization(self: LicenseStatus) = value
"""

    RegisteredOwner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The registered owner of the product. (e.g. "Dale Fugier")

Get: RegisteredOwner(self: LicenseStatus) -> str

Set: RegisteredOwner(self: LicenseStatus) = value
"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The "for display only" product license or serial number.

Get: SerialNumber(self: LicenseStatus) -> str

Set: SerialNumber(self: LicenseStatus) = value
"""



class LicenseType(Enum, IComparable, IFormattable, IConvertible):
    """
    LicenseType enumeration.
    
    enum LicenseType, values: Network (1), NetworkCheckedOut (3), NetworkLoanedOut (2), Standalone (0)
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

    Network = None
    NetworkCheckedOut = None
    NetworkLoanedOut = None
    Standalone = None
    value__ = None


class LicenseUtils(object):
    """ License Manager Utilities. """
    @staticmethod
    def AskUserForLicense(productType, standAlone, parentWindow, textMask, validateDelegate):
        """
        AskUserForLicense(productType: int, standAlone: bool, parentWindow: IWin32Window, textMask: str, validateDelegate: ValidateProductKeyDelegate) -> bool
        
            This version of Rhino.PlugIns.LicenseUtils.AskUserForLicense
                    is used by Rhino C++ 
             plug-ins.
        """
        pass

    @staticmethod
    def CheckInLicense(productId):
        """
        CheckInLicense(productId: Guid) -> bool
        
            Checks in a previously checked out license to
                    the Zoo server from which it was 
             checked out.
        
        
            productId: The Guid of the product that you want to check in.
            Returns: true if the license was checked in successful.
                    false if not successful or on error.
        """
        pass

    @staticmethod
    def CheckOutLicense(productId):
        """
        CheckOutLicense(productId: Guid) -> bool
        
            Checks out a license that is on loan from a Zoo server
                    on a permanent basis.
        
            productId: The Guid of the product that you want to check out.
            Returns: true if the license was checked out successful.
                    false if not successful or on error.
        """
        pass

    @staticmethod
    def ConvertLicense(productId):
        """
        ConvertLicense(productId: Guid) -> bool
        
            Converts a product license from a standalone node
                    to a network node.
        
            productId: The Guid of the product that you want to check in.
            Returns: true if the license was successfully converted.
                    false if not successful or on error.
        """
        pass

    @staticmethod
    def Echo(message):
        """
        Echo(message: str) -> str
        
            Tests connectivity with the Zoo.
        """
        pass

    @staticmethod
    def GetLicense(*__args):
        """
        GetLicense(validateDelegate: ValidateProductKeyDelegate, capabilities: int, textMask: str) -> bool
        
            This version of Rhino.PlugIns.LicenseUtils.GetLicense
                    is used by Rhino C++ plug-ins.
        GetLicense(productType: int, validateDelegate: ValidateProductKeyDelegate) -> bool
        
            This version of Rhino.PlugIns.LicenseUtils.GetLicense
                    is used by Rhino C++ plug-ins.
        """
        pass

    @staticmethod
    def GetLicenseCapabilities(filter):
        """
        GetLicenseCapabilities(filter: int) -> LicenseCapabilities
        
            Converts an integer to a LicenseCapabilities flag
        """
        pass

    @staticmethod
    def GetLicenseStatus():
        """
        GetLicenseStatus() -> Array[LicenseStatus]
        
            Returns the current status of every license for ui purposes.
        """
        pass

    @staticmethod
    def GetLicenseType(productId):
        """
        GetLicenseType(productId: Guid) -> int
        
            Returns the contentType of a specified product license
        """
        pass

    @staticmethod
    def GetOneLicenseStatus(productid):
        """
        GetOneLicenseStatus(productid: Guid) -> LicenseStatus
        
            Returns the current status of a license for ui purposes.
        """
        pass

    @staticmethod
    def Initialize():
        """
        Initialize() -> int
        
            Initializes the license manager.
        """
        pass

    @staticmethod
    def IsCheckOutEnabled():
        """
        IsCheckOutEnabled() -> bool
        
            Returns whether or not license checkout is enabled.
        """
        pass

    @staticmethod
    def LicenseOptionsHandler(productId, productTitle, bStandalone):
        """ LicenseOptionsHandler(productId: Guid, productTitle: str, bStandalone: bool) -> bool """
        pass

    @staticmethod
    def ReturnLicense(*__args):
        """
        ReturnLicense(productId: Guid) -> bool
        
            OBSOLETE - REMOVE WHEN POSSIBLE.
        ReturnLicense(validateDelegate: ValidateProductKeyDelegate) -> bool
        
            This (internal) version of Rhino.PlugIns.LicenseUtils.ReturnLicense is used
                    is used 
             by Rhino C++ plug-ins.
        """
        pass

    @staticmethod
    def ShowBuyLicenseUi(productId):
        """ ShowBuyLicenseUi(productId: Guid) """
        pass

    @staticmethod
    def ShowLicenseValidationUi(cdkey):
        """
        ShowLicenseValidationUi(cdkey: str) -> bool
        
            ShowLicenseValidationUi
        """
        pass

    @staticmethod
    def ShowRhinoExpiredMessage(mode):
        """
        ShowRhinoExpiredMessage(mode: int)
            Show Rhino or Beta expired message
        """
        pass

    __all__ = [
        'AskUserForLicense',
        'CheckInLicense',
        'CheckOutLicense',
        'ConvertLicense',
        'Echo',
        'GetLicense',
        'GetLicenseCapabilities',
        'GetLicenseStatus',
        'GetLicenseType',
        'GetOneLicenseStatus',
        'Initialize',
        'IsCheckOutEnabled',
        'LicenseOptionsHandler',
        'ReturnLicense',
        'ShowBuyLicenseUi',
        'ShowLicenseValidationUi',
        'ShowRhinoExpiredMessage',
    ]


class LoadReturnCode(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadReturnCode, values: ErrorNoDialog (-1), ErrorShowDialog (0), Success (1) """
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

    ErrorNoDialog = None
    ErrorShowDialog = None
    Success = None
    value__ = None


class PlugInDescriptionAttribute(Attribute, _Attribute):
    """ PlugInDescriptionAttribute(descriptionType: DescriptionType, value: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, descriptionType, value):
        """ __new__(cls: type, descriptionType: DescriptionType, value: str) """
        pass

    DescriptionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DescriptionType(self: PlugInDescriptionAttribute) -> DescriptionType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PlugInDescriptionAttribute) -> str

"""



class PlugInLoadTime(Enum, IComparable, IFormattable, IConvertible):
    """ enum PlugInLoadTime, values: AtStartup (1), Disabled (0), WhenNeeded (2), WhenNeededIgnoreDockingBars (6), WhenNeededOrOptionsDialog (10) """
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

    AtStartup = None
    Disabled = None
    value__ = None
    WhenNeeded = None
    WhenNeededIgnoreDockingBars = None
    WhenNeededOrOptionsDialog = None


class PlugInType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) PlugInType, values: Any (127), Digitizer (8), DisplayEngine (64), DisplayPipeline (32), FileExport (4), FileImport (2), None (0), Render (1), Utility (16) """
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

    Any = None
    Digitizer = None
    DisplayEngine = None
    DisplayPipeline = None
    FileExport = None
    FileImport = None
    None = None
    Render = None
    Utility = None
    value__ = None


class RenderPlugIn(PlugIn):
    # no doc
    def AllowChooseContent(self, *args): #cannot find CLR method
        """
        AllowChooseContent(self: RenderPlugIn, content: RenderContent) -> bool
        
            Default implementation returns true which means the content can be
                    picked from the 
             content browser by the user. Override this method and
                    return false if you don't 
             want to allow a certain content contentType to be
                    picked from the content browser 
             while your render engine is current.
        
        
            content: A render context.
            Returns: true if the operation was successful.
        """
        pass

    def CreatePreview(self, *args): #cannot find CLR method
        """
        CreatePreview(self: RenderPlugIn, args: CreatePreviewEventArgs)
            Creates the preview bitmap that will appear in the content editor's
                    thumbnail 
             display when previewing materials and environments. If this
                    function is not 
             overridden or the PreviewImage is not set on the
                    args, then the internal OpenGL 
             renderer will generate a simulation of
                    the content.
                    
                    This 
             function is called with four different preview quality settings.
                    The first quality 
             level of RealtimeQuick is called on the main thread
                    and needs to be drawn as fast 
             as possible.  This function is called
                    with the other three quality settings on a 
             separate thread and are
                    meant for generating progressively refined preview.
        
        
            args: Event argument with several preview option state properties.
        """
        pass

    def CreateTexture2dPreview(self, *args): #cannot find CLR method
        """
        CreateTexture2dPreview(self: RenderPlugIn, args: CreateTexture2dPreviewEventArgs)
            Creates the preview bitmap that will appear in the content editor's
                     thumbnail 
             display when previewing textures in 2d (UV) mode.
                    
                     If this function 
             is not overridden or the PreviewImage is not set on the
                     args, then the internal 
             OpenGL renderer will generate a simulation.
        
        
            args: Event argument with several preview option state properties.
        """
        pass

    def EnableAssignMaterialButton(self):
        """
        EnableAssignMaterialButton(self: RenderPlugIn) -> bool
        
            Called to enable/disable the "Material" button located on the
                    "Material" tab in the 
             Properties and Layer dialog boxes.  The default
                    return value is false which will 
             disable the button.  If the button is
                    disabled then the OnAssignMaterial function 
             is never called.
        """
        pass

    def EnableCreateMaterialButton(self):
        """
        EnableCreateMaterialButton(self: RenderPlugIn) -> bool
        
            Called to enable/disable the "New" button located on the "Material" in
                    the  
             Properties and Layer dialog boxes.  The default return value is
                    false which will 
             disable the button.  If the button is disabled then
                    the OnEditMaterial function is 
             never called.
        """
        pass

    def EnableEditMaterialButton(self, doc, material):
        """
        EnableEditMaterialButton(self: RenderPlugIn, doc: RhinoDoc, material: Material) -> bool
        
            Called to enable/disable the "Edit" button located on the "Material" in
                    the 
             Properties and Layer dialog boxes.  The default return value is
                    false  which will 
             disable the button.  If the button is disabled then
                    the OnEditMaterial function is 
             never called.
        """
        pass

    def InitializeDecalProperties(self, *args): #cannot find CLR method
        """ InitializeDecalProperties(self: RenderPlugIn, properties: List[NamedValue]) -> List[NamedValue] """
        pass

    def OnAssignMaterial(self, parent, doc, material):
        """
        OnAssignMaterial(self: RenderPlugIn, parent: IntPtr, doc: RhinoDoc, material: Material) -> (bool, Material)
        
            This function is called by the Object Properties and Layer Control
                    dialogs when the 
             "Material" button is pressed in the "Render" tab.
                    This is only called if 
             EnableAssignMaterialButton returns true.
        """
        pass

    def OnCreateMaterial(self, parent, doc, material):
        """
        OnCreateMaterial(self: RenderPlugIn, parent: IntPtr, doc: RhinoDoc, material: Material) -> (bool, Material)
        
            This function is called by the Object Properties and Layer Control
                    dialogs when the 
             "New" button is pressed in the "Material" tab.  This
                    is only called if 
             EnableCreateMaterialButton returns true.
        """
        pass

    def OnEditMaterial(self, parent, doc, material):
        """
        OnEditMaterial(self: RenderPlugIn, parent: IntPtr, doc: RhinoDoc, material: Material) -> (bool, Material)
        
            This function is called by the Object Properties and Layer Control
                    dialogs when the 
             "Edit" button is pressed in the "Material" tab.  This
                    is only called if 
             EnableEditMaterialButton returns true. A return value
                    of true means the material 
             has been updated.
        """
        pass

    def OnSetCurrent(self, *args): #cannot find CLR method
        """
        OnSetCurrent(self: RenderPlugIn, current: bool)
            This plug-in (has become)/(is no longer) the current render plug-in
        
            current: If true then this plug-in is now the current render plug-in otherwise
                    it is no 
             longer the current render plug-in.
        """
        pass

    def RegisterCustomRenderSaveFileTypes(self, *args): #cannot find CLR method
        """
        RegisterCustomRenderSaveFileTypes(self: RenderPlugIn, saveFileTypes: CustomRenderSaveFileTypes)
            Override this method to add custom file types to the render window save
                    file dialog.
        """
        pass

    def RegisterRenderPanels(self, *args): #cannot find CLR method
        """
        RegisterRenderPanels(self: RenderPlugIn, panels: RenderPanels)
            Override this method and call 
             Rhino.Render.RenderPanels.RegisterPanel(Rhino.PlugIns.PlugIn,Rhino.Render.RenderPanelType,System.
             Type,System.String,System.Boolean,System.Boolean)
                    to add custom render UI to the 
             render output window.
        """
        pass

    def RegisterRenderTabs(self, *args): #cannot find CLR method
        """
        RegisterRenderTabs(self: RenderPlugIn, tabs: RenderTabs)
            Override this method and call 
             Rhino.Render.RenderTabs.RegisterTab(Rhino.PlugIns.PlugIn,System.Type,System.String,System.Drawing
             .Icon)
                    to add custom tabs to the render output window
        """
        pass

    def Render(self, *args): #cannot find CLR method
        """
        Render(self: RenderPlugIn, doc: RhinoDoc, mode: RunMode, fastPreview: bool) -> Result
        
            Called by Render and RenderPreview commands if this plug-in is set as the default render engine.
        
            doc: A document.
            mode: A command running mode.
            fastPreview: If true, lower quality faster render expected.
            Returns: If true, then the renderer is required to construct a rapid preview and not the high-quality 
             final result.
        """
        pass

    def RenderContentSerializers(self, *args): #cannot find CLR method
        """
        RenderContentSerializers(self: RenderPlugIn) -> IEnumerable[RenderContentSerializer]
        
            Called by Rhino when it is time to register RenderContentSerializer
                    derived 
             classes.  Override this method and return an array of an
                    instance of each serialize 
             custom content object you wish to add.
        
            Returns: List of RenderContentSerializer objects to register with the Rhino
                    render content 
             browsers.
        """
        pass

    def RenderOptionsDialogPage(self, *args): #cannot find CLR method
        """
        RenderOptionsDialogPage(self: RenderPlugIn, doc: RhinoDoc) -> OptionsDialogPage
        
            Override this method to replace the render properties page in the Rhino
                    document 
             properties dialog.  The default implementation returns null
                    which means just use 
             the the default Rhino page.
        
        
            doc: The document properties to edit.
            Returns: Return null to use the default Rhino page or return a page derived from
                    
             Rhino.UI.OptionsDialogPage to replace the default page.
        """
        pass

    def RenderWindow(self, *args): #cannot find CLR method
        """ RenderWindow(self: RenderPlugIn, doc: RhinoDoc, modes: RunMode, fastPreview: bool, view: RhinoView, rect: Rectangle, inWindow: bool) -> Result """
        pass

    def ShowDecalProperties(self, *args): #cannot find CLR method
        """ ShowDecalProperties(self: RenderPlugIn, properties: List[NamedValue]) -> (bool, List[NamedValue]) """
        pass

    def SupportedOutputTypes(self, *args): #cannot find CLR method
        """
        SupportedOutputTypes(self: RenderPlugIn) -> List[FileType]
        
            Returns a list of output types which your renderer can write.
                    The default 
             implementation returns bmp, jpg, png, tif, tga.
        
            Returns: A list of file types.
        """
        pass

    def SupportsFeature(self, *args): #cannot find CLR method
        """ SupportsFeature(self: RenderPlugIn, feature: RenderFeature) -> bool """
        pass

    PerferBasicContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true if you would like Rhino to quickly create a basic render
            content in response to 'Create New' commands. Set to false if you would
            prefer Rhino to display the render content chooser dialog.

Get: PerferBasicContent(self: RenderPlugIn) -> bool

Set: PerferBasicContent(self: RenderPlugIn) = value
"""


    RenderFeature = None


class ValidateProductKeyDelegate(MulticastDelegate, ICloneable, ISerializable):
    """
    Validates a product key or license.
    
    ValidateProductKeyDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, productKey, licenseData, callback, object):
        """ BeginInvoke(self: ValidateProductKeyDelegate, productKey: str, callback: AsyncCallback, object: object) -> (IAsyncResult, LicenseData) """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, licenseData, result):
        """ EndInvoke(self: ValidateProductKeyDelegate, result: IAsyncResult) -> (ValidateResult, LicenseData) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, productKey, licenseData):
        """ Invoke(self: ValidateProductKeyDelegate, productKey: str) -> (ValidateResult, LicenseData) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class ValidateResult(Enum, IComparable, IFormattable, IConvertible):
    """
    ValidateProductKeyDelegate result code.
    
    enum ValidateResult, values: ErrorHideMessage (-1), ErrorShowMessage (0), Success (1)
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

    ErrorHideMessage = None
    ErrorShowMessage = None
    Success = None
    value__ = None


class WriteFileResult(Enum, IComparable, IFormattable, IConvertible):
    """ enum WriteFileResult, values: Cancel (-1), Failure (0), Success (1) """
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

    Cancel = None
    Failure = None
    Success = None
    value__ = None


