from Wms.RemotingImplementation import DataSet
# encoding: utf-8
# module Wms.RemotingImplementation.Properties.DataSources calls itself DataSources
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataSetPickListPtP(DataSet):
    """ DataSetPickListPtP() """
    def Clone(self):
        """ Clone(self: DataSetPickListPtP) -> DataSet """
        pass

    def DetermineSchemaSerializationMode(self, *args): #cannot find CLR method
        """
        DetermineSchemaSerializationMode(self: DataSet, info: SerializationInfo, context: StreamingContext) -> SchemaSerializationMode
        
            Determines the System.Data.DataSet.SchemaSerializationMode for a 
             System.Data.DataSet.
        
        
                     constructor 
             System.Data.DataSet.#ctor(System.Runtime.Serialization.SerializationInfo,System
             .Runtime.Serialization.StreamingContext) is invoked with during 
             deserialization in remoting scenarios.
        
                     constructor 
             System.Data.DataSet.#ctor(System.Runtime.Serialization.SerializationInfo,System
             .Runtime.Serialization.StreamingContext) is invoked with during 
             deserialization in remoting scenarios.
        
            Returns: An System.Data.SchemaSerializationMode enumeration indicating whether schema 
             information has been omitted from the payload.
        
        DetermineSchemaSerializationMode(self: DataSet, reader: XmlReader) -> SchemaSerializationMode
        
            Determines the System.Data.DataSet.SchemaSerializationMode for a 
             System.Data.DataSet.
        
        
            reader: The System.Xml.XmlReader instance that is passed during deserialization of the 
             System.Data.DataSet.
        
            Returns: An System.Data.SchemaSerializationMode enumeration indicating whether schema 
             information has been omitted from the payload.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: MarshalByValueComponent, disposing: bool)
            Releases the unmanaged resources used by the 
             System.ComponentModel.MarshalByValueComponent and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only 
             unmanaged resources.
        """
        pass

    def GetSchemaSerializable(self, *args): #cannot find CLR method
        """ GetSchemaSerializable(self: DataSetPickListPtP) -> XmlSchema """
        pass

    def GetSerializationData(self, *args): #cannot find CLR method
        """
        GetSerializationData(self: DataSet, info: SerializationInfo, context: StreamingContext)
            Deserializes the table data from the binary or XML stream.
        
            info: The System.Runtime.Serialization.SerializationInfo instance.
            context: The streaming context.
        """
        pass

    @staticmethod
    def GetTypedDataSetSchema(xs):
        """ GetTypedDataSetSchema(xs: XmlSchemaSet) -> XmlSchemaComplexType """
        pass

    def InitializeDerivedDataSet(self, *args): #cannot find CLR method
        """ InitializeDerivedDataSet(self: DataSetPickListPtP) """
        pass

    def IsBinarySerialized(self, *args): #cannot find CLR method
        """
        IsBinarySerialized(self: DataSet, info: SerializationInfo, context: StreamingContext) -> bool
        
            Inspects the format of the serialized representation of the DataSet.
        
            info: The System.Runtime.Serialization.SerializationInfo object.
            context: The System.Runtime.Serialization.StreamingContext object.
            Returns: true if the specified System.Runtime.Serialization.SerializationInfo 
             represents a DataSet serialized in its binary format, false otherwise.
        """
        pass

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """
        OnPropertyChanging(self: DataSet, pcevent: PropertyChangedEventArgs)
            Raises the 
             System.Data.DataSet.OnPropertyChanging(System.ComponentModel.PropertyChangedEve
             ntArgs) event.
        
        
            pcevent: A System.ComponentModel.PropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnRemoveRelation(self, *args): #cannot find CLR method
        """
        OnRemoveRelation(self: DataSet, relation: DataRelation)
            Occurs when a System.Data.DataRelation object is removed from a 
             System.Data.DataTable.
        
        
            relation: The System.Data.DataRelation being removed.
        """
        pass

    def OnRemoveTable(self, *args): #cannot find CLR method
        """
        OnRemoveTable(self: DataSet, table: DataTable)
            Occurs when a System.Data.DataTable is removed from a System.Data.DataSet.
        
            table: The System.Data.DataTable being removed.
        """
        pass

    def RaisePropertyChanging(self, *args): #cannot find CLR method
        """
        RaisePropertyChanging(self: DataSet, name: str)
            Sends a notification that the specified System.Data.DataSet property is about 
             to change.
        
        
            name: The name of the property that is about to change.
        """
        pass

    def ReadXmlSerializable(self, *args): #cannot find CLR method
        """ ReadXmlSerializable(self: DataSetPickListPtP, reader: XmlReader) """
        pass

    def ShouldSerializeRelations(self, *args): #cannot find CLR method
        """ ShouldSerializeRelations(self: DataSetPickListPtP) -> bool """
        pass

    def ShouldSerializeTables(self, *args): #cannot find CLR method
        """ ShouldSerializeTables(self: DataSetPickListPtP) -> bool """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this component.

"""

    PerLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PerLocation(self: DataSetPickListPtP) -> PerLocationDataTable

"""

    PickToPlace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickToPlace(self: DataSetPickListPtP) -> PickToPlaceDataTable

"""

    Relations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Relations(self: DataSetPickListPtP) -> DataRelationCollection

"""

    SchemaSerializationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SchemaSerializationMode(self: DataSetPickListPtP) -> SchemaSerializationMode

Set: SchemaSerializationMode(self: DataSetPickListPtP) = value
"""

    Tables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tables(self: DataSetPickListPtP) -> DataTableCollection

"""


    PerLocationDataTable = None
    PerLocationRow = None
    PerLocationRowChangeEvent = None
    PerLocationRowChangeEventHandler = None
    PickToPlaceDataTable = None
    PickToPlaceRow = None
    PickToPlaceRowChangeEvent = None
    PickToPlaceRowChangeEventHandler = None

    Instance = DataSetPickListPtP()
    """hardcoded/returns an instance of the class"""

