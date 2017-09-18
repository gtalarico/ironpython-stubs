# encoding: utf-8
# module Rhino.DocObjects.Tables calls itself Tables
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitmapTable(object, IEnumerable[BitmapEntry], IEnumerable, IRhinoTable[BitmapEntry]):
    """ Stores the list of bitmaps in a Rhino document. """
    def AddBitmap(self, bitmapFilename, replaceExisting):
        """
        AddBitmap(self: BitmapTable, bitmapFilename: str, replaceExisting: bool) -> int
        
            Adds a new bitmap with specified name to the bitmap table.
        
            bitmapFilename: If NULL or empty, then a unique name of the form "Bitmap 01" will be automatically created.
            replaceExisting: If true and the there is alread a bitmap using the specified name, then that bitmap is replaced.
             
                    If false and there is already a bitmap using the specified name, then -1 is 
             returned.
        
            Returns: index of new bitmap in table on success. -1 on error.
        """
        pass

    def DeleteBitmap(self, bitmapFilename):
        """
        DeleteBitmap(self: BitmapTable, bitmapFilename: str) -> bool
        
            Deletes a bitmap.
        
            bitmapFilename: The bitmap file name.
            Returns: true if successful. false if the bitmap cannot be deleted because it
                    is the current 
             bitmap or because it bitmap contains active geometry.
        """
        pass

    def ExportToFile(self, index, path):
        """
        ExportToFile(self: BitmapTable, index: int, path: str) -> bool
        
            Writes a bitmap to a file.
        
            index: The index of the bitmap to be written.
            path: The full path, including file name and extension, name of the file to write.
            Returns: true if successful.
        """
        pass

    def ExportToFiles(self, directoryPath, overwrite):
        """
        ExportToFiles(self: BitmapTable, directoryPath: str, overwrite: int) -> int
        
            Exports all the bitmaps in the table to files.
        
            directoryPath: full path to the directory where the bitmaps should be saved.
                    If NULL, a dialog is 
             used to interactively get the directory name.
        
            overwrite: 0 = no, 1 = yes, 2 = ask.
            Returns: Number of bitmaps written.
        """
        pass

    def Find(self, name, createFile, fileName):
        """
        Find(self: BitmapTable, name: str, createFile: bool) -> (BitmapEntry, str)
        
            This function first attempts to find the file with "name" on the disk.
                    If it does 
             find it, "fileName" is set to the full path of the file and
                    the BitmapEntry 
             returned will be null, even if there was a BitmapEntry
                    with "name" in the bitmap 
             table.
                    If the function cannot find the file on the disk, it searches the bitmap
           
                      table.  If it finds it, the returned BitmapEntry entry will be the entry
                    
             in the table with that name.
                    Additionally, if "createFile" is true, and an entry is 
             found, the file
                    will be written to the disk and it's full path will be contained in 
             "fileName".
        
        
            name: Name of the file to search for including file extension.
            createFile: If this is true, and the file is not found on the disk but is found in
                    the 
             BitmapTable, then the BitmapEntry will get saved to the Rhino bitmap
                    file cache and 
             fileName will contain the full path to the cached file.
        
            Returns: Returns null if "name" was found on the disk.  If name was not found on the disk,
                    
             returns the BitmapEntry with the specified name if it is found in the bitmap table
                    
             and null if it was not found in the bitmap table.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BitmapTable) -> IEnumerator[BitmapEntry]
        
            BitmapTable enumerator
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BitmapEntry](enumerable: IEnumerable[BitmapEntry], value: BitmapEntry) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bitmaps in the table.

Get: Count(self: BitmapTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that owns this bitmap table.

Get: Document(self: BitmapTable) -> RhinoDoc

"""



class DimStyleTable(object, IEnumerable[DimensionStyle], IEnumerable, IRhinoTable[DimensionStyle]):
    # no doc
    def Add(self, name, reference=None):
        """
        Add(self: DimStyleTable, name: str, reference: bool) -> int
        
            Adds a new dimension style to the document. The new dimension style will be initialized
                
                 with the current default dimension style properties.
        
        
            name: Name of the new dimension style. If null or empty, Rhino automatically generates the name.
            reference: if true the dimstyle will not be saved in files.
            Returns: index of new dimension style.
        Add(self: DimStyleTable, name: str) -> int
        
            Adds a new dimension style to the document. The new dimension style will be initialized
                
                 with the current default dimension style properties.
        
        
            name: Name of the new dimension style. If null or empty, Rhino automatically generates the name.
            Returns: index of new dimension style.
        """
        pass

    def DeleteDimensionStyle(self, index, quiet):
        """ DeleteDimensionStyle(self: DimStyleTable, index: int, quiet: bool) -> bool """
        pass

    def Find(self, name, ignoreDeletedDimensionStyles):
        """ Find(self: DimStyleTable, name: str, ignoreDeletedDimensionStyles: bool) -> DimensionStyle """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DimStyleTable) -> IEnumerator[DimensionStyle] """
        pass

    def GetUnusedDimensionStyleName(self):
        """ GetUnusedDimensionStyleName(self: DimStyleTable) -> str """
        pass

    def SetCurrentDimensionStyleIndex(self, index, quiet):
        """ SetCurrentDimensionStyleIndex(self: DimStyleTable, index: int, quiet: bool) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DimensionStyle](enumerable: IEnumerable[DimensionStyle], value: DimensionStyle) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of dimstyles in the table.

Get: Count(self: DimStyleTable) -> int

"""

    CurrentDimensionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDimensionStyle(self: DimStyleTable) -> DimensionStyle

"""

    CurrentDimensionStyleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDimensionStyleIndex(self: DimStyleTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this dimstyle table.

Get: Document(self: DimStyleTable) -> RhinoDoc

"""



class FontTable(object, IEnumerable[Font], IEnumerable, IRhinoTable[Font]):
    """ Font tables store the list of fonts in a Rhino document. """
    def FindOrCreate(self, face, bold, italic):
        """ FindOrCreate(self: FontTable, face: str, bold: bool, italic: bool) -> int """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FontTable) -> IEnumerator[Font] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Font](enumerable: IEnumerable[Font], value: Font) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of fonts in the table.

Get: Count(self: FontTable) -> int

"""

    CurrentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" font.  Unless otherwise specified,
            new dimension objects are assigned to the current font. The current
            font is never deleted.
            Returns: Zero based font index of the current font.

Get: CurrentIndex(self: FontTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: FontTable) -> RhinoDoc

"""



class GroupTable(object):
    """ Group tables store the list of groups in a Rhino document. """
    def Add(self, *__args):
        """
        Add(self: GroupTable, groupName: str, objectIds: IEnumerable[Guid]) -> int
        Add(self: GroupTable, objectIds: IEnumerable[Guid]) -> int
        Add(self: GroupTable, groupName: str) -> int
        
            Adds a new empty group to the group table.
        
            groupName: name of new group.
            Returns: >=0 index of new group. 
                    -1 group not added because a group with that name already 
             exists.
        
        Add(self: GroupTable) -> int
        
            Adds a new empty group to the group table.
            Returns: >=0 index of new group. 
                    -1 group not added because a group with that name already 
             exists.
        """
        pass

    def AddToGroup(self, groupIndex, *__args):
        """
        AddToGroup(self: GroupTable, groupIndex: int, objectIds: IEnumerable[Guid]) -> bool
        AddToGroup(self: GroupTable, groupIndex: int, objectId: Guid) -> bool
        
            Adds an object to an existing group.
        
            groupIndex: The group index value.
            objectId: An ID of an object.
            Returns: true if the operation was successful.
        """
        pass

    def ChangeGroupName(self, groupIndex, newName):
        """ ChangeGroupName(self: GroupTable, groupIndex: int, newName: str) -> bool """
        pass

    def Delete(self, groupIndex):
        """
        Delete(self: GroupTable, groupIndex: int) -> bool
        
            Deletes a group from this table.
                    Deleted groups are kept in the runtime group table 
             so that undo
                    will work with groups.  Call IsDeleted() to determine if a group is 
             deleted.
        
        
            groupIndex: An group index to be deleted.
            Returns: true if the operation was successful.
        """
        pass

    def Find(self, groupName, ignoreDeletedGroups):
        """
        Find(self: GroupTable, groupName: str, ignoreDeletedGroups: bool) -> int
        
            Finds a group with a given name.
        
            groupName: Name of group to search for. Ignores case.
            ignoreDeletedGroups: true means don't search deleted groups.
            Returns: >=0 index of the group with the given name.
                    -1 no group found with the given name.
        """
        pass

    def GroupMembers(self, groupIndex):
        """
        GroupMembers(self: GroupTable, groupIndex: int) -> Array[RhinoObject]
        
            Gets an array of all of the objects in a group.
        
            groupIndex: The index of the group in this table.
            Returns: An array with all the objects in the specified group.
        """
        pass

    def GroupName(self, groupIndex):
        """ GroupName(self: GroupTable, groupIndex: int) -> str """
        pass

    def GroupNames(self, ignoreDeletedGroups):
        """ GroupNames(self: GroupTable, ignoreDeletedGroups: bool) -> Array[str] """
        pass

    def GroupObjectCount(self, groupIndex):
        """ GroupObjectCount(self: GroupTable, groupIndex: int) -> int """
        pass

    def Hide(self, groupIndex):
        """ Hide(self: GroupTable, groupIndex: int) -> int """
        pass

    def IsDeleted(self, groupIndex):
        """ IsDeleted(self: GroupTable, groupIndex: int) -> bool """
        pass

    def Lock(self, groupIndex):
        """ Lock(self: GroupTable, groupIndex: int) -> int """
        pass

    def Show(self, groupIndex):
        """ Show(self: GroupTable, groupIndex: int) -> int """
        pass

    def Undelete(self, groupIndex):
        """ Undelete(self: GroupTable, groupIndex: int) -> bool """
        pass

    def Unlock(self, groupIndex):
        """ Unlock(self: GroupTable, groupIndex: int) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of groups in the group table.

Get: Count(self: GroupTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this group table.

Get: Document(self: GroupTable) -> RhinoDoc

"""



class GroupTableEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: GroupTableEventArgs) -> RhinoDoc

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventType(self: GroupTableEventArgs) -> GroupTableEventType

"""



class GroupTableEventType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GroupTableEventType, values: Added (0), Deleted (1), Modified (3), Sorted (4), Undeleted (2) """
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

    Added = None
    Deleted = None
    Modified = None
    Sorted = None
    Undeleted = None
    value__ = None


class HatchPatternTable(object, IEnumerable[HatchPattern], IEnumerable, IRhinoTable[HatchPattern]):
    """ All of the hatch pattern definitions contained in a rhino document. """
    def Add(self, pattern):
        """
        Add(self: HatchPatternTable, pattern: HatchPattern) -> int
        
            Adds a new hatch pattern with specified definition to the table.
        
            pattern: definition of new hatch pattern. The information in pattern is copied.
                    If 
             patern.Name is empty the a unique name of the form "HatchPattern 01"
                    will be 
             automatically created.
        
            Returns: >=0 index of new hatch pattern
                    -1  not added because a hatch pattern with that name 
             already exists or
                    some other problem occured.
        """
        pass

    def Find(self, name, ignoreDeleted):
        """
        Find(self: HatchPatternTable, name: str, ignoreDeleted: bool) -> int
        
            Finds the hatch pattern with a given name. Search ignores case.
        
            name: The name of the hatch patter to be found.
            ignoreDeleted: true means don't search deleted hatch patterns.
            Returns: Index of the hatch pattern with the given name. -1 if no hatch pattern found.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: HatchPatternTable) -> IEnumerator[HatchPattern] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HatchPattern](enumerable: IEnumerable[HatchPattern], value: HatchPattern) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of patterns in the table.

Get: Count(self: HatchPatternTable) -> int

"""

    CurrentHatchPatternIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" hatch pattern.  Unless otherwise
            specified, new objects are assigned to the current hatch pattern.
            The current hatch pattern is never locked, hidden, or deleted.

Get: CurrentHatchPatternIndex(self: HatchPatternTable) -> int

Set: CurrentHatchPatternIndex(self: HatchPatternTable) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: HatchPatternTable) -> RhinoDoc

"""



class InstanceDefinitionTable(object, IEnumerable[InstanceDefinition], IEnumerable, IRhinoTable[InstanceDefinition]):
    # no doc
    def Add(self, name, description, basePoint, geometry, attributes=None):
        """
        Add(self: InstanceDefinitionTable, name: str, description: str, basePoint: Point3d, geometry: GeometryBase, attributes: ObjectAttributes) -> int
        
            Adds an instance definition to the instance definition table.
        
            name: The definition name.
            description: The definition description.
            basePoint: A base point.
            geometry: An element.
            attributes: An attribute.
            Returns: >=0  index of instance definition in the instance definition table. -1 on failure.
        Add(self: InstanceDefinitionTable, name: str, description: str, basePoint: Point3d, geometry: IEnumerable[GeometryBase]) -> int
        Add(self: InstanceDefinitionTable, name: str, description: str, basePoint: Point3d, geometry: IEnumerable[GeometryBase], attributes: IEnumerable[ObjectAttributes]) -> int
        """
        pass

    def Compact(self, ignoreUndoReferences):
        """
        Compact(self: InstanceDefinitionTable, ignoreUndoReferences: bool)
            Purge deleted instance definition information that is not in use.
                    This function is 
             time consuming and should be used in a thoughtful manner.
        
        
            ignoreUndoReferences: If false, then deleted instance definition information that could possibly
                    be 
             undeleted by the Undo command will not be deleted. If true, then all
                    deleted 
             instance definition information is deleted.
        """
        pass

    def Delete(self, idefIndex, deleteReferences, quiet):
        """
        Delete(self: InstanceDefinitionTable, idefIndex: int, deleteReferences: bool, quiet: bool) -> bool
        
            Deletes the instance definition.
        
            idefIndex: zero based index of instance definition to delete.
                    This must be in the range 0 <= 
             idefIndex < InstanceDefinitionTable.Count.
        
            deleteReferences: true to delete all references to this definition.
                    false to delete definition only 
             if there are no references.
        
            quiet: If true, no warning message box appears if an instance definition cannot be
                    deleted 
             because it is the current layer or it contains active geometry.
        
            Returns: true if successful. false if the instance definition has active references and bDeleteReferences 
             is false.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: InstanceDefinitionTable, instanceId: Guid, ignoreDeletedInstanceDefinitions: bool) -> InstanceDefinition
        
            Finds the instance definition with a given id.
        
            instanceId: Unique id of the instance definition to search for.
            ignoreDeletedInstanceDefinitions: true means don't search deleted instance definitions.
            Returns: The specified instance definition, or null if nothing matching was found.
        Find(self: InstanceDefinitionTable, instanceDefinitionName: str, ignoreDeletedInstanceDefinitions: bool) -> InstanceDefinition
        
            Finds the instance definition with a given name.
        
            instanceDefinitionName: name of instance definition to search for (ignores case)
            ignoreDeletedInstanceDefinitions: true means don't search deleted instance definitions.
            Returns: The specified instance definition, or null if nothing matching was found.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: InstanceDefinitionTable) -> IEnumerator[InstanceDefinition] """
        pass

    def GetList(self, ignoreDeleted):
        """
        GetList(self: InstanceDefinitionTable, ignoreDeleted: bool) -> Array[InstanceDefinition]
        
            Gets an array of instance definitions.
        
            ignoreDeleted: If true then deleted idefs are filtered out.
            Returns: An array of instance definitions. This can be empty, but not null.
        """
        pass

    def GetUnusedInstanceDefinitionName(self, root=None, defaultSuffix=None):
        """
        GetUnusedInstanceDefinitionName(self: InstanceDefinitionTable, root: str, defaultSuffix: UInt32) -> str
        
            Gets unsed instance definition name used as default when creating
                    new instance 
             definitions.
        
        
            root: The returned name is 'root nn'  If root is empty, then 'Block' (localized) is used.
            defaultSuffix: Unique names are created by appending a decimal number to the
                    localized term for 
             "Block" as in "Block 01", "Block 02",
                    and so on.  When defaultSuffix is supplied, 
             the search for an unused
                    name begins at "Block suffix".
        
            Returns: An unused instance definition name string.
        GetUnusedInstanceDefinitionName(self: InstanceDefinitionTable, root: str) -> str
        
            Gets unsed instance definition name used as default when creating
                    new instance 
             definitions.
        
        
            root: The returned name is 'root nn'  If root is empty, then 'Block' (localized) is used.
            Returns: An unused instance definition name string.
        GetUnusedInstanceDefinitionName(self: InstanceDefinitionTable) -> str
        
            Gets unsed instance definition name used as default when creating
                    new instance 
             definitions.
        
            Returns: An unused instance definition name string.
        """
        pass

    def MakeSourcePathRelative(self, idef, relative, quiet):
        """
        MakeSourcePathRelative(self: InstanceDefinitionTable, idef: InstanceDefinition, relative: bool, quiet: bool) -> bool
        
            Marks the source path for a linked instance definition as relative or absolute.
        
            idef: The instance definition to be marked.
            relative: If true, the path should be considered as relative.If false, the path should be considered as 
             absolute.
        
            quiet: If true, then message boxes about erroneous parameters will not be shown.
            Returns: true if the instance defintion could be modified.
        """
        pass

    def Modify(self, *__args):
        """
        Modify(self: InstanceDefinitionTable, idefIndex: int, newName: str, newDescription: str, quiet: bool) -> bool
        
            Modifies the instance definition name and description.
                    Does not change instance 
             definition ID or geometry.
        
        
            idefIndex: The index of the instance definition to be modified.
            newName: The new name.
            newDescription: The new description string.
            quiet: If true, information message boxes pop up when illegal changes are attempted.
            Returns: true if successful.
        Modify(self: InstanceDefinitionTable, idef: InstanceDefinition, newName: str, newDescription: str, quiet: bool) -> bool
        
            Modifies the instance definition name and description.
                    Does not change instance 
             definition ID or geometry.
        
        
            idef: The instance definition to be modified.
            newName: The new name.
            newDescription: The new description string.
            quiet: If true, information message boxes pop up when illegal changes are attempted.
            Returns: true if successful.
        """
        pass

    def ModifyGeometry(self, idefIndex, newGeometry, newAttributes=None):
        """
        ModifyGeometry(self: InstanceDefinitionTable, idefIndex: int, newGeometry: GeometryBase, newAttributes: ObjectAttributes) -> bool
        ModifyGeometry(self: InstanceDefinitionTable, idefIndex: int, newGeometry: IEnumerable[GeometryBase]) -> bool
        ModifyGeometry(self: InstanceDefinitionTable, idefIndex: int, newGeometry: IEnumerable[GeometryBase], newAttributes: IEnumerable[ObjectAttributes]) -> bool
        """
        pass

    def Purge(self, idefIndex):
        """
        Purge(self: InstanceDefinitionTable, idefIndex: int) -> bool
        
            Purges an instance definition and its definition geometry.
        
            idefIndex: zero based index of instance definition to delete.
                    This must be in the range 0 <= 
             idefIndex < InstanceDefinitionTable.Count.
        
            Returns: True if successful. False if the instance definition cannot be purged
                    because it is 
             in use by reference objects or undo information.
        """
        pass

    def Undelete(self, idefIndex):
        """
        Undelete(self: InstanceDefinitionTable, idefIndex: int) -> bool
        
            Undeletes an instance definition that has been deleted by Delete()
        
            idefIndex: zero based index of instance definition to delete.
                    This must be in the range 0 <= 
             idefIndex < InstanceDefinitionTable.Count.
        
            Returns: true if successful
        """
        pass

    def UndoModify(self, idefIndex):
        """
        UndoModify(self: InstanceDefinitionTable, idefIndex: int) -> bool
        
            Restores the instance definition to its previous state,
                    if the instance definition 
             has been modified and the modification can be undone.
        
        
            idefIndex: The index of the instance definition to be restored.
            Returns: true if operation succeeded.
        """
        pass

    def UpdateLinkedInstanceDefinition(self, idefIndex, filename, updateNestedLinks, quiet):
        """
        UpdateLinkedInstanceDefinition(self: InstanceDefinitionTable, idefIndex: int, filename: str, updateNestedLinks: bool, quiet: bool) -> bool
        
            Read the objects from a file and use them as the instance's definition geometry.
        
            idefIndex: zero based index of instance definition to delete.
                    This must be in the range 0 <= 
             idefIndex < InstanceDefinitionTable.Count.
        
            filename: name of file (can be any type of file that Rhino or a plug-in can read)
            updateNestedLinks: If true and the instance definition referes to a linked instance definition,
                    that 
             needs to be updated, then the nested defition is also updated. If
                    false, nested 
             updates are skipped.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[InstanceDefinition](enumerable: IEnumerable[InstanceDefinition], value: InstanceDefinition) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of items in the instance definitions table, excluding deleted definitions.

Get: ActiveCount(self: InstanceDefinitionTable) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of items in the instance definitions table.

Get: Count(self: InstanceDefinitionTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: InstanceDefinitionTable) -> RhinoDoc

"""



class InstanceDefinitionTableEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: InstanceDefinitionTableEventArgs) -> RhinoDoc

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventType(self: InstanceDefinitionTableEventArgs) -> InstanceDefinitionTableEventType

"""

    InstanceDefinitionIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstanceDefinitionIndex(self: InstanceDefinitionTableEventArgs) -> int

"""

    NewState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewState(self: InstanceDefinitionTableEventArgs) -> InstanceDefinition

"""

    OldState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldState(self: InstanceDefinitionTableEventArgs) -> InstanceDefinitionGeometry

"""



class InstanceDefinitionTableEventType(Enum, IComparable, IFormattable, IConvertible):
    """ enum InstanceDefinitionTableEventType, values: Added (0), Deleted (1), Modified (3), Sorted (4), Undeleted (2) """
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

    Added = None
    Deleted = None
    Modified = None
    Sorted = None
    Undeleted = None
    value__ = None


class LayerTable(object, IEnumerable[Layer], IEnumerable, IRhinoTable[Layer]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: LayerTable) -> int
        
            Adds a new layer with default definition to the layer table.
            Returns: index of new layer.
        Add(self: LayerTable, layerName: str, layerColor: Color) -> int
        
            Adds a new layer with specified definition to the layer table.
        
            layerName: Name for new layer. Cannot be a null or zero-length string.
            layerColor: Color of new layer. Alpha components will be ignored.
            Returns: >=0 index of new layer
                    -1  layer not added because a layer with that name already 
             exists.
        
        Add(self: LayerTable, layer: Layer) -> int
        
            Adds a new layer with specified definition to the layer table.
        
            layer: definition of new layer. The information in layer is copied. If layer.Name is empty
                    
             the a unique name of the form "Layer 01" will be automatically created.
        
            Returns: >=0 index of new layer
                    -1  layer not added because a layer with that name already 
             exists.
        """
        pass

    def AddReferenceLayer(self, layer=None):
        """
        AddReferenceLayer(self: LayerTable) -> int
        
            Adds a new reference layer with default definition to the layer table.
                    Reference 
             layers are not saved in files.
        
            Returns: index of new layer.
        AddReferenceLayer(self: LayerTable, layer: Layer) -> int
        
            Adds a new reference layer with specified definition to the layer table
                    Reference 
             layers are not saved in files.
        
        
            layer: definition of new layer. The information in layer is copied. If layer.Name is empty
                    
             the a unique name of the form "Layer 01" will be automatically created.
        
            Returns: >=0 index of new layer
                    -1  layer not added because a layer with that name already 
             exists.
        """
        pass

    def Delete(self, layerIndex, quiet):
        """
        Delete(self: LayerTable, layerIndex: int, quiet: bool) -> bool
        
            Deletes layer.
        
            layerIndex: zero based index of layer to delete. This must be in the range 0 <= layerIndex < 
             LayerTable.Count.
        
            quiet: If true, no warning message box appears if a layer the layer cannot be
                    deleted 
             because it is the current layer or it contains active geometry.
        
            Returns: true if successful. false if layerIndex is out of range or the the layer cannot be
                    
             deleted because it is the current layer or because it layer contains active geometry.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: LayerTable, layerId: Guid, ignoreDeletedLayers: bool) -> int
        
            Finds a layer with a matching ID.
        
            layerId: A valid layer ID.
            ignoreDeletedLayers: If true, deleted layers are not checked.
            Returns: >=0 index of the layer with the given name
                    -1  no layer has the given name.
        Find(self: LayerTable, layerName: str, ignoreDeletedLayers: bool) -> int
        
            Finds the layer with a given name. If multiple layers exist that have the same name, the
               
                  first match layer index will be returned.
        
        
            layerName: name of layer to search for. The search ignores case.
            ignoreDeletedLayers: true means don't search deleted layers.
            Returns: >=0 index of the layer with the given name
                    -1  no layer has the given name.
        """
        pass

    def FindByFullPath(self, layerPath, ignoreDeletedLayers):
        """ FindByFullPath(self: LayerTable, layerPath: str, ignoreDeletedLayers: bool) -> int """
        pass

    def FindNext(self, index, layerName, ignoreDeletedLayers):
        """ FindNext(self: LayerTable, index: int, layerName: str, ignoreDeletedLayers: bool) -> int """
        pass

    def ForceLayerVisible(self, *__args):
        """
        ForceLayerVisible(self: LayerTable, layerIndex: int) -> bool
        
            Makes a layer and all of its parent layers visible.
        
            layerIndex: The layer index to be made visible.
            Returns: true if the operation succeeded.
        ForceLayerVisible(self: LayerTable, layerId: Guid) -> bool
        
            Makes a layer and all of its parent layers visible.
        
            layerId: The layer ID to be made visible.
            Returns: true if the operation succeeded.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LayerTable) -> IEnumerator[Layer] """
        pass

    def GetUnusedLayerName(self, ignoreDeleted):
        """
        GetUnusedLayerName(self: LayerTable, ignoreDeleted: bool) -> str
        
            Gets the next unused layer name used as default when creating new layers.
        
            ignoreDeleted: If this is true then Rhino may use a name used by a deleted layer.
            Returns: An unused layer name string.
        """
        pass

    def Modify(self, newSettings, layerIndex, quiet):
        """
        Modify(self: LayerTable, newSettings: Layer, layerIndex: int, quiet: bool) -> bool
        
            Modifies layer settings.
        
            newSettings: This information is copied.
            layerIndex: zero based index of layer to set.  This must be in the range 0 <= layerIndex < LayerTable.Count.
            quiet: if true, information message boxes pop up when illegal changes are attempted.
            Returns: true if successful. false if layerIndex is out of range or the settings attempt
                    to 
             lock or hide the current layer.
        """
        pass

    def Purge(self, layerIndex, quiet):
        """
        Purge(self: LayerTable, layerIndex: int, quiet: bool) -> bool
        
            Delete layer and all geometry objects on a layer
        
            layerIndex: zero based index of layer to delete. This must be in the range 0 <= layerIndex < 
             LayerTable.Count.
        
            quiet: If true, no warning message box appears if a layer the layer cannot be
                    deleted 
             because it is the current layer.
        
            Returns: true if successful. false if layerIndex is out of range or the the layer cannot be
                    
             deleted because it is the current layer.
        """
        pass

    def SetCurrentLayerIndex(self, layerIndex, quiet):
        """
        SetCurrentLayerIndex(self: LayerTable, layerIndex: int, quiet: bool) -> bool
        
            At all times, there is a "current" layer. Unless otherwise specified, new objects
                    
             are assigned to the current layer. The current layer is never locked, hidden, or deleted.
        
        
            layerIndex: Value for new current layer. 0 <= layerIndex < LayerTable.Count.
                    The layer's mode 
             is automatically set to NormalMode.
        
            quiet: if true, then no warning message box pops up if the current layer request can't be satisfied.
            Returns: true if current layer index successfully set.
        """
        pass

    def Undelete(self, layerIndex):
        """
        Undelete(self: LayerTable, layerIndex: int) -> bool
        
            Undeletes a layer that has been deleted by DeleteLayer().
        
            layerIndex: zero based index of layer to undelete.
                    This must be in the range 0 <= layerIndex < 
             LayerTable.Count.
        
            Returns: true if successful.
        """
        pass

    def UndoModify(self, layerIndex, undoRecordSerialNumber=None):
        """
        UndoModify(self: LayerTable, layerIndex: int) -> bool
        UndoModify(self: LayerTable, layerIndex: int, undoRecordSerialNumber: UInt32) -> bool
        
            Restores the layer to its previous state,
                    if the layer has been modified and the 
             modification can be undone.
        
        
            layerIndex: The layer index to be used.
            undoRecordSerialNumber: The undo record serial number. Pass 0 not to specify one.
            Returns: true if this layer had been modified and the modifications were undone.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Layer](enumerable: IEnumerable[Layer], value: Layer) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns number of layers in the layer table, excluding deleted layers.

Get: ActiveCount(self: LayerTable) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns number of layers in the layer table, including deleted layers.

Get: Count(self: LayerTable) -> int

"""

    CurrentLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" layer. Unless otherwise specified,
            new objects are assigned to the current layer. The current layer is
            never locked, hidden, or deleted.
            
            Returns reference to the current layer. Note that this reference may
            become invalid after a call to AddLayer().

Get: CurrentLayer(self: LayerTable) -> Layer

"""

    CurrentLayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" layer.  Unless otherwise specified, new objects
            are assigned to the current layer. The current layer is never locked, hidden, or deleted.
            Resturns: Zero based layer table index of the current layer.

Get: CurrentLayerIndex(self: LayerTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: LayerTable) -> RhinoDoc

"""



class LayerTableEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: LayerTableEventArgs) -> RhinoDoc

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventType(self: LayerTableEventArgs) -> LayerTableEventType

"""

    LayerIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerIndex(self: LayerTableEventArgs) -> int

"""

    NewState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewState(self: LayerTableEventArgs) -> Layer

"""

    OldState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldState(self: LayerTableEventArgs) -> Layer

"""



class LayerTableEventType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LayerTableEventType, values: Added (0), Current (5), Deleted (1), Modified (3), Sorted (4), Undeleted (2) """
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

    Added = None
    Current = None
    Deleted = None
    Modified = None
    Sorted = None
    Undeleted = None
    value__ = None


class LightTable(object, IEnumerable[LightObject], IEnumerable, IRhinoTable[LightObject]):
    # no doc
    def Add(self, light, attributes=None):
        """
        Add(self: LightTable, light: Light, attributes: ObjectAttributes) -> int
        Add(self: LightTable, light: Light) -> int
        """
        pass

    def Find(self, id, ignoreDeleted):
        """ Find(self: LightTable, id: Guid, ignoreDeleted: bool) -> int """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LightTable) -> IEnumerator[LightObject] """
        pass

    def Modify(self, *__args):
        """
        Modify(self: LightTable, index: int, light: Light) -> bool
        Modify(self: LightTable, id: Guid, light: Light) -> bool
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LightObject](enumerable: IEnumerable[LightObject], value: LightObject) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of lights in the light table.  Does not include Sun or Skylight.

Get: Count(self: LightTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this light table.

Get: Document(self: LightTable) -> RhinoDoc

"""

    Sun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Sun instance that is applied to the document.
            If the RDK is loaded, an instance is always returned.

Get: Sun(self: LightTable) -> Sun

"""



class LightTableEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: LightTableEventArgs) -> RhinoDoc

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventType(self: LightTableEventArgs) -> LightTableEventType

"""

    LightIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightIndex(self: LightTableEventArgs) -> int

"""

    NewState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewState(self: LightTableEventArgs) -> LightObject

"""

    OldState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldState(self: LightTableEventArgs) -> Light

"""



class LightTableEventType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LightTableEventType, values: Added (0), Deleted (1), Modified (3), Sorted (4), Undeleted (2) """
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

    Added = None
    Deleted = None
    Modified = None
    Sorted = None
    Undeleted = None
    value__ = None


class LinetypeTable(object, IEnumerable[Linetype], IEnumerable, IRhinoTable[Linetype]):
    # no doc
    def Add(self, *__args):
        """
        Add(self: LinetypeTable, name: str, segmentLengths: IEnumerable[float]) -> int
        Add(self: LinetypeTable, linetype: Linetype) -> int
        
            Adds a new linetype with specified definition to the linetype table.
        
            linetype: Definition of new linetype.  The information in linetype is copied.
                    If 
             linetype.Name is empty then a unique name of the form "Linetype 01"
                    will be 
             automatically created.
        
            Returns: Index of newline type or -1 on error.
        """
        pass

    def AddReferenceLinetype(self, linetype):
        """
        AddReferenceLinetype(self: LinetypeTable, linetype: Linetype) -> int
        
            Adds a reference linetypes that will not be saved in files.
        
            linetype: Definition of new linetype.  The information in linetype is copied.
                    If 
             linetype.Name is empty then a unique name of the form "Linetype 01"
                    will be 
             automatically created.
        
            Returns: Index of new linetype or -1 on error.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: LinetypeTable, indices: IEnumerable[int], quiet: bool) -> bool
        Delete(self: LinetypeTable, index: int, quiet: bool) -> bool
        
            Deletes linetype.
        
            index: zero based index of linetype to delete.
            quiet: If true, no warning message box appears if a linetype the
                    linetype cannot be 
             deleted because it is the current linetype
                    or it contains active geometry.
        
            Returns: true if successful. false if linetypeIndex is out of range or the
                    linetype cannot 
             be deleted because it is the current linetype or
                    because it linetype is referenced 
             by active geometry.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: LinetypeTable, id: Guid, ignoreDeletedLinetypes: bool) -> int
        
            Finds a linetype with a matching ID.
        
            id: The ID of the line type to be found.
            ignoreDeletedLinetypes: If true, deleted linetypes are not checked.
            Returns: Zero or a positive value if the index of the linetype with the given ID is found.
                    
             -1 if no linetype has the given ID.
        
        Find(self: LinetypeTable, name: str, ignoreDeletedLinetypes: bool) -> int
        
            Finds the linetype with a given name.
        
            name: search ignores case.
            ignoreDeletedLinetypes: If true, deleted linetypes are not checked.
            Returns: >=0 index of the linetype with the given name
                    -1  no linetype has the given name.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LinetypeTable) -> IEnumerator[Linetype] """
        pass

    def GetUnusedLinetypeName(self, ignoreDeleted):
        """
        GetUnusedLinetypeName(self: LinetypeTable, ignoreDeleted: bool) -> str
        
            Gets unused linetype name used as default when creating new linetypes.
        
            ignoreDeleted: If this is true then a name used by a deleted linetype is allowed.
            Returns: The unused linetype name.
        """
        pass

    def LinetypeIndexForObject(self, rhinoObject):
        """
        LinetypeIndexForObject(self: LinetypeTable, rhinoObject: RhinoObject) -> int
        
            Returns the effective linetype index to be used to find the 
                    linetype definition to 
             draw an object. If an object's linetype
                    source is LinetypeFromObject, the linetype 
             index in the object's
                    attributes is used. If an object's linetype source is 
             LinetypeFromLayer
                    the linetype index from the object's layer is used.
        
        
            rhinoObject: The Rhino object to use in the query.
            Returns: The effective linetype index.
        """
        pass

    def Modify(self, linetype, index, quiet):
        """
        Modify(self: LinetypeTable, linetype: Linetype, index: int, quiet: bool) -> bool
        
            Modify linetype settings.
        
            linetype: New linetype settings. This information is copied.
            index: Zero based index of linetype to set.
            quiet: if true, information message boxes pop up when illegal changes are attempted.
            Returns: true if successful. false if linetype_index is out of range or the
                    settings attempt 
             to lock or hide the current linetype.
        """
        pass

    def SetCurrentLinetypeIndex(self, linetypeIndex, quiet):
        """
        SetCurrentLinetypeIndex(self: LinetypeTable, linetypeIndex: int, quiet: bool) -> bool
        
            At all times, there is a "current" linetype. Unless otherwise specified, new objects
                   
              are assigned to the current linetype. The current linetype is never deleted.
        
        
            linetypeIndex: Value for new current linetype. 0 <= linetypeIndex < LinetypeTable.Count.
            quiet: if true, then no warning message box pops up if the current linetype request can't be satisfied.
            Returns: true if current linetype index successfully set.
        """
        pass

    def Undelete(self, index):
        """
        Undelete(self: LinetypeTable, index: int) -> bool
        
            Restores a linetype that has been deleted.
        
            index: A linetype index to be undeleted.
            Returns: true if successful.
        """
        pass

    def UndoModify(self, index):
        """
        UndoModify(self: LinetypeTable, index: int) -> bool
        
            If the linetype has been modified and the modifcation can be undone,
                    then 
             UndoModify() will restore the linetype to its previous state.
        
        
            index: Zero based index of linetype for which to undo changes.
            Returns: true if this linetype had been modified and the modifications were undone.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Linetype](enumerable: IEnumerable[Linetype], value: Linetype) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns number of linetypes in the linetypes table, excluding deleted linetypes.

Get: ActiveCount(self: LinetypeTable) -> int

"""

    ByLayerLinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the text name of the bylayer linetype.

Get: ByLayerLinetypeName(self: LinetypeTable) -> str

"""

    ContinuousLinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the text name of the continuous linetype.

Get: ContinuousLinetypeName(self: LinetypeTable) -> str

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns number of linetypes in the linetypes table, including deleted linetypes.

Get: Count(self: LinetypeTable) -> int

"""

    CurrentLinetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns reference to the current linetype. Note that this reference may
            become invalid after a call to AddLinetype().

Get: CurrentLinetype(self: LinetypeTable) -> Linetype

"""

    CurrentLinetypeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" linetype.  Unless otherwise specified,
            new objects are assigned to the current linetype. If the current linetype
            source is LinetypeFromLayer the object's layer's linetype is used instead.

Get: CurrentLinetypeIndex(self: LinetypeTable) -> int

"""

    CurrentLinetypeSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Source used by an object to determine its current linetype to be used by new objects.

Get: CurrentLinetypeSource(self: LinetypeTable) -> ObjectLinetypeSource

Set: CurrentLinetypeSource(self: LinetypeTable) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: LinetypeTable) -> RhinoDoc

"""

    LinetypeScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For display in Rhino viewports, the linetypes are scaled by a single scale
            factor for all viewports. This is not used for printing, where all linetype
            patterns are scaled to print in their defined size 1:1 on the paper.

Get: LinetypeScale(self: LinetypeTable) -> float

Set: LinetypeScale(self: LinetypeTable) = value
"""



class MaterialTable(object, IEnumerable[Material], IEnumerable, IRhinoTable[Material]):
    # no doc
    def Add(self, material=None, reference=None):
        """
        Add(self: MaterialTable, material: Material, reference: bool) -> int
        
            Adds a new material to the table based on a given material.
        
            material: A model of the material to be added.
            reference: true if this material is supposed to be a reference material.
                    Reference materials 
             are not saved in the file.
        
            Returns: The position of the new material in the table.
        Add(self: MaterialTable, material: Material) -> int
        
            Adds a new material to the table based on a given material.
        
            material: A model of the material to be added.
            Returns: The position of the new material in the table.
        Add(self: MaterialTable) -> int
        
            Adds a new material to the table based on the default material.
            Returns: The position of the new material in the table.
        """
        pass

    def DeleteAt(self, materialIndex):
        """
        DeleteAt(self: MaterialTable, materialIndex: int) -> bool
        
            Removes a material at a specific position from this material table.
        
            materialIndex: The position to be removed.
            Returns: true if successful. false if materialIndex is out of range or the
                    material cannot 
             be deleted because it is the current material or because
                    it material contains 
             active geometry.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: MaterialTable, materialId: Guid, ignoreDeletedMaterials: bool) -> int
        
            Finds a material with a matching id.
        
            materialId: A material ID to be found.
            ignoreDeletedMaterials: If true, deleted materials are not checked.
            Returns: >=0 index of the material with the given name
                    -1  no material has the given name.
        Find(self: MaterialTable, materialName: str, ignoreDeletedMaterials: bool) -> int
        
            Finds a meterial with a given name.
        
            materialName: Name of the material to search for. The search ignores case.
            ignoreDeletedMaterials: true means don't search deleted materials.
            Returns: >=0 index of the material with the given name
                    -1  no material has the given name.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MaterialTable) -> IEnumerator[Material] """
        pass

    def Modify(self, newSettings, materialIndex, quiet):
        """
        Modify(self: MaterialTable, newSettings: Material, materialIndex: int, quiet: bool) -> bool
        
            Modify material settings.
        
            newSettings: This information is copied.
            materialIndex: zero based index of material to set.  This must be in the range 0 <= layerIndex < 
             MaterialTable.Count.
        
            quiet: if true, information message boxes pop up when illegal changes are attempted.
            Returns: true if successful. false if materialIndex is out of range or the settings attempt
                    
             to lock or hide the current material.
        """
        pass

    def ResetMaterial(self, materialIndex):
        """ ResetMaterial(self: MaterialTable, materialIndex: int) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Material](enumerable: IEnumerable[Material], value: Material) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns number of materials in the material table, including deleted materials.

Get: Count(self: MaterialTable) -> int

"""

    CurrentMaterialIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """At all times, there is a "current" material.  Unless otherwise
            specified, new objects are assigned to the current material.
            The current material is never locked, hidden, or deleted.

Get: CurrentMaterialIndex(self: MaterialTable) -> int

Set: CurrentMaterialIndex(self: MaterialTable) = value
"""

    CurrentMaterialSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current material source.

Get: CurrentMaterialSource(self: MaterialTable) -> ObjectMaterialSource

Set: CurrentMaterialSource(self: MaterialTable) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: MaterialTable) -> RhinoDoc

"""



class MaterialTableEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: MaterialTableEventArgs) -> RhinoDoc

"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventType(self: MaterialTableEventArgs) -> MaterialTableEventType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: MaterialTableEventArgs) -> int

"""

    OldSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldSettings(self: MaterialTableEventArgs) -> Material

"""



class MaterialTableEventType(Enum, IComparable, IFormattable, IConvertible):
    """ enum MaterialTableEventType, values: Added (0), Current (5), Deleted (1), Modified (3), Sorted (4), Undeleted (2) """
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

    Added = None
    Current = None
    Deleted = None
    Modified = None
    Sorted = None
    Undeleted = None
    value__ = None


class NamedConstructionPlaneTable(object, IEnumerable[ConstructionPlane], IEnumerable, IRhinoTable[ConstructionPlane]):
    """
    Contains all named construction planes in a rhino document.
                This class cannot be inherited.
    """
    def Add(self, name, plane):
        """
        Add(self: NamedConstructionPlaneTable, name: str, plane: Plane) -> int
        
            Adds named construction plane to document.
        
            name: If name is empty, a unique name is automatically created.
                    If there is already a 
             named onstruction plane with the same name, that 
                    construction plane is replaced.
        
            plane: The plane value.
            Returns: 0 based index of named construction plane.
                    -1 on failure.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: NamedConstructionPlaneTable, name: str) -> bool
        
            Remove named construction plane from the document.
        
            name: name of the construction plane.
            Returns: true if successful.
        Delete(self: NamedConstructionPlaneTable, index: int) -> bool
        
            Remove named construction plane from the document.
        
            index: zero based array index.
            Returns: true if successful.
        """
        pass

    def Find(self, name):
        """
        Find(self: NamedConstructionPlaneTable, name: str) -> int
        
            Finds a named construction plane.
        
            name: Name of construction plane to search for.
            Returns: >=0 index of the construction plane with the given name.
                    -1 no construction plane 
             found with the given name.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NamedConstructionPlaneTable) -> IEnumerator[ConstructionPlane] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConstructionPlane](enumerable: IEnumerable[ConstructionPlane], value: ConstructionPlane) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of construction planes in the table.

Get: Count(self: NamedConstructionPlaneTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that owns this table.

Get: Document(self: NamedConstructionPlaneTable) -> RhinoDoc

"""



class NamedViewTable(object, IEnumerable[ViewInfo], IEnumerable, IRhinoTable[ViewInfo]):
    """ All named views in a rhino document. """
    def Add(self, *__args):
        """
        Add(self: NamedViewTable, view: ViewInfo) -> int
        Add(self: NamedViewTable, name: str, viewportId: Guid) -> int
        
            Adds named view to document which is based on an existing viewport.
        
            name: If name is empty, a unique name is automatically created.
                    If there is already a 
             named view with the same name, that view is replaced.
        
            viewportId: Id of an existing viewport in the document. View information is copied from this viewport.
            Returns: 0 based index of named view.
                    -1 on failure.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: NamedViewTable, name: str) -> bool
        
            Remove named view from the document.
        
            name: name of the view.
            Returns: true if successful.
        Delete(self: NamedViewTable, index: int) -> bool
        
            Remove named view from the document.
        
            index: index of the named view in the named view table.
            Returns: true if successful.
        """
        pass

    def FindByName(self, name):
        """
        FindByName(self: NamedViewTable, name: str) -> int
        
            Finds a named view.
        
            name: name to search for.
            Returns: >=0 index of the found named view
                    -1 no named view found.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NamedViewTable) -> IEnumerator[ViewInfo] """
        pass

    def Restore(self, index, *__args):
        """
        Restore(self: NamedViewTable, index: int, viewport: RhinoViewport, backgroundBitmap: bool) -> bool
        Restore(self: NamedViewTable, index: int, view: RhinoView, backgroundBitmap: bool) -> bool
        
            Sets the MainViewport of a standard RhinoView to a named views settings
        """
        pass

    def RestoreAnimated(self, index, *__args):
        """
        RestoreAnimated(self: NamedViewTable, index: int, viewport: RhinoViewport, backgroundBitmap: bool) -> bool
        RestoreAnimated(self: NamedViewTable, index: int, viewport: RhinoViewport, backgroundBitmap: bool, frames: int, frameRate: int) -> bool
        RestoreAnimated(self: NamedViewTable, index: int, view: RhinoView, backgroundBitmap: bool) -> bool
        RestoreAnimated(self: NamedViewTable, index: int, view: RhinoView, backgroundBitmap: bool, frames: int, frameRate: int) -> bool
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ViewInfo](enumerable: IEnumerable[ViewInfo], value: ViewInfo) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of named views in the table.

Get: Count(self: NamedViewTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this table.

Get: Document(self: NamedViewTable) -> RhinoDoc

"""



class ObjectTable(object, IEnumerable[RhinoObject], IEnumerable):
    # no doc
    def Add(self, geometry, attributes=None):
        """
        Add(self: ObjectTable, geometry: GeometryBase, attributes: ObjectAttributes) -> Guid
        
            Adds geometry that is not further specified.
                    This is meant, for example, to handle 
             addition of sets of different geometrical entities.
        
        
            geometry: The base geometry. This cannot be null.
            attributes: The object attributes. This can be null.
            Returns: The new object ID on success.
        Add(self: ObjectTable, geometry: GeometryBase) -> Guid
        
            Adds geometry that is not further specified.
                    This is meant, for example, to handle 
             addition of sets of different geometrical entities.
        
        
            geometry: The base geometry. This cannot be null.
            Returns: The new object ID on success.
        """
        pass

    def AddAngularDimension(self, dimension, attributes=None, history=None, reference=None):
        """
        AddAngularDimension(self: ObjectTable, dimension: AngularDimension, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddAngularDimension(self: ObjectTable, dimension: AngularDimension, attributes: ObjectAttributes) -> Guid
        AddAngularDimension(self: ObjectTable, dimension: AngularDimension) -> Guid
        """
        pass

    def AddArc(self, arc, attributes=None, history=None, reference=None):
        """
        AddArc(self: ObjectTable, arc: Arc, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddArc(self: ObjectTable, arc: Arc, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing an arc.
        
            arc: An arc value.
            attributes: Attributes to apply to arc.
            Returns: A unique identifier for the object.
        AddArc(self: ObjectTable, arc: Arc) -> Guid
        
            Adds a curve object to the document representing an arc.
        
            arc: An arc value.
            Returns: A unique identifier for the object.
        """
        pass

    def AddBrep(self, brep, attributes=None, history=None, reference=None, splitKinkySurfaces=None):
        """
        AddBrep(self: ObjectTable, brep: Brep, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddBrep(self: ObjectTable, brep: Brep, attributes: ObjectAttributes, history: HistoryRecord, reference: bool, splitKinkySurfaces: bool) -> Guid
        AddBrep(self: ObjectTable, brep: Brep) -> Guid
        
            Adds a brep object to Rhino.
        
            brep: A duplicate of this brep is added to Rhino.
            Returns: A unique identifier for the object.
        AddBrep(self: ObjectTable, brep: Brep, attributes: ObjectAttributes) -> Guid
        
            Adds a brep object to Rhino.
        
            brep: A duplicate of this brep is added to Rhino.
            attributes: attributes to apply to brep.
            Returns: A unique identifier for the object.
        """
        pass

    def AddCircle(self, circle, attributes=None, history=None, reference=None):
        """
        AddCircle(self: ObjectTable, circle: Circle, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddCircle(self: ObjectTable, circle: Circle, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing a circle.
        
            circle: A circle value.
            attributes: Attributes to apply to circle.
            Returns: A unique identifier for the object.
        AddCircle(self: ObjectTable, circle: Circle) -> Guid
        
            Adds a curve object to the document representing a circle.
        
            circle: A circle value.
            Returns: A unique identifier for the object.
        """
        pass

    def AddClippingPlane(self, plane, uMagnitude, vMagnitude, *__args):
        """
        AddClippingPlane(self: ObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddClippingPlane(self: ObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid], attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddClippingPlane(self: ObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid], attributes: ObjectAttributes) -> Guid
        AddClippingPlane(self: ObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid) -> Guid
        
            Adds a clipping plane object to Rhino.
        
            plane: The plane value.
            uMagnitude: The size in the U direction.
            vMagnitude: The size in the V direction.
            clippedViewportId: Viewport ID that the new clipping plane will clip.
            Returns: A unique identifier for the object.
        AddClippingPlane(self: ObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid]) -> Guid
        """
        pass

    def AddCurve(self, curve, attributes=None, history=None, reference=None):
        """
        AddCurve(self: ObjectTable, curve: Curve, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddCurve(self: ObjectTable, curve: Curve, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to Rhino.
        
            curve: A curve. A duplicate of this curve is added to Rhino.
            attributes: Attributes to apply to curve.
            Returns: A unique identifier for the object.
        AddCurve(self: ObjectTable, curve: Curve) -> Guid
        
            Adds a curve object to Rhino.
        
            curve: A curve. A duplicate of this curve is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddEllipse(self, ellipse, attributes=None, history=None, reference=None):
        """
        AddEllipse(self: ObjectTable, ellipse: Ellipse, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddEllipse(self: ObjectTable, ellipse: Ellipse, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing an ellipse.
        
            ellipse: An ellipse value.
            attributes: Attributes to apply to ellipse.
            Returns: A unique identifier for the object.
        AddEllipse(self: ObjectTable, ellipse: Ellipse) -> Guid
        
            Adds a curve object to the document representing an ellipse.
        
            ellipse: An ellipse value.
            Returns: A unique identifier for the object.
        """
        pass

    def AddExplodedInstancePieces(self, instance, explodeNestedInstances, deleteInstance):
        """ AddExplodedInstancePieces(self: ObjectTable, instance: InstanceObject, explodeNestedInstances: bool, deleteInstance: bool) -> Array[Guid] """
        pass

    def AddExtrusion(self, extrusion, attributes=None, history=None, reference=None):
        """
        AddExtrusion(self: ObjectTable, extrusion: Extrusion, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddExtrusion(self: ObjectTable, extrusion: Extrusion, attributes: ObjectAttributes) -> Guid
        
            Adds an extrusion object to Rhino.
        
            extrusion: A duplicate of this extrusion is added to Rhino.
            attributes: Attributes that will be linked with the extrusion object.
            Returns: A unique identifier for the object.
        AddExtrusion(self: ObjectTable, extrusion: Extrusion) -> Guid
        
            Adds an extrusion object to Rhino.
        
            extrusion: A duplicate of this extrusion is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddHatch(self, hatch, attributes=None, history=None, reference=None):
        """
        AddHatch(self: ObjectTable, hatch: Hatch, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddHatch(self: ObjectTable, hatch: Hatch, attributes: ObjectAttributes) -> Guid
        AddHatch(self: ObjectTable, hatch: Hatch) -> Guid
        """
        pass

    def AddInstanceObject(self, instanceDefinitionIndex, instanceXform, attributes=None):
        """
        AddInstanceObject(self: ObjectTable, instanceDefinitionIndex: int, instanceXform: Transform, attributes: ObjectAttributes) -> Guid
        AddInstanceObject(self: ObjectTable, instanceDefinitionIndex: int, instanceXform: Transform) -> Guid
        """
        pass

    def AddLeader(self, *__args):
        """
        AddLeader(self: ObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: ObjectTable, text: str, points: IEnumerable[Point3d]) -> Guid
        AddLeader(self: ObjectTable, points: IEnumerable[Point3d]) -> Guid
        AddLeader(self: ObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddLeader(self: ObjectTable, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: ObjectTable, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        AddLeader(self: ObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        """
        pass

    def AddLine(self, *__args):
        """
        AddLine(self: ObjectTable, line: Line) -> Guid
        
            Adds a line object to Rhino.
            Returns: A unique identifier for the object.
        AddLine(self: ObjectTable, line: Line, attributes: ObjectAttributes) -> Guid
        
            Adds a line object to Rhino.
        
            line: The line value.
            attributes: Attributes to apply to line.
            Returns: A unique identifier for the object.
        AddLine(self: ObjectTable, from: Point3d, to: Point3d, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddLine(self: ObjectTable, from: Point3d, to: Point3d) -> Guid
        
            Adds a line object to Rhino.
        
            from: The line origin.
            to: The line end.
            Returns: A unique identifier for the object.
        AddLine(self: ObjectTable, from: Point3d, to: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a line object to Rhino.
        
            from: The line origin.
            to: The line end.
            attributes: Attributes to apply to line.
            Returns: A unique identifier for the object.
        """
        pass

    def AddLinearDimension(self, dimension, attributes=None, history=None, reference=None):
        """
        AddLinearDimension(self: ObjectTable, dimension: LinearDimension, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddLinearDimension(self: ObjectTable, dimension: LinearDimension, attributes: ObjectAttributes) -> Guid
        AddLinearDimension(self: ObjectTable, dimension: LinearDimension) -> Guid
        """
        pass

    def AddMesh(self, mesh, attributes=None, history=None, reference=None):
        """
        AddMesh(self: ObjectTable, mesh: Mesh, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddMesh(self: ObjectTable, mesh: Mesh, attributes: ObjectAttributes) -> Guid
        
            Adds a mesh object to Rhino.
        
            mesh: A duplicate of this mesh is added to Rhino.
            attributes: Attributes that will be linked with the mesh object.
            Returns: A unique identifier for the object.
        AddMesh(self: ObjectTable, mesh: Mesh) -> Guid
        
            Adds a mesh object to Rhino.
        
            mesh: A duplicate of this mesh is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddMorphControl(self, morphControl, attributes=None):
        """
        AddMorphControl(self: ObjectTable, morphControl: MorphControl, attributes: ObjectAttributes) -> Guid
        AddMorphControl(self: ObjectTable, morphControl: MorphControl) -> Guid
        """
        pass

    def AddPictureFrame(self, plane, texturePath, asMesh, width, height, selfIllumination, embedBitmap):
        """
        AddPictureFrame(self: ObjectTable, plane: Plane, texturePath: str, asMesh: bool, width: float, height: float, selfIllumination: bool, embedBitmap: bool) -> Guid
        
            Creates a PictureFrame object from a plane and a path to an image file,
                    Note, a 
             PictureFrame object is just a Plane surface or mesh that has a
                    material with a 
             texture assigned to it that displays in all display
                    modes.
        
        
            plane: Plane in which the PictureFrame will be created.  Bottom left corner of
                    picture 
             will be at plane's origin, width will be in the plane's x axis
                    direction, height 
             will be in the plane's y axis direction.
        
            texturePath: path to an image file
            asMesh: If true, the function will make a MeshObject rather than a surface
            width: Width of the resulting PictureFrame. If 0.0, the width of the pictureframe
                    is the 
             width of the image if height is also 0.0 or calculated from the
                    height and aspect 
             ratio of the image if height is not 0.0.
        
            height: Height of the resulting PictureFrame. If 0.0, the height of the pictureframe
                    is the 
             height of the image if width is also 0.0 or calculated from the width
                    and aspect 
             ratio of the image if width is not 0.0.
        
            selfIllumination: If true, the image mapped to the picture frame plane always displays at full
                    
             intensity and is not affected by light or shadow.
        
            embedBitmap: If true, the funtion adds the the image to the bitmaptable of the document
                    to which 
             the PictureFrame will be added
        
            Returns: A unique identifier for the object
        """
        pass

    def AddPoint(self, *__args):
        """
        AddPoint(self: ObjectTable, point: Point3d, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        
            Adds a point object to the document
        
            point: location of point
            attributes: attributes to apply to point. null is acceptible
            history: history associated with this point. null is acceptable
            reference: true if the object is from a reference file.  Reference objects do
                    not persist in 
             archives
        
            Returns: A unique identifier for the object.
        AddPoint(self: ObjectTable, point: Point3f) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            Returns: A unique identifier for the object.
        AddPoint(self: ObjectTable, point: Point3f, attributes: ObjectAttributes) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            attributes: attributes to apply to point.
            Returns: A unique identifier for the object.
        AddPoint(self: ObjectTable, x: float, y: float, z: float) -> Guid
        
            Adds a point object to the document.
        
            x: X component of point coordinate.
            y: Y component of point coordinate.
            z: Z component of point coordinate.
            Returns: A unique identifier for the object..
        AddPoint(self: ObjectTable, point: Point3d) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            Returns: A unique identifier for the object.
        AddPoint(self: ObjectTable, point: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            attributes: attributes to apply to point. null is acceptible
            Returns: A unique identifier for the object.
        """
        pass

    def AddPointCloud(self, *__args):
        """
        AddPointCloud(self: ObjectTable, points: IEnumerable[Point3d]) -> Guid
        AddPointCloud(self: ObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Guid
        AddPointCloud(self: ObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddPointCloud(self: ObjectTable, cloud: PointCloud) -> Guid
        
            Adds a point cloud object to the document.
        
            cloud: PointCloud to add.
            Returns: A unique identifier for the object.
        AddPointCloud(self: ObjectTable, cloud: PointCloud, attributes: ObjectAttributes) -> Guid
        
            Adds a point cloud object to the document.
        
            cloud: PointCloud to add.
            attributes: Attributes to apply to point cloud.
            Returns: A unique identifier for the object.
        AddPointCloud(self: ObjectTable, cloud: PointCloud, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        
            Adds a point cloud object to the document.
        
            cloud: PointCloud to add.
            attributes: Attributes to apply to point cloud. null is acceptable
            history: history associated with this pointcloud. null is acceptable
            reference: true if the object is from a reference file.  Reference objects do
                    not persist in 
             archives
        
            Returns: A unique identifier for the object.
        """
        pass

    def AddPoints(self, points, attributes=None):
        """
        AddPoints(self: ObjectTable, points: IEnumerable[Point3f]) -> RhinoList[Guid]
        AddPoints(self: ObjectTable, points: IEnumerable[Point3f], attributes: ObjectAttributes) -> RhinoList[Guid]
        AddPoints(self: ObjectTable, points: IEnumerable[Point3d]) -> RhinoList[Guid]
        AddPoints(self: ObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> RhinoList[Guid]
        """
        pass

    def AddPolyline(self, points, attributes=None, history=None, reference=None):
        """
        AddPolyline(self: ObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddPolyline(self: ObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Guid
        AddPolyline(self: ObjectTable, points: IEnumerable[Point3d]) -> Guid
        """
        pass

    def AddRadialDimension(self, dimension, attributes=None, history=None, reference=None):
        """
        AddRadialDimension(self: ObjectTable, dimension: RadialDimension, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddRadialDimension(self: ObjectTable, dimension: RadialDimension, attributes: ObjectAttributes) -> Guid
        AddRadialDimension(self: ObjectTable, dimension: RadialDimension) -> Guid
        """
        pass

    def AddRhinoObject(self, *__args):
        """ AddRhinoObject(self: ObjectTable, pointObject: CustomPointObject)AddRhinoObject(self: ObjectTable, pointObject: PointObject, point: Point)AddRhinoObject(self: ObjectTable, curveObject: CurveObject, curve: Curve)AddRhinoObject(self: ObjectTable, brepObject: BrepObject, brep: Brep)AddRhinoObject(self: ObjectTable, meshObject: CustomMeshObject)AddRhinoObject(self: ObjectTable, meshObject: MeshObject, mesh: Mesh)AddRhinoObject(self: ObjectTable, brepObject: CustomBrepObject) """
        pass

    def AddSphere(self, sphere, attributes=None, history=None, reference=None):
        """
        AddSphere(self: ObjectTable, sphere: Sphere, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddSphere(self: ObjectTable, sphere: Sphere, attributes: ObjectAttributes) -> Guid
        AddSphere(self: ObjectTable, sphere: Sphere) -> Guid
        """
        pass

    def AddSurface(self, surface, attributes=None, history=None, reference=None):
        """
        AddSurface(self: ObjectTable, surface: Surface, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddSurface(self: ObjectTable, surface: Surface, attributes: ObjectAttributes) -> Guid
        
            Adds a surface object to Rhino.
        
            surface: A duplicate of this surface is added to Rhino.
            attributes: Attributes that will be linked with the surface object.
            Returns: A unique identifier for the object.
        AddSurface(self: ObjectTable, surface: Surface) -> Guid
        
            Adds a surface object to Rhino.
        
            surface: A duplicate of this surface is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddText(self, *__args):
        """
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, attributes: ObjectAttributes) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            attributes: Attributes that will be linked with the object.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: ObjectTable, text: TextEntity) -> Guid
        AddText(self: ObjectTable, text: TextEntity, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddText(self: ObjectTable, text: TextEntity, attributes: ObjectAttributes) -> Guid
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddText(self: ObjectTable, text3d: Text3d, attributes: ObjectAttributes) -> Guid
        
            Adds an annotation text object to the document.
        
            text3d: The text object to add.
            attributes: Object Attributes.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: ObjectTable, text3d: Text3d) -> Guid
        
            Adds an annotation text object to the document.
        
            text3d: The text object to add.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes) -> Guid
        AddText(self: ObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification) -> Guid
        """
        pass

    def AddTextDot(self, *__args):
        """
        AddTextDot(self: ObjectTable, dot: TextDot, attributes: ObjectAttributes) -> Guid
        
            Adds a text dot object to Rhino.
        
            dot: A text dot that will be copied.
            attributes: Attributes to apply to text dot.
            Returns: A unique identifier for the object.
        AddTextDot(self: ObjectTable, dot: TextDot, attributes: ObjectAttributes, history: HistoryRecord, reference: bool) -> Guid
        AddTextDot(self: ObjectTable, dot: TextDot) -> Guid
        
            Adds a text dot object to Rhino.
        
            dot: A text dot that will be copied.
            Returns: A unique identifier for the object.
        AddTextDot(self: ObjectTable, text: str, location: Point3d) -> Guid
        
            Adds a text dot object to Rhino.
        
            text: A text string.
            location: A point position.
            Returns: A unique identifier for the object.
        AddTextDot(self: ObjectTable, text: str, location: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a text dot object to Rhino.
        
            text: A text string.
            location: A point position.
            attributes: Attributes to apply to curve.
            Returns: A unique identifier for the object.
        """
        pass

    def AllObjectsSince(self, runtimeSerialNumber):
        """
        AllObjectsSince(self: ObjectTable, runtimeSerialNumber: UInt32) -> Array[RhinoObject]
        
            Gets all the objects that have been added to the document since a given runtime serial number.
        
            runtimeSerialNumber: Runtime serial number of the last object not to include in the list.
            Returns: An array of objects or null if no objects were added since the given runtime serial number.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: ObjectTable, objectId: Guid, quiet: bool) -> bool
        
            Deletes object from document. The deletion can be undone by calling UndeleteObject().
        
            objectId: Id of the object to delete.
            quiet: If false, a message box will appear when an object cannot be deleted.
            Returns: true on success, false on failure.
        Delete(self: ObjectTable, objectIds: IEnumerable[Guid], quiet: bool) -> int
        Delete(self: ObjectTable, objref: ObjRef, quiet: bool) -> bool
        
            Deletes objref.Object(). The deletion can be undone by calling UndeleteObject().
        
            objref: objref.Object() will be deleted.
            quiet: If false, a message box will appear when an object cannot be deleted.
            Returns: true on success, false on failure.
        Delete(self: ObjectTable, obj: RhinoObject, quiet: bool) -> bool
        
            Deletes object from document. The deletion can be undone by calling UndeleteObject().
        
            obj: The object to delete.
            quiet: If false, a message box will appear when an object cannot be deleted.
            Returns: true on success, false on failure.
        """
        pass

    def Duplicate(self, *__args):
        """
        Duplicate(self: ObjectTable, objectId: Guid) -> Guid
        
            Same as TransformObject(objref, ON_Xform.Identity, false)
        
            objectId: An ID to an object in the document that needs to be duplicated.
            Returns: The new object ID.
        Duplicate(self: ObjectTable, obj: RhinoObject) -> Guid
        
            Duplicates the object that is referenced by obj.
                    Same as TransformObject(obj, 
             Rhino.Geometry.Transform.IdentityTransform.Identityy, false)
        
        
            obj: A Rhino object to duplicate.
            Returns: The new object ID.
        Duplicate(self: ObjectTable, objref: ObjRef) -> Guid
        
            Duplicates the object that is referenced by objref.
                    Same as Transform(objref, 
             Rhino.Geometry.Transform.IdentityTransform.Identity, false)
        
        
            objref: A Rhino object reference to follow for object duplication.
            Returns: The new object ID.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: ObjectTable, runtimeSerialNumber: UInt32) -> RhinoObject
        
            Use the object runtime serial number to find a rhino object in the document. This is the value 
             stored on
                    RhinoObject.RuntimeObjectSerialNumber. The RhinoObject constructor sets 
             the runtime serial number and every
                    instance of a RhinoObject class will have a 
             unique serial number for the duration of the Rhino application.
                    If an object is 
             replaced with a new object, then the new object will have a different runtime serial number.
           
                      Deleted objects stored in the undo list maintain their runtime serial numbers and this 
             funtion will return
                    pointers to these objects. Call RhinoObject.IsDeleted if you 
             need to determine if the returned object is
                    active or deleted.  The runtime serial 
             number is not saved in files.
        
        
            runtimeSerialNumber: Runtime serial number to search for.
            Returns: Reference to the rhino object with the objectId or null if no such object could be found.
        Find(self: ObjectTable, objectId: Guid) -> RhinoObject
        
            Uses the object guid to find a rhino object. Deleted objects cannot be found by id.
                    
             The guid is the value that is stored on RhinoObject.Id
                    In a single document, no two 
             active objects have the same guid. If an object is
                    replaced with a new object, then 
             the guid  persists. For example, if the _Move command
                    moves an object, then the 
             moved object inherits it's guid from the starting object.
                    If the Copy command 
             copies an object, then the copy gets a new guid. This guid persists
                    through file 
             saving/openning operations. This function will not find grip objects.
        
        
            objectId: ID of object to search for.
            Returns: Reference to the rhino object with the objectId or null if no such object could be found.
        """
        pass

    def FindByCrossingWindowRegion(self, viewport, *__args):
        """
        FindByCrossingWindowRegion(self: ObjectTable, viewport: RhinoViewport, screen1: Point2d, screen2: Point2d, inside: bool, filter: ObjectType) -> Array[RhinoObject]
        
            Finds objects bounded by a region
        
            viewport: viewport to use for selection
            screen1: first screen corner
            screen2: second screen corner
            inside: should objects returned be the ones inside of this region (or outside)
            filter: filter down list by object type
            Returns: An array of RhinoObjects that are inside of this region
        FindByCrossingWindowRegion(self: ObjectTable, viewport: RhinoViewport, region: IEnumerable[Point3d], inside: bool, filter: ObjectType) -> Array[RhinoObject]
        """
        pass

    def FindByDrawColor(self, drawColor, includeLights):
        """
        FindByDrawColor(self: ObjectTable, drawColor: Color, includeLights: bool) -> Array[RhinoObject]
        
            Finds all objects whose draw color matches a given color.
        
            drawColor: The alpha value of this color is ignored.
            includeLights: true if lights should be included.
            Returns: An array of Rhino document objects. This array can be empty.
        """
        pass

    def FindByFilter(self, filter):
        """
        FindByFilter(self: ObjectTable, filter: ObjectEnumeratorSettings) -> Array[RhinoObject]
        
            Same as GetObjectList but converts the result to an array.
        
            filter: The object enumerator filter to customize inclusion requirements.
            Returns: A Rhino object array. This array can be emptry but not null.
        """
        pass

    def FindByGroup(self, groupIndex):
        """
        FindByGroup(self: ObjectTable, groupIndex: int) -> Array[RhinoObject]
        
            Finds all RhinoObjects that are in a given group.
        
            groupIndex: Index of group to search for.
            Returns: An array of objects that belong to the specified group or null if no objects could be found.
        """
        pass

    def FindByLayer(self, *__args):
        """
        FindByLayer(self: ObjectTable, layerName: str) -> Array[RhinoObject]
        
            Finds all RhinoObjects that are in a given layer.
        
            layerName: Name of layer to search.
            Returns: Array of objects that belong to the specified group or null if no objects could be found.
        FindByLayer(self: ObjectTable, layer: Layer) -> Array[RhinoObject]
        
            Finds all RhinoObjects that are in a given layer.
        
            layer: Layer to search.
            Returns: Array of objects that belong to the specified group or null if no objects could be found.
        """
        pass

    def FindByObjectType(self, typeFilter):
        """ FindByObjectType(self: ObjectTable, typeFilter: ObjectType) -> Array[RhinoObject] """
        pass

    def FindByUserString(self, key, value, caseSensitive, searchGeometry=None, searchAttributes=None, filter=None):
        """
        FindByUserString(self: ObjectTable, key: str, value: str, caseSensitive: bool, searchGeometry: bool, searchAttributes: bool, filter: ObjectEnumeratorSettings) -> Array[RhinoObject]
        
            Finds all objects whose UserString matches the search patterns.
        
            key: Search pattern for UserString keys (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            value: Search pattern for UserString values (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            caseSensitive: If true, string comparison will be case sensitive.
            searchGeometry: If true, UserStrings attached to the geometry of an object will be searched.
            searchAttributes: If true, UserStrings attached to the attributes of an object will be searched.
            filter: Filter used to restrict the number of objects searched.
            Returns: An array of all objects whose UserString matches with the search patterns or null when no such 
             objects could be found.
        
        FindByUserString(self: ObjectTable, key: str, value: str, caseSensitive: bool, searchGeometry: bool, searchAttributes: bool, filter: ObjectType) -> Array[RhinoObject]
        
            Finds all objects whose UserString matches the search patterns.
        
            key: Search pattern for UserString keys (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            value: Search pattern for UserString values (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            caseSensitive: If true, string comparison will be case sensitive.
            searchGeometry: If true, UserStrings attached to the geometry of an object will be searched.
            searchAttributes: If true, UserStrings attached to the attributes of an object will be searched.
            filter: Object type filter.
            Returns: An array of all objects whose UserString matches with the search patterns or null when no such 
             objects could be found.
        
        FindByUserString(self: ObjectTable, key: str, value: str, caseSensitive: bool) -> Array[RhinoObject]
        
            Finds all objects whose UserString matches the search patterns.
        
            key: Search pattern for UserString keys (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            value: Search pattern for UserString values (supported wildcards are: ? = any single character, * = any 
             sequence of characters).
        
            caseSensitive: If true, string comparison will be case sensitive.
            Returns: An array of all objects whose UserString matches with the search patterns or null when no such 
             objects could be found.
        """
        pass

    def FindByWindowRegion(self, viewport, *__args):
        """
        FindByWindowRegion(self: ObjectTable, viewport: RhinoViewport, screen1: Point2d, screen2: Point2d, inside: bool, filter: ObjectType) -> Array[RhinoObject]
        
            Finds objects bounded by a polyline region
        
            viewport: viewport to use for selection
            screen1: first screen corner
            screen2: second screen corner
            inside: should objects returned be the ones inside of this region (or outside)
            filter: filter down list by object type
            Returns: An array of RhinoObjects that are inside of this region
        FindByWindowRegion(self: ObjectTable, viewport: RhinoViewport, region: IEnumerable[Point3d], inside: bool, filter: ObjectType) -> Array[RhinoObject]
        """
        pass

    def FindClippingPlanesForViewport(self, viewport):
        """
        FindClippingPlanesForViewport(self: ObjectTable, viewport: RhinoViewport) -> Array[ClippingPlaneObject]
        
            Finds all of the clipping plane objects that actively clip a viewport.
        
            viewport: The viewport in which clipping planes are searched.
            Returns: An array of clipping plane objects. The array can be emptry but not null.
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ObjectTable) -> IEnumerator[RhinoObject] """
        pass

    def GetObjectList(self, *__args):
        """
        GetObjectList(self: ObjectTable, typeFilter: ObjectType) -> IEnumerable[RhinoObject]
        GetObjectList(self: ObjectTable, typeFilter: Type) -> IEnumerable[RhinoObject]
        GetObjectList(self: ObjectTable, settings: ObjectEnumeratorSettings) -> IEnumerable[RhinoObject]
        """
        pass

    def GetSelectedObjects(self, includeLights, includeGrips):
        """ GetSelectedObjects(self: ObjectTable, includeLights: bool, includeGrips: bool) -> IEnumerable[RhinoObject] """
        pass

    def GripUpdate(self, obj, deleteOriginal):
        """
        GripUpdate(self: ObjectTable, obj: RhinoObject, deleteOriginal: bool) -> RhinoObject
        
            Altered grip positions on a RhinoObject are used to calculate an updated object
                    
             that is added to the document.
        
        
            obj: object with modified grips to update.
            deleteOriginal: if true, obj is deleted from the document.
            Returns: new RhinoObject on success; otherwise null.
        """
        pass

    def Hide(self, *__args):
        """
        Hide(self: ObjectTable, objectId: Guid, ignoreLayerMode: bool) -> bool
        
            If Object().IsNormal() is true, then the object will be hidden.
        
            objectId: Id of object to hide.
            ignoreLayerMode: if true, the object will be hidden even if it is on a layer that is locked or off.
            Returns: true if the object was successfully hidden.
        Hide(self: ObjectTable, obj: RhinoObject, ignoreLayerMode: bool) -> bool
        
            If obj.IsNormal() is true, then the object will be hidden.
        
            obj: object to hide.
            ignoreLayerMode: if true, the object will be hidden even if it is on a layer that is locked or off.
            Returns: true if the object was successfully hidden.
        Hide(self: ObjectTable, objref: ObjRef, ignoreLayerMode: bool) -> bool
        
            If objref.Object().IsNormal() is true, then the object will be hidden.
        
            objref: reference to object to hide.
            ignoreLayerMode: if true, the object will be hidden even if it is on a layer that is locked or off.
            Returns: true if the object was successfully hidden.
        """
        pass

    def Lock(self, *__args):
        """
        Lock(self: ObjectTable, objectId: Guid, ignoreLayerMode: bool) -> bool
        
            If objref.Object().IsNormal() is true, then the object will be locked.
        
            objectId: Id of normal object to lock.
            ignoreLayerMode: if true, the object will be locked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully locked.
        Lock(self: ObjectTable, obj: RhinoObject, ignoreLayerMode: bool) -> bool
        
            If obj.IsNormal() is true, then the object will be locked.
        
            obj: normal object to lock.
            ignoreLayerMode: if true, the object will be locked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully locked.
        Lock(self: ObjectTable, objref: ObjRef, ignoreLayerMode: bool) -> bool
        
            If objref.Object().IsNormal() is true, then the object will be locked.
        
            objref: reference to normal object to lock.
            ignoreLayerMode: if true, the object will be locked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully locked.
        """
        pass

    def ModifyAttributes(self, *__args):
        """
        ModifyAttributes(self: ObjectTable, objectId: Guid, newAttributes: ObjectAttributes, quiet: bool) -> bool
        
            Modifies an object's attributes.  Cannot be used to change object id.
        
            objectId: Id of object to modify.
            newAttributes: new attributes.
            quiet: if true, then warning message boxes are disabled.
            Returns: true if successful.
        ModifyAttributes(self: ObjectTable, obj: RhinoObject, newAttributes: ObjectAttributes, quiet: bool) -> bool
        
            Modifies an object's attributes.  Cannot be used to change object id.
        
            obj: object to modify.
            newAttributes: new attributes.
            quiet: if true, then warning message boxes are disabled.
            Returns: true if successful.
        ModifyAttributes(self: ObjectTable, objref: ObjRef, newAttributes: ObjectAttributes, quiet: bool) -> bool
        
            Modifies an object's attributes.  Cannot be used to change object id.
        
            objref: reference to object to modify.
            newAttributes: new attributes.
            quiet: if true, then warning message boxes are disabled.
            Returns: true if successful.
        """
        pass

    def ModifyRenderMaterial(self, *__args):
        """
        ModifyRenderMaterial(self: ObjectTable, objectId: Guid, material: RenderMaterial) -> bool
        
            Modifies an object's render material assignment, this will set the
                    objects material 
             source to ObjectMaterialSource.MaterialFromObject.
        
        
            objectId: Id of object to modify.
            material: Material to assign to this object.
            Returns: Returns true on success otherwise returns false.
        ModifyRenderMaterial(self: ObjectTable, objRef: ObjRef, material: RenderMaterial) -> bool
        
            Modifies an object's render material assignment, this will set the
                    objects material 
             source to ObjectMaterialSource.MaterialFromObject.
        
        
            objRef: Object to modify.
            material: Material to assign to this object.
            Returns: Returns true on success otherwise returns false.
        ModifyRenderMaterial(self: ObjectTable, obj: RhinoObject, material: RenderMaterial) -> bool
        
            Modifies an object's render material assignment, this will set the
                    objects material 
             source to ObjectMaterialSource.MaterialFromObject.
        
        
            obj: Object to modify.
            material: Material to assign to this object.
            Returns: Returns true on success otherwise returns false.
        """
        pass

    def ModifyTextureMapping(self, *__args):
        """
        ModifyTextureMapping(self: ObjectTable, obj: RhinoObject, channel: int, mapping: TextureMapping) -> bool
        ModifyTextureMapping(self: ObjectTable, objId: Guid, channel: int, mapping: TextureMapping) -> bool
        ModifyTextureMapping(self: ObjectTable, objRef: ObjRef, channel: int, mapping: TextureMapping) -> bool
        """
        pass

    def MostRecentObject(self):
        """
        MostRecentObject(self: ObjectTable) -> RhinoObject
        
            Gets the most recently added object that is still in the Document.
            Returns: The most recent (non-deleted) object in the document, or null if no such object exists.
        """
        pass

    def ObjectCount(self, filter):
        """ ObjectCount(self: ObjectTable, filter: ObjectEnumeratorSettings) -> int """
        pass

    def Purge(self, *__args):
        """
        Purge(self: ObjectTable, rhinoObject: RhinoObject) -> bool
        
            Removes object from document and deletes the pointer. Typically you will
                    want to 
             call Delete instead in order to keep the object on the undo list.
        
        
            rhinoObject: A Rhino object that will be deleted.
            Returns: true if the object was purged; otherwise false.
        Purge(self: ObjectTable, runtimeSerialNumber: UInt32) -> bool
        
            Removes object from document and deletes the pointer. Typically you will
                    want to 
             call Delete instead in order to keep the object on the undo list.
        
        
            runtimeSerialNumber: A runtime serial number of the object that will be deleted.
            Returns: true if the object was purged; otherwise false.
        """
        pass

    def Replace(self, *__args):
        """
        Replace(self: ObjectTable, objref: ObjRef, pointcloud: PointCloud) -> bool
        
            Replaces one object with new pointcloud object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            pointcloud: new pointcloud to be added
                    A duplicate of the pointcloud is added to the Rhino 
             model.
        
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, pointcloud: PointCloud) -> bool
        
            Replaces one object with new pointcloud object.
        
            objectId: Id of object to be replaced.
            pointcloud: new pointcloud to be added
                    A duplicate of the pointcloud is added to the Rhino 
             model.
        
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, newObject: RhinoObject) -> bool
        
            Replaces one object with another. Conceptually, this function is the same as calling
                   
              Setting new_object attributes = old_object attributes
                    DeleteObject(old_object);
          
                       AddObject(old_object);
        
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            newObject: new replacement object - must not be in document.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, mesh: Mesh) -> bool
        
            Replaces one object with new mesh object.
        
            objectId: Id of object to be replaced.
            mesh: new mesh to be added
                    A duplicate of the mesh is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, text: TextEntity) -> bool
        
            Replaces one object with new text object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            text: new text to be added
                    A duplicate of the text is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, text: TextEntity) -> bool
        
            Replaces one object with new text object.
        
            objectId: Id of object to be replaced.
            text: new text to be added
                    A duplicate of the text is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, dot: TextDot) -> bool
        
            Replaces one object with new textdot object.
        
            objectId: Id of object to be replaced.
            dot: new textdot to be added.  The textdot is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, line: Line) -> bool
        
            Replaces one object with new line curve object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            line: new line to be added.  The line is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, line: Line) -> bool
        
            Replaces one object with new line curve object.
        
            objectId: Id of object to be replaced.
            line: new line to be added.  The line is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, point: Point3d) -> bool
        
            Replaces one object with new point object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            point: new point to be added.  The point is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, point: Point3d) -> bool
        
            Replaces one object with new point object.
        
            objectId: Id of object to be replaced.
            point: new point to be added.  The point is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, dot: TextDot) -> bool
        
            Replaces one object with new textdot object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            dot: new textdot to be added.  The textdot is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, mesh: Mesh) -> bool
        
            Replaces one object with new mesh object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            mesh: new mesh to be added
                    A duplicate of the mesh is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, arc: Arc) -> bool
        
            Replaces one object with new curve object.
        
            objectId: Id of object to be replaced.
            arc: new arc to be added.  The arc is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, polyline: Polyline) -> bool
        
            Replaces one object with new curve object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            polyline: new polyline to be added.  The polyline is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, polyline: Polyline) -> bool
        
            Replaces one object with new curve object.
        
            objectId: Id of object to be replaced.
            polyline: new polyline to be added.  The polyline is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, circle: Circle) -> bool
        
            Replaces one object with new curve object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            circle: new circle to be added.  The circle is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, circle: Circle) -> bool
        
            Replaces one object with new curve object.
        
            objectId: Id of object to be replaced.
            circle: new circle to be added.  The circle is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, arc: Arc) -> bool
        
            Replaces one object with new curve object.
        
            objref: Reference to old object to be replaced. The object objref.Object() will be deleted.
            arc: new arc to be added.  The arc is copied.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, surface: Surface) -> bool
        
            Replaces one object with new surface object.
        
            objectId: Id of object to be replaced.
            surface: new surface to be added
                    A duplicate of the surface is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, brep: Brep) -> bool
        
            Replaces one object with new brep object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            brep: new brep to be added
                    A duplicate of the brep is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, brep: Brep) -> bool
        
            Replaces one object with new brep object.
        
            objectId: Id of object to be replaced.
            brep: new surface to be added
                    A duplicate of the brep is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, curve: Curve) -> bool
        
            Replaces one object with new curve object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            curve: New curve to be added. A duplicate of the curve is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objectId: Guid, curve: Curve) -> bool
        
            Replaces one object with new curve object.
        
            objectId: Id of object to be replaced.
            curve: New curve to be added. A duplicate of the curve is added to the Rhino model.
            Returns: true if successful.
        Replace(self: ObjectTable, objref: ObjRef, surface: Surface) -> bool
        
            Replaces one object with new surface object.
        
            objref: reference to old object to be replaced. The objref.Object() will be deleted.
            surface: new surface to be added
                    A duplicate of the surface is added to the Rhino model.
            Returns: true if successful.
        """
        pass

    def Select(self, *__args):
        """
        Select(self: ObjectTable, objectId: Guid, select: bool, syncHighlight: bool) -> bool
        
            Select or deselects a single object.
        
            objectId: Id of object to select.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objectId: Guid, select: bool) -> bool
        
            Select or deselects a single object.
        
            objectId: Id of object to select.
            select: If true, the object will be selected, if false, it will be deselected.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objectId: Guid) -> bool
        
            Select a single object.
        
            objectId: Id of object to select.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objectId: Guid, select: bool, syncHighlight: bool, persistentSelect: bool) -> bool
        
            Select or deselects a single object.
        
            objectId: Id of object to select.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            persistentSelect: Objects that are persistently selected stay selected when a command terminates.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objectIds: IEnumerable[Guid], select: bool) -> int
        Select(self: ObjectTable, objectIds: IEnumerable[Guid]) -> int
        Select(self: ObjectTable, objectId: Guid, select: bool, syncHighlight: bool, persistentSelect: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> bool
        
            Select or deselects a single object.
        
            objectId: Id of object to select.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            persistentSelect: Objects that are persistently selected stay selected when a command terminates.
            ignoreGripsState: If true, then objects with grips on can be selected.
                    If false, then the value 
             returned by the object's IsSelectableWithGripsOn() function
                    decides if the object 
             can be selected when it has grips turned on.
        
            ignoreLayerLocking: If true, then objects on locked layers can be selected.
            ignoreLayerVisibility: If true, then objects on hidden layers can be selectable.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objref: ObjRef, select: bool, syncHighlight: bool) -> bool
        
            Select or deselects a single object.
        
            objref: Object represented by this ObjRef is selected.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objref: ObjRef, select: bool) -> bool
        
            Select or deselects a single object.
        
            objref: Object represented by this ObjRef is selected.
            select: If true, the object will be selected, if false, it will be deselected.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objref: ObjRef) -> bool
        
            Select a single object.
        
            objref: Object represented by this ObjRef is selected.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objref: ObjRef, select: bool, syncHighlight: bool, persistentSelect: bool) -> bool
        
            Select or deselects a single object.
        
            objref: Object represented by this ObjRef is selected.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            persistentSelect: Objects that are persistently selected stay selected when a command terminates.
            Returns: true on success, false on failure.
        Select(self: ObjectTable, objRefs: IEnumerable[ObjRef], select: bool) -> int
        Select(self: ObjectTable, objRefs: IEnumerable[ObjRef]) -> int
        Select(self: ObjectTable, objref: ObjRef, select: bool, syncHighlight: bool, persistentSelect: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> bool
        
            Select or deselects a single object.
        
            objref: Object represented by this ObjRef is selected.
            select: If true, the object will be selected, if false, it will be deselected.
            syncHighlight: If true, then the object is highlighted if it is selected 
                    and unhighlighted if is 
             is not selected.
        
            persistentSelect: Objects that are persistently selected stay selected when a command terminates.
            ignoreGripsState: If true, then objects with grips on can be selected.
                    If false, then the value 
             returned by the object's IsSelectableWithGripsOn() function
                    decides if the object 
             can be selected when it has grips turned on.
        
            ignoreLayerLocking: If true, then objects on locked layers can be selected.
            ignoreLayerVisibility: If true, then objects on hidden layers can be selectable.
            Returns: true on success, false on failure.
        """
        pass

    def Show(self, *__args):
        """
        Show(self: ObjectTable, objectId: Guid, ignoreLayerMode: bool) -> bool
        
            If Object().IsHidden() is true, then the object will be returned to normal (visible and 
             selectable) mode.
        
        
            objectId: Id of the normal object to show.
            ignoreLayerMode: if true, the object will be shown even if it is on a layer that is locked or off.
            Returns: true if the object was successfully shown.
        Show(self: ObjectTable, obj: RhinoObject, ignoreLayerMode: bool) -> bool
        
            If obj.IsHidden() is true, then the object will be returned to normal (visible and selectable) 
             mode.
        
        
            obj: the normal object to show.
            ignoreLayerMode: if true, the object will be shown even if it is on a layer that is locked or off.
            Returns: true if the object was successfully shown.
        Show(self: ObjectTable, objref: ObjRef, ignoreLayerMode: bool) -> bool
        
            If objref.Object().IsHidden() is true, then the object will be returned to normal (visible and 
             selectable) mode.
        
        
            objref: reference to normal object to show.
            ignoreLayerMode: if true, the object will be shown even if it is on a layer that is locked or off.
            Returns: true if the object was successfully shown.
        """
        pass

    def Transform(self, *__args):
        """
        Transform(self: ObjectTable, objectId: Guid, xform: Transform, deleteOriginal: bool) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             deletes the existing object if deleteOriginal is true.
        
        
            objectId: Id of rhino object to transform. This object will be deleted if deleteOriginal is true.
            xform: transformation to apply.
            deleteOriginal: if true, the original object is deleted
                    if false, the original object is not 
             deleted.
        
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        
        Transform(self: ObjectTable, obj: RhinoObject, xform: Transform, deleteOriginal: bool) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             deletes the existing object if deleteOriginal is true.
        
        
            obj: Rhino object to transform. This object will be deleted if deleteOriginal is true.
            xform: transformation to apply.
            deleteOriginal: if true, the original object is deleted
                    if false, the original object is not 
             deleted.
        
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        
        Transform(self: ObjectTable, objref: ObjRef, xform: Transform, deleteOriginal: bool) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             deletes the existing object if deleteOriginal is true.
        
        
            objref: reference to object to transform. The objref.Object() will be deleted if deleteOriginal is true.
            xform: transformation to apply.
            deleteOriginal: if true, the original object is deleted
                    if false, the original object is not 
             deleted.
        
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        """
        pass

    def TransformWithHistory(self, *__args):
        """
        TransformWithHistory(self: ObjectTable, objectId: Guid, xform: Transform) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             records history of the transformation if history recording is turned on.
                    If history 
             recording is not enabled, this function will act the same as
                    Transform(objectId, 
             xform, false)
        
        
            objectId: Id of rhino object to transform.
            xform: transformation to apply.
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        
        TransformWithHistory(self: ObjectTable, obj: RhinoObject, xform: Transform) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             records history of the transformation if history recording is turned on.
                    If history 
             recording is not enabled, this function will act the same as
                    Transform(obj, xform, 
             false)
        
        
            obj: Rhino object to transform.
            xform: transformation to apply.
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        
        TransformWithHistory(self: ObjectTable, objref: ObjRef, xform: Transform) -> Guid
        
            Constructs a new object that is the transformation of the existing object
                    and 
             records history of the transformation if history recording is turned on.
                    If history 
             recording is not enabled, this function will act the same as
                    Transform(objref, 
             xform, false)
        
        
            objref: reference to object to transform.
            xform: transformation to apply.
            Returns: Id of the new object that is the transformation of the existing_object.
                    The new 
             object has identical attributes.
        """
        pass

    def Undelete(self, *__args):
        """
        Undelete(self: ObjectTable, rhinoObject: RhinoObject) -> bool
        Undelete(self: ObjectTable, runtimeSerialNumber: UInt32) -> bool
        """
        pass

    def Unlock(self, *__args):
        """
        Unlock(self: ObjectTable, objectId: Guid, ignoreLayerMode: bool) -> bool
        
            If Object().IsLocked() is true, then the object will be returned to normal (visible and 
             selectable) mode.
        
        
            objectId: Id of locked object to unlock.
            ignoreLayerMode: if true, the object will be unlocked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully unlocked.
        Unlock(self: ObjectTable, obj: RhinoObject, ignoreLayerMode: bool) -> bool
        
            If obj.IsLocked() is true, then the object will be returned to normal (visible and selectable) 
             mode.
        
        
            obj: locked object to unlock.
            ignoreLayerMode: if true, the object will be unlocked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully unlocked.
        Unlock(self: ObjectTable, objref: ObjRef, ignoreLayerMode: bool) -> bool
        
            If objref.Object().IsLocked() is true, then the object will be returned to normal (visible and 
             selectable) mode.
        
        
            objref: reference to locked object to unlock.
            ignoreLayerMode: if true, the object will be unlocked even if it is on a layer that is locked or off.
            Returns: true if the object was successfully unlocked.
        """
        pass

    def UnselectAll(self, ignorePersistentSelections=None):
        """
        UnselectAll(self: ObjectTable) -> int
        
            Unselect objects.
            Returns: Number of object that were unselected.
        UnselectAll(self: ObjectTable, ignorePersistentSelections: bool) -> int
        
            Unselect objects.
        
            ignorePersistentSelections: if true, then objects that are persistently selected will not be unselected.
            Returns: Number of object that were unselected.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RhinoObject](enumerable: IEnumerable[RhinoObject], value: RhinoObject) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the boundingbox for all objects (normal, locked and hidden) in this
            document that exist in "model" space. This bounding box does not include
            objects that exist in layout space.

Get: BoundingBox(self: ObjectTable) -> BoundingBox

"""

    BoundingBoxVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the boundingbox for all visible objects (normal and locked) in this
            document that exist in "model" space. This bounding box does not include
            hidden objects or any objects that exist in layout space.

Get: BoundingBoxVisible(self: ObjectTable) -> BoundingBox

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document that owns this object table.

Get: Document(self: ObjectTable) -> RhinoDoc

"""



class StringTable(object):
    # no doc
    def Delete(self, *__args):
        """
        Delete(self: StringTable, key: str)Delete(self: StringTable, section: str, entry: str)
            Removes user data strings from the document.
        
            section: name of section to delete. If null, all sections will be deleted.
            entry: name of entry to delete. If null, all entries will be deleted for a given section.
        """
        pass

    def GetEntryNames(self, section):
        """
        GetEntryNames(self: StringTable, section: str) -> Array[str]
        
            Return list of all entry names for a given section of user data strings in the document.
        
            section: The section from which to retrieve section names.
            Returns: An array of section names. This can be empty, but not null.
        """
        pass

    def GetKey(self, i):
        """ GetKey(self: StringTable, i: int) -> str """
        pass

    def GetSectionNames(self):
        """
        GetSectionNames(self: StringTable) -> Array[str]
        
            Returns a list of all the section names for user data strings in the document.
                    By 
             default a section name is a key that is prefixed with a string separated by a backslash.
        
            Returns: An array of section names. This can be empty, but not null.
        """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: StringTable, section: str, entry: str) -> str
        
            Gets a user data string from the document.
        
            section: The section at which to get the value.
            entry: The entry to search for.
            Returns: The user data.
        GetValue(self: StringTable, key: str) -> str
        GetValue(self: StringTable, i: int) -> str
        """
        pass

    def SetString(self, *__args):
        """
        SetString(self: StringTable, key: str, value: str) -> str
        SetString(self: StringTable, section: str, entry: str, value: str) -> str
        
            Adds or sets a user data string to the document.
        
            section: The section.
            entry: The entry name.
            value: The entry value.
            Returns: The previous value if successful and a previous value existed.
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of user data strings in the current document.

Get: Count(self: StringTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this object table.

Get: Document(self: StringTable) -> RhinoDoc

"""



class ViewTable(object, IEnumerable[RhinoView], IEnumerable):
    # no doc
    def Add(self, title, projection, position, floating):
        """
        Add(self: ViewTable, title: str, projection: DefinedViewportProjection, position: Rectangle, floating: bool) -> RhinoView
        
            Constructs a new Rhino view and, at the same time, adds it to the list.
        
            title: The title of the new Rhino view.
            projection: A basic projection type.
            position: A position.
            floating: true if the view floats; false if it is docked.
            Returns: The newly constructed Rhino view; or null on error.
        """
        pass

    def AddPageView(self, title, pageWidth=None, pageHeight=None):
        """
        AddPageView(self: ViewTable, title: str, pageWidth: float, pageHeight: float) -> RhinoPageView
        
            Constructs a new page view with a given title and size and, at the same time, adds it to the 
             list.
        
        
            title: If null or empty, a name will be generated as "Page #" where # is the largest page number.
            pageWidth: The page total width.
            pageHeight: The page total height.
            Returns: The newly created page view on success; or null on error.
        AddPageView(self: ViewTable, title: str) -> RhinoPageView
        
            Constructs a new page view with a given title and, at the same time, adds it to the list.
        
            title: If null or empty, a name will be generated as "Page #" where # is the largest page number.
            Returns: The newly created page view on success; or null on error.
        """
        pass

    def DefaultViewLayout(self):
        """ DefaultViewLayout(self: ViewTable) """
        pass

    def Find(self, *__args):
        """
        Find(self: ViewTable, mainViewportName: str, compareCase: bool) -> RhinoView
        
            Finds a view in this document with a main viewport that has a given name. Note that there
              
                   may be multiple views in this document that have the same name. This function only returns
             
                    the first view found. If you want to find all the views with a given name, use the 
             GetViewList
                    function and iterate through the views.
        
        
            mainViewportName: The name of the main viewport.
            compareCase: true if capitalization influences comparison; otherwise, false.
            Returns: A Rhino view on success; null on error.
        Find(self: ViewTable, mainViewportId: Guid) -> RhinoView
        
            Finds a view in this document with a given main viewport Id.
        
            mainViewportId: The ID of the main viewport looked for.
            Returns: View on success. null if the view could not be found in this document.
        """
        pass

    def FlashObjects(self, list, useSelectionColor):
        """ FlashObjects(self: ViewTable, list: IEnumerable[RhinoObject], useSelectionColor: bool) """
        pass

    def FourViewLayout(self, useMatchingViews):
        """ FourViewLayout(self: ViewTable, useMatchingViews: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ViewTable) -> IEnumerator[RhinoView] """
        pass

    def GetPageViews(self):
        """
        GetPageViews(self: ViewTable) -> Array[RhinoPageView]
        
            Gets all page views in the document.
            Returns: An array with all page views. The return value can be an empty array but not null.
        """
        pass

    def GetStandardRhinoViews(self):
        """ GetStandardRhinoViews(self: ViewTable) -> Array[RhinoView] """
        pass

    def GetViewList(self, includeStandardViews, includePageViews):
        """
        GetViewList(self: ViewTable, includeStandardViews: bool, includePageViews: bool) -> Array[RhinoView]
        
            Gets an array of all the views.
        
            includeStandardViews: true if "Right", "Perspective", etc., view should be included; false otherwise.
            includePageViews: true if page-related views should be included; false otherwise.
            Returns: A array of Rhino views. This array can be emptry, but not null.
        """
        pass

    def Redraw(self):
        """
        Redraw(self: ViewTable)
            Redraws all views.
        """
        pass

    def ThreeViewLayout(self, useMatchingViews):
        """ ThreeViewLayout(self: ViewTable, useMatchingViews: bool) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RhinoView](enumerable: IEnumerable[RhinoView], value: RhinoView) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or Sets the active view.

Get: ActiveView(self: ViewTable) -> RhinoView

Set: ActiveView(self: ViewTable) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document that owns this object table.

Get: Document(self: ViewTable) -> RhinoDoc

"""

    ModelSpaceIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSpaceIsActive(self: ViewTable) -> bool

"""

    RedrawEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns or sets (enable or disables) screen redrawing.

Get: RedrawEnabled(self: ViewTable) -> bool

Set: RedrawEnabled(self: ViewTable) = value
"""



