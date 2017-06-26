class NumberingSchema(Element, IDisposable):
    """ A class to support assigning numbers to elements of a particular kind for the purpose of tagging and scheduling them. """
    def AppendSequence(self, fromPartition, toPartition):
        """
        AppendSequence(self: NumberingSchema, fromPartition: str, toPartition: str)
            Appends all elements of one numbering sequence to the end of another sequence.
        
            fromPartition: Name of the partition that determines which numbering sequence to append.
           
             The sequence must exist already, otherwise an exception will be thrown.
        
            toPartition: Name of a partition into which the source sequence is going to be appended.
           
             The sequence must exist already, otherwise an exception will be thrown.
        """
        pass

    def AssignElementsToSequence(self, elementIds, partitionName):
        """ AssignElementsToSequence(self: NumberingSchema, elementIds: ISet[ElementId], partitionName: str) """
        pass

    def ChangeNumber(self, partition, fromNumber, toNumber):
        """
        ChangeNumber(self: NumberingSchema, partition: str, fromNumber: int, toNumber: int) -> IList[ElementId]
        
            Replaces an existing number with a new one (that does not exist yet).
        
            partition: Name of the partition that identifies the sequence containing the number to be 
             changed.
        
            fromNumber: Number to be changed; there must already be an element with that number in the 
             sequence.
        
            toNumber: Number to change to; no element must have this number yet in the sequence.
            Returns: A collection of elements affected by the change of the number
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetMinimumNumberOfDigits(document):
        """
        GetMinimumNumberOfDigits(document: Document) -> int
        
            Returns the minimum number of digits to be used for formating
           the Number 
             parameter of all enumerable elements of the given document.
        
        
            document: The document this value is going to be applied to.
            Returns: The current number of formatting digits
        """
        pass

    @staticmethod
    def GetNumberingSchema(document, schemaType):
        """
        GetNumberingSchema(document: Document, schemaType: NumberingSchemaType) -> NumberingSchema
        
            Returns an instance of the specified Numbering Schema in the given document.
        
            document: A document to get the numbering schema from.
            schemaType: The type of a built-in schema to get.
            Returns: Instance of the specified schema.
        """
        pass

    def GetNumberingSequences(self):
        """
        GetNumberingSequences(self: NumberingSchema) -> IList[str]
        
            Returns all numbering sequences within this numbering schema.
            Returns: A collection of partition names of all numbering sequences currently present in 
             this schema.
        """
        pass

    def GetNumbers(self, partition):
        """
        GetNumbers(self: NumberingSchema, partition: str) -> IList[IntegerRange]
        
            Returns all numbers currently used in the given numbering sequence
        
            partition: Name of the partition that identifies the sequence. The sequence must exist.
            Returns: A collection of integer ranges
        """
        pass

    @staticmethod
    def GetSchemasInDocument(document):
        """
        GetSchemasInDocument(document: Document) -> ISet[ElementId]
        
            Returns a set of Ids of all Numbering Schema elements for a given document.
        
            document: A document to get numbering schema from.
            Returns: Ids of NumberingSchema elements. An empty set if no schemas are found in the 
             given document.
        """
        pass

    @staticmethod
    def IsValidPartitionName(name, message):
        """
        IsValidPartitionName(name: str) -> (bool, str)
        
            Tests if the given string can be used as a name for a numbering partition.
        
            name: A name to validate.
            Returns: Returns True if the name can be used; or False if the string contains invalid 
             characters.
        """
        pass

    def MergeSequences(self, sourcePartitions, newPartition):
        """ MergeSequences(self: NumberingSchema, sourcePartitions: IList[str], newPartition: str) """
        pass

    def MoveSequence(self, fromPartition, newPartition):
        """
        MoveSequence(self: NumberingSchema, fromPartition: str, newPartition: str)
            Moves all elements of a numbering sequence from one partition to another.
        
            fromPartition: Name of the partition that determines which numbering sequence to move.
           The 
             sequence must exist already, otherwise an exception will be thrown.
        
            newPartition: Name of a partition into which the source sequence is going to be moved.
           
             The schema must not have a sequence for this partition yet
           (i.e. the schema 
             does not have an element that was assigned to such a partition.)
           Leading 
             and trailing white space is ignored in the given string and will be
           removed 
             automatically.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveGaps(self, partition):
        """
        RemoveGaps(self: NumberingSchema, partition: str)
            Removes gaps, if any, in a numbering sequence
        
            partition: Name of the partition that identifies the sequence. The sequence must exist.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    @staticmethod
    def SetMinimumNumberOfDigits(document, value):
        """
        SetMinimumNumberOfDigits(document: Document, value: int)
            Sets a new value for the minimum number of digits to be used for formating
           
             the Number parameter of all numbered elements of the given document.
        
        
            document: The document in which the new value will be in applied.
            value: New value for the minimum number of digits.
        """
        pass

    def ShiftNumbers(self, partition, firstNumber):
        """
        ShiftNumbers(self: NumberingSchema, partition: str, firstNumber: int)
            Shifts all numbers in the sequence so the starting number has the given value.
        
            partition: Name of the partition that identifies the sequence. The sequence must exist.
            firstNumber: Value for the new first (lowest) number of the sequence.
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

    NumberingParameterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the parameter that stores values of the numbers on enumerated elements.

Get: NumberingParameterId(self: NumberingSchema) -> ElementId

"""

    SchemaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the kind of elements/objects this numbering schema is used for.

Get: SchemaType(self: NumberingSchema) -> NumberingSchemaType

"""


    MaximumStartingNumber = 1073741822

