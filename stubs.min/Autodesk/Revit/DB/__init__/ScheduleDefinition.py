class ScheduleDefinition(object, IDisposable):
    """ Settings that define the contents of a schedule. """
    def AddEmbeddedSchedule(self, categoryId):
        """
        AddEmbeddedSchedule(self: ScheduleDefinition, categoryId: ElementId)
            Adds an embedded ScheduleDefinition.
        
            categoryId: The category ID of elements to display in the embedded schedule.
        """
        pass

    def AddField(self, *__args):
        """
        AddField(self: ScheduleDefinition, schedulableField: SchedulableField) -> ScheduleField
        
            Adds a regular field at the end of the list.
        
            schedulableField: A SchedulableField object representing the field.
            Returns: The new field.
        AddField(self: ScheduleDefinition, fieldType: ScheduleFieldType) -> ScheduleField
        
            Adds a regular field at the end of the list.
        
            fieldType: The type of data displayed by the field.
            Returns: The new field.
        AddField(self: ScheduleDefinition, fieldType: ScheduleFieldType, parameterId: ElementId) -> ScheduleField
        
            Adds a regular field at the end of the list.
        
            fieldType: The type of data displayed by the field.
            parameterId: The ID of the parameter displayed by the field.
            Returns: The new field.
        """
        pass

    def AddFilter(self, filter):
        """
        AddFilter(self: ScheduleDefinition, filter: ScheduleFilter)
            Adds a new filter at the end of the list.
        
            filter: The filter to add.
        """
        pass

    def AddSortGroupField(self, sortGroupField):
        """
        AddSortGroupField(self: ScheduleDefinition, sortGroupField: ScheduleSortGroupField)
            Adds a new sorting/grouping field at the end of the list.
        
            sortGroupField: The sorting/grouping field to add.
        """
        pass

    def CanFilter(self):
        """
        CanFilter(self: ScheduleDefinition) -> bool
        
            Checks whether filters can be added to this ScheduleDefinition.
            Returns: True if this ScheduleDefinition supports filters, false otherwise.
        """
        pass

    def CanFilterByGlobalParameters(self, fieldId):
        """
        CanFilterByGlobalParameters(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a field can be used with a global parameter-based filter.
        
            fieldId: The ID of the field to check.
            Returns: True if the field can be used with a global parameter-based filter, false 
             otherwise.
        """
        pass

    def CanFilterByParameterExistence(self, fieldId):
        """
        CanFilterByParameterExistence(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a field can be used with a HasParameter filter.
        
            fieldId: The ID of the field to check.
            Returns: True if the field can be used with a HasParameter filter, false otherwise.
        """
        pass

    def CanFilterBySubstring(self, fieldId):
        """
        CanFilterBySubstring(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a field can be used with a substring-based filter.
        
            fieldId: The ID of the field to check.
            Returns: True if the field can be used with a substring-based filter, false otherwise.
        """
        pass

    def CanFilterByValue(self, fieldId):
        """
        CanFilterByValue(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a field can be used with a value-based filter.
        
            fieldId: The ID of the field to check.
            Returns: True if the field can be used with a value based filter, false otherwise.
        """
        pass

    def CanHaveEmbeddedSchedule(self):
        """
        CanHaveEmbeddedSchedule(self: ScheduleDefinition) -> bool
        
            Indicates if this ScheduleDefinition can have an embedded ScheduleDefinition
          
              added.
        
            Returns: True if this ScheduleDefinition can have an embedded ScheduleDefinition,
           
             false otherwise.
        """
        pass

    def CanIncludeLinkedFiles(self):
        """
        CanIncludeLinkedFiles(self: ScheduleDefinition) -> bool
        
            Checks whether the schedule is a type that supports
           including elements from 
             linked files.
        
            Returns: True if elements from linked files can be included, false otherwise.
        """
        pass

    def CanSortByField(self, fieldId):
        """
        CanSortByField(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a field can be used for sorting/grouping.
        
            fieldId: The ID of the field to check.
            Returns: True if the field can be used for sorting/grouping, false otherwise.
        """
        pass

    def ClearFields(self):
        """
        ClearFields(self: ScheduleDefinition)
            Removes all fields.
        """
        pass

    def ClearFilters(self):
        """
        ClearFilters(self: ScheduleDefinition)
            Removes all filters.
        """
        pass

    def ClearSortGroupFields(self):
        """
        ClearSortGroupFields(self: ScheduleDefinition)
            Removes all sorting/grouping fields.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ScheduleDefinition) """
        pass

    def GetField(self, *__args):
        """
        GetField(self: ScheduleDefinition, index: int) -> ScheduleField
        
            Gets a field.
        
            index: The index of the field.
            Returns: The field.
        GetField(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> ScheduleField
        
            Gets a field.
        
            fieldId: The ID of the field.
            Returns: The field.
        """
        pass

    def GetFieldCount(self):
        """
        GetFieldCount(self: ScheduleDefinition) -> int
        
            Gets the number of fields in this ScheduleDefinition.
            Returns: The number of fields.
        """
        pass

    def GetFieldId(self, index):
        """
        GetFieldId(self: ScheduleDefinition, index: int) -> ScheduleFieldId
        
            Converts a field index to the corresponding field ID.
        
            index: The field index.
            Returns: The field ID.
        """
        pass

    def GetFieldIndex(self, fieldId):
        """
        GetFieldIndex(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> int
        
            Converts a field ID to the corresponding field index.
        
            fieldId: The field ID.
            Returns: The field index.
        """
        pass

    def GetFieldOrder(self):
        """
        GetFieldOrder(self: ScheduleDefinition) -> IList[ScheduleFieldId]
        
            Gets the IDs of the current list of fields in order.
            Returns: The IDs of the current list of fields.
        """
        pass

    def GetFilter(self, index):
        """
        GetFilter(self: ScheduleDefinition, index: int) -> ScheduleFilter
        
            Gets a filter.
        
            index: The index of the filter.
            Returns: A copy of the filter.
        """
        pass

    def GetFilterCount(self):
        """
        GetFilterCount(self: ScheduleDefinition) -> int
        
            Gets the number of filters in this ScheduleDefinition.
            Returns: The number of filters.
        """
        pass

    def GetFilters(self):
        """
        GetFilters(self: ScheduleDefinition) -> IList[ScheduleFilter]
        
            Gets all filters in this ScheduleDefinition.
            Returns: A list of all filters.
        """
        pass

    def GetSchedulableFields(self):
        """
        GetSchedulableFields(self: ScheduleDefinition) -> IList[SchedulableField]
        
            Gets a list of all non-calculated/non-combined fields that are eligible to be
         
               included in this schedule.
        
            Returns: A list of SchedulableField objects representing the non-calculated/non-combined
             
           fields that may be included in the schedule.
        """
        pass

    def GetSortGroupField(self, index):
        """
        GetSortGroupField(self: ScheduleDefinition, index: int) -> ScheduleSortGroupField
        
            Gets a sorting/grouping field.
        
            index: The index of the sorting/grouping field.
            Returns: A copy of the sorting/grouping field.
        """
        pass

    def GetSortGroupFieldCount(self):
        """
        GetSortGroupFieldCount(self: ScheduleDefinition) -> int
        
            Gets the number of sorting/grouping fields in this ScheduleDefinition.
            Returns: The number of sorting/grouping fields.
        """
        pass

    def GetSortGroupFields(self):
        """
        GetSortGroupFields(self: ScheduleDefinition) -> IList[ScheduleSortGroupField]
        
            Gets all sorting/grouping fields in this ScheduleDefinition.
            Returns: A list of all sorting/grouping fields.
        """
        pass

    def GetValidCategoriesForEmbeddedSchedule(self):
        """
        GetValidCategoriesForEmbeddedSchedule(self: ScheduleDefinition) -> ICollection[ElementId]
        
            Get all categories that can be used for an embedded ScheduleDefinition
           in 
             this ScheduleDefinition.
        
            Returns: The IDs of all valid categories.
        """
        pass

    def InsertCombinedParameterField(self, data, fieldName, index):
        """ InsertCombinedParameterField(self: ScheduleDefinition, data: IList[TableCellCombinedParameterData], fieldName: str, index: int) -> ScheduleField """
        pass

    def InsertField(self, *__args):
        """
        InsertField(self: ScheduleDefinition, schedulableField: SchedulableField, index: int) -> ScheduleField
        
            Adds a regular field at the specified position in the list.
        
            schedulableField: A SchedulableField object representing the field.
            index: The index in the list of fields.
            Returns: The new field.
        InsertField(self: ScheduleDefinition, fieldType: ScheduleFieldType, index: int) -> ScheduleField
        
            Adds a regular field at the specified position in the list.
        
            fieldType: The type of data displayed by the field.
            index: The index in the list of fields.
            Returns: The new field.
        InsertField(self: ScheduleDefinition, fieldType: ScheduleFieldType, parameterId: ElementId, index: int) -> ScheduleField
        
            Adds a regular field at the specified position in the list.
        
            fieldType: The type of data displayed by the field.
            parameterId: The ID of the parameter displayed by the field.
            index: The index in the list of fields.
            Returns: The new field.
        """
        pass

    def InsertFilter(self, filter, index):
        """
        InsertFilter(self: ScheduleDefinition, filter: ScheduleFilter, index: int)
            Adds a new filter at the specified position in the list.
        
            filter: The filter to add.
            index: The index in the list of filters.
        """
        pass

    def InsertSortGroupField(self, sortGroupField, index):
        """
        InsertSortGroupField(self: ScheduleDefinition, sortGroupField: ScheduleSortGroupField, index: int)
            Adds a new sorting/grouping field at the specified position in the list.
        
            sortGroupField: The sorting/grouping field to add.
            index: The index in the list of sorting/grouping fields.
        """
        pass

    def IsSchedulableField(self, schedulableField):
        """
        IsSchedulableField(self: ScheduleDefinition, schedulableField: SchedulableField) -> bool
        
            Checks whether a non-calculated/non-combined field is eligible to be included 
             in
           this schedule.
        
        
            schedulableField: The field to check.
            Returns: True if the field may be included in the schedule, false otherwise.
        """
        pass

    def IsValidCategoryForEmbeddedSchedule(self, categoryId):
        """
        IsValidCategoryForEmbeddedSchedule(self: ScheduleDefinition, categoryId: ElementId) -> bool
        
            Indicates if a category can be used for an embedded ScheduleDefinition
           in 
             this ScheduleDefinition.
        
        
            categoryId: The category ID to check.
            Returns: True if the category can be used for an embedded ScheduleDefinition,
           false 
             otherwise.
        """
        pass

    def IsValidCombinedParameters(self, data):
        """ IsValidCombinedParameters(self: ScheduleDefinition, data: IList[TableCellCombinedParameterData]) -> bool """
        pass

    def IsValidFieldId(self, fieldId):
        """
        IsValidFieldId(self: ScheduleDefinition, fieldId: ScheduleFieldId) -> bool
        
            Checks whether a ScheduleFieldId is the ID of a field in this 
             ScheduleDefinition.
        
        
            fieldId: The field ID to check.
            Returns: True if the field ID is valid, false otherwise.
        """
        pass

    def IsValidFieldIndex(self, index):
        """
        IsValidFieldIndex(self: ScheduleDefinition, index: int) -> bool
        
            Checks whether an integer is a valid zero-based field index in this 
             ScheduleDefinition.
        
        
            index: The field index to check.
            Returns: True if the field index is valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ScheduleDefinition, disposing: bool) """
        pass

    def RemoveEmbeddedSchedule(self):
        """
        RemoveEmbeddedSchedule(self: ScheduleDefinition)
            Removes the embedded ScheduleDefinition.
        """
        pass

    def RemoveField(self, *__args):
        """
        RemoveField(self: ScheduleDefinition, index: int)
            Removes a field.
        
            index: The index of the field to remove.
        RemoveField(self: ScheduleDefinition, fieldId: ScheduleFieldId)
            Removes a field.
        
            fieldId: The ID of the field to remove.
        """
        pass

    def RemoveFilter(self, index):
        """
        RemoveFilter(self: ScheduleDefinition, index: int)
            Removes a filter.
        
            index: The index of the filter to remove.
        """
        pass

    def RemoveSortGroupField(self, index):
        """
        RemoveSortGroupField(self: ScheduleDefinition, index: int)
            Removes a sorting/grouping field.
        
            index: The index of the sorting/grouping field to remove.
        """
        pass

    def SetFieldOrder(self, fieldIds):
        """ SetFieldOrder(self: ScheduleDefinition, fieldIds: IList[ScheduleFieldId]) """
        pass

    def SetFilter(self, index, filter):
        """
        SetFilter(self: ScheduleDefinition, index: int, filter: ScheduleFilter)
            Replaces a filter.
        
            index: The index of the filter to replace.
            filter: The new filter.
        """
        pass

    def SetFilters(self, filters):
        """ SetFilters(self: ScheduleDefinition, filters: IList[ScheduleFilter]) """
        pass

    def SetSortGroupField(self, index, sortGroupField):
        """
        SetSortGroupField(self: ScheduleDefinition, index: int, sortGroupField: ScheduleSortGroupField)
            Replaces a sorting/grouping field.
        
            index: The index of the sorting/grouping field to replace.
            sortGroupField: The new sorting/grouping field.
        """
        pass

    def SetSortGroupFields(self, sortGroupFields):
        """ SetSortGroupFields(self: ScheduleDefinition, sortGroupFields: IList[ScheduleSortGroupField]) """
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

    AreaSchemeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """In an area schedule, the ID of the area scheme to display.

Get: AreaSchemeId(self: ScheduleDefinition) -> ElementId

"""

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category ID of elements appearing in the schedule.

Get: CategoryId(self: ScheduleDefinition) -> ElementId

"""

    EmbeddedDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The embedded ScheduleDefinition.

Get: EmbeddedDefinition(self: ScheduleDefinition) -> ScheduleDefinition

"""

    FamilyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """In a note block schedule, the ID of the Generic Annotation family
   displayed by the schedule.

Get: FamilyId(self: ScheduleDefinition) -> ElementId

"""

    GrandTotalTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title name is used to display at the grand total row. The name is "Grand total", expressed in the Revit session language, by default.

Get: GrandTotalTitle(self: ScheduleDefinition) -> str

Set: GrandTotalTitle(self: ScheduleDefinition) = value
"""

    HasEmbeddedSchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this ScheduleDefinition has an embedded ScheduleDefinition.

Get: HasEmbeddedSchedule(self: ScheduleDefinition) -> bool

"""

    IncludeLinkedFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the schedule includes elements from linked files.

Get: IncludeLinkedFiles(self: ScheduleDefinition) -> bool

Set: IncludeLinkedFiles(self: ScheduleDefinition) = value
"""

    IsEmbedded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this is an embedded ScheduleDefinition.

Get: IsEmbedded(self: ScheduleDefinition) -> bool

"""

    IsItemized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the schedule displays each element on a separate row or
   combines multiple grouped elements onto the same row.

Get: IsItemized(self: ScheduleDefinition) -> bool

Set: IsItemized(self: ScheduleDefinition) = value
"""

    IsKeySchedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the schedule is a key schedule.

Get: IsKeySchedule(self: ScheduleDefinition) -> bool

"""

    IsMaterialTakeoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the schedule is a material takeoff.

Get: IsMaterialTakeoff(self: ScheduleDefinition) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ScheduleDefinition) -> bool

"""

    ShowGrandTotal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if a grand total row should be displayed at the bottom of
   the schedule.

Get: ShowGrandTotal(self: ScheduleDefinition) -> bool

Set: ShowGrandTotal(self: ScheduleDefinition) = value
"""

    ShowGrandTotalCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the grand total row should display a count of elements
   in the schedule.

Get: ShowGrandTotalCount(self: ScheduleDefinition) -> bool

Set: ShowGrandTotalCount(self: ScheduleDefinition) = value
"""

    ShowGrandTotalTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the grand total row should display a title.

Get: ShowGrandTotalTitle(self: ScheduleDefinition) -> bool

Set: ShowGrandTotalTitle(self: ScheduleDefinition) = value
"""

    ShowHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the headers will be displayed in the schedule.

Get: ShowHeaders(self: ScheduleDefinition) -> bool

Set: ShowHeaders(self: ScheduleDefinition) = value
"""

    ShowTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the title will be displayed in the schedule.

Get: ShowTitle(self: ScheduleDefinition) -> bool

Set: ShowTitle(self: ScheduleDefinition) = value
"""


