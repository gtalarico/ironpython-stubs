class GC(object):
 """ Controls the system garbage collector,a service that automatically reclaims unused memory. """
 @staticmethod
 def AddMemoryPressure(bytesAllocated):
  """
  AddMemoryPressure(bytesAllocated: Int64)

   Informs the runtime of a large allocation of unmanaged memory that should be taken into account 

    when scheduling garbage collection.

  

  

   bytesAllocated: The incremental amount of unmanaged memory that has been allocated.
  """
  pass
 @staticmethod
 def CancelFullGCNotification():
  """
  CancelFullGCNotification()

   Cancels the registration of a garbage collection notification.
  """
  pass
 @staticmethod
 def Collect(generation=None,mode=None,blocking=None,compacting=None):
  """
  Collect(generation: int,mode: GCCollectionMode,blocking: bool)Collect(generation: int,mode: GCCollectionMode,blocking: bool,compacting: bool)Collect(generation: int,mode: GCCollectionMode)

   Forces a garbage collection from generation zero through a specified generation,at a time 

    specified by a System.GCCollectionMode value.

  

  

   generation: The number of the oldest generation that garbage collection can be performed on.

   mode: One of the System.GCCollectionMode values.

  Collect(generation: int)

   Forces an immediate garbage collection from generation zero through a specified generation.

  

   generation: The number of the oldest generation that garbage collection can be performed on.

  Collect()

   Forces an immediate garbage collection of all generations.
  """
  pass
 @staticmethod
 def CollectionCount(generation):
  """
  CollectionCount(generation: int) -> int

  

   Returns the number of times garbage collection has occurred for the specified generation of 

    objects.

  

  

   generation: The generation of objects for which the garbage collection count is to be determined.

   Returns: The number of times garbage collection has occurred for the specified generation since the 

    process was started.
  """
  pass
 @staticmethod
 def EndNoGCRegion():
  """ EndNoGCRegion() """
  pass
 @staticmethod
 def GetGeneration(*__args):
  """
  GetGeneration(wo: WeakReference) -> int

  

   Returns the current generation number of the target of a specified weak reference.

  

   wo: A System.WeakReference that refers to the target object whose generation number is to be 

    determined.

  

   Returns: The current generation number of the target of wo.

  GetGeneration(obj: object) -> int

  

   Returns the current generation number of the specified object.

  

   obj: The object that generation information is retrieved for.

   Returns: The current generation number of obj.
  """
  pass
 @staticmethod
 def GetTotalMemory(forceFullCollection):
  """
  GetTotalMemory(forceFullCollection: bool) -> Int64

  

   Retrieves the number of bytes currently thought to be allocated. A parameter indicates whether 

    this method can wait a short interval before returning,to allow the system to collect garbage 

    and finalize objects.

  

  

   forceFullCollection: true to indicate that this method can wait for garbage collection to occur before returning; 

    otherwise,false.

  

   Returns: A number that is the best available approximation of the number of bytes currently allocated in 

    managed memory.
  """
  pass
 @staticmethod
 def KeepAlive(obj):
  """
  KeepAlive(obj: object)

   References the specified object,which makes it ineligible for garbage collection from the start 

    of the current routine to the point where this method is called.

  

  

   obj: The object to reference.
  """
  pass
 @staticmethod
 def RegisterForFullGCNotification(maxGenerationThreshold,largeObjectHeapThreshold):
  """
  RegisterForFullGCNotification(maxGenerationThreshold: int,largeObjectHeapThreshold: int)

   Specifies that a garbage collection notification should be raised when conditions favor full 

    garbage collection and when the collection has been completed.

  

  

   maxGenerationThreshold: A number between 1 and 99 that specifies when the notification should be raised based on the 

    objects surviving in generation 2.

  

   largeObjectHeapThreshold: A number between 1 and 99 that specifies when the notification should be raised based on objects 

    allocated in the large object heap.
  """
  pass
 @staticmethod
 def RemoveMemoryPressure(bytesAllocated):
  """
  RemoveMemoryPressure(bytesAllocated: Int64)

   Informs the runtime that unmanaged memory has been released and no longer needs to be taken into 

    account when scheduling garbage collection.

  

  

   bytesAllocated: The amount of unmanaged memory that has been released.
  """
  pass
 @staticmethod
 def ReRegisterForFinalize(obj):
  """
  ReRegisterForFinalize(obj: object)

   Requests that the system call the finalizer for the specified object for which 

    System.GC.SuppressFinalize(System.Object) has previously been called.

  

  

   obj: The object that a finalizer must be called for.
  """
  pass
 @staticmethod
 def SuppressFinalize(obj):
  """
  SuppressFinalize(obj: object)

   Requests that the system not call the finalizer for the specified object.

  

   obj: The object that a finalizer must not be called for.
  """
  pass
 @staticmethod
 def TryStartNoGCRegion(totalSize,*__args):
  """
  TryStartNoGCRegion(totalSize: Int64,disallowFullBlockingGC: bool) -> bool

  TryStartNoGCRegion(totalSize: Int64,lohSize: Int64,disallowFullBlockingGC: bool) -> bool

  TryStartNoGCRegion(totalSize: Int64) -> bool

  TryStartNoGCRegion(totalSize: Int64,lohSize: Int64) -> bool
  """
  pass
 @staticmethod
 def WaitForFullGCApproach(millisecondsTimeout=None):
  """
  WaitForFullGCApproach(millisecondsTimeout: int) -> GCNotificationStatus

  

   Returns,in a specified time-out period,the status of a registered notification for determining 

    whether a full garbage collection by the common language runtime is imminent.

  

  

   millisecondsTimeout: The length of time to wait before a notification status can be obtained. Specify -1 to wait 

    indefinitely.

  

   Returns: The status of the registered garbage collection notification.

  WaitForFullGCApproach() -> GCNotificationStatus

  

   Returns the status of a registered notification for determining whether a full garbage 

    collection by the common langauge runtime is imminent.

  

   Returns: The status of the registered garbage collection notification.
  """
  pass
 @staticmethod
 def WaitForFullGCComplete(millisecondsTimeout=None):
  """
  WaitForFullGCComplete(millisecondsTimeout: int) -> GCNotificationStatus

  

   Returns,in a specified time-out period,the status of a registered notification for determining 

    whether a full garbage collection by common language the runtime has completed.

  

  

   millisecondsTimeout: The length of time to wait before a notification status can be obtained. Specify -1 to wait 

    indefinitely.

  

   Returns: The status of the registered garbage collection notification.

  WaitForFullGCComplete() -> GCNotificationStatus

  

   Returns the status of a registered notification for determining whether a full garbage 

    collection by the common language runtime has completed.

  

   Returns: The status of the registered garbage collection notification.
  """
  pass
 @staticmethod
 def WaitForPendingFinalizers():
  """
  WaitForPendingFinalizers()

   Suspends the current thread until the thread that is processing the queue of finalizers has 

    emptied that queue.
  """
  pass
 MaxGeneration=2
 __all__=[
  'AddMemoryPressure',
  'CancelFullGCNotification',
  'Collect',
  'CollectionCount',
  'EndNoGCRegion',
  'GetGeneration',
  'GetTotalMemory',
  'KeepAlive',
  'RegisterForFullGCNotification',
  'RemoveMemoryPressure',
  'ReRegisterForFinalize',
  'SuppressFinalize',
  'TryStartNoGCRegion',
  'WaitForFullGCApproach',
  'WaitForFullGCComplete',
  'WaitForPendingFinalizers',
 ]

