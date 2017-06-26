class RenderCapability(object):
    """ Enables WPF applications to query for the current rendering tier for their associated System.Windows.Threading.Dispatcher object and to register for notification of changes. """
    @staticmethod
    def IsPixelShaderVersionSupported(majorVersionRequested, minorVersionRequested):
        """
        IsPixelShaderVersionSupported(majorVersionRequested: Int16, minorVersionRequested: Int16) -> bool
        
            Gets a value that indicates whether the specified pixel shader version is supported.
        
            majorVersionRequested: The major version of the pixel shader.
            minorVersionRequested: The minor version of the pixel shader.
            Returns: true if the pixel shader version is supported by the current version of WPF; otherwise, false.
        """
        pass

    @staticmethod
    def IsPixelShaderVersionSupportedInSoftware(majorVersionRequested, minorVersionRequested):
        """
        IsPixelShaderVersionSupportedInSoftware(majorVersionRequested: Int16, minorVersionRequested: Int16) -> bool
        
            Gets a value that indicates whether the specified pixel shader version can be rendered in software on the current system.
        
            majorVersionRequested: The major version of the pixel shader.
            minorVersionRequested: The minor version of the pixel shader.
            Returns: true if the pixel shader can be rendered in software on the current system; otherwise, false.
        """
        pass

    @staticmethod
    def MaxPixelShaderInstructionSlots(majorVersionRequested, minorVersionRequested):
        """
        MaxPixelShaderInstructionSlots(majorVersionRequested: Int16, minorVersionRequested: Int16) -> int
        
            Gets the maximum number of instruction slots supported by the specified pixel shader version.
        
            majorVersionRequested: The major version of the pixel shader.
            minorVersionRequested: The minor version of the pixel shader.
            Returns: 96 for Pixel Shader 2.0, 512 or greater for Pixel Shader 3.0, or 0 for any other version of Pixel Shader.
        """
        pass

    IsShaderEffectSoftwareRenderingSupported = True
    MaxHardwareTextureSize = None
    Tier = 131072
    TierChanged = None
    __all__ = [
        'IsPixelShaderVersionSupported',
        'IsPixelShaderVersionSupportedInSoftware',
        'MaxPixelShaderInstructionSlots',
        'TierChanged',
    ]

