# encoding: utf-8
# module Wms.RemotingObjects.RemotePublishing calls itself RemotePublishing
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddRemotePublisherArgs():
    """ AddRemotePublisherArgs() """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AddRemotePublisherArgs) -> str

Set: Name(self: AddRemotePublisherArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AddRemotePublisherArgs()

class DeleteRemotePublisherArgs():
    """ DeleteRemotePublisherArgs() """
    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: DeleteRemotePublisherArgs) -> str

Set: Key(self: DeleteRemotePublisherArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return DeleteRemotePublisherArgs()

class EditRemotePublisherArgs():
    """ EditRemotePublisherArgs() """
    ExpiresAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresAt(self: EditRemotePublisherArgs) -> DateTime

Set: ExpiresAt(self: EditRemotePublisherArgs) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: EditRemotePublisherArgs) -> str

Set: Key(self: EditRemotePublisherArgs) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EditRemotePublisherArgs) -> str

Set: Name(self: EditRemotePublisherArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return EditRemotePublisherArgs()

