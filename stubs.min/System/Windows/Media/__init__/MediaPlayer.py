class MediaPlayer(Animatable, ISealable, IAnimatable, IResource):
    """
    Provides media playback for drawings.
    
    MediaPlayer()
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: MediaPlayer, sourceFreezable: Freezable)
            Makes this instance a deep copy of the specified System.Windows.Media.MediaPlayer. When copying dependency properties, this method copies resource references and data bindings (but they might no longer 
             resolve) but not animations or their current values.
        
        
            sourceFreezable: The System.Windows.Media.MediaPlayer to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: MediaPlayer, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified System.Windows.Media.MediaPlayer using current property values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
        
            sourceFreezable: The System.Windows.Media.MediaPlayer to clone.
        """
        pass

    def Close(self):
        """
        Close(self: MediaPlayer)
            Closes the underlying media.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: MediaPlayer) -> Freezable
        
            Creates a new System.Windows.Media.MediaPlayer instance.
            Returns: A new System.Windows.Media.MediaPlayer instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether it can be made unmodifiable.
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this instance should actually freeze itself when this method is called.
            Returns: If isChecking is true, this method returns true if this System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if this System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made unmodifiable, with the side effect of having begun to change the frozen status of 
             this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: MediaPlayer, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.MediaPlayer object.
        
            sourceFreezable: The System.Windows.Media.MediaPlayer object to clone and freeze.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def Open(self, source):
        """
        Open(self: MediaPlayer, source: Uri)
            Opens the given System.Uri for media playback.
        
            source: The media source System.Uri.
        """
        pass

    def Pause(self):
        """
        Pause(self: MediaPlayer)
            Pauses media playback.
        """
        pass

    def Play(self):
        """
        Play(self: MediaPlayer)
            Plays media from the current System.Windows.Media.MediaPlayer.Position.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: MediaPlayer)
            Ensures that the MediaPlayer is being accessed from a valid thread.
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def Stop(self):
        """
        Stop(self: MediaPlayer)
            Stops media playback.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: MediaPlayer)
            Verifies that the MediaPlayer is not frozen and that it is being accessed from a valid threading context.
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Balance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the balance between the left and right speaker volumes.

Get: Balance(self: MediaPlayer) -> float

Set: Balance(self: MediaPlayer) = value
"""

    BufferingProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the percentage of buffering completed for streaming content.

Get: BufferingProgress(self: MediaPlayer) -> float

"""

    CanPause = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the media can be paused.

Get: CanPause(self: MediaPlayer) -> bool

"""

    Clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.MediaClock associated with the System.Windows.Media.MediaTimeline to be played.

Get: Clock(self: MediaPlayer) -> MediaClock

Set: Clock(self: MediaPlayer) = value
"""

    DownloadProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the percentage of download progress for content located at a remote server.

Get: DownloadProgress(self: MediaPlayer) -> float

"""

    HasAudio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicating whether the media has audio output.

Get: HasAudio(self: MediaPlayer) -> bool

"""

    HasVideo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the media has video output.

Get: HasVideo(self: MediaPlayer) -> bool

"""

    IsBuffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the media is buffering.

Get: IsBuffering(self: MediaPlayer) -> bool

"""

    IsMuted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the media is muted.

Get: IsMuted(self: MediaPlayer) -> bool

Set: IsMuted(self: MediaPlayer) = value
"""

    NaturalDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the natural duration of the media.

Get: NaturalDuration(self: MediaPlayer) -> Duration

"""

    NaturalVideoHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the pixel height of the video.

Get: NaturalVideoHeight(self: MediaPlayer) -> int

"""

    NaturalVideoWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the pixel width of the video.

Get: NaturalVideoWidth(self: MediaPlayer) -> int

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current position of the media.

Get: Position(self: MediaPlayer) -> TimeSpan

Set: Position(self: MediaPlayer) = value
"""

    ScrubbingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether scrubbing is enabled.

Get: ScrubbingEnabled(self: MediaPlayer) -> bool

Set: ScrubbingEnabled(self: MediaPlayer) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the media System.Uri.

Get: Source(self: MediaPlayer) -> Uri

"""

    SpeedRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ratio of speed that media is played at.

Get: SpeedRatio(self: MediaPlayer) -> float

Set: SpeedRatio(self: MediaPlayer) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the media's volume.

Get: Volume(self: MediaPlayer) -> float

Set: Volume(self: MediaPlayer) = value
"""


    BufferingEnded = None
    BufferingStarted = None
    MediaEnded = None
    MediaFailed = None
    MediaOpened = None
    ScriptCommand = None

