class ExtensibleClassFactory(object):
 """ Enables customization of managed objects that extend from unmanaged objects during creation. """
 @staticmethod
 def RegisterObjectCreationCallback(callback):
  """
  RegisterObjectCreationCallback(callback: ObjectCreationDelegate)

   Registers a delegate that is called when an instance of a managed type,that extends from an 

    unmanaged type,needs to allocate the aggregated unmanaged object.

  

  

   callback: A delegate that is called in place of CoCreateInstance.
  """
  pass
