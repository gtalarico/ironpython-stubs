# encoding: utf-8
# module System.Runtime.InteropServices.ComTypes calls itself ComTypes
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ADVF(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the requested behavior when setting up an advise sink or a caching connection with an object.
    
    enum (flags) ADVF, values: ADVF_DATAONSTOP (64), ADVF_NODATA (1), ADVF_ONLYONCE (4), ADVF_PRIMEFIRST (2), ADVFCACHE_FORCEBUILTIN (16), ADVFCACHE_NOHANDLER (8), ADVFCACHE_ONSAVE (32)
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

    ADVFCACHE_FORCEBUILTIN = None
    ADVFCACHE_NOHANDLER = None
    ADVFCACHE_ONSAVE = None
    ADVF_DATAONSTOP = None
    ADVF_NODATA = None
    ADVF_ONLYONCE = None
    ADVF_PRIMEFIRST = None
    value__ = None


class BINDPTR(object):
    """ Contains a pointer to a bound-to System.Runtime.InteropServices.FUNCDESC structure, System.Runtime.InteropServices.VARDESC structure, or an ITypeComp interface. """
    lpfuncdesc = None
    lptcomp = None
    lpvardesc = None


class BIND_OPTS(object):
    """ Stores the parameters that are used during a moniker binding operation. """
    cbStruct = None
    dwTickCountDeadline = None
    grfFlags = None
    grfMode = None


class CALLCONV(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the calling convention used by a method described in a METHODDATA Data Type structure.
    
    enum CALLCONV, values: CC_CDECL (1), CC_MACPASCAL (3), CC_MAX (9), CC_MPWCDECL (7), CC_MPWPASCAL (8), CC_MSCPASCAL (2), CC_PASCAL (2), CC_RESERVED (5), CC_STDCALL (4), CC_SYSCALL (6)
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

    CC_CDECL = None
    CC_MACPASCAL = None
    CC_MAX = None
    CC_MPWCDECL = None
    CC_MPWPASCAL = None
    CC_MSCPASCAL = None
    CC_PASCAL = None
    CC_RESERVED = None
    CC_STDCALL = None
    CC_SYSCALL = None
    value__ = None


class CONNECTDATA(object):
    """ Describes a connection that exists to a given connection point. """
    dwCookie = None
    pUnk = None


class DATADIR(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the direction of the data flow in the dwDirection parameter of the System.Runtime.InteropServices.ComTypes.IDataObject.EnumFormatEtc(System.Runtime.InteropServices.ComTypes.DATADIR) method. This determines the formats that the resulting enumerator can enumerate.
    
    enum DATADIR, values: DATADIR_GET (1), DATADIR_SET (2)
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

    DATADIR_GET = None
    DATADIR_SET = None
    value__ = None


class DESCKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the type description being bound to.
    
    enum DESCKIND, values: DESCKIND_FUNCDESC (1), DESCKIND_IMPLICITAPPOBJ (4), DESCKIND_MAX (5), DESCKIND_NONE (0), DESCKIND_TYPECOMP (3), DESCKIND_VARDESC (2)
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

    DESCKIND_FUNCDESC = None
    DESCKIND_IMPLICITAPPOBJ = None
    DESCKIND_MAX = None
    DESCKIND_NONE = None
    DESCKIND_TYPECOMP = None
    DESCKIND_VARDESC = None
    value__ = None


class DISPPARAMS(object):
    """ Contains the arguments passed to a method or property by IDispatch::Invoke. """
    cArgs = None
    cNamedArgs = None
    rgdispidNamedArgs = None
    rgvarg = None


class DVASPECT(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the desired data or view aspect of the object when drawing or getting data.
    
    enum (flags) DVASPECT, values: DVASPECT_CONTENT (1), DVASPECT_DOCPRINT (8), DVASPECT_ICON (4), DVASPECT_THUMBNAIL (2)
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

    DVASPECT_CONTENT = None
    DVASPECT_DOCPRINT = None
    DVASPECT_ICON = None
    DVASPECT_THUMBNAIL = None
    value__ = None


class ELEMDESC(object):
    """ Contains the type description and process transfer information for a variable, function, or a function parameter. """
    desc = None
    DESCUNION = None
    tdesc = None


class EXCEPINFO(object):
    """ Describes the exceptions that occur during IDispatch::Invoke. """
    bstrDescription = None
    bstrHelpFile = None
    bstrSource = None
    dwHelpContext = None
    pfnDeferredFillIn = None
    pvReserved = None
    scode = None
    wCode = None
    wReserved = None


class FILETIME(object):
    """ Represents the number of 100-nanosecond intervals since January 1, 1601. This structure is a 64-bit value. """
    dwHighDateTime = None
    dwLowDateTime = None


class FORMATETC(object):
    """ Represents a generalized Clipboard format. """
    cfFormat = None
    dwAspect = None
    lindex = None
    ptd = None
    tymed = None


class FUNCDESC(object):
    """ Defines a function description. """
    callconv = None
    cParams = None
    cParamsOpt = None
    cScodes = None
    elemdescFunc = None
    funckind = None
    invkind = None
    lprgelemdescParam = None
    lprgscode = None
    memid = None
    oVft = None
    wFuncFlags = None


class FUNCFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the constants that define the properties of a function.
    
    enum (flags) FUNCFLAGS, values: FUNCFLAG_FBINDABLE (4), FUNCFLAG_FDEFAULTBIND (32), FUNCFLAG_FDEFAULTCOLLELEM (256), FUNCFLAG_FDISPLAYBIND (16), FUNCFLAG_FHIDDEN (64), FUNCFLAG_FIMMEDIATEBIND (4096), FUNCFLAG_FNONBROWSABLE (1024), FUNCFLAG_FREPLACEABLE (2048), FUNCFLAG_FREQUESTEDIT (8), FUNCFLAG_FRESTRICTED (1), FUNCFLAG_FSOURCE (2), FUNCFLAG_FUIDEFAULT (512), FUNCFLAG_FUSESGETLASTERROR (128)
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

    FUNCFLAG_FBINDABLE = None
    FUNCFLAG_FDEFAULTBIND = None
    FUNCFLAG_FDEFAULTCOLLELEM = None
    FUNCFLAG_FDISPLAYBIND = None
    FUNCFLAG_FHIDDEN = None
    FUNCFLAG_FIMMEDIATEBIND = None
    FUNCFLAG_FNONBROWSABLE = None
    FUNCFLAG_FREPLACEABLE = None
    FUNCFLAG_FREQUESTEDIT = None
    FUNCFLAG_FRESTRICTED = None
    FUNCFLAG_FSOURCE = None
    FUNCFLAG_FUIDEFAULT = None
    FUNCFLAG_FUSESGETLASTERROR = None
    value__ = None


class FUNCKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines how to access a function.
    
    enum FUNCKIND, values: FUNC_DISPATCH (4), FUNC_NONVIRTUAL (2), FUNC_PUREVIRTUAL (1), FUNC_STATIC (3), FUNC_VIRTUAL (0)
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

    FUNC_DISPATCH = None
    FUNC_NONVIRTUAL = None
    FUNC_PUREVIRTUAL = None
    FUNC_STATIC = None
    FUNC_VIRTUAL = None
    value__ = None


class IAdviseSink:
    """ Provides a managed definition of the IAdviseSink interface. """
    def OnClose(self):
        """
        OnClose(self: IAdviseSink)
            Notifies all registered advisory sinks that the object has changed from the running state to the 
             loaded state.  This method is called by a server.
        """
        pass

    def OnDataChange(self, format, stgmedium):
        """
        OnDataChange(self: IAdviseSink, format: FORMATETC, stgmedium: STGMEDIUM) -> (FORMATETC, STGMEDIUM)
        
            Notifies all data objects currently registered advisory sinks that data in the object has 
             changed.
        
        
            format: A System.Runtime.InteropServices.ComTypes.FORMATETC, passed by reference, which describes the 
             format, target device, rendering, and storage information of the calling data object.
        
            stgmedium: A System.Runtime.InteropServices.ComTypes.STGMEDIUM, passed by reference, which defines the 
             storage medium (global memory, disk file, storage object, stream object, Graphics Device 
             Interface (GDI) object, or undefined) and ownership of that medium for the calling data object.
        """
        pass

    def OnRename(self, moniker):
        """
        OnRename(self: IAdviseSink, moniker: IMoniker)
            Notifies all registered advisory sinks that the object has been renamed. This method is called 
             by a server.
        
        
            moniker: A pointer to the IMoniker interface on the new full moniker of the object.
        """
        pass

    def OnSave(self):
        """
        OnSave(self: IAdviseSink)
            Notifies all registered advisory sinks that the object has been saved. This method is called by 
             a server.
        """
        pass

    def OnViewChange(self, aspect, index):
        """
        OnViewChange(self: IAdviseSink, aspect: int, index: int)
            Notifies an object's registered advisory sinks that its view has changed. This method is called 
             by a server.
        
        
            aspect: The aspect, or view, of the object. Contains a value taken from the 
             System.Runtime.InteropServices.ComTypes.DVASPECT enumeration.
        
            index: The portion of the view that has changed. Currently, only -1 is valid.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IBindCtx:
    """ Provides the managed definition of the IBindCtx interface. """
    def EnumObjectParam(self, ppenum):
        """
        EnumObjectParam(self: IBindCtx) -> IEnumString
        
            Enumerates the strings that are the keys of the internally maintained table of contextual object 
             parameters.
        """
        pass

    def GetBindOptions(self, pbindopts):
        """
        GetBindOptions(self: IBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS
        
            Returns the current binding options stored in the current bind context.
        
            pbindopts: A pointer to the structure to receive the binding options.
        """
        pass

    def GetObjectParam(self, pszKey, ppunk):
        """
        GetObjectParam(self: IBindCtx, pszKey: str) -> object
        
            Looks up the given key in the internally maintained table of contextual object parameters and 
             returns the corresponding object, if one exists.
        
        
            pszKey: The name of the object to search for.
        """
        pass

    def GetRunningObjectTable(self, pprot):
        """
        GetRunningObjectTable(self: IBindCtx) -> IRunningObjectTable
        
            Returns access to the Running Object Table (ROT) relevant to this binding process.
        """
        pass

    def RegisterObjectBound(self, punk):
        """
        RegisterObjectBound(self: IBindCtx, punk: object)
            Registers the passed object as one of the objects that has been bound during a moniker operation 
             and that should be released when the operation is complete.
        
        
            punk: The object to register for release.
        """
        pass

    def RegisterObjectParam(self, pszKey, punk):
        """
        RegisterObjectParam(self: IBindCtx, pszKey: str, punk: object)
            Registers the specified object pointer under the specified name in the internally maintained 
             table of object pointers.
        
        
            pszKey: The name to register punk with.
            punk: The object to register.
        """
        pass

    def ReleaseBoundObjects(self):
        """
        ReleaseBoundObjects(self: IBindCtx)
            Releases all the objects currently registered with the bind context by using the 
             System.Runtime.InteropServices.ComTypes.IBindCtx.RegisterObjectBound(System.Object) method.
        """
        pass

    def RevokeObjectBound(self, punk):
        """
        RevokeObjectBound(self: IBindCtx, punk: object)
            Removes the object from the set of registered objects that need to be released.
        
            punk: The object to unregister for release.
        """
        pass

    def RevokeObjectParam(self, pszKey):
        """
        RevokeObjectParam(self: IBindCtx, pszKey: str) -> int
        
            Revokes the registration of the object currently found under the specified key in the internally 
             maintained table of contextual object parameters, if that key is currently registered.
        
        
            pszKey: The key to unregister.
            Returns: An S_OKHRESULT value if the specified key was successfully removed from the table; otherwise, an 
             S_FALSEHRESULT value.
        """
        pass

    def SetBindOptions(self, pbindopts):
        """
        SetBindOptions(self: IBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS
        
            Stores a block of parameters in the bind context. These parameters will apply to later 
             UCOMIMoniker operations that use this bind context.
        
        
            pbindopts: The structure containing the binding options to set.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IConnectionPoint:
    """ Provides the managed definition of the IConnectionPoint interface. """
    def Advise(self, pUnkSink, pdwCookie):
        """
        Advise(self: IConnectionPoint, pUnkSink: object) -> int
        
            Establishes an advisory connection between the connection point and the caller's sink object.
        
            pUnkSink: A reference to the sink to receive calls for the outgoing interface managed by this connection 
             point.
        """
        pass

    def EnumConnections(self, ppEnum):
        """
        EnumConnections(self: IConnectionPoint) -> IEnumConnections
        
            Creates an enumerator object for iteration through the connections that exist to this connection 
             point.
        """
        pass

    def GetConnectionInterface(self, pIID):
        """
        GetConnectionInterface(self: IConnectionPoint) -> Guid
        
            Returns the IID of the outgoing interface managed by this connection point.
        """
        pass

    def GetConnectionPointContainer(self, ppCPC):
        """
        GetConnectionPointContainer(self: IConnectionPoint) -> IConnectionPointContainer
        
            Retrieves the IConnectionPointContainer interface pointer to the connectable object that 
             conceptually owns this connection point.
        """
        pass

    def Unadvise(self, dwCookie):
        """
        Unadvise(self: IConnectionPoint, dwCookie: int)
            Terminates an advisory connection previously established through the 
             System.Runtime.InteropServices.ComTypes.IConnectionPoint.Advise(System.Object,System.Int32@) 
             method.
        
        
            dwCookie: The connection cookie previously returned from the 
             System.Runtime.InteropServices.ComTypes.IConnectionPoint.Advise(System.Object,System.Int32@) 
             method.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IConnectionPointContainer:
    """ Provides the managed definition of the IConnectionPointContainer interface. """
    def EnumConnectionPoints(self, ppEnum):
        """
        EnumConnectionPoints(self: IConnectionPointContainer) -> IEnumConnectionPoints
        
            Creates an enumerator of all the connection points supported in the connectable object, one 
             connection point per IID.
        """
        pass

    def FindConnectionPoint(self, riid, ppCP):
        """
        FindConnectionPoint(self: IConnectionPointContainer, riid: Guid) -> (Guid, IConnectionPoint)
        
            Asks the connectable object if it has a connection point for a particular IID, and if so, 
             returns the IConnectionPoint interface pointer to that connection point.
        
        
            riid: A reference to the outgoing interface IID whose connection point is being requested.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDataObject:
    """ Provides the managed definition of the IDataObject interface. """
    def DAdvise(self, pFormatetc, advf, adviseSink, connection):
        """
        DAdvise(self: IDataObject, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink) -> (int, FORMATETC, int)
        
            Creates a connection between a data object and an advisory sink. This method is called by an 
             object that supports an advisory sink and enables the advisory sink to be notified of changes in 
             the object's data.
        
        
            pFormatetc: A System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, that defines 
             the format, target device, aspect, and medium that will be used for future notifications.
        
            advf: One of the System.Runtime.InteropServices.ComTypes.ADVF values that specifies a group of flags 
             for controlling the advisory connection.
        
            adviseSink: A pointer to the System.Runtime.InteropServices.ComTypes.IAdviseSink interface on the advisory 
             sink that will receive the change notification.
        
            Returns: This method supports the standard return values E_INVALIDARG, E_UNEXPECTED, and E_OUTOFMEMORY, 
             as well as the following: ValueDescriptionS_OKThe advisory connection was created.E_NOTIMPLThis 
             method is not implemented on the data object.DV_E_LINDEXThere is an invalid value for 
             System.Runtime.InteropServices.ComTypes.FORMATETC.lindex; currently, only -1 is 
             supported.DV_E_FORMATETCThere is an invalid value for the pFormatetc 
             parameter.OLE_E_ADVISENOTSUPPORTEDThe data object does not support change notification.
        """
        pass

    def DUnadvise(self, connection):
        """
        DUnadvise(self: IDataObject, connection: int)
            Destroys a notification connection that had been previously established.
        
            connection: A DWORD token that specifies the connection to remove. Use the value returned by 
             System.Runtime.InteropServices.ComTypes.IDataObject.DAdvise(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.ADVF,System.Runtime.InteropServices.ComType
             s.IAdviseSink,System.Int32@) when the connection was originally established.
        """
        pass

    def EnumDAdvise(self, enumAdvise):
        """
        EnumDAdvise(self: IDataObject) -> (int, IEnumSTATDATA)
        
            Creates an object that can be used to enumerate the current advisory connections.
            Returns: This method supports the standard return value E_OUTOFMEMORY, as well as the 
             following:ValueDescriptionS_OKThe enumerator object is successfully instantiated or there are no 
             connections.OLE_E_ADVISENOTSUPPORTEDThis object does not support advisory notifications.
        """
        pass

    def EnumFormatEtc(self, direction):
        """
        EnumFormatEtc(self: IDataObject, direction: DATADIR) -> IEnumFORMATETC
        
            Creates an object for enumerating the System.Runtime.InteropServices.ComTypes.FORMATETC 
             structures for a data object. These structures are used in calls to 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@) or 
             System.Runtime.InteropServices.ComTypes.IDataObject.SetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@,System.Boolean).
        
        
            direction: One of the System.Runtime.InteropServices.ComTypes.DATADIR values that specifies the direction 
             of the data.
        
            Returns: This method supports the standard return values E_INVALIDARG and E_OUTOFMEMORY, as well as the 
             following:ValueDescriptionS_OKThe enumerator object was successfully created.E_NOTIMPLThe 
             direction specified by the direction parameter is not supported.OLE_S_USEREGRequests that OLE 
             enumerate the formats from the registry.
        """
        pass

    def GetCanonicalFormatEtc(self, formatIn, formatOut):
        """
        GetCanonicalFormatEtc(self: IDataObject, formatIn: FORMATETC) -> (int, FORMATETC, FORMATETC)
        
            Provides a standard System.Runtime.InteropServices.ComTypes.FORMATETC structure that is 
             logically equivalent to a more complex structure. Use this method to determine whether two 
             different System.Runtime.InteropServices.ComTypes.FORMATETC structures would return the same 
             data, removing the need for duplicate rendering.
        
        
            formatIn: A pointer to a System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, 
             that defines the format, medium, and target device that the caller would like to use to retrieve 
             data in a subsequent call such as 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@). The 
             System.Runtime.InteropServices.ComTypes.TYMED member is not significant in this case and should 
             be ignored.
        
            Returns: This method supports the standard return values E_INVALIDARG, E_UNEXPECTED, and E_OUTOFMEMORY, 
             as well as the following: ValueDescriptionS_OKThe returned 
             System.Runtime.InteropServices.ComTypes.FORMATETC structure is different from the one that was 
             passed.DATA_S_SAMEFORMATETCThe System.Runtime.InteropServices.ComTypes.FORMATETC structures are 
             the same and null is returned in the formatOut parameter.DV_E_LINDEXThere is an invalid value 
             for System.Runtime.InteropServices.ComTypes.FORMATETC.lindex; currently, only -1 is 
             supported.DV_E_FORMATETCThere is an invalid value for the pFormatetc 
             parameter.OLE_E_NOTRUNNINGThe application is not running.
        """
        pass

    def GetData(self, format, medium):
        """
        GetData(self: IDataObject, format: FORMATETC) -> (FORMATETC, STGMEDIUM)
        
            Obtains data from a source data object. The 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@) method, which is called by a 
             data consumer, renders the data described in the specified 
             System.Runtime.InteropServices.ComTypes.FORMATETC structure and transfers it through the 
             specified System.Runtime.InteropServices.ComTypes.STGMEDIUM structure. The caller then assumes 
             responsibility for releasing the System.Runtime.InteropServices.ComTypes.STGMEDIUM structure.
        
        
            format: A pointer to a System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, 
             that defines the format, medium, and target device to use when passing the data. It is possible 
             to specify more than one medium by using the Boolean OR operator, allowing the method to choose 
             the best medium among those specified.
        """
        pass

    def GetDataHere(self, format, medium):
        """
        GetDataHere(self: IDataObject, format: FORMATETC, medium: STGMEDIUM) -> (FORMATETC, STGMEDIUM)
        
            Obtains data from a source data object. This method, which is called by a data consumer, differs 
             from the 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@) method in that the caller must 
             allocate and free the specified storage medium.
        
        
            format: A pointer to a System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, 
             that defines the format, medium, and target device to use when passing the data. Only one medium 
             can be specified in System.Runtime.InteropServices.ComTypes.TYMED, and only the following 
             System.Runtime.InteropServices.ComTypes.TYMED values are valid: 
             System.Runtime.InteropServices.ComTypes.TYMED.TYMED_ISTORAGE, 
             System.Runtime.InteropServices.ComTypes.TYMED.TYMED_ISTREAM, 
             System.Runtime.InteropServices.ComTypes.TYMED.TYMED_HGLOBAL, or 
             System.Runtime.InteropServices.ComTypes.TYMED.TYMED_FILE.
        
            medium: A System.Runtime.InteropServices.ComTypes.STGMEDIUM, passed by reference, that defines the 
             storage medium containing the data being transferred. The medium must be allocated by the caller 
             and filled in by 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetDataHere(System.Runtime.InteropServices.Co
             mTypes.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@). The caller must also free 
             the medium. The implementation of this method must always supply a value of null for the 
             System.Runtime.InteropServices.ComTypes.STGMEDIUM.pUnkForRelease member of the 
             System.Runtime.InteropServices.ComTypes.STGMEDIUM structure that this parameter points to.
        """
        pass

    def QueryGetData(self, format):
        """
        QueryGetData(self: IDataObject, format: FORMATETC) -> (int, FORMATETC)
        
            Determines whether the data object is capable of rendering the data described in the 
             System.Runtime.InteropServices.ComTypes.FORMATETC structure. Objects attempting a paste or drop 
             operation can call this method before calling 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@) to get an indication of 
             whether the operation may be successful.
        
        
            format: A pointer to a System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, 
             that defines the format, medium, and target device to use for the query.
        
            Returns: This method supports the standard return values E_INVALIDARG, E_UNEXPECTED, and E_OUTOFMEMORY, 
             as well as the following: ValueDescriptionS_OKA subsequent call to 
             System.Runtime.InteropServices.ComTypes.IDataObject.GetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@) would probably be 
             successful.DV_E_LINDEXAn invalid value for 
             System.Runtime.InteropServices.ComTypes.FORMATETC.lindex; currently, only -1 is 
             supported.DV_E_FORMATETCAn invalid value for the pFormatetc parameter.DV_E_TYMEDAn invalid 
             System.Runtime.InteropServices.ComTypes.FORMATETC.tymed value.DV_E_DVASPECTAn invalid 
             System.Runtime.InteropServices.ComTypes.FORMATETC.dwAspect value.OLE_E_NOTRUNNINGThe application 
             is not running.
        """
        pass

    def SetData(self, formatIn, medium, release):
        """
        SetData(self: IDataObject, formatIn: FORMATETC, medium: STGMEDIUM, release: bool) -> (FORMATETC, STGMEDIUM)
        
            Transfers data to the object that implements this method. This method is called by an object 
             that contains a data source.
        
        
            formatIn: A System.Runtime.InteropServices.ComTypes.FORMATETC structure, passed by reference, that defines 
             the format used by the data object when interpreting the data contained in the storage medium.
        
            medium: A System.Runtime.InteropServices.ComTypes.STGMEDIUM structure, passed by reference, that defines 
             the storage medium in which the data is being passed.
        
            release: true to specify that the data object called, which implements 
             System.Runtime.InteropServices.ComTypes.IDataObject.SetData(System.Runtime.InteropServices.ComTyp
             es.FORMATETC@,System.Runtime.InteropServices.ComTypes.STGMEDIUM@,System.Boolean), owns the 
             storage medium after the call returns. This means that the data object must free the medium 
             after it has been used by calling the ReleaseStgMedium function. false to specify that the 
             caller retains ownership of the storage medium, and the data object called uses the storage 
             medium for the duration of the call only.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDLDESC(object):
    """ Contains information needed for transferring a structure element, parameter, or function return value between processes. """
    dwReserved = None
    wIDLFlags = None


class IDLFLAG(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes how to transfer a structure element, parameter, or function return value between processes.
    
    enum (flags) IDLFLAG, values: IDLFLAG_FIN (1), IDLFLAG_FLCID (4), IDLFLAG_FOUT (2), IDLFLAG_FRETVAL (8), IDLFLAG_NONE (0)
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

    IDLFLAG_FIN = None
    IDLFLAG_FLCID = None
    IDLFLAG_FOUT = None
    IDLFLAG_FRETVAL = None
    IDLFLAG_NONE = None
    value__ = None


class IEnumConnectionPoints:
    """ Manages the definition of the IEnumConnectionPoints interface. """
    def Clone(self, ppenum):
        """
        Clone(self: IEnumConnectionPoints) -> IEnumConnectionPoints
        
            Creates a new enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumConnectionPoints, celt: int, pceltFetched: IntPtr) -> (int, Array[IConnectionPoint])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of IConnectionPoint references to return in rgelt.
            pceltFetched: When this method returns, contains a reference to the actual number of connections enumerated in 
             rgelt.
        
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumConnectionPoints)
            Resets the enumeration sequence to the beginning.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumConnectionPoints, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumConnections:
    """ Manages the definition of the IEnumConnections interface. """
    def Clone(self, ppenum):
        """
        Clone(self: IEnumConnections) -> IEnumConnections
        
            Creates a new enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumConnections, celt: int, pceltFetched: IntPtr) -> (int, Array[CONNECTDATA])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of System.Runtime.InteropServices.CONNECTDATA structures to return in rgelt.
            pceltFetched: When this method returns, contains a reference to the actual number of connections enumerated in 
             rgelt.
        
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumConnections)
            Resets the enumeration sequence to the beginning.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumConnections, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumFORMATETC:
    """ Provides the managed definition of the IEnumFORMATETC interface. """
    def Clone(self, newEnum):
        """
        Clone(self: IEnumFORMATETC) -> IEnumFORMATETC
        
            Creates a new enumerator that contains the same enumeration state as the current enumerator.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumFORMATETC, celt: int) -> (int, Array[FORMATETC], Array[int])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of System.Runtime.InteropServices.ComTypes.FORMATETC references to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumFORMATETC) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumFORMATETC, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumMoniker:
    """ Manages the definition of the IEnumMoniker interface. """
    def Clone(self, ppenum):
        """
        Clone(self: IEnumMoniker) -> IEnumMoniker
        
            Creates a new enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumMoniker, celt: int, pceltFetched: IntPtr) -> (int, Array[IMoniker])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of monikers to return in rgelt.
            pceltFetched: When this method returns, contains a reference to the actual number of monikers enumerated in 
             rgelt.
        
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumMoniker)
            Resets the enumeration sequence to the beginning.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumMoniker, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumSTATDATA:
    """ Provides the managed definition of the IEnumSTATDATA interface. """
    def Clone(self, newEnum):
        """
        Clone(self: IEnumSTATDATA) -> IEnumSTATDATA
        
            Creates a new enumerator that contains the same enumeration state as the current enumerator.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumSTATDATA, celt: int) -> (int, Array[STATDATA], Array[int])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of System.Runtime.InteropServices.ComTypes.STATDATA references to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumSTATDATA) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumSTATDATA, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumString:
    """ Manages the definition of the IEnumString interface. """
    def Clone(self, ppenum):
        """
        Clone(self: IEnumString) -> IEnumString
        
            Creates a new enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: IEnumString, celt: int, pceltFetched: IntPtr) -> (int, Array[str])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of strings to return in rgelt.
            pceltFetched: When this method returns, contains a reference to the actual number of strings enumerated in 
             rgelt.
        
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumString)
            Resets the enumeration sequence to the beginning.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumString, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumVARIANT:
    """ Manages the definition of the IEnumVARIANT interface. """
    def Clone(self):
        """
        Clone(self: IEnumVARIANT) -> IEnumVARIANT
        
            Creates a new enumerator that contains the same enumeration state as the current one.
            Returns: An System.Runtime.InteropServices.ComTypes.IEnumVARIANT  reference to the newly created 
             enumerator.
        """
        pass

    def Next(self, celt, rgVar, pceltFetched):
        """
        Next(self: IEnumVARIANT, celt: int, pceltFetched: IntPtr) -> (int, Array[object])
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of elements to return in rgelt.
            pceltFetched: When this method returns, contains a reference to the actual number of elements enumerated in 
             rgelt.
        
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: IEnumVARIANT) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: IEnumVARIANT, celt: int) -> int
        
            Skips a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMoniker:
    """ Provides the managed definition of the IMoniker interface, with COM functionality from IPersist and IPersistStream. """
    def BindToObject(self, pbc, pmkToLeft, riidResult, ppvResult):
        """
        BindToObject(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: Guid) -> (Guid, object)
        
            Uses the moniker to bind to the object that it identifies.
        
            pbc: A reference to the IBindCtx interface on the bind context object used in this binding operation.
            pmkToLeft: A reference to the moniker to the left of the current moniker, if the moniker is part of a 
             composite moniker.
        
            riidResult: The interface identifier (IID) of the interface that the client intends to use to communicate 
             with the object that the moniker identifies.
        """
        pass

    def BindToStorage(self, pbc, pmkToLeft, riid, ppvObj):
        """
        BindToStorage(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker, riid: Guid) -> (Guid, object)
        
            Retrieves an interface pointer to the storage that contains the object identified by the moniker.
        
            pbc: A reference to the IBindCtx interface on the bind context object used during this binding 
             operation.
        
            pmkToLeft: A reference to the moniker to the left of the current moniker, if the moniker is part of a 
             composite moniker.
        
            riid: The interface identifier (IID) of the storage interface requested.
        """
        pass

    def CommonPrefixWith(self, pmkOther, ppmkPrefix):
        """
        CommonPrefixWith(self: IMoniker, pmkOther: IMoniker) -> IMoniker
        
            Creates a new moniker based on the common prefix that this moniker shares with another moniker.
        
            pmkOther: A reference to the IMoniker interface on another moniker to compare with the current moniker for 
             a common prefix.
        """
        pass

    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric, ppmkComposite):
        """
        ComposeWith(self: IMoniker, pmkRight: IMoniker, fOnlyIfNotGeneric: bool) -> IMoniker
        
            Combines the current moniker with another moniker, creating a new composite moniker.
        
            pmkRight: A reference to the IMoniker interface on a moniker to append to the end of the current moniker.
            fOnlyIfNotGeneric: true to indicate that the caller requires a nongeneric composition. The operation proceeds only 
             if pmkRight is a moniker class that the current moniker can combine with in some way other than 
             forming a generic composite. false to indicate that the method can create a generic composite if 
             necessary.
        """
        pass

    def Enum(self, fForward, ppenumMoniker):
        """
        Enum(self: IMoniker, fForward: bool) -> IEnumMoniker
        
            Supplies a pointer to an enumerator that can enumerate the components of a composite moniker.
        
            fForward: true to enumerate the monikers from left to right. false to enumerate from right to left.
        """
        pass

    def GetClassID(self, pClassID):
        """
        GetClassID(self: IMoniker) -> Guid
        
            Retrieves the class identifier (CLSID) of an object.
        """
        pass

    def GetDisplayName(self, pbc, pmkToLeft, ppszDisplayName):
        """
        GetDisplayName(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker) -> str
        
            Gets the display name, which is a user-readable representation of the current moniker.
        
            pbc: A reference to the bind context to use in this operation.
            pmkToLeft: A reference to the moniker to the left of the current moniker, if the moniker is part of a 
             composite moniker.
        """
        pass

    def GetSizeMax(self, pcbSize):
        """
        GetSizeMax(self: IMoniker) -> Int64
        
            Returns the size, in bytes, of the stream needed to save the object.
        """
        pass

    def GetTimeOfLastChange(self, pbc, pmkToLeft, pFileTime):
        """
        GetTimeOfLastChange(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker) -> FILETIME
        
            Provides a number representing the time that the object identified by the current moniker was 
             last changed.
        
        
            pbc: A reference to the bind context to use in this binding operation.
            pmkToLeft: A reference to the moniker to the left of the current moniker, if the moniker is part of a 
             composite moniker.
        """
        pass

    def Hash(self, pdwHash):
        """
        Hash(self: IMoniker) -> int
        
            Calculates a 32-bit integer using the internal state of the moniker.
        """
        pass

    def Inverse(self, ppmk):
        """
        Inverse(self: IMoniker) -> IMoniker
        
            Provides a moniker that, when composed to the right of the current moniker or one of similar 
             structure, composes to nothing.
        """
        pass

    def IsDirty(self):
        """
        IsDirty(self: IMoniker) -> int
        
            Checks the object for changes since it was last saved.
            Returns: An S_OKHRESULT value if the object has changed; otherwise, an S_FALSEHRESULT value.
        """
        pass

    def IsEqual(self, pmkOtherMoniker):
        """
        IsEqual(self: IMoniker, pmkOtherMoniker: IMoniker) -> int
        
            Compares the current moniker with a specified moniker and indicates whether they are identical.
        
            pmkOtherMoniker: A reference to the moniker to use for comparison.
            Returns: An S_OKHRESULT value if the monikers are identical; otherwise, an S_FALSEHRESULT value.
        """
        pass

    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
        """
        IsRunning(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> int
        
            Determines whether the object that is identified by the current moniker is currently loaded and 
             running.
        
        
            pbc: A reference to the bind context to use in this binding operation.
            pmkToLeft: A reference to the moniker to the left of the current moniker if the current moniker is part of 
             a composite.
        
            pmkNewlyRunning: A reference to the moniker most recently added to the Running Object Table (ROT).
            Returns: An S_OKHRESULT value if the moniker is running; an S_FALSEHRESULT value if the moniker is not 
             running; or an E_UNEXPECTEDHRESULT value.
        """
        pass

    def IsSystemMoniker(self, pdwMksys):
        """
        IsSystemMoniker(self: IMoniker) -> (int, int)
        
            Indicates whether this moniker is of one of the system-supplied moniker classes.
            Returns: An S_OKHRESULT value if the moniker is a system moniker; otherwise, an S_FALSEHRESULT value.
        """
        pass

    def Load(self, pStm):
        """
        Load(self: IMoniker, pStm: IStream)
            Initializes an object from the stream where it was previously saved.
        
            pStm: The stream that the object is loaded from.
        """
        pass

    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName, pchEaten, ppmkOut):
        """
        ParseDisplayName(self: IMoniker, pbc: IBindCtx, pmkToLeft: IMoniker, pszDisplayName: str) -> (int, IMoniker)
        
            Reads as many characters of the specified display name as the 
             System.Runtime.InteropServices.ComTypes.IMoniker.ParseDisplayName(System.Runtime.InteropServices.
             ComTypes.IBindCtx,System.Runtime.InteropServices.ComTypes.IMoniker,System.String,System.Int32@,Sy
             stem.Runtime.InteropServices.ComTypes.IMoniker@) understands and builds a moniker corresponding 
             to the portion read.
        
        
            pbc: A reference to the bind context to use in this binding operation.
            pmkToLeft: A reference to the moniker that has been built from the display name up to this point.
            pszDisplayName: A reference to the string containing the remaining display name to parse.
        """
        pass

    def Reduce(self, pbc, dwReduceHowFar, ppmkToLeft, ppmkReduced):
        """
        Reduce(self: IMoniker, pbc: IBindCtx, dwReduceHowFar: int, ppmkToLeft: IMoniker) -> (IMoniker, IMoniker)
        
            Returns a reduced moniker, which is another moniker that refers to the same object as the 
             current moniker but can be bound with equal or greater efficiency.
        
        
            pbc: A reference to the IBindCtx interface on the bind context to use in this binding operation.
            dwReduceHowFar: A value that specifies how far the current moniker should be reduced.
            ppmkToLeft: A reference to the moniker to the left of the current moniker.
        """
        pass

    def RelativePathTo(self, pmkOther, ppmkRelPath):
        """
        RelativePathTo(self: IMoniker, pmkOther: IMoniker) -> IMoniker
        
            Supplies a moniker that, when appended to the current moniker (or one with a similar structure), 
             yields the specified moniker.
        
        
            pmkOther: A reference to the moniker to which a relative path should be taken.
        """
        pass

    def Save(self, pStm, fClearDirty):
        """
        Save(self: IMoniker, pStm: IStream, fClearDirty: bool)
            Saves an object to the specified stream.
        
            pStm: The stream to which the object is saved.
            fClearDirty: true to clear the modified flag after the save is complete; otherwise false
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMPLTYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the attributes of an implemented or inherited interface of a type.
    
    enum (flags) IMPLTYPEFLAGS, values: IMPLTYPEFLAG_FDEFAULT (1), IMPLTYPEFLAG_FDEFAULTVTABLE (8), IMPLTYPEFLAG_FRESTRICTED (4), IMPLTYPEFLAG_FSOURCE (2)
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

    IMPLTYPEFLAG_FDEFAULT = None
    IMPLTYPEFLAG_FDEFAULTVTABLE = None
    IMPLTYPEFLAG_FRESTRICTED = None
    IMPLTYPEFLAG_FSOURCE = None
    value__ = None


class INVOKEKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how to invoke a function by IDispatch::Invoke.
    
    enum (flags) INVOKEKIND, values: INVOKE_FUNC (1), INVOKE_PROPERTYGET (2), INVOKE_PROPERTYPUT (4), INVOKE_PROPERTYPUTREF (8)
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

    INVOKE_FUNC = None
    INVOKE_PROPERTYGET = None
    INVOKE_PROPERTYPUT = None
    INVOKE_PROPERTYPUTREF = None
    value__ = None


class IPersistFile:
    """ Provides the managed definition of the IPersistFile interface, with functionality from IPersist. """
    def GetClassID(self, pClassID):
        """
        GetClassID(self: IPersistFile) -> Guid
        
            Retrieves the class identifier (CLSID) of an object.
        """
        pass

    def GetCurFile(self, ppszFileName):
        """
        GetCurFile(self: IPersistFile) -> str
        
            Retrieves either the absolute path to the current working file of the object or, if there is no 
             current working file, the default file name prompt of the object.
        """
        pass

    def IsDirty(self):
        """
        IsDirty(self: IPersistFile) -> int
        
            Checks an object for changes since it was last saved to its current file.
            Returns: S_OK if the file has changed since it was last saved; S_FALSE if the file has not changed since 
             it was last saved.
        """
        pass

    def Load(self, pszFileName, dwMode):
        """
        Load(self: IPersistFile, pszFileName: str, dwMode: int)
            Opens the specified file and initializes an object from the file contents.
        
            pszFileName: A zero-terminated string containing the absolute path of the file to open.
            dwMode: A combination of values from the STGM enumeration to indicate the access mode in which to open 
             pszFileName.
        """
        pass

    def Save(self, pszFileName, fRemember):
        """
        Save(self: IPersistFile, pszFileName: str, fRemember: bool)
            Saves a copy of the object into the specified file.
        
            pszFileName: A zero-terminated string containing the absolute path of the file to which the object is saved.
            fRemember: true to used the pszFileName parameter as the current working file; otherwise false.
        """
        pass

    def SaveCompleted(self, pszFileName):
        """
        SaveCompleted(self: IPersistFile, pszFileName: str)
            Notifies the object that it can write to its file.
        
            pszFileName: The absolute path of the file where the object was previously saved.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IRunningObjectTable:
    """ Provides the managed definition of the IRunningObjectTable interface. """
    def EnumRunning(self, ppenumMoniker):
        """
        EnumRunning(self: IRunningObjectTable) -> IEnumMoniker
        
            Enumerates the objects currently registered as running.
        """
        pass

    def GetObject(self, pmkObjectName, ppunkObject):
        """
        GetObject(self: IRunningObjectTable, pmkObjectName: IMoniker) -> (int, object)
        
            Returns the registered object if the supplied object name is registered as running.
        
            pmkObjectName: A reference to the moniker to search for in the Running Object Table (ROT).
            Returns: An HRESULT value that indicates the success or failure of the operation.
        """
        pass

    def GetTimeOfLastChange(self, pmkObjectName, pfiletime):
        """
        GetTimeOfLastChange(self: IRunningObjectTable, pmkObjectName: IMoniker) -> (int, FILETIME)
        
            Searches for this moniker in the Running Object Table (ROT) and reports the recorded time of 
             change, if present.
        
        
            pmkObjectName: A reference to the moniker to search for in the Running Object Table (ROT).
            Returns: An HRESULT value that indicates the success or failure of the operation.
        """
        pass

    def IsRunning(self, pmkObjectName):
        """
        IsRunning(self: IRunningObjectTable, pmkObjectName: IMoniker) -> int
        
            Determines whether the specified moniker is currently registered in the Running Object Table 
             (ROT).
        
        
            pmkObjectName: A reference to the moniker to search for in the Running Object Table (ROT).
            Returns: An HRESULT value that indicates the success or failure of the operation.
        """
        pass

    def NoteChangeTime(self, dwRegister, pfiletime):
        """
        NoteChangeTime(self: IRunningObjectTable, dwRegister: int, pfiletime: FILETIME) -> FILETIME
        
            Notes the time that a particular object changed so IMoniker::GetTimeOfLastChange can report an 
             appropriate change time.
        
        
            dwRegister: The Running Object Table (ROT) entry of the changed object.
            pfiletime: A reference to the object's last change time.
        """
        pass

    def Register(self, grfFlags, punkObject, pmkObjectName):
        """
        Register(self: IRunningObjectTable, grfFlags: int, punkObject: object, pmkObjectName: IMoniker) -> int
        
            Registers that the supplied object has entered the running state.
        
            grfFlags: Specifies whether the Running Object Table's (ROT) reference to punkObject is weak or strong, 
             and controls access to the object through its entry in the ROT.
        
            punkObject: A reference to the object being registered as running.
            pmkObjectName: A reference to the moniker that identifies punkObject.
            Returns: A value that can be used to identify this ROT entry in subsequent calls to 
             System.Runtime.InteropServices.ComTypes.IRunningObjectTable.Revoke(System.Int32) or 
             System.Runtime.InteropServices.ComTypes.IRunningObjectTable.NoteChangeTime(System.Int32,System.Ru
             ntime.InteropServices.ComTypes.FILETIME@).
        """
        pass

    def Revoke(self, dwRegister):
        """
        Revoke(self: IRunningObjectTable, dwRegister: int)
            Unregisters the specified object from the Running Object Table (ROT).
        
            dwRegister: The Running Object Table (ROT) entry to revoke.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStream:
    """ Provides the managed definition of the IStream interface, with ISequentialStream functionality. """
    def Clone(self, ppstm):
        """
        Clone(self: IStream) -> IStream
        
            Creates a new stream object with its own seek pointer that references the same bytes as the 
             original stream.
        """
        pass

    def Commit(self, grfCommitFlags):
        """
        Commit(self: IStream, grfCommitFlags: int)
            Ensures that any changes made to a stream object that is open in transacted mode are reflected 
             in the parent storage.
        
        
            grfCommitFlags: A value that controls how the changes for the stream object are committed.
        """
        pass

    def CopyTo(self, pstm, cb, pcbRead, pcbWritten):
        """
        CopyTo(self: IStream, pstm: IStream, cb: Int64, pcbRead: IntPtr, pcbWritten: IntPtr)
            Copies a specified number of bytes from the current seek pointer in the stream to the current 
             seek pointer in another stream.
        
        
            pstm: A reference to the destination stream.
            cb: The number of bytes to copy from the source stream.
            pcbRead: On successful return, contains the actual number of bytes read from the source.
            pcbWritten: On successful return, contains the actual number of bytes written to the destination.
        """
        pass

    def LockRegion(self, libOffset, cb, dwLockType):
        """
        LockRegion(self: IStream, libOffset: Int64, cb: Int64, dwLockType: int)
            Restricts access to a specified range of bytes in the stream.
        
            libOffset: The byte offset for the beginning of the range.
            cb: The length of the range, in bytes, to restrict.
            dwLockType: The requested restrictions on accessing the range.
        """
        pass

    def Read(self, pv, cb, pcbRead):
        """
        Read(self: IStream, cb: int, pcbRead: IntPtr) -> Array[Byte]
        
            Reads a specified number of bytes from the stream object into memory starting at the current 
             seek pointer.
        
        
            cb: The number of bytes to read from the stream object.
            pcbRead: A pointer to a ULONG variable that receives the actual number of bytes read from the stream 
             object.
        """
        pass

    def Revert(self):
        """
        Revert(self: IStream)
            Discards all changes that have been made to a transacted stream since the last 
             System.Runtime.InteropServices.ComTypes.IStream.Commit(System.Int32) call.
        """
        pass

    def Seek(self, dlibMove, dwOrigin, plibNewPosition):
        """
        Seek(self: IStream, dlibMove: Int64, dwOrigin: int, plibNewPosition: IntPtr)
            Changes the seek pointer to a new location relative to the beginning of the stream, to the end 
             of the stream, or to the current seek pointer.
        
        
            dlibMove: The displacement to add to dwOrigin.
            dwOrigin: The origin of the seek. The origin can be the beginning of the file, the current seek pointer, 
             or the end of the file.
        
            plibNewPosition: On successful return, contains the offset of the seek pointer from the beginning of the stream.
        """
        pass

    def SetSize(self, libNewSize):
        """
        SetSize(self: IStream, libNewSize: Int64)
            Changes the size of the stream object.
        
            libNewSize: The new size of the stream as a number of bytes.
        """
        pass

    def Stat(self, pstatstg, grfStatFlag):
        """
        Stat(self: IStream, grfStatFlag: int) -> STATSTG
        
            Retrieves the System.Runtime.InteropServices.STATSTG structure for this stream.
        
            grfStatFlag: Members in the STATSTG structure that this method does not return, thus saving some memory 
             allocation operations.
        """
        pass

    def UnlockRegion(self, libOffset, cb, dwLockType):
        """
        UnlockRegion(self: IStream, libOffset: Int64, cb: Int64, dwLockType: int)
            Removes the access restriction on a range of bytes previously restricted with the 
             System.Runtime.InteropServices.ComTypes.IStream.LockRegion(System.Int64,System.Int64,System.Int32
             ) method.
        
        
            libOffset: The byte offset for the beginning of the range.
            cb: The length, in bytes, of the range to restrict.
            dwLockType: The access restrictions previously placed on the range.
        """
        pass

    def Write(self, pv, cb, pcbWritten):
        """
        Write(self: IStream, pv: Array[Byte], cb: int, pcbWritten: IntPtr)
            Writes a specified number of bytes into the stream object starting at the current seek pointer.
        
            pv: The buffer to write this stream to.
            cb: The number of bytes to write to the stream.
            pcbWritten: On successful return, contains the actual number of bytes written to the stream object. If the 
             caller sets this pointer to System.IntPtr.Zero, this method does not provide the actual number 
             of bytes written.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeComp:
    """ Provides the managed definition of the ITypeComp interface. """
    def Bind(self, szName, lHashVal, wFlags, ppTInfo, pDescKind, pBindPtr):
        """
        Bind(self: ITypeComp, szName: str, lHashVal: int, wFlags: Int16) -> (ITypeInfo, DESCKIND, BINDPTR)
        
            Maps a name to a member of a type, or binds global variables and functions contained in a type 
             library.
        
        
            szName: The name to bind.
            lHashVal: A hash value for szName computed by LHashValOfNameSys.
            wFlags: A flags word containing one or more of the invoke flags defined in the INVOKEKIND enumeration.
        """
        pass

    def BindType(self, szName, lHashVal, ppTInfo, ppTComp):
        """
        BindType(self: ITypeComp, szName: str, lHashVal: int) -> (ITypeInfo, ITypeComp)
        
            Binds to the type descriptions contained within a type library.
        
            szName: The name to bind.
            lHashVal: A hash value for szName determined by LHashValOfNameSys.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeInfo:
    """ Provides the managed definition of the Component Automation ITypeInfo interface. """
    def AddressOfMember(self, memid, invKind, ppv):
        """
        AddressOfMember(self: ITypeInfo, memid: int, invKind: INVOKEKIND) -> IntPtr
        
            Retrieves the addresses of static functions or variables, such as those defined in a DLL.
        
            memid: The member ID of the static member's address to retrieve.
            invKind: One of the System.Runtime.InteropServices.ComTypes.INVOKEKIND  values that specifies whether the 
             member is a property, and if so, what kind.
        """
        pass

    def CreateInstance(self, pUnkOuter, riid, ppvObj):
        """
        CreateInstance(self: ITypeInfo, pUnkOuter: object, riid: Guid) -> (Guid, object)
        
            Creates a new instance of a type that describes a component class (coclass).
        
            pUnkOuter: The object that acts as the controlling IUnknown.
            riid: The IID of the interface that the caller uses to communicate with the resulting object.
        """
        pass

    def GetContainingTypeLib(self, ppTLB, pIndex):
        """
        GetContainingTypeLib(self: ITypeInfo) -> (ITypeLib, int)
        
            Retrieves the type library that contains this type description and its index within that type 
             library.
        """
        pass

    def GetDllEntry(self, memid, invKind, pBstrDllName, pBstrName, pwOrdinal):
        """
        GetDllEntry(self: ITypeInfo, memid: int, invKind: INVOKEKIND, pBstrDllName: IntPtr, pBstrName: IntPtr, pwOrdinal: IntPtr)
            Retrieves a description or specification of an entry point for a function in a DLL.
        
            memid: The ID of the member function whose DLL entry description is to be returned.
            invKind: One of the System.Runtime.InteropServices.ComTypes.INVOKEKIND values that specifies the kind of 
             member identified by memid.
        
            pBstrDllName: If not null, the function sets pBstrDllName to a BSTR that contains the name of the DLL.
            pBstrName: If not null, the function sets lpbstrName to a BSTR that contains the name of the entry point.
            pwOrdinal: If not null, and the function is defined by an ordinal, then lpwOrdinal is set to point to the 
             ordinal.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: ITypeInfo, index: int) -> (str, str, int, str)
        
            Retrieves the documentation string, the complete Help file name and path, and the context ID for 
             the Help topic for a specified type description.
        
        
            index: The ID of the member whose documentation is to be returned.
        """
        pass

    def GetFuncDesc(self, index, ppFuncDesc):
        """
        GetFuncDesc(self: ITypeInfo, index: int) -> IntPtr
        
            Retrieves the System.Runtime.InteropServices.FUNCDESC structure that contains information about 
             a specified function.
        
        
            index: The index of the function description to return.
        """
        pass

    def GetIDsOfNames(self, rgszNames, cNames, pMemId):
        """
        GetIDsOfNames(self: ITypeInfo, rgszNames: Array[str], cNames: int) -> Array[int]
        
            Maps between member names and member IDs, and parameter names and parameter IDs.
        
            rgszNames: An array of names to map.
            cNames: The count of names to map.
        """
        pass

    def GetImplTypeFlags(self, index, pImplTypeFlags):
        """
        GetImplTypeFlags(self: ITypeInfo, index: int) -> IMPLTYPEFLAGS
        
            Retrieves the System.Runtime.InteropServices.IMPLTYPEFLAGS value for one implemented interface 
             or base interface in a type description.
        
        
            index: The index of the implemented interface or base interface.
        """
        pass

    def GetMops(self, memid, pBstrMops):
        """
        GetMops(self: ITypeInfo, memid: int) -> str
        
            Retrieves marshaling information.
        
            memid: The member ID that indicates which marshaling information is needed.
        """
        pass

    def GetNames(self, memid, rgBstrNames, cMaxNames, pcNames):
        """
        GetNames(self: ITypeInfo, memid: int, cMaxNames: int) -> (Array[str], int)
        
            Retrieves the variable with the specified member ID (or the name of the property or method and 
             its parameters) that corresponds to the specified function ID.
        
        
            memid: The ID of the member whose name (or names) is to be returned.
            cMaxNames: The length of the rgBstrNames array.
        """
        pass

    def GetRefTypeInfo(self, hRef, ppTI):
        """
        GetRefTypeInfo(self: ITypeInfo, hRef: int) -> ITypeInfo
        
            Retrieves the referenced type descriptions if a type description references other type 
             descriptions.
        
        
            hRef: A handle to the referenced type description to return.
        """
        pass

    def GetRefTypeOfImplType(self, index, href):
        """
        GetRefTypeOfImplType(self: ITypeInfo, index: int) -> int
        
            Retrieves the type description of the implemented interface types if a type description 
             describes a COM class.
        
        
            index: The index of the implemented type whose handle is returned.
        """
        pass

    def GetTypeAttr(self, ppTypeAttr):
        """
        GetTypeAttr(self: ITypeInfo) -> IntPtr
        
            Retrieves a System.Runtime.InteropServices.TYPEATTR structure that contains the attributes of 
             the type description.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: ITypeInfo) -> ITypeComp
        
            Retrieves the ITypeComp interface for the type description, which enables a client compiler to 
             bind to the type description's members.
        """
        pass

    def GetVarDesc(self, index, ppVarDesc):
        """
        GetVarDesc(self: ITypeInfo, index: int) -> IntPtr
        
            Retrieves a VARDESC structure that describes the specified variable.
        
            index: The index of the variable description to return.
        """
        pass

    def Invoke(self, pvInstance, memid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: ITypeInfo, pvInstance: object, memid: int, wFlags: Int16, pDispParams: DISPPARAMS, pVarResult: IntPtr, pExcepInfo: IntPtr) -> (DISPPARAMS, int)
        
            Invokes a method, or accesses a property of an object, that implements the interface described 
             by the type description.
        
        
            pvInstance: A reference to the interface described by this type description.
            memid: A value that identifies the interface member.
            wFlags: Flags that describe the context of the invoke call.
            pDispParams: A reference to a structure that contains an array of arguments, an array of DISPIDs for named 
             arguments, and counts of the number of elements in each array.
        
            pVarResult: A reference to the location at which the result is to be stored. If wFlags specifies 
             DISPATCH_PROPERTYPUT or DISPATCH_PROPERTYPUTREF, pVarResult is ignored. Set to null if no result 
             is desired.
        
            pExcepInfo: A pointer to an exception information structure, which is filled in only if DISP_E_EXCEPTION is 
             returned.
        """
        pass

    def ReleaseFuncDesc(self, pFuncDesc):
        """
        ReleaseFuncDesc(self: ITypeInfo, pFuncDesc: IntPtr)
            Releases a System.Runtime.InteropServices.FUNCDESC structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetFuncDesc(System.Int32,System.IntPtr@) 
             method.
        
        
            pFuncDesc: A reference to the FUNCDESC structure to release.
        """
        pass

    def ReleaseTypeAttr(self, pTypeAttr):
        """
        ReleaseTypeAttr(self: ITypeInfo, pTypeAttr: IntPtr)
            Releases a System.Runtime.InteropServices.TYPEATTR structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetTypeAttr(System.IntPtr@) method.
        
        
            pTypeAttr: A reference to the TYPEATTR structure to release.
        """
        pass

    def ReleaseVarDesc(self, pVarDesc):
        """
        ReleaseVarDesc(self: ITypeInfo, pVarDesc: IntPtr)
            Releases a VARDESC structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetVarDesc(System.Int32,System.IntPtr@) 
             method.
        
        
            pVarDesc: A reference to the VARDESC structure to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeInfo2(ITypeInfo):
    """ Provides the managed definition of the ITypeInfo2 interface. """
    def AddressOfMember(self, memid, invKind, ppv):
        """
        AddressOfMember(self: ITypeInfo2, memid: int, invKind: INVOKEKIND) -> IntPtr
        
            Retrieves the addresses of static functions or variables, such as those defined in a DLL.
        
            memid: The member ID of the static member's address to retrieve.
            invKind: One of the System.Runtime.InteropServices.ComTypes.INVOKEKIND  values that specifies whether the 
             member is a property, and if so, what kind.
        """
        pass

    def CreateInstance(self, pUnkOuter, riid, ppvObj):
        """
        CreateInstance(self: ITypeInfo2, pUnkOuter: object, riid: Guid) -> (Guid, object)
        
            Creates a new instance of a type that describes a component class (coclass).
        
            pUnkOuter: An object that acts as the controlling IUnknown.
            riid: The IID of the interface that the caller uses to communicate with the resulting object.
        """
        pass

    def GetAllCustData(self, pCustData):
        """
        GetAllCustData(self: ITypeInfo2, pCustData: IntPtr)
            Gets all custom data items for the library.
        
            pCustData: A pointer to CUSTDATA, which holds all custom data items.
        """
        pass

    def GetAllFuncCustData(self, index, pCustData):
        """
        GetAllFuncCustData(self: ITypeInfo2, index: int, pCustData: IntPtr)
            Gets all custom data from the specified function.
        
            index: The index of the function to get the custom data for.
            pCustData: A pointer to CUSTDATA, which holds all custom data items.
        """
        pass

    def GetAllImplTypeCustData(self, index, pCustData):
        """
        GetAllImplTypeCustData(self: ITypeInfo2, index: int, pCustData: IntPtr)
            Gets all custom data for the specified implementation type.
        
            index: The index of the implementation type for the custom data.
            pCustData: A pointer to CUSTDATA which holds all custom data items.
        """
        pass

    def GetAllParamCustData(self, indexFunc, indexParam, pCustData):
        """
        GetAllParamCustData(self: ITypeInfo2, indexFunc: int, indexParam: int, pCustData: IntPtr)
            Gets all of the custom data for the specified function parameter.
        
            indexFunc: The index of the function to get the custom data for.
            indexParam: The index of the parameter of this function to get the custom data for.
            pCustData: A pointer to CUSTDATA, which holds all custom data items.
        """
        pass

    def GetAllVarCustData(self, index, pCustData):
        """
        GetAllVarCustData(self: ITypeInfo2, index: int, pCustData: IntPtr)
            Gets the variable for the custom data.
        
            index: The index of the variable to get the custom data for.
            pCustData: A pointer to CUSTDATA, which holds all custom data items.
        """
        pass

    def GetContainingTypeLib(self, ppTLB, pIndex):
        """
        GetContainingTypeLib(self: ITypeInfo2) -> (ITypeLib, int)
        
            Retrieves the type library that contains this type description and its index within that type 
             library.
        """
        pass

    def GetCustData(self, guid, pVarVal):
        """
        GetCustData(self: ITypeInfo2, guid: Guid) -> (Guid, object)
        
            Gets the custom data.
        
            guid: The GUID used to identify the data.
        """
        pass

    def GetDllEntry(self, memid, invKind, pBstrDllName, pBstrName, pwOrdinal):
        """
        GetDllEntry(self: ITypeInfo2, memid: int, invKind: INVOKEKIND, pBstrDllName: IntPtr, pBstrName: IntPtr, pwOrdinal: IntPtr)
            Retrieves a description or specification of an entry point for a function in a DLL.
        
            memid: The ID of the member function whose DLL entry description is to be returned.
            invKind: One of the System.Runtime.InteropServices.ComTypes.INVOKEKIND values that specifies the kind of 
             member identified by memid.
        
            pBstrDllName: If not null, the function sets pBstrDllName to a BSTR that contains the name of the DLL.
            pBstrName: If not null, the function sets lpbstrName to a BSTR that contains the name of the entry point.
            pwOrdinal: If not null, and the function is defined by an ordinal, then lpwOrdinal is set to point to the 
             ordinal.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: ITypeInfo2, index: int) -> (str, str, int, str)
        
            Retrieves the documentation string, the complete Help file name and path, and the context ID for 
             the Help topic for a specified type description.
        
        
            index: The ID of the member whose documentation is to be returned.
        """
        pass

    def GetDocumentation2(self, memid, pbstrHelpString, pdwHelpStringContext, pbstrHelpStringDll):
        """
        GetDocumentation2(self: ITypeInfo2, memid: int) -> (str, int, str)
        
            Retrieves the documentation string, the complete Help file name and path, the localization 
             context to use, and the context ID for the library Help topic in the Help file.
        
        
            memid: The member identifier for the type description.
        """
        pass

    def GetFuncCustData(self, index, guid, pVarVal):
        """
        GetFuncCustData(self: ITypeInfo2, index: int, guid: Guid) -> (Guid, object)
        
            Gets the custom data from the specified function.
        
            index: The index of the function to get the custom data for.
            guid: The GUID used to identify the data.
        """
        pass

    def GetFuncDesc(self, index, ppFuncDesc):
        """
        GetFuncDesc(self: ITypeInfo2, index: int) -> IntPtr
        
            Retrieves the System.Runtime.InteropServices.FUNCDESC structure that contains information about 
             a specified function.
        
        
            index: The index of the function description to return.
        """
        pass

    def GetFuncIndexOfMemId(self, memid, invKind, pFuncIndex):
        """
        GetFuncIndexOfMemId(self: ITypeInfo2, memid: int, invKind: INVOKEKIND) -> int
        
            Binds to a specific member based on a known DISPID, where the member name is not known (for 
             example, when binding to a default member).
        
        
            memid: The member identifier.
            invKind: One of the System.Runtime.InteropServices.ComTypes.INVOKEKIND values that specifies the kind of 
             member identified by memid.
        """
        pass

    def GetIDsOfNames(self, rgszNames, cNames, pMemId):
        """
        GetIDsOfNames(self: ITypeInfo2, rgszNames: Array[str], cNames: int) -> Array[int]
        
            Maps between member names and member IDs, and parameter names and parameter IDs.
        
            rgszNames: An array of names to map.
            cNames: The count of names to map.
        """
        pass

    def GetImplTypeCustData(self, index, guid, pVarVal):
        """
        GetImplTypeCustData(self: ITypeInfo2, index: int, guid: Guid) -> (Guid, object)
        
            Gets the implementation type of the custom data.
        
            index: The index of the implementation type for the custom data.
            guid: The GUID used to identify the data.
        """
        pass

    def GetImplTypeFlags(self, index, pImplTypeFlags):
        """
        GetImplTypeFlags(self: ITypeInfo2, index: int) -> IMPLTYPEFLAGS
        
            Retrieves the System.Runtime.InteropServices.IMPLTYPEFLAGS value for one implemented interface 
             or base interface in a type description.
        
        
            index: The index of the implemented interface or base interface.
        """
        pass

    def GetMops(self, memid, pBstrMops):
        """
        GetMops(self: ITypeInfo2, memid: int) -> str
        
            Retrieves marshaling information.
        
            memid: The member ID that indicates which marshaling information is needed.
        """
        pass

    def GetNames(self, memid, rgBstrNames, cMaxNames, pcNames):
        """
        GetNames(self: ITypeInfo2, memid: int, cMaxNames: int) -> (Array[str], int)
        
            Retrieves the variable with the specified member ID (or the name of the property or method and 
             its parameters) that corresponds to the specified function ID.
        
        
            memid: The ID of the member whose name (or names) is to be returned.
            cMaxNames: The length of the rgBstrNames array.
        """
        pass

    def GetParamCustData(self, indexFunc, indexParam, guid, pVarVal):
        """
        GetParamCustData(self: ITypeInfo2, indexFunc: int, indexParam: int, guid: Guid) -> (Guid, object)
        
            Gets the specified custom data parameter.
        
            indexFunc: The index of the function to get the custom data for.
            indexParam: The index of the parameter of this function to get the custom data for.
            guid: The GUID used to identify the data.
        """
        pass

    def GetRefTypeInfo(self, hRef, ppTI):
        """
        GetRefTypeInfo(self: ITypeInfo2, hRef: int) -> ITypeInfo
        
            Retrieves the referenced type descriptions, if a type description references other type 
             descriptions.
        
        
            hRef: A handle to the referenced type description to return.
        """
        pass

    def GetRefTypeOfImplType(self, index, href):
        """
        GetRefTypeOfImplType(self: ITypeInfo2, index: int) -> int
        
            Retrieves the type description of the implemented interface types, if a type description 
             describes a COM class.
        
        
            index: The index of the implemented type whose handle is returned.
        """
        pass

    def GetTypeAttr(self, ppTypeAttr):
        """
        GetTypeAttr(self: ITypeInfo2) -> IntPtr
        
            Retrieves a System.Runtime.InteropServices.TYPEATTR structure that contains the attributes of 
             the type description.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: ITypeInfo2) -> ITypeComp
        
            Retrieves the ITypeComp interface for the type description, which enables a client compiler to 
             bind to the type description's members.
        """
        pass

    def GetTypeFlags(self, pTypeFlags):
        """
        GetTypeFlags(self: ITypeInfo2) -> int
        
            Returns the type flags without any allocations. This method returns a DWORD type flag, which 
             expands the type flags without growing the TYPEATTR (type attribute).
        """
        pass

    def GetTypeKind(self, pTypeKind):
        """
        GetTypeKind(self: ITypeInfo2) -> TYPEKIND
        
            Returns the TYPEKIND enumeration quickly, without doing any allocations.
        """
        pass

    def GetVarCustData(self, index, guid, pVarVal):
        """
        GetVarCustData(self: ITypeInfo2, index: int, guid: Guid) -> (Guid, object)
        
            Gets the variable for the custom data.
        
            index: The index of the variable to get the custom data for.
            guid: The GUID used to identify the data.
        """
        pass

    def GetVarDesc(self, index, ppVarDesc):
        """
        GetVarDesc(self: ITypeInfo2, index: int) -> IntPtr
        
            Retrieves a VARDESC structure that describes the specified variable.
        
            index: The index of the variable description to return.
        """
        pass

    def GetVarIndexOfMemId(self, memid, pVarIndex):
        """
        GetVarIndexOfMemId(self: ITypeInfo2, memid: int) -> int
        
            Binds to a specific member based on a known DISPID, where the member name is not known (for 
             example, when binding to a default member).
        
        
            memid: The member identifier.
        """
        pass

    def Invoke(self, pvInstance, memid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: ITypeInfo2, pvInstance: object, memid: int, wFlags: Int16, pDispParams: DISPPARAMS, pVarResult: IntPtr, pExcepInfo: IntPtr) -> (DISPPARAMS, int)
        
            Invokes a method, or accesses a property of an object, that implements the interface described 
             by the type description.
        
        
            pvInstance: A reference to the interface described by this type description.
            memid: Identifier of the interface member.
            wFlags: Flags describing the context of the invoke call.
            pDispParams: A reference to a structure that contains an array of arguments, an array of DISPIDs for named 
             arguments, and counts of the number of elements in each array.
        
            pVarResult: A reference to the location at which the result is to be stored. If wFlags specifies 
             DISPATCH_PROPERTYPUT or DISPATCH_PROPERTYPUTREF, pVarResult is ignored. Set to null if no result 
             is desired.
        
            pExcepInfo: A pointer to an exception information structure, which is filled in only if DISP_E_EXCEPTION is 
             returned.
        """
        pass

    def ReleaseFuncDesc(self, pFuncDesc):
        """
        ReleaseFuncDesc(self: ITypeInfo2, pFuncDesc: IntPtr)
            Releases a System.Runtime.InteropServices.FUNCDESC structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetFuncDesc(System.Int32,System.IntPtr@) 
             method.
        
        
            pFuncDesc: A reference to the FUNCDESC structure to release.
        """
        pass

    def ReleaseTypeAttr(self, pTypeAttr):
        """
        ReleaseTypeAttr(self: ITypeInfo2, pTypeAttr: IntPtr)
            Releases a System.Runtime.InteropServices.TYPEATTR structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetTypeAttr(System.IntPtr@) method.
        
        
            pTypeAttr: A reference to the TYPEATTR structure to release.
        """
        pass

    def ReleaseVarDesc(self, pVarDesc):
        """
        ReleaseVarDesc(self: ITypeInfo2, pVarDesc: IntPtr)
            Releases a VARDESC structure previously returned by the 
             System.Runtime.InteropServices.ComTypes.ITypeInfo.GetVarDesc(System.Int32,System.IntPtr@) 
             method.
        
        
            pVarDesc: A reference to the VARDESC structure to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLib:
    """ Provides the managed definition of the ITypeLib interface. """
    def FindName(self, szNameBuf, lHashVal, ppTInfo, rgMemId, pcFound):
        """
        FindName(self: ITypeLib, szNameBuf: str, lHashVal: int, pcFound: Int16) -> (Array[ITypeInfo], Array[int], Int16)
        
            Finds occurrences of a type description in a type library.
        
            szNameBuf: The name to search for. This is an in/out parameter.
            lHashVal: A hash value to speed up the search, computed by the LHashValOfNameSys function. If lHashVal is 
             0, a value is computed.
        
            pcFound: On entry, indicates how many instances to look for. For example, pcFound = 1 can be called to 
             find the first occurrence. The search stops when one instance is found.On exit, indicates the 
             number of instances that were found. If the in and out values of pcFound are identical, there 
             might be more type descriptions that contain the name.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: ITypeLib, index: int) -> (str, str, int, str)
        
            Retrieves the library's documentation string, the complete Help file name and path, and the 
             context identifier for the library Help topic in the Help file.
        
        
            index: The index of the type description whose documentation is to be returned.
        """
        pass

    def GetLibAttr(self, ppTLibAttr):
        """
        GetLibAttr(self: ITypeLib) -> IntPtr
        
            Retrieves the structure that contains the library's attributes.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: ITypeLib) -> ITypeComp
        
            Enables a client compiler to bind to a library's types, variables, constants, and global 
             functions.
        """
        pass

    def GetTypeInfo(self, index, ppTI):
        """
        GetTypeInfo(self: ITypeLib, index: int) -> ITypeInfo
        
            Retrieves the specified type description in the library.
        
            index: The index of the ITypeInfo interface to return.
        """
        pass

    def GetTypeInfoCount(self):
        """
        GetTypeInfoCount(self: ITypeLib) -> int
        
            Returns the number of type descriptions in the type library.
            Returns: The number of type descriptions in the type library.
        """
        pass

    def GetTypeInfoOfGuid(self, guid, ppTInfo):
        """
        GetTypeInfoOfGuid(self: ITypeLib, guid: Guid) -> (Guid, ITypeInfo)
        
            Retrieves the type description that corresponds to the specified GUID.
        
            guid: The IID of the interface or CLSID of the class whose type info is requested.
        """
        pass

    def GetTypeInfoType(self, index, pTKind):
        """
        GetTypeInfoType(self: ITypeLib, index: int) -> TYPEKIND
        
            Retrieves the type of a type description.
        
            index: The index of the type description within the type library.
        """
        pass

    def IsName(self, szNameBuf, lHashVal):
        """
        IsName(self: ITypeLib, szNameBuf: str, lHashVal: int) -> bool
        
            Indicates whether a passed-in string contains the name of a type or member described in the 
             library.
        
        
            szNameBuf: The string to test. This is an in/out parameter.
            lHashVal: The hash value of szNameBuf.
            Returns: true if szNameBuf was found in the type library; otherwise, false.
        """
        pass

    def ReleaseTLibAttr(self, pTLibAttr):
        """
        ReleaseTLibAttr(self: ITypeLib, pTLibAttr: IntPtr)
            Releases the System.Runtime.InteropServices.TYPELIBATTR structure originally obtained from the 
             System.Runtime.InteropServices.ComTypes.ITypeLib.GetLibAttr(System.IntPtr@) method.
        
        
            pTLibAttr: The TLIBATTR structure to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLib2(ITypeLib):
    """ Provides a managed definition of the ITypeLib2 interface. """
    def FindName(self, szNameBuf, lHashVal, ppTInfo, rgMemId, pcFound):
        """
        FindName(self: ITypeLib2, szNameBuf: str, lHashVal: int, pcFound: Int16) -> (Array[ITypeInfo], Array[int], Int16)
        
            Finds occurrences of a type description in a type library.
        
            szNameBuf: The name to search for.
            lHashVal: A hash value to speed up the search, computed by the LHashValOfNameSys function. If lHashVal is 
             0, a value is computed.
        
            pcFound: On entry, a value, passed by reference, that indicates how many instances to look for. For 
             example, pcFound = 1 can be called to find the first occurrence. The search stops when one 
             instance is found.On exit, indicates the number of instances that were found. If the in and out 
             values of pcFound are identical, there might be more type descriptions that contain the name.
        """
        pass

    def GetAllCustData(self, pCustData):
        """
        GetAllCustData(self: ITypeLib2, pCustData: IntPtr)
            Gets all custom data items for the library.
        
            pCustData: A pointer to CUSTDATA, which holds all custom data items.
        """
        pass

    def GetCustData(self, guid, pVarVal):
        """
        GetCustData(self: ITypeLib2, guid: Guid) -> (Guid, object)
        
            Gets the custom data.
        
            guid: A System.Guid , passed by reference, that is used to identify the data.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: ITypeLib2, index: int) -> (str, str, int, str)
        
            Retrieves the library's documentation string, the complete Help file name and path, and the 
             context identifier for the library Help topic in the Help file.
        
        
            index: An index of the type description whose documentation is to be returned.
        """
        pass

    def GetDocumentation2(self, index, pbstrHelpString, pdwHelpStringContext, pbstrHelpStringDll):
        """
        GetDocumentation2(self: ITypeLib2, index: int) -> (str, int, str)
        
            Retrieves the library's documentation string, the complete Help file name and path, the 
             localization context to use, and the context ID for the library Help topic in the Help file.
        
        
            index: An index of the type description whose documentation is to be returned; if index is -1, the 
             documentation for the library is returned.
        """
        pass

    def GetLibAttr(self, ppTLibAttr):
        """
        GetLibAttr(self: ITypeLib2) -> IntPtr
        
            Retrieves the structure that contains the library's attributes.
        """
        pass

    def GetLibStatistics(self, pcUniqueNames, pcchUniqueNames):
        """
        GetLibStatistics(self: ITypeLib2, pcUniqueNames: IntPtr) -> int
        
            Returns statistics about a type library that are required for efficient sizing of hash tables.
        
            pcUniqueNames: A pointer to a count of unique names. If the caller does not need this information, set to null.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: ITypeLib2) -> ITypeComp
        
            Enables a client compiler to bind to a library's types, variables, constants, and global 
             functions.
        """
        pass

    def GetTypeInfo(self, index, ppTI):
        """
        GetTypeInfo(self: ITypeLib2, index: int) -> ITypeInfo
        
            Retrieves the specified type description in the library.
        
            index: An index of the ITypeInfo interface to return.
        """
        pass

    def GetTypeInfoCount(self):
        """
        GetTypeInfoCount(self: ITypeLib2) -> int
        
            Returns the number of type descriptions in the type library.
            Returns: The number of type descriptions in the type library.
        """
        pass

    def GetTypeInfoOfGuid(self, guid, ppTInfo):
        """
        GetTypeInfoOfGuid(self: ITypeLib2, guid: Guid) -> (Guid, ITypeInfo)
        
            Retrieves the type description that corresponds to the specified GUID.
        
            guid: The System.Guid, passed by reference, that represents the IID of the CLSID interface of the 
             class whose type info is requested.
        """
        pass

    def GetTypeInfoType(self, index, pTKind):
        """
        GetTypeInfoType(self: ITypeLib2, index: int) -> TYPEKIND
        
            Retrieves the type of a type description.
        
            index: The index of the type description within the type library.
        """
        pass

    def IsName(self, szNameBuf, lHashVal):
        """
        IsName(self: ITypeLib2, szNameBuf: str, lHashVal: int) -> bool
        
            Indicates whether a passed-in string contains the name of a type or member described in the 
             library.
        
        
            szNameBuf: The string to test.
            lHashVal: The hash value of szNameBuf.
            Returns: true if szNameBuf was found in the type library; otherwise, false.
        """
        pass

    def ReleaseTLibAttr(self, pTLibAttr):
        """
        ReleaseTLibAttr(self: ITypeLib2, pTLibAttr: IntPtr)
            Releases the System.Runtime.InteropServices.TYPELIBATTR structure originally obtained from the 
             System.Runtime.InteropServices.ComTypes.ITypeLib.GetLibAttr(System.IntPtr@) method.
        
        
            pTLibAttr: The TLIBATTR structure to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LIBFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines flags that apply to type libraries.
    
    enum (flags) LIBFLAGS, values: LIBFLAG_FCONTROL (2), LIBFLAG_FHASDISKIMAGE (8), LIBFLAG_FHIDDEN (4), LIBFLAG_FRESTRICTED (1)
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

    LIBFLAG_FCONTROL = None
    LIBFLAG_FHASDISKIMAGE = None
    LIBFLAG_FHIDDEN = None
    LIBFLAG_FRESTRICTED = None
    value__ = None


class PARAMDESC(object):
    """ Contains information about how to transfer a structure element, parameter, or function return value between processes. """
    lpVarValue = None
    wParamFlags = None


class PARAMFLAG(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes how to transfer a structure element, parameter, or function return value between processes.
    
    enum (flags) PARAMFLAG, values: PARAMFLAG_FHASCUSTDATA (64), PARAMFLAG_FHASDEFAULT (32), PARAMFLAG_FIN (1), PARAMFLAG_FLCID (4), PARAMFLAG_FOPT (16), PARAMFLAG_FOUT (2), PARAMFLAG_FRETVAL (8), PARAMFLAG_NONE (0)
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

    PARAMFLAG_FHASCUSTDATA = None
    PARAMFLAG_FHASDEFAULT = None
    PARAMFLAG_FIN = None
    PARAMFLAG_FLCID = None
    PARAMFLAG_FOPT = None
    PARAMFLAG_FOUT = None
    PARAMFLAG_FRETVAL = None
    PARAMFLAG_NONE = None
    value__ = None


class STATDATA(object):
    """ Provides the managed definition of the STATDATA structure. """
    advf = None
    advSink = None
    connection = None
    formatetc = None


class STATSTG(object):
    """ Contains statistical information about an open storage, stream, or byte-array object. """
    atime = None
    cbSize = None
    clsid = None
    ctime = None
    grfLocksSupported = None
    grfMode = None
    grfStateBits = None
    mtime = None
    pwcsName = None
    reserved = None
    type = None


class STGMEDIUM(object):
    """ Provides the managed definition of the STGMEDIUM structure. """
    pUnkForRelease = None
    tymed = None
    unionmember = None


class SYSKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the target operating system platform.
    
    enum SYSKIND, values: SYS_MAC (2), SYS_WIN16 (0), SYS_WIN32 (1), SYS_WIN64 (3)
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

    SYS_MAC = None
    SYS_WIN16 = None
    SYS_WIN32 = None
    SYS_WIN64 = None
    value__ = None


class TYMED(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides the managed definition of the TYMED structure.
    
    enum (flags) TYMED, values: TYMED_ENHMF (64), TYMED_FILE (2), TYMED_GDI (16), TYMED_HGLOBAL (1), TYMED_ISTORAGE (8), TYMED_ISTREAM (4), TYMED_MFPICT (32), TYMED_NULL (0)
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

    TYMED_ENHMF = None
    TYMED_FILE = None
    TYMED_GDI = None
    TYMED_HGLOBAL = None
    TYMED_ISTORAGE = None
    TYMED_ISTREAM = None
    TYMED_MFPICT = None
    TYMED_NULL = None
    value__ = None


class TYPEATTR(object):
    """ Contains attributes of a UCOMITypeInfo. """
    cbAlignment = None
    cbSizeInstance = None
    cbSizeVft = None
    cFuncs = None
    cImplTypes = None
    cVars = None
    dwReserved = None
    guid = None
    idldescType = None
    lcid = None
    lpstrSchema = None
    MEMBER_ID_NIL = -1
    memidConstructor = None
    memidDestructor = None
    tdescAlias = None
    typekind = None
    wMajorVerNum = None
    wMinorVerNum = None
    wTypeFlags = None


class TYPEDESC(object):
    """ Describes the type of a variable, return type of a function, or the type of a function parameter. """
    lpValue = None
    vt = None


class TYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the properties and attributes of a type description.
    
    enum (flags) TYPEFLAGS, values: TYPEFLAG_FAGGREGATABLE (1024), TYPEFLAG_FAPPOBJECT (1), TYPEFLAG_FCANCREATE (2), TYPEFLAG_FCONTROL (32), TYPEFLAG_FDISPATCHABLE (4096), TYPEFLAG_FDUAL (64), TYPEFLAG_FHIDDEN (16), TYPEFLAG_FLICENSED (4), TYPEFLAG_FNONEXTENSIBLE (128), TYPEFLAG_FOLEAUTOMATION (256), TYPEFLAG_FPREDECLID (8), TYPEFLAG_FPROXY (16384), TYPEFLAG_FREPLACEABLE (2048), TYPEFLAG_FRESTRICTED (512), TYPEFLAG_FREVERSEBIND (8192)
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

    TYPEFLAG_FAGGREGATABLE = None
    TYPEFLAG_FAPPOBJECT = None
    TYPEFLAG_FCANCREATE = None
    TYPEFLAG_FCONTROL = None
    TYPEFLAG_FDISPATCHABLE = None
    TYPEFLAG_FDUAL = None
    TYPEFLAG_FHIDDEN = None
    TYPEFLAG_FLICENSED = None
    TYPEFLAG_FNONEXTENSIBLE = None
    TYPEFLAG_FOLEAUTOMATION = None
    TYPEFLAG_FPREDECLID = None
    TYPEFLAG_FPROXY = None
    TYPEFLAG_FREPLACEABLE = None
    TYPEFLAG_FRESTRICTED = None
    TYPEFLAG_FREVERSEBIND = None
    value__ = None


class TYPEKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies various types of data and functions.
    
    enum TYPEKIND, values: TKIND_ALIAS (6), TKIND_COCLASS (5), TKIND_DISPATCH (4), TKIND_ENUM (0), TKIND_INTERFACE (3), TKIND_MAX (8), TKIND_MODULE (2), TKIND_RECORD (1), TKIND_UNION (7)
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

    TKIND_ALIAS = None
    TKIND_COCLASS = None
    TKIND_DISPATCH = None
    TKIND_ENUM = None
    TKIND_INTERFACE = None
    TKIND_MAX = None
    TKIND_MODULE = None
    TKIND_RECORD = None
    TKIND_UNION = None
    value__ = None


class TYPELIBATTR(object):
    """ Identifies a particular type library and provides localization support for member names. """
    guid = None
    lcid = None
    syskind = None
    wLibFlags = None
    wMajorVerNum = None
    wMinorVerNum = None


class VARDESC(object):
    """ Describes a variable, constant, or data member. """
    desc = None
    DESCUNION = None
    elemdescVar = None
    lpstrSchema = None
    memid = None
    varkind = None
    wVarFlags = None


class VARFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the constants that define the properties of a variable.
    
    enum (flags) VARFLAGS, values: VARFLAG_FBINDABLE (4), VARFLAG_FDEFAULTBIND (32), VARFLAG_FDEFAULTCOLLELEM (256), VARFLAG_FDISPLAYBIND (16), VARFLAG_FHIDDEN (64), VARFLAG_FIMMEDIATEBIND (4096), VARFLAG_FNONBROWSABLE (1024), VARFLAG_FREADONLY (1), VARFLAG_FREPLACEABLE (2048), VARFLAG_FREQUESTEDIT (8), VARFLAG_FRESTRICTED (128), VARFLAG_FSOURCE (2), VARFLAG_FUIDEFAULT (512)
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

    value__ = None
    VARFLAG_FBINDABLE = None
    VARFLAG_FDEFAULTBIND = None
    VARFLAG_FDEFAULTCOLLELEM = None
    VARFLAG_FDISPLAYBIND = None
    VARFLAG_FHIDDEN = None
    VARFLAG_FIMMEDIATEBIND = None
    VARFLAG_FNONBROWSABLE = None
    VARFLAG_FREADONLY = None
    VARFLAG_FREPLACEABLE = None
    VARFLAG_FREQUESTEDIT = None
    VARFLAG_FRESTRICTED = None
    VARFLAG_FSOURCE = None
    VARFLAG_FUIDEFAULT = None


class VARKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the kind of variable.
    
    enum VARKIND, values: VAR_CONST (2), VAR_DISPATCH (3), VAR_PERINSTANCE (0), VAR_STATIC (1)
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

    value__ = None
    VAR_CONST = None
    VAR_DISPATCH = None
    VAR_PERINSTANCE = None
    VAR_STATIC = None


