class PerformanceCounterCategory(object):
 """
 Represents a performance object,which defines a category of performance counters.

 

 PerformanceCounterCategory()

 PerformanceCounterCategory(categoryName: str)

 PerformanceCounterCategory(categoryName: str,machineName: str)
 """
 def CounterExists(self,counterName,categoryName=None,machineName=None):
  """
  CounterExists(counterName: str,categoryName: str,machineName: str) -> bool

  

   Determines whether the specified counter is registered to the specified category on a remote 

    computer.

  

  

   counterName: The name of the performance counter to look for.

   categoryName: The name of the performance counter category,or performance object,with which the specified 

    performance counter is associated.

  

   machineName: The name of the computer on which the performance counter category and its associated counters 

    exist.

  

   Returns: true,if the counter is registered to the specified category on the specified computer; 

    otherwise,false.

  

  CounterExists(counterName: str,categoryName: str) -> bool

  

   Determines whether the specified counter is registered to the specified category on the local 

    computer.

  

  

   counterName: The name of the performance counter to look for.

   categoryName: The name of the performance counter category,or performance object,with which the specified 

    performance counter is associated.

  

   Returns: true,if the counter is registered to the specified category on the local computer; otherwise,

    false.

  

  CounterExists(self: PerformanceCounterCategory,counterName: str) -> bool

  

   Determines whether the specified counter is registered to this category,which is indicated by 

    the System.Diagnostics.PerformanceCounterCategory.CategoryName and 

    System.Diagnostics.PerformanceCounterCategory.MachineName properties.

  

  

   counterName: The name of the performance counter to look for.

   Returns: true if the counter is registered to the category that is specified by the 

    System.Diagnostics.PerformanceCounterCategory.CategoryName and 

    System.Diagnostics.PerformanceCounterCategory.MachineName properties; otherwise,false.
  """
  pass
 @staticmethod
 def Create(categoryName,categoryHelp,*__args):
  """
  Create(categoryName: str,categoryHelp: str,counterData: CounterCreationDataCollection) -> PerformanceCounterCategory

  

   Registers the custom performance counter category containing the specified counters on the local 

    computer.

  

  

   categoryName: The name of the custom performance counter category to create and register with the system.

   categoryHelp: A description of the custom category.

   counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part 

    of the new category.

  

   Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category,

    or performance object.

  

  Create(categoryName: str,categoryHelp: str,categoryType: PerformanceCounterCategoryType,counterData: CounterCreationDataCollection) -> PerformanceCounterCategory

  

   Registers the custom performance counter category containing the specified counters on the local 

    computer.

  

  

   categoryName: The name of the custom performance counter category to create and register with the system.

   categoryHelp: A description of the custom category.

   categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values.

   counterData: A System.Diagnostics.CounterCreationDataCollection that specifies the counters to create as part 

    of the new category.

  

   Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new custom category,

    or performance object.

  

  Create(categoryName: str,categoryHelp: str,counterName: str,counterHelp: str) -> PerformanceCounterCategory

  

   Registers a custom performance counter category containing a single counter of type 

    NumberOfItems32 on the local computer.

  

  

   categoryName: The name of the custom performance counter category to create and register with the system.

   categoryHelp: A description of the custom category.

   counterName: The name of a new counter,of type NumberOfItems32,to create as part of the new category.

   counterHelp: A description of the counter that is associated with the new custom category.

   Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category,

    or performance object.

  

  Create(categoryName: str,categoryHelp: str,categoryType: PerformanceCounterCategoryType,counterName: str,counterHelp: str) -> PerformanceCounterCategory

  

   Registers the custom performance counter category containing a single counter of type 

    System.Diagnostics.PerformanceCounterType.NumberOfItems32 on the local computer.

  

  

   categoryName: The name of the custom performance counter category to create and register with the system.

   categoryHelp: A description of the custom category.

   categoryType: One of the System.Diagnostics.PerformanceCounterCategoryType  values specifying whether the 

    category is System.Diagnostics.PerformanceCounterCategoryType.MultiInstance,

    System.Diagnostics.PerformanceCounterCategoryType.SingleInstance,or 

    System.Diagnostics.PerformanceCounterCategoryType.Unknown.

  

   counterName: The name of a new counter to create as part of the new category.

   counterHelp: A description of the counter that is associated with the new custom category.

   Returns: A System.Diagnostics.PerformanceCounterCategory that is associated with the new system category,

    or performance object.
  """
  pass
 @staticmethod
 def Delete(categoryName):
  """
  Delete(categoryName: str)

   Removes the category and its associated counters from the local computer.

  

   categoryName: The name of the custom performance counter category to delete.
  """
  pass
 @staticmethod
 def Exists(categoryName,machineName=None):
  """
  Exists(categoryName: str,machineName: str) -> bool

  

   Determines whether the category is registered on the specified computer.

  

   categoryName: The name of the performance counter category to look for.

   machineName: The name of the computer to examine for the category.

   Returns: true if the category is registered; otherwise,false.

  Exists(categoryName: str) -> bool

  

   Determines whether the category is registered on the local computer.

  

   categoryName: The name of the performance counter category to look for.

   Returns: true if the category is registered; otherwise,false.
  """
  pass
 @staticmethod
 def GetCategories(machineName=None):
  """
  GetCategories(machineName: str) -> Array[PerformanceCounterCategory]

  

   Retrieves a list of the performance counter categories that are registered on the specified 

    computer.

  

  

   machineName: The computer to look on.

   Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that 

    are registered on the specified computer.

  

  GetCategories() -> Array[PerformanceCounterCategory]

  

   Retrieves a list of the performance counter categories that are registered on the local computer.

   Returns: An array of System.Diagnostics.PerformanceCounterCategory objects indicating the categories that 

    are registered on the local computer.
  """
  pass
 def GetCounters(self,instanceName=None):
  """
  GetCounters(self: PerformanceCounterCategory,instanceName: str) -> Array[PerformanceCounter]

  

   Retrieves a list of the counters in a performance counter category that contains one or more 

    instances.

  

  

   instanceName: The performance object instance for which to retrieve the list of associated counters.

   Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are 

    associated with the specified object instance of this performance counter category.

  

  GetCounters(self: PerformanceCounterCategory) -> Array[PerformanceCounter]

  

   Retrieves a list of the counters in a performance counter category that contains exactly one 

    instance.

  

   Returns: An array of System.Diagnostics.PerformanceCounter objects indicating the counters that are 

    associated with this single-instance performance counter category.
  """
  pass
 def GetInstanceNames(self):
  """
  GetInstanceNames(self: PerformanceCounterCategory) -> Array[str]

  

   Retrieves the list of performance object instances that are associated with this category.

   Returns: An array of strings representing the performance object instance names that are associated with 

    this category or,if the category contains only one performance object instance,a single-entry 

    array that contains an empty string ("").
  """
  pass
 def InstanceExists(self,instanceName,categoryName=None,machineName=None):
  """
  InstanceExists(instanceName: str,categoryName: str,machineName: str) -> bool

  

   Determines whether a specified category on a specified computer contains the specified 

    performance object instance.

  

  

   instanceName: The performance object instance to search for.

   categoryName: The performance counter category to search.

   machineName: The name of the computer on which to look for the category instance pair.

   Returns: true if the category contains the specified performance object instance; otherwise,false.

  InstanceExists(instanceName: str,categoryName: str) -> bool

  

   Determines whether a specified category on the local computer contains the specified performance 

    object instance.

  

  

   instanceName: The performance object instance to search for.

   categoryName: The performance counter category to search.

   Returns: true if the category contains the specified performance object instance; otherwise,false.

  InstanceExists(self: PerformanceCounterCategory,instanceName: str) -> bool

  

   Determines whether the specified performance object instance exists in the category that is 

    identified by this System.Diagnostics.PerformanceCounterCategory object's 

    System.Diagnostics.PerformanceCounterCategory.CategoryName property.

  

  

   instanceName: The performance object instance in this performance counter category to search for.

   Returns: true if the category contains the specified performance object instance; otherwise,false.
  """
  pass
 def ReadCategory(self):
  """
  ReadCategory(self: PerformanceCounterCategory) -> InstanceDataCollectionCollection

  

   Reads all the counter and performance object instance data that is associated with this 

    performance counter category.

  

   Returns: An System.Diagnostics.InstanceDataCollectionCollection that contains the counter and performance 

    object instance data for the category.
  """
  pass
 @staticmethod
 def __new__(self,categoryName=None,machineName=None):
  """
  __new__(cls: type)

  __new__(cls: type,categoryName: str)

  __new__(cls: type,categoryName: str,machineName: str)
  """
  pass
 CategoryHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the category's help text.



Get: CategoryHelp(self: PerformanceCounterCategory) -> str



"""

 CategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the performance object that defines this category.



Get: CategoryName(self: PerformanceCounterCategory) -> str



Set: CategoryName(self: PerformanceCounterCategory)=value

"""

 CategoryType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the performance counter category type.



Get: CategoryType(self: PerformanceCounterCategory) -> PerformanceCounterCategoryType



"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the computer on which this category exists.



Get: MachineName(self: PerformanceCounterCategory) -> str



Set: MachineName(self: PerformanceCounterCategory)=value

"""


