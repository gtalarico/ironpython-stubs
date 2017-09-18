# encoding: utf-8
# module System.Media calls itself Media
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class SoundPlayer(Component, IComponent, IDisposable, ISerializable):
    """
    Controls playback of a sound from a .wav file.
    
    SoundPlayer()
    SoundPlayer(soundLocation: str)
    SoundPlayer(stream: Stream)
    """
    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def Load(self):
        """
        Load(self: SoundPlayer)
            Loads a sound synchronously.
        """
        pass

    def LoadAsync(self):
        """
        LoadAsync(self: SoundPlayer)
            Loads a .wav file from a stream or a Web resource using a new thread.
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

    def OnLoadCompleted(self, *args): #cannot find CLR method
        """
        OnLoadCompleted(self: SoundPlayer, e: AsyncCompletedEventArgs)
            Raises the System.Media.SoundPlayer.LoadCompleted event.
        
            e: An System.ComponentModel.AsyncCompletedEventArgs  that contains the event data.
        """
        pass

    def OnSoundLocationChanged(self, *args): #cannot find CLR method
        """
        OnSoundLocationChanged(self: SoundPlayer, e: EventArgs)
            Raises the System.Media.SoundPlayer.SoundLocationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnStreamChanged(self, *args): #cannot find CLR method
        """
        OnStreamChanged(self: SoundPlayer, e: EventArgs)
            Raises the System.Media.SoundPlayer.StreamChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def Play(self):
        """
        Play(self: SoundPlayer)
            Plays the .wav file using a new thread, and loads the .wav file first if it has not been loaded.
        """
        pass

    def PlayLooping(self):
        """
        PlayLooping(self: SoundPlayer)
            Plays and loops the .wav file using a new thread, and loads the .wav file first if it has not 
             been loaded.
        """
        pass

    def PlaySync(self):
        """
        PlaySync(self: SoundPlayer)
            Plays the .wav file and loads the .wav file first if it has not been loaded.
        """
        pass

    def Stop(self):
        """
        Stop(self: SoundPlayer)
            Stops playback of the sound if playback is occurring.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, soundLocation: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, serializationInfo: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    IsLoadCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether loading of a .wav file has successfully completed.

Get: IsLoadCompleted(self: SoundPlayer) -> bool

"""

    LoadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time, in milliseconds, in which the .wav file must load.

Get: LoadTimeout(self: SoundPlayer) -> int

Set: LoadTimeout(self: SoundPlayer) = value
"""

    SoundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file path or URL of the .wav file to load.

Get: SoundLocation(self: SoundPlayer) -> str

Set: SoundLocation(self: SoundPlayer) = value
"""

    Stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.IO.Stream from which to load the .wav file.

Get: Stream(self: SoundPlayer) -> Stream

Set: Stream(self: SoundPlayer) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Object that contains data about the System.Media.SoundPlayer.

Get: Tag(self: SoundPlayer) -> object

Set: Tag(self: SoundPlayer) = value
"""


    LoadCompleted = None
    SoundLocationChanged = None
    StreamChanged = None


class SystemSound(object):
    """ Represents a system sound type. """
    def Play(self):
        """
        Play(self: SystemSound)
            Plays the system sound type.
        """
        pass


class SystemSounds(object):
    """ Retrieves sounds associated with a set of Windows operating system sound-event types. This class cannot be inherited. """
    Asterisk = None
    Beep = None
    Exclamation = None
    Hand = None
    Question = None


