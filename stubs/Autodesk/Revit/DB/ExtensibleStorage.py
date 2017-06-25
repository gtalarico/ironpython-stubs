# encoding: utf-8
# module Autodesk.Revit.DB.ExtensibleStorage calls itself ExtensibleStorage
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccessLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines access levels to objects in the Extensible Storage framework.
    
    enum AccessLevel, values: Application (3), Public (1), Vendor (2)
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

    Application = None
    Public = None
    value__ = None
    Vendor = None


class ContainerType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type indicating if the field represents a single value or a container of multiple values.
    
    enum ContainerType, values: Array (1), Map (2), Simple (0)
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

    Array = None
    Map = None
    Simple = None
    value__ = None


class DataStorage(Element, IDisposable):
    """ An element which allows an API applications to organize and store data. """
    @staticmethod
    def Create(doc):
        """
        Create(doc: Document) -> DataStorage
        
            Creates a new DataStorage element and adds it to the document.
        
            doc: Document to which the new element should be added.
            Returns: The newly created DataStorage element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class Entity(object, IDisposable):
    """
    An object stored in the Extensible Storage framework. An Entity is described by a Schema,
       which serves both to identify an Entity, and to describe its contents (Fields).
    
    Entity(schemaGUID: Guid)
    Entity(schema: Schema)
    Entity()
    Entity(other: Entity)
    """
    def Clear(self, *__args):
        """
        Clear(self: Entity, field: Field)
            Resets the field to its default value.
        
            field: The field to clear.
        Clear(self: Entity, fieldName: str)
            Resets the field to its default value.
        
            fieldName: The name of the field to clear.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Entity) """
        pass

    def Get(self, *__args):
        """
        Get[FieldType](self: Entity, fieldName: str) -> FieldType
        Get[FieldType](self: Entity, field: Field) -> FieldType
        Get[FieldType](self: Entity, fieldName: str, displayUnits: DisplayUnitType) -> FieldType
        Get[FieldType](self: Entity, field: Field, displayUnits: DisplayUnitType) -> FieldType
        """
        pass

    def IsValid(self):
        """
        IsValid(self: Entity) -> bool
        
            Checks whether this Entity has a live Schema corresponding to it.
            Returns: True if the Entity is valid.
        """
        pass

    def ReadAccessGranted(self):
        """
        ReadAccessGranted(self: Entity) -> bool
        
            Checks whether this Entity may be retrieved by the current add-in.
            Returns: True if read access is allowed.
        """
        pass

    def RecognizedField(self, field):
        """
        RecognizedField(self: Entity, field: Field) -> bool
        
            Checks whether a Field belongs to the same Schema as this Entity.
        
            field: The Field to check.
            Returns: True if the Field belongs to the same Schema as this Entity.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Entity, disposing: bool) """
        pass

    def Set(self, *__args):
        """ Set[FieldType](self: Entity, fieldName: str, value: FieldType)Set[FieldType](self: Entity, field: Field, value: FieldType)Set[FieldType](self: Entity, fieldName: str, value: FieldType, displayUnits: DisplayUnitType)Set[FieldType](self: Entity, field: Field, value: FieldType, displayUnits: DisplayUnitType) """
        pass

    def WriteAccessGranted(self):
        """
        WriteAccessGranted(self: Entity) -> bool
        
            Checks whether this Entity may be stored by the current add-in.
            Returns: True if write access is allowed.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, schemaGUID: Guid)
        __new__(cls: type, schema: Schema)
        __new__(cls: type)
        __new__(cls: type, other: Entity)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Entity) -> bool

"""

    Schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schema describing this Entity.

Get: Schema(self: Entity) -> Schema

"""

    SchemaGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID of the Schema describing this Entity.

Get: SchemaGUID(self: Entity) -> Guid

"""



class ExtensibleStorageFilter(ElementQuickFilter, IDisposable):
    """
    A filter used to filter elements with extensible storage data based on specific Schema id.
    
    ExtensibleStorageFilter(schemaGuid: Guid)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, schemaGuid):
        """ __new__(cls: type, schemaGuid: Guid) """
        pass

    SchemaGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Schema id used to filter elements with extensible storage data

Get: SchemaGuid(self: ExtensibleStorageFilter) -> Guid

"""



class Field(object, IDisposable):
    """
    The description of a field within a Schema in the Extensible Storage framework. Contains
       the field's name, type, access control and documentation.
    """
    def CompatibleDisplayUnitType(self, type):
        """
        CompatibleDisplayUnitType(self: Field, type: DisplayUnitType) -> bool
        
            Checks if the specified type is compatible with the field description.
        
            type: The type to check.
            Returns: True if the type is compatible, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Field) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Field, disposing: bool) """
        pass

    def SubEntityReadAccessGranted(self):
        """
        SubEntityReadAccessGranted(self: Field) -> bool
        
            Checks whether there is read access to subentities storable in this field.
            Returns: True if subentities are readable.
        """
        pass

    def SubEntityWriteAccessGranted(self):
        """
        SubEntityWriteAccessGranted(self: Field) -> bool
        
            Checks whether there is write access to subentities storable in this field.
            Returns: True if subentities are writable.
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

    ContainerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether this is a simple field containing one value,
   or a container of multiple values.

Get: ContainerType(self: Field) -> ContainerType

"""

    Documentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The overall description of the Field.

Get: Documentation(self: Field) -> str

"""

    FieldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the field.

Get: FieldName(self: Field) -> str

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Field) -> bool

"""

    KeyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the keys stored in the field.

Get: KeyType(self: Field) -> Type

"""

    Schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schema to which this Field belongs.

Get: Schema(self: Field) -> Schema

"""

    SubSchema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schema describing the subentity (or subentities) stored in this Field.

Get: SubSchema(self: Field) -> Schema

"""

    SubSchemaGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID of the Schema describing the subentity (or subentities) stored in this Field.

Get: SubSchemaGUID(self: Field) -> Guid

"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of units represented by values stored in this field

Get: UnitType(self: Field) -> UnitType

"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the values stored in the field.

Get: ValueType(self: Field) -> Type

"""



class FieldBuilder(object, IDisposable):
    """
    This class is used to create Fields in the Extensible Storage framework.
    
    FieldBuilder(field: Field, builder: SchemaBuilder)
    FieldBuilder(other: FieldBuilder)
    """
    def Dispose(self):
        """ Dispose(self: FieldBuilder) """
        pass

    def NeedsSubSchemaGUID(self):
        """
        NeedsSubSchemaGUID(self: FieldBuilder) -> bool
        
            Checks whether the SubSchema GUID needs to be explicitly specified for this 
             field type.
        
            Returns: True if SubSchemaGUID is required.
        """
        pass

    def NeedsUnits(self):
        """
        NeedsUnits(self: FieldBuilder) -> bool
        
            Checks whether the field type requires explicit unit conversions.
            Returns: True if units are required.
        """
        pass

    def Ready(self):
        """
        Ready(self: FieldBuilder) -> bool
        
            Checks whether the builder may be used.
            Returns: True if the SchemaBuilder has not yet been finished.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldBuilder, disposing: bool) """
        pass

    def SetDocumentation(self, documentation):
        """
        SetDocumentation(self: FieldBuilder, documentation: str) -> FieldBuilder
        
            Sets the documentation string for the Field.
        
            documentation: The documentation string.
            Returns: The FieldBuilder object may be used to add more details to the field.
        """
        pass

    def SetSubSchemaGUID(self, guid):
        """
        SetSubSchemaGUID(self: FieldBuilder, guid: Guid) -> FieldBuilder
        
            Sets the GUID of the Schema of the Entities that are intended to be stored in 
             this field.
        
        
            guid: The GUID of the subschema.
            Returns: The FieldBuilder object may be used to add more details to the field.
        """
        pass

    def SetUnitType(self, units):
        """
        SetUnitType(self: FieldBuilder, units: UnitType) -> FieldBuilder
        
            Sets the type of units for the field.
        
            units: Units type value to be set
            Returns: The FieldBuilder object may be used to add more details to the field.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, field: Field, builder: SchemaBuilder)
        __new__(cls: type, other: FieldBuilder)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FieldBuilder) -> bool

"""



class Schema(object, IDisposable):
    """
    The description of a single object (Entity) in the Extensible Storage framework. Contains
       identity information, documentation and the list of fields to be stored in the Entity.
    """
    def Dispose(self):
        """ Dispose(self: Schema) """
        pass

    @staticmethod
    def EraseSchemaAndAllEntities(schema, overrideWriteAccessWithUserPermission):
        """
        EraseSchemaAndAllEntities(schema: Schema, overrideWriteAccessWithUserPermission: bool)
            Erases all Entities corresponding to this Schema from all open documents, and 
             erases
           this Schema from memory.
        
        
            schema: The Schema to erase.
            overrideWriteAccessWithUserPermission: Normally, the usual write access controls apply to prevent deletion of Entities 
             that
           you don't have write permissions for. However, the user may choose to 
             override the
           controls. Set this flag to true only if the user gave explicit 
             permission to destroy
           the Schema.
        """
        pass

    def GetField(self, name):
        """
        GetField(self: Schema, name: str) -> Field
        
            Gets a Field of a given name from the Schema.
        
            name: The Field name
            Returns: The Field
        """
        pass

    def ListFields(self):
        """
        ListFields(self: Schema) -> IList[Field]
        
            The complete list of fields in the Schema, sorted by name.
        """
        pass

    @staticmethod
    def ListSchemas():
        """
        ListSchemas() -> IList[Schema]
        
            Lists all schemas in memory.
        """
        pass

    @staticmethod
    def Lookup(guid):
        """
        Lookup(guid: Guid) -> Schema
        
            Finds the Schema corresponding to the GUID in memory.
        """
        pass

    def ReadAccessGranted(self):
        """
        ReadAccessGranted(self: Schema) -> bool
        
            Checks whether Entities of this Schema may be retrieved by the current add-in.
            Returns: True if read access is allowed.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Schema, disposing: bool) """
        pass

    def WriteAccessGranted(self):
        """
        WriteAccessGranted(self: Schema) -> bool
        
            Checks whether Entities of this Schema may be stored by the current add-in.
            Returns: True if write access is allowed.
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

    ApplicationGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID of the application or add-in that may access entities of this Schema under the
   Application access level.

Get: ApplicationGUID(self: Schema) -> Guid

"""

    Documentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The overall description of the Schema.

Get: Documentation(self: Schema) -> str

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier of the Schema.
   Setter made unavailable, because it would violate set-correctness

Get: GUID(self: Schema) -> Guid

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Schema) -> bool

"""

    ReadAccessLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read access level of the schema.

Get: ReadAccessLevel(self: Schema) -> AccessLevel

"""

    SchemaName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-friendly name of the Schema.

Get: SchemaName(self: Schema) -> str

"""

    VendorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the third-party vendor that may access entities of this Schema under the
   Vendor access level.

Get: VendorId(self: Schema) -> str

"""

    WriteAccessLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Write access level of the schema.

Get: WriteAccessLevel(self: Schema) -> AccessLevel

"""



class SchemaBuilder(object, IDisposable):
    """
    This class is used to create Schemas in the Extensible Storage framework.
    
    SchemaBuilder(guid: Guid)
    """
    def AcceptableName(self, name):
        """
        AcceptableName(self: SchemaBuilder, name: str) -> bool
        
            Checks whether a string is an acceptable name for a Schema or a Field.
        
            name: The string to check.
            Returns: True if the name is acceptable.
        """
        pass

    def AddArrayField(self, fieldName, fieldType):
        """
        AddArrayField(self: SchemaBuilder, fieldName: str, fieldType: Type) -> FieldBuilder
        
            Creates a field containing an array of values in the Schema, with given name 
             and type
           of contained values.
        
        
            fieldName: The name of the new field.
            fieldType: The type of the contents in the new field.
            Returns: The FieldBuilder object may be used to add more details to the field. Make sure 
             to set
           the unit type if the field contains floating-point values.
        """
        pass

    def AddMapField(self, fieldName, keyType, valueType):
        """
        AddMapField(self: SchemaBuilder, fieldName: str, keyType: Type, valueType: Type) -> FieldBuilder
        
            Creates a field containing an ordered key-value map in the Schema, with given 
             name and
           type of contained values.
        
        
            fieldName: The name of the new field.
            keyType: The type of the keys for the new field.
            valueType: The type of the values for the new field.
            Returns: The FieldBuilder object may be used to add more details to the field. Make sure 
             to set
           the unit type if the field contains floating-point values.
        """
        pass

    def AddSimpleField(self, fieldName, fieldType):
        """
        AddSimpleField(self: SchemaBuilder, fieldName: str, fieldType: Type) -> FieldBuilder
        
            Creates a field containing a single value in the Schema, with given name and 
             type.
        
        
            fieldName: The name of the new field.
            fieldType: The type of the new field.
            Returns: The FieldBuilder object may be used to add more details to the field. Make sure 
             to set
           the unit type if the field contains floating-point values.
        """
        pass

    def Dispose(self):
        """ Dispose(self: SchemaBuilder) """
        pass

    def Finish(self):
        """
        Finish(self: SchemaBuilder) -> Schema
        
            Registers and returns the created Schema object.
            Returns: The newly created Schema.
        """
        pass

    @staticmethod
    def GUIDIsValid(guid):
        """
        GUIDIsValid(guid: Guid) -> bool
        
            Checks whether the supplied GUID value is valid.
        
            guid: The GUID to check
            Returns: True if the GUID is valid
        """
        pass

    def Ready(self):
        """
        Ready(self: SchemaBuilder) -> bool
        
            Checks whether the builder may be used.
            Returns: True if the SchemaBuilder has not yet been finished.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SchemaBuilder, disposing: bool) """
        pass

    def SetApplicationGUID(self, applicationGUID):
        """
        SetApplicationGUID(self: SchemaBuilder, applicationGUID: Guid) -> SchemaBuilder
        
            Sets the GUID of the application or add-in that may access entities of this 
             Schema under
           the Application acess level.
        
        
            applicationGUID: The application id.
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    def SetDocumentation(self, documentation):
        """
        SetDocumentation(self: SchemaBuilder, documentation: str) -> SchemaBuilder
        
            Sets the documentation string for the Schema.
        
            documentation: The documentation string.
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    def SetReadAccessLevel(self, readAccessLevel):
        """
        SetReadAccessLevel(self: SchemaBuilder, readAccessLevel: AccessLevel) -> SchemaBuilder
        
            Sets top level read access (for entities)
        
            readAccessLevel: Read access level value to be set
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    def SetSchemaName(self, schemaName):
        """
        SetSchemaName(self: SchemaBuilder, schemaName: str) -> SchemaBuilder
        
            Sets the name of the Schema.
        
            schemaName: The name for the Schema.
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    def SetVendorId(self, vendorId):
        """
        SetVendorId(self: SchemaBuilder, vendorId: str) -> SchemaBuilder
        
            Sets the ID of the third-party vendor that may access entities of this Schema 
             under the
           Vendor acess level, and to generally identify the owner of this 
             Schema.
        
        
            vendorId: The vendor id.
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    def SetWriteAccessLevel(self, writeAccessLevel):
        """
        SetWriteAccessLevel(self: SchemaBuilder, writeAccessLevel: AccessLevel) -> SchemaBuilder
        
            Sets top level write access (for entities)
        
            writeAccessLevel: Write access level value to be set
            Returns: The SchemaBuilder object may be used to add more settings.
        """
        pass

    @staticmethod
    def VendorIdIsValid(vendorId):
        """
        VendorIdIsValid(vendorId: str) -> bool
        
            Checks whether the given vendor ID string is valid. A valid vendor ID string:
         
               1. Has a length of at least 4 characters and no more than 253 characters, and
             
           2. Contains only letters, digits, or any of the following special 
             characters:
           ! " # & \ ( ) + , . - : ; < = > ? _ ` | ~
        
        
            vendorId: The vendor ID to check.
            Returns: True if the vendor ID is valid.
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

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SchemaBuilder) -> bool

"""



