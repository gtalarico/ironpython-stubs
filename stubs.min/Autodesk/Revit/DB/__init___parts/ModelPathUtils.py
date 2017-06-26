class ModelPathUtils(object):
    """ Utility functions using ModelPaths """
    @staticmethod
    def ConvertModelPathToUserVisiblePath(path):
        """
        ConvertModelPathToUserVisiblePath(path: ModelPath) -> str
        
            Gets a string version of the path of a given ModelPath.
        
            path: A ModelPath representing a file path or a server path.
            Returns: The path in string form
        """
        pass

    @staticmethod
    def ConvertUserVisiblePathToModelPath(strPath):
        """
        ConvertUserVisiblePathToModelPath(strPath: str) -> ModelPath
        
            Converts a user-visible path (string) to a ModelPath.
        
            strPath: The path in string form, like RSN://{HostNodeName}/school/project.rvt
            Returns: A ModelPath representing either a server or file path.
        """
        pass

    @staticmethod
    def IsValidUserVisibleFullServerPath(strPath):
        """
        IsValidUserVisibleFullServerPath(strPath: str) -> bool
        
            Determines whether the given string represents a valid
           server path.
        
            strPath: The path, in string form
            Returns: True if the given path is a valid server path, false otherwise.
        """
        pass

    __all__ = [
        'ConvertModelPathToUserVisiblePath',
        'ConvertUserVisiblePathToModelPath',
        'IsValidUserVisibleFullServerPath',
    ]

