# encoding: utf-8
# module GH_IO.Serialization calls itself Serialization
# from GH_IO, Version=1.0.0.0, Culture=neutral, PublicKeyToken=6a29997d2e6b4f97
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class EncodedStringWriter(StringWriter, IDisposable):
    """
    This class is needed to override the UTF-16 encoding property of the default DotNET StringWriter.
    
    EncodedStringWriter()
    """
    def Dispose(self):
        """
        Dispose(self: StringWriter, disposing: bool)
            Releases the unmanaged resources used by the System.IO.StringWriter and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Always return UTF-8.

Get: Encoding(self: EncodedStringWriter) -> Encoding

"""


    CoreNewLine = None


class GH_Archive(object):
    """
    This is the base archive class which takes care of all (de)serialization and messaging.
    
    GH_Archive()
    """
    def AddMessage(self, *__args):
        """
        AddMessage(self: GH_Archive, message: GH_Message)
            Add a new message to the record.
        
            message: Message to add
        AddMessage(self: GH_Archive, message_text: str, message_type: GH_Message_Type)
            Add a new message to the record.
        
            message_text: Message text.
            message_type: Message type.
        """
        pass

    def AppendObject(self, target, target_name):
        """
        AppendObject(self: GH_Archive, target: GH_ISerializable, target_name: str) -> bool
        
            Appends a target object into the root node of this archive tree. 
                    If the root 
             doesn't exist yet, it will be created. Existing objects at the root scope 
                    will not 
             be affected.
        
        
            target: Object to append. Cannot be null.
            target_name: Name of object to append, name must be unique.
            Returns: True on succes, false on failure.
        """
        pass

    def ClearMessages(self):
        """
        ClearMessages(self: GH_Archive)
            Remove all messages from the log.
        """
        pass

    def CreateNewRoot(self, forWriting):
        """
        CreateNewRoot(self: GH_Archive, forWriting: bool)
            Discards the current data tree and instantiates a new root node. 
                    This root node 
             contains some comments, a version value containing the current version of GH_IO.dll 
                   
              and a DateTime value containing the current date and time.
        
        
            forWriting: If true, all data fields are reset.
        """
        pass

    def CreateTopLevelNode(self, root_name):
        """
        CreateTopLevelNode(self: GH_Archive, root_name: str) -> GH_IWriter
        
            Creates and returns a new root node for this archive in the form of a GH_IWriter instance. 
            
                     Typically you do not call this method. If you want to add an object to the archive, use 
             AppendObject() instead.
        
        
            root_name: Name of root object.
            Returns: The GH_IWriter incarnation of the GH_Chunk that represents the new Node.
        """
        pass

    def Deserialize_Binary(self, data):
        """
        Deserialize_Binary(self: GH_Archive, data: Array[Byte]) -> bool
        
            Deserializes an array of bytes.
        
            data: Byte array to deserialize.
            Returns: True on success, false on failure.
        """
        pass

    def Deserialize_Xml(self, xml_content):
        """
        Deserialize_Xml(self: GH_Archive, xml_content: str) -> bool
        
            Deserializes an Xml string.
        
            xml_content: Xml to deserialize.
            Returns: True on success, false on failure.
        """
        pass

    def ExtractObject(self, target, target_name):
        """
        ExtractObject(self: GH_Archive, target: GH_ISerializable, target_name: str) -> bool
        
            Extract a target object from the data tree.
        
            target: Object to extract. Cannot be null.
            target_name: Name of object to extract, name must identify an existing chunk.
            Returns: True on succes, false on failure.
        """
        pass

    def MessageCount(self, includeInfo=None, includeWarnings=None, includeErrors=None):
        """
        MessageCount(self: GH_Archive, includeInfo: bool, includeWarnings: bool, includeErrors: bool) -> int
        
            Gets the number of messages recorded since the most recent IO operation began. 
                    
             Message count can be filtered by message type.
        
        
            includeInfo: If true, info messages will be included in the count.
            includeWarnings: If true, warnings will be included in the count.
            includeErrors: If true, errors will be included in the count.
            Returns: The number of recoded messages that pass the type filters.
        MessageCount(self: GH_Archive) -> int
        
            Gets the number of messages recorded since the most recent IO operation began.
            Returns: The number of recorded messages.
        """
        pass

    @staticmethod
    def OpenFileDialog(title, file_path, additional_filters):
        """ OpenFileDialog(title: str, file_path: str, additional_filters: List[str]) -> (bool, str) """
        pass

    def ReadFromFile(self, file_name):
        """
        ReadFromFile(self: GH_Archive, file_name: str) -> bool
        
            Reads a new archive tree from a file.
        
            file_name: Path of file to parse.
            Returns: True on success, false on failure. If the read operation fails, 
                    all the member 
             fields of this archive ought to be treated as invalid.
        """
        pass

    @staticmethod
    def SaveFileDialog(title, file_path, additional_filters):
        """ SaveFileDialog(title: str, file_path: str, additional_filters: List[str]) -> (bool, str) """
        pass

    def Serialize_Binary(self):
        """
        Serialize_Binary(self: GH_Archive) -> Array[Byte]
        
            Serializes the data tree into a Binary byte array.
            Returns: A byte array containing the Binary stream.
        """
        pass

    def Serialize_Xml(self):
        """
        Serialize_Xml(self: GH_Archive) -> str
        
            Serializes the data tree into an Xml string.
            Returns: A string containing the Xml content.
        """
        pass

    def ShowMessageLog(self):
        """
        ShowMessageLog(self: GH_Archive) -> DialogResult
        
            Displays the message log viewer. You should typically only display the viewer if 
                    
             the WorstCaseMessageType equals GH_Message_Type.warning or GH_Message_Type.error
        
            Returns: The closing flag for the displayed log form.
        """
        pass

    def WriteToFile(self, file_name, overwrite, remember_path):
        """
        WriteToFile(self: GH_Archive, file_name: str, overwrite: bool, remember_path: bool) -> bool
        
            Writes the current tree to a file.
        
            file_name: Path of file to write to. If the extension is not a recognized Grasshopper extension, 
                 
                an exception will be thrown.
        
            overwrite: True to overwrite file at specified location.
            remember_path: If True, the MRU path field will be updated to reflect the new path.
            Returns: True on succes, false if file already exists and overwrite is set to false.
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the filename (without extension) of the currently loaded data tree.
            If the path field has not been set, "unnamed" is returned.

Get: FileName(self: GH_Archive) -> str

"""

    GetRootNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root node of this archive. 
            Typically you do not need to modify the Root. 
            Use functions like CreateTopLevelNode(), AppendObject() and ExtractObject() instead. 
            If you modify the Root node, you may corrupt the archive.

Get: GetRootNode(self: GH_Archive) -> GH_Chunk

"""

    IsBinaryPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the Path field points to a Binary Grasshopper file.

Get: IsBinaryPath(self: GH_Archive) -> bool

"""

    IsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not the path field has been set.

Get: IsPath(self: GH_Archive) -> bool

"""

    IsXmlPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the Path field points to an Xml Grasshopper file.

Get: IsXmlPath(self: GH_Archive) -> bool

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal list of messages.

Get: Messages(self: GH_Archive) -> List[GH_Message]

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path to the file from which this archive was read and/or written to. 
            If the archive hasn't been read or written yet, this field will be null.

Get: Path(self: GH_Archive) -> str

Set: Path(self: GH_Archive) = value
"""

    WorstCaseMessageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the worst case message type. 
            If the record contains at least 1 error, the worst case is GH_Message_Type.error. 
            If the record contains no errors, but at least 1 warning, 
            the worst case is GH_Message_Type.warning. 
            If the record contains no messages or only infos, the worst case type is GH_Message_Type.info.

Get: WorstCaseMessageType(self: GH_Archive) -> GH_Message_Type

"""


    GH_IO_Version = None
    GrasshopperBinaryExtension = '.gh'
    GrasshopperUserExtension = '.ghuser'
    GrasshopperXmlExtension = '.ghx'


class GH_Chunk(object, GH_IWriter, GH_IChunk, GH_IBinarySupport, GH_IXmlSupport, GH_IReader):
    """
    Full implementation of GH_IChunk, GH_IReader, GH_IWriter, GH_IBinarySupport and GH_IXmlSupport. 
                Instances of this class are usually disguised as one of the interfaces it implements.
    """
    def AddComment(self, comment_text):
        """
        AddComment(self: GH_Chunk, comment_text: str)
            Adds a text comment to this chunk. Comments are serialized only if the output flavour is a 
            
                     human readable format. Comments are never deserialized, they are purely for the benefit 
             of the
                    humans reading the file data.
        
        
            comment_text: The content of the comment, 
                    text might be altered if it contains invalid 
             characters for a chosen format flavour.
        """
        pass

    def AddMessage(self, m, t):
        """
        AddMessage(self: GH_Chunk, m: str, t: GH_Message_Type)
            Log a new message with the top-level archive. 
                    Messages are collected during 
             read/write operations, 
                    and can be displayed to the user upon completion using 
             GH_Archive.ShowMessageLog().
        
        
            m: Message text.
            t: Message type.
        """
        pass

    def ChunkExists(self, name, index=None):
        """
        ChunkExists(self: GH_Chunk, name: str, index: int) -> bool
        
            Checks whether a chunk with the specified name and index exists in the litter. 
                    
             Only chunks with index qualifiers are considered. 
                    Name comparisons are not 
             case-sensitive.
        
        
            name: Name of chunk to test for.
            index: Index of chunk to test for. 
                    If less than zero, ChunkExists(string name) is called 
             instead.
        
            Returns: True if a chunk with the specified name and index exists, otherwise false.
        ChunkExists(self: GH_Chunk, name: str) -> bool
        
            Checks whether a chunk with the specified name exists in the litter. 
                    Only chunks 
             without index qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of chunk to test for.
            Returns: True if a chunk with the specified name exists, otherwise false.
        """
        pass

    def CreateChunk(self, chunk_name, chunk_index=None):
        """
        CreateChunk(self: GH_Chunk, chunk_name: str, chunk_index: int) -> GH_IWriter
        
            Create a new child chunk with the specified name and index qualifier. 
                    If another 
             chunk already exists with similar properties, an exception will be thrown.
        
        
            chunk_name: Name of new child.
            chunk_index: Index of new child.
            Returns: The newly created child chunk.
        CreateChunk(self: GH_Chunk, chunk_name: str) -> GH_IWriter
        
            Create a new child chunk with the specified name and without an index qualifier. 
                    
             If another chunk already exists with similar properties, an exception will be thrown.
        
        
            chunk_name: Name of new child.
            Returns: The newly created child chunk.
        """
        pass

    def FindChunk(self, name, index=None):
        """
        FindChunk(self: GH_Chunk, name: str, index: int) -> GH_IReader
        
            Finds the first chunk in the list that matches the given name and index. 
                    Only 
             chunks with index qualifiers are considered.
        
        
            name: Name of chunk to search for.
            index: Index of chunk to search for. 
                    If less than zero, FindChunk(string chunk_name) is 
             called instead.
        
            Returns: The child chunk that matches the given name and index, 
                    or null of no matching 
             chunk could be found.
        
        FindChunk(self: GH_Chunk, name: str) -> GH_IReader
        
            Finds the first chunk in the litter that matches the given name. 
                    Only chunks 
             without index qualifiers are considered.
        
        
            name: Name of chunk to search for.
            Returns: The child chunk that matches the given name, 
                    or null of no matching chunk could be 
             found.
        """
        pass

    def FindItem(self, name, index=None):
        """
        FindItem(self: GH_Chunk, name: str, index: int) -> GH_Item
        
            Finds the first item that matches the given name and index. 
                    Only items with index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to search for.
            index: Index of item to search for. 
                    If less than zero, then FindItem(string name) is 
             called instead.
        
            Returns: The item that matches the given name and index, 
                    or null of no matching item could 
             be found.
        
        FindItem(self: GH_Chunk, name: str) -> GH_Item
        
            Finds the first item that matches the given name. 
                    Only items without index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to search for.
            Returns: The item that matches the given name, 
                    or null of no matching item could be found.
        """
        pass

    def GetBoolean(self, item_name, item_index=None):
        """
        GetBoolean(self: GH_Chunk, item_name: str, item_index: int) -> bool
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetBoolean(self: GH_Chunk, item_name: str) -> bool
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetBoundingBox(self, item_name, item_index=None):
        """
        GetBoundingBox(self: GH_Chunk, item_name: str, item_index: int) -> GH_BoundingBox
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetBoundingBox(self: GH_Chunk, item_name: str) -> GH_BoundingBox
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetByte(self, item_name, item_index=None):
        """
        GetByte(self: GH_Chunk, item_name: str, item_index: int) -> Byte
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetByte(self: GH_Chunk, item_name: str) -> Byte
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetByteArray(self, item_name, item_index=None):
        """
        GetByteArray(self: GH_Chunk, item_name: str, item_index: int) -> Array[Byte]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetByteArray(self: GH_Chunk, item_name: str) -> Array[Byte]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDate(self, item_name, item_index=None):
        """
        GetDate(self: GH_Chunk, item_name: str, item_index: int) -> DateTime
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDate(self: GH_Chunk, item_name: str) -> DateTime
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDecimal(self, item_name, item_index=None):
        """
        GetDecimal(self: GH_Chunk, item_name: str, item_index: int) -> Decimal
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDecimal(self: GH_Chunk, item_name: str) -> Decimal
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDouble(self, item_name, item_index=None):
        """
        GetDouble(self: GH_Chunk, item_name: str, item_index: int) -> float
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDouble(self: GH_Chunk, item_name: str) -> float
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDoubleArray(self, item_name, item_index=None):
        """
        GetDoubleArray(self: GH_Chunk, item_name: str, item_index: int) -> Array[float]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDoubleArray(self: GH_Chunk, item_name: str) -> Array[float]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingBitmap(self, item_name, item_index=None):
        """
        GetDrawingBitmap(self: GH_Chunk, item_name: str, item_index: int) -> Bitmap
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingBitmap(self: GH_Chunk, item_name: str) -> Bitmap
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingColor(self, item_name, item_index=None):
        """
        GetDrawingColor(self: GH_Chunk, item_name: str, item_index: int) -> Color
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingColor(self: GH_Chunk, item_name: str) -> Color
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingPoint(self, item_name, item_index=None):
        """
        GetDrawingPoint(self: GH_Chunk, item_name: str, item_index: int) -> Point
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingPoint(self: GH_Chunk, item_name: str) -> Point
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingPointF(self, item_name, item_index=None):
        """
        GetDrawingPointF(self: GH_Chunk, item_name: str, item_index: int) -> PointF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingPointF(self: GH_Chunk, item_name: str) -> PointF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingRectangle(self, item_name, item_index=None):
        """
        GetDrawingRectangle(self: GH_Chunk, item_name: str, item_index: int) -> Rectangle
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingRectangle(self: GH_Chunk, item_name: str) -> Rectangle
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingRectangleF(self, item_name, item_index=None):
        """
        GetDrawingRectangleF(self: GH_Chunk, item_name: str, item_index: int) -> RectangleF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingRectangleF(self: GH_Chunk, item_name: str) -> RectangleF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingSize(self, item_name, item_index=None):
        """
        GetDrawingSize(self: GH_Chunk, item_name: str, item_index: int) -> Size
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingSize(self: GH_Chunk, item_name: str) -> Size
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingSizeF(self, item_name, item_index=None):
        """
        GetDrawingSizeF(self: GH_Chunk, item_name: str, item_index: int) -> SizeF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingSizeF(self: GH_Chunk, item_name: str) -> SizeF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetGuid(self, item_name, item_index=None):
        """
        GetGuid(self: GH_Chunk, item_name: str, item_index: int) -> Guid
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetGuid(self: GH_Chunk, item_name: str) -> Guid
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInt32(self, item_name, item_index=None):
        """
        GetInt32(self: GH_Chunk, item_name: str, item_index: int) -> int
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInt32(self: GH_Chunk, item_name: str) -> int
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInt64(self, item_name, item_index=None):
        """
        GetInt64(self: GH_Chunk, item_name: str, item_index: int) -> Int64
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInt64(self: GH_Chunk, item_name: str) -> Int64
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInterval1D(self, item_name, item_index=None):
        """
        GetInterval1D(self: GH_Chunk, item_name: str, item_index: int) -> GH_Interval1D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInterval1D(self: GH_Chunk, item_name: str) -> GH_Interval1D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInterval2D(self, item_name, item_index=None):
        """
        GetInterval2D(self: GH_Chunk, item_name: str, item_index: int) -> GH_Interval2D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInterval2D(self: GH_Chunk, item_name: str) -> GH_Interval2D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetLine(self, item_name, item_index=None):
        """
        GetLine(self: GH_Chunk, item_name: str, item_index: int) -> GH_Line
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetLine(self: GH_Chunk, item_name: str) -> GH_Line
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPath(self, item_name, *__args):
        """
        GetPath(self: GH_Chunk, item_name: str, basePath: str) -> Array[str]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            basePath: Base path for relative path resolution.
            Returns: An array of path strings. If the resolved relative path is different from the stored absolute 
             path, two strings will be returned.
        
        GetPath(self: GH_Chunk, item_name: str, item_index: int, basePath: str) -> Array[str]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            basePath: Base path for relative path resolution.
            Returns: An array of path strings. If the resolved relative path is different from the stored absolute 
             path, two strings will be returned.
        """
        pass

    def GetPlane(self, item_name, item_index=None):
        """
        GetPlane(self: GH_Chunk, item_name: str, item_index: int) -> GH_Plane
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPlane(self: GH_Chunk, item_name: str) -> GH_Plane
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint2D(self, item_name, item_index=None):
        """
        GetPoint2D(self: GH_Chunk, item_name: str, item_index: int) -> GH_Point2D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint2D(self: GH_Chunk, item_name: str) -> GH_Point2D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint3D(self, item_name, item_index=None):
        """
        GetPoint3D(self: GH_Chunk, item_name: str, item_index: int) -> GH_Point3D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint3D(self: GH_Chunk, item_name: str) -> GH_Point3D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint4D(self, item_name, item_index=None):
        """
        GetPoint4D(self: GH_Chunk, item_name: str, item_index: int) -> GH_Point4D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint4D(self: GH_Chunk, item_name: str) -> GH_Point4D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetSingle(self, item_name, item_index=None):
        """
        GetSingle(self: GH_Chunk, item_name: str, item_index: int) -> Single
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetSingle(self: GH_Chunk, item_name: str) -> Single
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetString(self, item_name, item_index=None):
        """
        GetString(self: GH_Chunk, item_name: str, item_index: int) -> str
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetString(self: GH_Chunk, item_name: str) -> str
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetVersion(self, item_name, item_index=None):
        """
        GetVersion(self: GH_Chunk, item_name: str, item_index: int) -> GH_Version
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetVersion(self: GH_Chunk, item_name: str) -> GH_Version
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    @staticmethod
    def InstantiateRoot(owner):
        """
        InstantiateRoot(owner: GH_Archive) -> GH_Chunk
        
            Construct a new instance of GH_Chunk which acts as a Root node. If you must 
                    create 
             a chunk from scratch, use this static method to create one.
        
        
            owner: The archive which owns this chunk.
        """
        pass

    def ItemExists(self, name, index=None):
        """
        ItemExists(self: GH_Chunk, name: str, index: int) -> bool
        
            Checks whether an item with the specified name and index exists. 
                    Only items with 
             index qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to test for.
            index: Index of item to test for. 
                    If index is less than zero, then ItemExists(string 
             name) is called instead.
        
            Returns: True if an item with the specified name and index exists, otherwise false.
        ItemExists(self: GH_Chunk, name: str) -> bool
        
            Gets the occupancy for a specific item name. Only items without index qualifiers are considered.
        
            name: Name of item to check for.
            Returns: True if an item with a similar name already exists, false if not.
        """
        pass

    def Read(self, *__args):
        """
        Read(self: GH_Chunk, node: XmlNode)
            Read this chunk and all child chunks from an Xml node.
        
            node: The Xml node to deserialize from, cannot be null.
        Read(self: GH_Chunk, reader: BinaryReader)
            Read this chunk and all child chunks from a binary stream.
        
            reader: The Binary reader to use, cannot be null.
        """
        pass

    def RemoveChunk(self, *__args):
        """
        RemoveChunk(self: GH_Chunk, chunk: GH_IChunk) -> bool
        
            Remove the specified chunk from the litter.
        
            chunk: Chunk to remove.
            Returns: True is chunk was removed, false if chunk is not part of this litter.
        RemoveChunk(self: GH_Chunk, chunk_name: str, chunk_index: int) -> bool
        
            Remove the first chunk with a matching name and index. 
                    Only chunks with index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            chunk_name: Name of chunk to remove.
            chunk_index: Index of chunk to remove.
            Returns: True is chunk was removed, false if no matching chunk could be found.
        RemoveChunk(self: GH_Chunk, chunk_name: str) -> bool
        
            Remove the first chunk with a matching name. 
                    Only chunks without index qualifiers 
             are considered. 
                    Name comparisons are not case-sensitive.
        
        
            chunk_name: Name of chunk to remove.
            Returns: True is chunk was removed, false if no matching chunk could be found.
        """
        pass

    def RemoveItem(self, itemName, itemIndex=None):
        """
        RemoveItem(self: GH_Chunk, itemName: str, itemIndex: int) -> bool
        
            Remove an indexed item from this chunk.
        
            itemName: Name of item.
            itemIndex: Index of item.
            Returns: True on success, false on failure.
        RemoveItem(self: GH_Chunk, itemName: str) -> bool
        
            Remove an unindexed item from this chunk.
        
            itemName: Name of item.
            Returns: True on success, false on failure.
        """
        pass

    def SetBoolean(self, item_name, *__args):
        """
        SetBoolean(self: GH_Chunk, item_name: str, item_index: int, item_value: bool)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetBoolean(self: GH_Chunk, item_name: str, item_value: bool)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetBoundingBox(self, item_name, *__args):
        """
        SetBoundingBox(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_BoundingBox)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetBoundingBox(self: GH_Chunk, item_name: str, item_value: GH_BoundingBox)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetByte(self, item_name, *__args):
        """
        SetByte(self: GH_Chunk, item_name: str, item_index: int, item_value: Byte)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetByte(self: GH_Chunk, item_name: str, item_value: Byte)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetByteArray(self, item_name, *__args):
        """
        SetByteArray(self: GH_Chunk, item_name: str, item_index: int, item_value: Array[Byte])
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetByteArray(self: GH_Chunk, item_name: str, item_value: Array[Byte])
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDate(self, item_name, *__args):
        """
        SetDate(self: GH_Chunk, item_name: str, item_index: int, item_value: DateTime)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDate(self: GH_Chunk, item_name: str, item_value: DateTime)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDecimal(self, item_name, *__args):
        """
        SetDecimal(self: GH_Chunk, item_name: str, item_index: int, item_value: Decimal)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDecimal(self: GH_Chunk, item_name: str, item_value: Decimal)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDouble(self, item_name, *__args):
        """
        SetDouble(self: GH_Chunk, item_name: str, item_index: int, item_value: float)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDouble(self: GH_Chunk, item_name: str, item_value: float)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDoubleArray(self, item_name, *__args):
        """
        SetDoubleArray(self: GH_Chunk, item_name: str, item_index: int, item_value: Array[float])
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDoubleArray(self: GH_Chunk, item_name: str, item_value: Array[float])
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingBitmap(self, item_name, *__args):
        """
        SetDrawingBitmap(self: GH_Chunk, item_name: str, item_index: int, item_value: Bitmap)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingBitmap(self: GH_Chunk, item_name: str, item_value: Bitmap)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingColor(self, item_name, *__args):
        """
        SetDrawingColor(self: GH_Chunk, item_name: str, item_index: int, item_value: Color)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingColor(self: GH_Chunk, item_name: str, item_value: Color)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingPoint(self, item_name, *__args):
        """
        SetDrawingPoint(self: GH_Chunk, item_name: str, item_index: int, item_value: Point)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingPoint(self: GH_Chunk, item_name: str, item_value: Point)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingPointF(self, item_name, *__args):
        """
        SetDrawingPointF(self: GH_Chunk, item_name: str, item_index: int, item_value: PointF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingPointF(self: GH_Chunk, item_name: str, item_value: PointF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingRectangle(self, item_name, *__args):
        """
        SetDrawingRectangle(self: GH_Chunk, item_name: str, item_index: int, item_value: Rectangle)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingRectangle(self: GH_Chunk, item_name: str, item_value: Rectangle)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingRectangleF(self, item_name, *__args):
        """
        SetDrawingRectangleF(self: GH_Chunk, item_name: str, item_index: int, item_value: RectangleF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingRectangleF(self: GH_Chunk, item_name: str, item_value: RectangleF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingSize(self, item_name, *__args):
        """
        SetDrawingSize(self: GH_Chunk, item_name: str, item_index: int, item_value: Size)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingSize(self: GH_Chunk, item_name: str, item_value: Size)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingSizeF(self, item_name, *__args):
        """
        SetDrawingSizeF(self: GH_Chunk, item_name: str, item_index: int, item_value: SizeF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingSizeF(self: GH_Chunk, item_name: str, item_value: SizeF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetGuid(self, item_name, *__args):
        """
        SetGuid(self: GH_Chunk, item_name: str, item_index: int, item_value: Guid)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetGuid(self: GH_Chunk, item_name: str, item_value: Guid)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInt32(self, item_name, *__args):
        """
        SetInt32(self: GH_Chunk, item_name: str, item_index: int, item_value: int)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInt32(self: GH_Chunk, item_name: str, item_value: int)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInt64(self, item_name, *__args):
        """
        SetInt64(self: GH_Chunk, item_name: str, item_index: int, item_value: Int64)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInt64(self: GH_Chunk, item_name: str, item_value: Int64)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInterval1D(self, item_name, *__args):
        """
        SetInterval1D(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Interval1D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInterval1D(self: GH_Chunk, item_name: str, item_value: GH_Interval1D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInterval2D(self, item_name, *__args):
        """
        SetInterval2D(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Interval2D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInterval2D(self: GH_Chunk, item_name: str, item_value: GH_Interval2D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetLine(self, item_name, *__args):
        """
        SetLine(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Line)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetLine(self: GH_Chunk, item_name: str, item_value: GH_Line)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPath(self, item_name, *__args):
        """
        SetPath(self: GH_Chunk, item_name: str, item_index: int, absolutePath: str, basePath: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            absolutePath: Absolute path to store.
            basePath: Base path. This will be used to also store a relative path.
        SetPath(self: GH_Chunk, item_name: str, absolutePath: str, basePath: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            absolutePath: Absolute path to store.
            basePath: Base path. This will be used to also store a relative path.
        """
        pass

    def SetPlane(self, item_name, *__args):
        """
        SetPlane(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Plane)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPlane(self: GH_Chunk, item_name: str, item_value: GH_Plane)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint2D(self, item_name, *__args):
        """
        SetPoint2D(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Point2D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint2D(self: GH_Chunk, item_name: str, item_value: GH_Point2D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint3D(self, item_name, *__args):
        """
        SetPoint3D(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Point3D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint3D(self: GH_Chunk, item_name: str, item_value: GH_Point3D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint4D(self, item_name, *__args):
        """
        SetPoint4D(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Point4D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint4D(self: GH_Chunk, item_name: str, item_value: GH_Point4D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetSingle(self, item_name, *__args):
        """
        SetSingle(self: GH_Chunk, item_name: str, item_index: int, item_value: Single)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetSingle(self: GH_Chunk, item_name: str, item_value: Single)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetString(self, item_name, *__args):
        """
        SetString(self: GH_Chunk, item_name: str, item_index: int, item_value: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetString(self: GH_Chunk, item_name: str, item_value: str)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetVersion(self, item_name, *__args):
        """
        SetVersion(self: GH_Chunk, item_name: str, item_value: GH_Version)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        SetVersion(self: GH_Chunk, item_name: str, item_index: int, item_value: GH_Version)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetVersion(self: GH_Chunk, item_name: str, major: int, minor: int, revision: int)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            major: Major component of Version structure.
            minor: Minor component of Version structure.
            revision: Revision component of Version structure.
        SetVersion(self: GH_Chunk, item_name: str, item_index: int, major: int, minor: int, revision: int)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            major: Major component of Version structure.
            minor: Minor component of Version structure.
            revision: Revision component of Version structure.
        """
        pass

    def TryGetBoolean(self, item_name, *__args):
        """
        TryGetBoolean(self: GH_Chunk, item_name: str, item_index: int, value: bool) -> (bool, bool)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetBoolean(self: GH_Chunk, item_name: str, value: bool) -> (bool, bool)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetBoundingBox(self, item_name, *__args):
        """
        TryGetBoundingBox(self: GH_Chunk, item_name: str, item_index: int, value: GH_BoundingBox) -> (bool, GH_BoundingBox)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetBoundingBox(self: GH_Chunk, item_name: str, value: GH_BoundingBox) -> (bool, GH_BoundingBox)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetByte(self, item_name, *__args):
        """
        TryGetByte(self: GH_Chunk, item_name: str, item_index: int, value: Byte) -> (bool, Byte)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetByte(self: GH_Chunk, item_name: str, value: Byte) -> (bool, Byte)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDate(self, item_name, *__args):
        """
        TryGetDate(self: GH_Chunk, item_name: str, item_index: int, value: DateTime) -> (bool, DateTime)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDate(self: GH_Chunk, item_name: str, value: DateTime) -> (bool, DateTime)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDecimal(self, item_name, *__args):
        """
        TryGetDecimal(self: GH_Chunk, item_name: str, item_index: int, value: Decimal) -> (bool, Decimal)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDecimal(self: GH_Chunk, item_name: str, value: Decimal) -> (bool, Decimal)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDouble(self, item_name, *__args):
        """
        TryGetDouble(self: GH_Chunk, item_name: str, item_index: int, value: float) -> (bool, float)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDouble(self: GH_Chunk, item_name: str, value: float) -> (bool, float)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingColor(self, item_name, *__args):
        """
        TryGetDrawingColor(self: GH_Chunk, item_name: str, item_index: int, value: Color) -> (bool, Color)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingColor(self: GH_Chunk, item_name: str, value: Color) -> (bool, Color)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingPoint(self, item_name, *__args):
        """
        TryGetDrawingPoint(self: GH_Chunk, item_name: str, item_index: int, value: Point) -> (bool, Point)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingPoint(self: GH_Chunk, item_name: str, value: Point) -> (bool, Point)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingPointF(self, item_name, *__args):
        """
        TryGetDrawingPointF(self: GH_Chunk, item_name: str, item_index: int, value: PointF) -> (bool, PointF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingPointF(self: GH_Chunk, item_name: str, value: PointF) -> (bool, PointF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingRectangle(self, item_name, *__args):
        """
        TryGetDrawingRectangle(self: GH_Chunk, item_name: str, item_index: int, value: Rectangle) -> (bool, Rectangle)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingRectangle(self: GH_Chunk, item_name: str, value: Rectangle) -> (bool, Rectangle)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingRectangleF(self, item_name, *__args):
        """
        TryGetDrawingRectangleF(self: GH_Chunk, item_name: str, item_index: int, value: RectangleF) -> (bool, RectangleF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingRectangleF(self: GH_Chunk, item_name: str, value: RectangleF) -> (bool, RectangleF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingSize(self, item_name, *__args):
        """
        TryGetDrawingSize(self: GH_Chunk, item_name: str, item_index: int, value: Size) -> (bool, Size)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingSize(self: GH_Chunk, item_name: str, value: Size) -> (bool, Size)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingSizeF(self, item_name, *__args):
        """
        TryGetDrawingSizeF(self: GH_Chunk, item_name: str, item_index: int, value: SizeF) -> (bool, SizeF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingSizeF(self: GH_Chunk, item_name: str, value: SizeF) -> (bool, SizeF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetGuid(self, item_name, *__args):
        """
        TryGetGuid(self: GH_Chunk, item_name: str, item_index: int, value: Guid) -> (bool, Guid)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetGuid(self: GH_Chunk, item_name: str, value: Guid) -> (bool, Guid)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInt32(self, item_name, *__args):
        """
        TryGetInt32(self: GH_Chunk, item_name: str, item_index: int, value: int) -> (bool, int)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInt32(self: GH_Chunk, item_name: str, value: int) -> (bool, int)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInt64(self, item_name, *__args):
        """
        TryGetInt64(self: GH_Chunk, item_name: str, item_index: int, value: Int64) -> (bool, Int64)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInt64(self: GH_Chunk, item_name: str, value: Int64) -> (bool, Int64)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInterval1D(self, item_name, *__args):
        """
        TryGetInterval1D(self: GH_Chunk, item_name: str, item_index: int, value: GH_Interval1D) -> (bool, GH_Interval1D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInterval1D(self: GH_Chunk, item_name: str, value: GH_Interval1D) -> (bool, GH_Interval1D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInterval2D(self, item_name, *__args):
        """
        TryGetInterval2D(self: GH_Chunk, item_name: str, item_index: int, value: GH_Interval2D) -> (bool, GH_Interval2D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInterval2D(self: GH_Chunk, item_name: str, value: GH_Interval2D) -> (bool, GH_Interval2D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetLine(self, item_name, *__args):
        """
        TryGetLine(self: GH_Chunk, item_name: str, item_index: int, value: GH_Line) -> (bool, GH_Line)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetLine(self: GH_Chunk, item_name: str, value: GH_Line) -> (bool, GH_Line)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPlane(self, item_name, *__args):
        """
        TryGetPlane(self: GH_Chunk, item_name: str, item_index: int, value: GH_Plane) -> (bool, GH_Plane)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPlane(self: GH_Chunk, item_name: str, value: GH_Plane) -> (bool, GH_Plane)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint2D(self, item_name, *__args):
        """
        TryGetPoint2D(self: GH_Chunk, item_name: str, item_index: int, value: GH_Point2D) -> (bool, GH_Point2D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint2D(self: GH_Chunk, item_name: str, value: GH_Point2D) -> (bool, GH_Point2D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint3D(self, item_name, *__args):
        """
        TryGetPoint3D(self: GH_Chunk, item_name: str, item_index: int, value: GH_Point3D) -> (bool, GH_Point3D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint3D(self: GH_Chunk, item_name: str, value: GH_Point3D) -> (bool, GH_Point3D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint4D(self, item_name, *__args):
        """
        TryGetPoint4D(self: GH_Chunk, item_name: str, item_index: int, value: GH_Point4D) -> (bool, GH_Point4D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint4D(self: GH_Chunk, item_name: str, value: GH_Point4D) -> (bool, GH_Point4D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetSingle(self, item_name, *__args):
        """
        TryGetSingle(self: GH_Chunk, item_name: str, item_index: int, value: Single) -> (bool, Single)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetSingle(self: GH_Chunk, item_name: str, value: Single) -> (bool, Single)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetString(self, item_name, *__args):
        """
        TryGetString(self: GH_Chunk, item_name: str, item_index: int, value: str) -> (bool, str)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetString(self: GH_Chunk, item_name: str, value: str) -> (bool, str)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetVersion(self, item_name, *__args):
        """
        TryGetVersion(self: GH_Chunk, item_name: str, item_index: int, value: GH_Version) -> (bool, GH_Version)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetVersion(self: GH_Chunk, item_name: str, value: GH_Version) -> (bool, GH_Version)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def Write(self, writer):
        """
        Write(self: GH_Chunk, writer: XmlWriter)
            Serialize this chunk into an Xml stream.
        
            writer: Xml writer used for serialization.
        Write(self: GH_Chunk, writer: BinaryWriter)
            Write this chunk and all child chunks to a binary stream.
        
            writer: The Binary writer to use, cannot be null.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, chunk_archive: GH_Archive)
        __new__(cls: type, chunk_archive: GH_Archive, chunk_name: str)
        __new__(cls: type, chunk_archive: GH_Archive, chunk_name: str, chunk_index: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Archive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the archive that owns the Root of the tree this chunk belongs to.

Get: Archive(self: GH_Chunk) -> GH_Archive

"""

    ArchiveLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representing the URI with which the archive is associated. 
            The location may be a null string.

Get: ArchiveLocation(self: GH_Chunk) -> str

"""

    ChunkCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of child chunks contained in this chunk. 
            The set of all child chunks is referred to as a 'litter'.

Get: ChunkCount(self: GH_Chunk) -> int

"""

    Chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the internal list of child chunks. 
            Do not access this list unless you know what you are doing.

Get: Chunks(self: GH_Chunk) -> List[GH_IChunk]

"""

    HasComments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether or not comments have been stored in this chunk.

Get: HasComments(self: GH_Chunk) -> bool

"""

    HasIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index existence implication. The item is considered to have an index qualifier 
            if the index value is larger than or equal to zero.

Get: HasIndex(self: GH_Chunk) -> bool

"""

    HasName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name validity of this item. 
            The item is considered to have an invalid name if string.IsNullOrEmpty(name)

Get: HasName(self: GH_Chunk) -> bool

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this chunk. The index is set by the owner of this chunk. 
            Indices smaller than zero imply no index has been set. 
            The combination of name+index is always unique among a set of chunks in the same litter.

Get: Index(self: GH_Chunk) -> int

"""

    ItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items contained in this chunk.

Get: ItemCount(self: GH_Chunk) -> int

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the internal list of items. 
            Do not access this list unless you know what you are doing.

Get: Items(self: GH_Chunk) -> List[GH_Item]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this chunk. The name is set by the owner of this chunk. 
            Names must be at least 1 character long. 
            The combination of name+index is always unique among a set of chunks in a single litter.

Get: Name(self: GH_Chunk) -> str

"""


    ChunkKeyedCollection = None
    m_archive = None
    m_chunks = None
    m_comments = None
    m_index = None
    m_items = None
    m_name = None
    name_comp = None


class GH_Compression(object):
    """ Provides static methods for compression of byte-arrays. """
    @staticmethod
    def Compress(data):
        """
        Compress(data: Array[Byte]) -> Array[Byte]
        
            Compress an array of bytes using the Deflate algorithm.
        
            data: Byte array to compress.
            Returns: An array of compressed bytes.
        """
        pass

    @staticmethod
    def Decompress(compressedData):
        """
        Decompress(compressedData: Array[Byte]) -> Array[Byte]
        
            Decompress an array of bytes using the Deflate algorithm.
        
            compressedData: Byte array to decompress.
            Returns: An array of decompressed bytes.
        """
        pass


class GH_IBinarySupport:
    """
    Interface which declares all methods required for objects that 
                can be (de)serialized to and from a binary archive.
    """
    def Read(self, reader):
        """
        Read(self: GH_IBinarySupport, reader: BinaryReader)
            Called when an object is required to deserialize itself.
        
            reader: Reader object to be used for deserialization.
        """
        pass

    def Write(self, writer):
        """
        Write(self: GH_IBinarySupport, writer: BinaryWriter)
            Called when an object is required to serialize itself.
        
            writer: Writer object to be used for serialization.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GH_IXmlSupport:
    """
    Interface which declares all methods required for objects that 
                can be (de)serialized to and from an Xml archive.
    """
    def Read(self, node):
        """
        Read(self: GH_IXmlSupport, node: XmlNode)
            Called when an object is required to deserialize itself.
        
            node: Node object to be used for deserialization.
        """
        pass

    def Write(self, writer):
        """
        Write(self: GH_IXmlSupport, writer: XmlWriter)
            Called when an object is required to serialize itself.
        
            writer: Writer object to be used for serialization.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GH_IChunk(GH_IBinarySupport, GH_IXmlSupport):
    """ Base interface for all Archive Chunks. """
    def AddMessage(self, m, t):
        """
        AddMessage(self: GH_IChunk, m: str, t: GH_Message_Type)
            Log a new message with the top-level archive. 
                    Messages are collected during 
             read/write operations, 
                    and can be displayed to the user upon completion using 
             GH_Archive.ShowMessageLog().
        
        
            m: Message text.
            t: Message type.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Archive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the archive that owns the Root of the tree this chunk belongs to.

Get: Archive(self: GH_IChunk) -> GH_Archive

"""

    ArchiveLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representing the URI with which the archive is associated. 
            The location may be a null string.

Get: ArchiveLocation(self: GH_IChunk) -> str

"""

    ChunkCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of child chunks contained in this chunk. 
            The set of all child chunks is referred to as a 'litter'.

Get: ChunkCount(self: GH_IChunk) -> int

"""

    Chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the internal list of child chunks. 
            Do not access this list unless you know what you are doing.

Get: Chunks(self: GH_IChunk) -> List[GH_IChunk]

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this chunk. The index is set by the owner of this chunk. 
            Indices smaller than zero imply no index has been set. 
            The combination of name+index is always unique among a set of chunks in the same litter.

Get: Index(self: GH_IChunk) -> int

"""

    ItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items contained in this chunk.

Get: ItemCount(self: GH_IChunk) -> int

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the internal list of items. 
            Do not access this list unless you know what you are doing.

Get: Items(self: GH_IChunk) -> List[GH_Item]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this chunk. The name is set by the owner of this chunk. 
            Names must be at least 1 character long. 
            The combination of name+index is always unique among a set of chunks in a single litter.

Get: Name(self: GH_IChunk) -> str

"""



class GH_IReader(GH_IChunk, GH_IBinarySupport, GH_IXmlSupport):
    """ Provides access to a subset of GH_Chunk methods used for reading archives. """
    def ChunkExists(self, name, index=None):
        """
        ChunkExists(self: GH_IReader, name: str, index: int) -> bool
        
            Checks whether a chunk with the specified name and index exists in the litter. 
                    
             Only chunks with index qualifiers are considered. 
                    Name comparisons are not 
             case-sensitive.
        
        
            name: Name of chunk to test for.
            index: Index of chunk to test for. 
                    If less than zero, ChunkExists(string chunk_name) is 
             called instead.
        
            Returns: True if a chunk with the specified name and index exists, otherwise false.
        ChunkExists(self: GH_IReader, name: str) -> bool
        
            Checks whether a chunk with the specified name exists in the litter. 
                    Only chunks 
             without index qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of chunk to test for.
            Returns: True if a chunk with the specified name exists, otherwise false.
        """
        pass

    def FindChunk(self, name, index=None):
        """
        FindChunk(self: GH_IReader, name: str, index: int) -> GH_IReader
        
            Finds the first chunk in the list that matches the given name and index. 
                    Only 
             chunks with index qualifiers are considered.
        
        
            name: Name of chunk to search for.
            index: Index of chunk to search for. 
                    If less than zero, FindChunk(string chunk_name) is 
             called instead.
        
            Returns: The child chunk that matches the given name and index, 
                    or null of no matching 
             chunk could be found.
        
        FindChunk(self: GH_IReader, name: str) -> GH_IReader
        
            Finds the first chunk in the litter that matches the given name. 
                    Only chunks 
             without index qualifiers are considered.
        
        
            name: Name of chunk to search for.
            Returns: The child chunk that matches the given name, 
                    or null of no matching chunk could be 
             found.
        """
        pass

    def FindItem(self, name, index=None):
        """
        FindItem(self: GH_IReader, name: str, index: int) -> GH_Item
        
            Finds the first item that matches the given name and index. 
                    Only items with index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to search for.
            index: Index of item to search for. 
                    If less than zero, then FindItem(string name) is 
             called instead.
        
            Returns: The item that matches the given name and index, 
                    or null of no matching item could 
             be found.
        
        FindItem(self: GH_IReader, name: str) -> GH_Item
        
            Finds the first item that matches the given name. 
                    Only items without index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to search for.
            Returns: The item that matches the given name, 
                    or null of no matching item could be found.
        """
        pass

    def GetBoolean(self, item_name, item_index=None):
        """
        GetBoolean(self: GH_IReader, item_name: str, item_index: int) -> bool
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetBoolean(self: GH_IReader, item_name: str) -> bool
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetBoundingBox(self, item_name, item_index=None):
        """
        GetBoundingBox(self: GH_IReader, item_name: str, item_index: int) -> GH_BoundingBox
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetBoundingBox(self: GH_IReader, item_name: str) -> GH_BoundingBox
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetByte(self, item_name, item_index=None):
        """
        GetByte(self: GH_IReader, item_name: str, item_index: int) -> Byte
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetByte(self: GH_IReader, item_name: str) -> Byte
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetByteArray(self, item_name, item_index=None):
        """
        GetByteArray(self: GH_IReader, item_name: str, item_index: int) -> Array[Byte]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetByteArray(self: GH_IReader, item_name: str) -> Array[Byte]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDate(self, item_name, item_index=None):
        """
        GetDate(self: GH_IReader, item_name: str, item_index: int) -> DateTime
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDate(self: GH_IReader, item_name: str) -> DateTime
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDecimal(self, item_name, item_index=None):
        """
        GetDecimal(self: GH_IReader, item_name: str, item_index: int) -> Decimal
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDecimal(self: GH_IReader, item_name: str) -> Decimal
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDouble(self, item_name, item_index=None):
        """
        GetDouble(self: GH_IReader, item_name: str, item_index: int) -> float
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDouble(self: GH_IReader, item_name: str) -> float
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDoubleArray(self, item_name, item_index=None):
        """
        GetDoubleArray(self: GH_IReader, item_name: str, item_index: int) -> Array[float]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDoubleArray(self: GH_IReader, item_name: str) -> Array[float]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingBitmap(self, item_name, item_index=None):
        """
        GetDrawingBitmap(self: GH_IReader, item_name: str, item_index: int) -> Bitmap
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingBitmap(self: GH_IReader, item_name: str) -> Bitmap
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingColor(self, item_name, item_index=None):
        """
        GetDrawingColor(self: GH_IReader, item_name: str, item_index: int) -> Color
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingColor(self: GH_IReader, item_name: str) -> Color
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingPoint(self, item_name, item_index=None):
        """
        GetDrawingPoint(self: GH_IReader, item_name: str, item_index: int) -> Point
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingPoint(self: GH_IReader, item_name: str) -> Point
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingPointF(self, item_name, item_index=None):
        """
        GetDrawingPointF(self: GH_IReader, item_name: str, item_index: int) -> PointF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingPointF(self: GH_IReader, item_name: str) -> PointF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingRectangle(self, item_name, item_index=None):
        """
        GetDrawingRectangle(self: GH_IReader, item_name: str, item_index: int) -> Rectangle
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingRectangle(self: GH_IReader, item_name: str) -> Rectangle
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingRectangleF(self, item_name, item_index=None):
        """
        GetDrawingRectangleF(self: GH_IReader, item_name: str, item_index: int) -> RectangleF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingRectangleF(self: GH_IReader, item_name: str) -> RectangleF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingSize(self, item_name, item_index=None):
        """
        GetDrawingSize(self: GH_IReader, item_name: str, item_index: int) -> Size
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingSize(self: GH_IReader, item_name: str) -> Size
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetDrawingSizeF(self, item_name, item_index=None):
        """
        GetDrawingSizeF(self: GH_IReader, item_name: str, item_index: int) -> SizeF
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetDrawingSizeF(self: GH_IReader, item_name: str) -> SizeF
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetGuid(self, item_name, item_index=None):
        """
        GetGuid(self: GH_IReader, item_name: str, item_index: int) -> Guid
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetGuid(self: GH_IReader, item_name: str) -> Guid
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInt32(self, item_name, item_index=None):
        """
        GetInt32(self: GH_IReader, item_name: str, item_index: int) -> int
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInt32(self: GH_IReader, item_name: str) -> int
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInt64(self, item_name, item_index=None):
        """
        GetInt64(self: GH_IReader, item_name: str, item_index: int) -> Int64
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInt64(self: GH_IReader, item_name: str) -> Int64
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInterval1D(self, item_name, item_index=None):
        """
        GetInterval1D(self: GH_IReader, item_name: str, item_index: int) -> GH_Interval1D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInterval1D(self: GH_IReader, item_name: str) -> GH_Interval1D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetInterval2D(self, item_name, item_index=None):
        """
        GetInterval2D(self: GH_IReader, item_name: str, item_index: int) -> GH_Interval2D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetInterval2D(self: GH_IReader, item_name: str) -> GH_Interval2D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetLine(self, item_name, item_index=None):
        """
        GetLine(self: GH_IReader, item_name: str, item_index: int) -> GH_Line
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetLine(self: GH_IReader, item_name: str) -> GH_Line
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPath(self, item_name, *__args):
        """
        GetPath(self: GH_IReader, item_name: str, item_index: int, basePath: str) -> Array[str]
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            basePath: Base path for relative path resolution.
            Returns: An array of path strings. If the resolved relative path is different from the stored absolute 
             path, two strings will be returned.
        
        GetPath(self: GH_IReader, item_name: str, basePath: str) -> Array[str]
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            basePath: Base path for relative path resolution.
            Returns: An array of path strings. If the resolved relative path is different from the stored absolute 
             path, two strings will be returned.
        """
        pass

    def GetPlane(self, item_name, item_index=None):
        """
        GetPlane(self: GH_IReader, item_name: str, item_index: int) -> GH_Plane
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPlane(self: GH_IReader, item_name: str) -> GH_Plane
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint2D(self, item_name, item_index=None):
        """
        GetPoint2D(self: GH_IReader, item_name: str, item_index: int) -> GH_Point2D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint2D(self: GH_IReader, item_name: str) -> GH_Point2D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint3D(self, item_name, item_index=None):
        """
        GetPoint3D(self: GH_IReader, item_name: str, item_index: int) -> GH_Point3D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint3D(self: GH_IReader, item_name: str) -> GH_Point3D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetPoint4D(self, item_name, item_index=None):
        """
        GetPoint4D(self: GH_IReader, item_name: str, item_index: int) -> GH_Point4D
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetPoint4D(self: GH_IReader, item_name: str) -> GH_Point4D
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetSingle(self, item_name, item_index=None):
        """
        GetSingle(self: GH_IReader, item_name: str, item_index: int) -> Single
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetSingle(self: GH_IReader, item_name: str) -> Single
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetString(self, item_name, item_index=None):
        """
        GetString(self: GH_IReader, item_name: str, item_index: int) -> str
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetString(self: GH_IReader, item_name: str) -> str
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def GetVersion(self, item_name, item_index=None):
        """
        GetVersion(self: GH_IReader, item_name: str, item_index: int) -> GH_Version
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            Returns: The inner value of the item.
        GetVersion(self: GH_IReader, item_name: str) -> GH_Version
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            Returns: The inner value of the item.
        """
        pass

    def ItemExists(self, name, index=None):
        """
        ItemExists(self: GH_IReader, name: str, index: int) -> bool
        
            Checks whether an item with the specified name and index exists. 
                    Only items with 
             index qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to test for.
            index: Index of item to test for. 
                    If index is less than zero, then ItemExists(string 
             name) is called instead.
        
            Returns: True if an item with the specified name and index exists, otherwise false.
        ItemExists(self: GH_IReader, name: str) -> bool
        
            Checks whether an item with the specified name exists. 
                    Only items without index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            name: Name of item to test for.
            Returns: True if an item with the specified name exists, otherwise false.
        """
        pass

    def TryGetBoolean(self, item_name, *__args):
        """
        TryGetBoolean(self: GH_IReader, item_name: str, item_index: int, value: bool) -> (bool, bool)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetBoolean(self: GH_IReader, item_name: str, value: bool) -> (bool, bool)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetBoundingBox(self, item_name, *__args):
        """
        TryGetBoundingBox(self: GH_IReader, item_name: str, item_index: int, value: GH_BoundingBox) -> (bool, GH_BoundingBox)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetBoundingBox(self: GH_IReader, item_name: str, value: GH_BoundingBox) -> (bool, GH_BoundingBox)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetByte(self, item_name, *__args):
        """
        TryGetByte(self: GH_IReader, item_name: str, item_index: int, value: Byte) -> (bool, Byte)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetByte(self: GH_IReader, item_name: str, value: Byte) -> (bool, Byte)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDate(self, item_name, *__args):
        """
        TryGetDate(self: GH_IReader, item_name: str, item_index: int, value: DateTime) -> (bool, DateTime)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDate(self: GH_IReader, item_name: str, value: DateTime) -> (bool, DateTime)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDecimal(self, item_name, *__args):
        """
        TryGetDecimal(self: GH_IReader, item_name: str, item_index: int, value: Decimal) -> (bool, Decimal)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDecimal(self: GH_IReader, item_name: str, value: Decimal) -> (bool, Decimal)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDouble(self, item_name, *__args):
        """
        TryGetDouble(self: GH_IReader, item_name: str, item_index: int, value: float) -> (bool, float)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDouble(self: GH_IReader, item_name: str, value: float) -> (bool, float)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingColor(self, item_name, *__args):
        """
        TryGetDrawingColor(self: GH_IReader, item_name: str, item_index: int, value: Color) -> (bool, Color)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingColor(self: GH_IReader, item_name: str, value: Color) -> (bool, Color)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingPoint(self, item_name, *__args):
        """
        TryGetDrawingPoint(self: GH_IReader, item_name: str, item_index: int, value: Point) -> (bool, Point)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingPoint(self: GH_IReader, item_name: str, value: Point) -> (bool, Point)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingPointF(self, item_name, *__args):
        """
        TryGetDrawingPointF(self: GH_IReader, item_name: str, item_index: int, value: PointF) -> (bool, PointF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingPointF(self: GH_IReader, item_name: str, value: PointF) -> (bool, PointF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingRectangle(self, item_name, *__args):
        """
        TryGetDrawingRectangle(self: GH_IReader, item_name: str, item_index: int, value: Rectangle) -> (bool, Rectangle)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingRectangle(self: GH_IReader, item_name: str, value: Rectangle) -> (bool, Rectangle)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingRectangleF(self, item_name, *__args):
        """
        TryGetDrawingRectangleF(self: GH_IReader, item_name: str, item_index: int, value: RectangleF) -> (bool, RectangleF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingRectangleF(self: GH_IReader, item_name: str, value: RectangleF) -> (bool, RectangleF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingSize(self, item_name, *__args):
        """
        TryGetDrawingSize(self: GH_IReader, item_name: str, item_index: int, value: Size) -> (bool, Size)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingSize(self: GH_IReader, item_name: str, value: Size) -> (bool, Size)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetDrawingSizeF(self, item_name, *__args):
        """
        TryGetDrawingSizeF(self: GH_IReader, item_name: str, item_index: int, value: SizeF) -> (bool, SizeF)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetDrawingSizeF(self: GH_IReader, item_name: str, value: SizeF) -> (bool, SizeF)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetGuid(self, item_name, *__args):
        """
        TryGetGuid(self: GH_IReader, item_name: str, value: Guid) -> (bool, Guid)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetGuid(self: GH_IReader, item_name: str, item_index: int, value: Guid) -> (bool, Guid)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInt32(self, item_name, *__args):
        """
        TryGetInt32(self: GH_IReader, item_name: str, item_index: int, value: int) -> (bool, int)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInt32(self: GH_IReader, item_name: str, value: int) -> (bool, int)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInt64(self, item_name, *__args):
        """
        TryGetInt64(self: GH_IReader, item_name: str, item_index: int, value: Int64) -> (bool, Int64)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInt64(self: GH_IReader, item_name: str, value: Int64) -> (bool, Int64)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInterval1D(self, item_name, *__args):
        """
        TryGetInterval1D(self: GH_IReader, item_name: str, item_index: int, value: GH_Interval1D) -> (bool, GH_Interval1D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInterval1D(self: GH_IReader, item_name: str, value: GH_Interval1D) -> (bool, GH_Interval1D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetInterval2D(self, item_name, *__args):
        """
        TryGetInterval2D(self: GH_IReader, item_name: str, item_index: int, value: GH_Interval2D) -> (bool, GH_Interval2D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetInterval2D(self: GH_IReader, item_name: str, value: GH_Interval2D) -> (bool, GH_Interval2D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetLine(self, item_name, *__args):
        """
        TryGetLine(self: GH_IReader, item_name: str, item_index: int, value: GH_Line) -> (bool, GH_Line)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetLine(self: GH_IReader, item_name: str, value: GH_Line) -> (bool, GH_Line)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPlane(self, item_name, *__args):
        """
        TryGetPlane(self: GH_IReader, item_name: str, item_index: int, value: GH_Plane) -> (bool, GH_Plane)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPlane(self: GH_IReader, item_name: str, value: GH_Plane) -> (bool, GH_Plane)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint2D(self, item_name, *__args):
        """
        TryGetPoint2D(self: GH_IReader, item_name: str, item_index: int, value: GH_Point2D) -> (bool, GH_Point2D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint2D(self: GH_IReader, item_name: str, value: GH_Point2D) -> (bool, GH_Point2D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint3D(self, item_name, *__args):
        """
        TryGetPoint3D(self: GH_IReader, item_name: str, item_index: int, value: GH_Point3D) -> (bool, GH_Point3D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint3D(self: GH_IReader, item_name: str, value: GH_Point3D) -> (bool, GH_Point3D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetPoint4D(self, item_name, *__args):
        """
        TryGetPoint4D(self: GH_IReader, item_name: str, item_index: int, value: GH_Point4D) -> (bool, GH_Point4D)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetPoint4D(self: GH_IReader, item_name: str, value: GH_Point4D) -> (bool, GH_Point4D)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetSingle(self, item_name, *__args):
        """
        TryGetSingle(self: GH_IReader, item_name: str, item_index: int, value: Single) -> (bool, Single)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetSingle(self: GH_IReader, item_name: str, value: Single) -> (bool, Single)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetString(self, item_name, *__args):
        """
        TryGetString(self: GH_IReader, item_name: str, item_index: int, value: str) -> (bool, str)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetString(self: GH_IReader, item_name: str, value: str) -> (bool, str)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def TryGetVersion(self, item_name, *__args):
        """
        TryGetVersion(self: GH_IReader, item_name: str, item_index: int, value: GH_Version) -> (bool, GH_Version)
        
            Gets the value of the item with the specified name and index. 
                    Name comparison is 
             not case-sensitive.
        
        
            item_name: Name of item to retrieve.
            item_index: Index of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        TryGetVersion(self: GH_IReader, item_name: str, value: GH_Version) -> (bool, GH_Version)
        
            Gets the value of the item with the specified name. 
                    Name comparison is not 
             case-sensitive.
        
        
            item_name: Name of item to retrieve.
            value: Target of assignment.
            Returns: True if the value was set.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GH_IWriter(GH_IChunk, GH_IBinarySupport, GH_IXmlSupport):
    """ Provides access to a subset of GH_Chunk methods used for writing archives. """
    def AddComment(self, comment_text):
        """
        AddComment(self: GH_IWriter, comment_text: str)
            Adds a text comment to this chunk. Comments are serialized only if the output flavour is a 
            
                     human readable format. Comments are never deserialized, they are purely for the benefit 
             of the
                    humans reading the file data.
        
        
            comment_text: The content of the comment, 
                    text might be altered if it contains invalid 
             characters for a chosen format flavour.
        """
        pass

    def CreateChunk(self, chunk_name, chunk_index=None):
        """
        CreateChunk(self: GH_IWriter, chunk_name: str, chunk_index: int) -> GH_IWriter
        
            Create a new child chunk with the specified name and index qualifier. 
                    If another 
             chunk already exists with similar properties, an exception will be thrown.
        
        
            chunk_name: Name of new child.
            chunk_index: Index of new child.
        CreateChunk(self: GH_IWriter, chunk_name: str) -> GH_IWriter
        
            Create a new child chunk with the specified name but without an index qualifier. 
                    
             If another chunk already exists with similar properties, an exception will be thrown.
        
        
            chunk_name: Name of new child chunk.
        """
        pass

    def RemoveChunk(self, *__args):
        """
        RemoveChunk(self: GH_IWriter, chunk: GH_IChunk) -> bool
        
            Remove the specified chunk from the litter.
        
            chunk: Chunk to remove.
            Returns: True is chunk was removed, false if chunk is not part of this litter.
        RemoveChunk(self: GH_IWriter, chunk_name: str, chunk_index: int) -> bool
        
            Remove the first chunk with a matching name and index. 
                    Only chunks with index 
             qualifiers are considered. 
                    Name comparisons are not case-sensitive.
        
        
            chunk_name: Name of chunk to remove.
            chunk_index: Index of chunk to remove.
            Returns: True is chunk was removed, false if no matching chunk could be found.
        RemoveChunk(self: GH_IWriter, chunk_name: str) -> bool
        
            Remove the first chunk with a matching name. 
                    Only chunks without index qualifiers 
             are considered. 
                    Name comparisons are not case-sensitive.
        
        
            chunk_name: Name of chunk to remove.
            Returns: True is chunk was removed, false if no matching chunk could be found.
        """
        pass

    def RemoveItem(self, itemName, itemIndex=None):
        """
        RemoveItem(self: GH_IWriter, itemName: str, itemIndex: int) -> bool
        
            Remove an indexed item from this chunk.
        
            itemName: Name of item.
            itemIndex: Index of item.
            Returns: True on success, false on failure.
        RemoveItem(self: GH_IWriter, itemName: str) -> bool
        
            Remove an unindexed item from this chunk.
        
            itemName: Name of item.
            Returns: True on success, false on failure.
        """
        pass

    def SetBoolean(self, item_name, *__args):
        """
        SetBoolean(self: GH_IWriter, item_name: str, item_index: int, item_value: bool)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetBoolean(self: GH_IWriter, item_name: str, item_value: bool)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetBoundingBox(self, item_name, *__args):
        """
        SetBoundingBox(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_BoundingBox)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetBoundingBox(self: GH_IWriter, item_name: str, item_value: GH_BoundingBox)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetByte(self, item_name, *__args):
        """
        SetByte(self: GH_IWriter, item_name: str, item_index: int, item_value: Byte)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetByte(self: GH_IWriter, item_name: str, item_value: Byte)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetByteArray(self, item_name, *__args):
        """
        SetByteArray(self: GH_IWriter, item_name: str, item_index: int, item_value: Array[Byte])
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetByteArray(self: GH_IWriter, item_name: str, item_value: Array[Byte])
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDate(self, item_name, *__args):
        """
        SetDate(self: GH_IWriter, item_name: str, item_index: int, item_value: DateTime)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDate(self: GH_IWriter, item_name: str, item_value: DateTime)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDecimal(self, item_name, *__args):
        """
        SetDecimal(self: GH_IWriter, item_name: str, item_index: int, item_value: Decimal)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDecimal(self: GH_IWriter, item_name: str, item_value: Decimal)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDouble(self, item_name, *__args):
        """
        SetDouble(self: GH_IWriter, item_name: str, item_index: int, item_value: float)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDouble(self: GH_IWriter, item_name: str, item_value: float)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDoubleArray(self, item_name, *__args):
        """
        SetDoubleArray(self: GH_IWriter, item_name: str, item_index: int, item_value: Array[float])
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDoubleArray(self: GH_IWriter, item_name: str, item_value: Array[float])
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingBitmap(self, item_name, *__args):
        """
        SetDrawingBitmap(self: GH_IWriter, item_name: str, item_index: int, item_value: Bitmap)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingBitmap(self: GH_IWriter, item_name: str, item_value: Bitmap)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingColor(self, item_name, *__args):
        """
        SetDrawingColor(self: GH_IWriter, item_name: str, item_index: int, item_value: Color)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingColor(self: GH_IWriter, item_name: str, item_value: Color)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingPoint(self, item_name, *__args):
        """
        SetDrawingPoint(self: GH_IWriter, item_name: str, item_index: int, item_value: Point)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingPoint(self: GH_IWriter, item_name: str, item_value: Point)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingPointF(self, item_name, *__args):
        """
        SetDrawingPointF(self: GH_IWriter, item_name: str, item_index: int, item_value: PointF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingPointF(self: GH_IWriter, item_name: str, item_value: PointF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingRectangle(self, item_name, *__args):
        """
        SetDrawingRectangle(self: GH_IWriter, item_name: str, item_index: int, item_value: Rectangle)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingRectangle(self: GH_IWriter, item_name: str, item_value: Rectangle)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingRectangleF(self, item_name, *__args):
        """
        SetDrawingRectangleF(self: GH_IWriter, item_name: str, item_index: int, item_value: RectangleF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingRectangleF(self: GH_IWriter, item_name: str, item_value: RectangleF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingSize(self, item_name, *__args):
        """
        SetDrawingSize(self: GH_IWriter, item_name: str, item_index: int, item_value: Size)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingSize(self: GH_IWriter, item_name: str, item_value: Size)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetDrawingSizeF(self, item_name, *__args):
        """
        SetDrawingSizeF(self: GH_IWriter, item_name: str, item_index: int, item_value: SizeF)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetDrawingSizeF(self: GH_IWriter, item_name: str, item_value: SizeF)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetGuid(self, item_name, *__args):
        """
        SetGuid(self: GH_IWriter, item_name: str, item_index: int, item_value: Guid)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetGuid(self: GH_IWriter, item_name: str, item_value: Guid)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInt32(self, item_name, *__args):
        """
        SetInt32(self: GH_IWriter, item_name: str, item_index: int, item_value: int)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInt32(self: GH_IWriter, item_name: str, item_value: int)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInt64(self, item_name, *__args):
        """
        SetInt64(self: GH_IWriter, item_name: str, item_index: int, item_value: Int64)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInt64(self: GH_IWriter, item_name: str, item_value: Int64)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInterval1D(self, item_name, *__args):
        """
        SetInterval1D(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Interval1D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInterval1D(self: GH_IWriter, item_name: str, item_value: GH_Interval1D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetInterval2D(self, item_name, *__args):
        """
        SetInterval2D(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Interval2D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetInterval2D(self: GH_IWriter, item_name: str, item_value: GH_Interval2D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetLine(self, item_name, *__args):
        """
        SetLine(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Line)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetLine(self: GH_IWriter, item_name: str, item_value: GH_Line)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPath(self, item_name, *__args):
        """
        SetPath(self: GH_IWriter, item_name: str, item_index: int, absolutePath: str, basePath: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            absolutePath: Absolute path to store.
            basePath: Base path. This will be used to also store a relative path.
        SetPath(self: GH_IWriter, item_name: str, absolutePath: str, basePath: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            absolutePath: Absolute path to store.
            basePath: Base path. This will be used to also store a relative path.
        """
        pass

    def SetPlane(self, item_name, *__args):
        """
        SetPlane(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Plane)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPlane(self: GH_IWriter, item_name: str, item_value: GH_Plane)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint2D(self, item_name, *__args):
        """
        SetPoint2D(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Point2D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint2D(self: GH_IWriter, item_name: str, item_value: GH_Point2D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint3D(self, item_name, *__args):
        """
        SetPoint3D(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Point3D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint3D(self: GH_IWriter, item_name: str, item_value: GH_Point3D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetPoint4D(self, item_name, *__args):
        """
        SetPoint4D(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Point4D)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetPoint4D(self: GH_IWriter, item_name: str, item_value: GH_Point4D)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetSingle(self, item_name, *__args):
        """
        SetSingle(self: GH_IWriter, item_name: str, item_index: int, item_value: Single)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        SetSingle(self: GH_IWriter, item_name: str, item_value: Single)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        """
        pass

    def SetString(self, item_name, *__args):
        """
        SetString(self: GH_IWriter, item_name: str, item_index: int, item_value: str)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add. If a null String is supplied, a zero-length String will be serialized.
        SetString(self: GH_IWriter, item_name: str, item_value: str)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add. If a null String is supplied, a zero-length String will be serialized.
        """
        pass

    def SetVersion(self, item_name, *__args):
        """
        SetVersion(self: GH_IWriter, item_name: str, major: int, minor: int, revision: int)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            major: Major component of version structure.
            minor: Minor component of version structure.
            revision: Revision component of version structure.
        SetVersion(self: GH_IWriter, item_name: str, item_index: int, major: int, minor: int, revision: int)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            major: Major component of version structure.
            minor: Minor component of version structure.
            revision: Revision component of version structure.
        SetVersion(self: GH_IWriter, item_name: str, item_value: GH_Version)
            Add a new data item to this chunk. 
                    The name must be unique or an exception will be 
             thrown.
        
        
            item_name: Name of item to add.
            item_value: Value of item to add.
        SetVersion(self: GH_IWriter, item_name: str, item_index: int, item_value: GH_Version)
            Add a new data item to this chunk. 
                    The combination of name and index must be 
             unique or an exception will be thrown.
        
        
            item_name: Name of item to add.
            item_index: Index of item to add.
            item_value: Value of item to add.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GH_LooseChunk(GH_Chunk, GH_IWriter, GH_IChunk, GH_IBinarySupport, GH_IXmlSupport, GH_IReader):
    """
    A utility class for creating partial archives.
    
    GH_LooseChunk(chunk_name: str)
    """
    def Deserialize_Binary(self, content):
        """
        Deserialize_Binary(self: GH_LooseChunk, content: Array[Byte])
            Deserializes a byte array.
        
            content: Byte array to deserialize.
            Returns: True on success, false on failure.
        """
        pass

    def Deserialize_Xml(self, xml_content):
        """
        Deserialize_Xml(self: GH_LooseChunk, xml_content: str)
            Deserializes an Xml string.
        
            xml_content: Xml to deserialize.
            Returns: True on success, false on failure.
        """
        pass

    def Serialize_Binary(self):
        """
        Serialize_Binary(self: GH_LooseChunk) -> Array[Byte]
        
            Serializes the data tree into a byte array.
            Returns: An array of bytes representing the Loose chunk.
        """
        pass

    def Serialize_Xml(self):
        """
        Serialize_Xml(self: GH_LooseChunk) -> str
        
            Serializes the data tree into an Xml string.
            Returns: A string containing the Xml content.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, chunk_name):
        """ __new__(cls: type, chunk_name: str) """
        pass

    m_archive = None
    m_chunks = None
    m_comments = None
    m_index = None
    m_items = None
    m_name = None


class GH_Message(object):
    """
    Represents an archive log message. 
                Messages are collected during read/write operations.
    
    GH_Message()
    GH_Message(message_content: str)
    GH_Message(message_content: str, message_type: GH_Message_Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, message_content=None, message_type=None):
        """
        __new__(cls: type)
        __new__(cls: type, message_content: str)
        __new__(cls: type, message_content: str, message_type: GH_Message_Type)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text content of this message.

Get: Message(self: GH_Message) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of this message.

Get: Type(self: GH_Message) -> GH_Message_Type

"""



class GH_Message_Type(Enum, IComparable, IFormattable, IConvertible):
    """
    Message type flag.
    
    enum GH_Message_Type, values: error (2), info (0), warning (1)
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

    error = None
    info = None
    value__ = None
    warning = None


class ID(object, IComparable[ID]):
    """
    An ID is used to uniquely identify a specific item.
    
    ID(name: str)
    ID(name: str, index: int)
    """
    def ToString(self):
        """
        ToString(self: ID) -> str
        
            Gets a string representation for this ID.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, index=None):
        """
        __new__[ID]() -> ID
        
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, index: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HasIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the index has been set.

Get: HasIndex(self: ID) -> bool

"""

    HasName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the name has been set. 
            Every valid ID must have a name.

Get: HasName(self: ID) -> bool

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of this ID, if there is no valid index then -1 is returned.

Get: Index(self: ID) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this ID.

Get: Name(self: ID) -> str

"""



