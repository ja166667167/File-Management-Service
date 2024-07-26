from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class statusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    unknown: _ClassVar[statusType]
    success: _ClassVar[statusType]
    fail: _ClassVar[statusType]
unknown: statusType
success: statusType
fail: statusType

class userFile(_message.Message):
    __slots__ = ("fileName", "filePath")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    filePath: str
    def __init__(self, fileName: _Optional[str] = ..., filePath: _Optional[str] = ...) -> None: ...

class fullFile(_message.Message):
    __slots__ = ("userName", "fileName", "filePath")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    userName: str
    fileName: str
    filePath: str
    def __init__(self, userName: _Optional[str] = ..., fileName: _Optional[str] = ..., filePath: _Optional[str] = ...) -> None: ...

class UploadRecordRequest(_message.Message):
    __slots__ = ("userName", "fileName", "filePath")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    userName: str
    fileName: str
    filePath: str
    def __init__(self, userName: _Optional[str] = ..., fileName: _Optional[str] = ..., filePath: _Optional[str] = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: statusType
    message: str
    def __init__(self, status: _Optional[_Union[statusType, str]] = ..., message: _Optional[str] = ...) -> None: ...

class GetRecordsRequest(_message.Message):
    __slots__ = ("userName",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    userName: str
    def __init__(self, userName: _Optional[str] = ...) -> None: ...

class GetRecordResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[userFile]
    def __init__(self, files: _Optional[_Iterable[_Union[userFile, _Mapping]]] = ...) -> None: ...

class GetPtclrRecordsRequest(_message.Message):
    __slots__ = ("userName", "fileName", "filePath")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    userName: str
    fileName: str
    filePath: str
    def __init__(self, userName: _Optional[str] = ..., fileName: _Optional[str] = ..., filePath: _Optional[str] = ...) -> None: ...

class GetPtclrRecordsResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[fullFile]
    def __init__(self, files: _Optional[_Iterable[_Union[fullFile, _Mapping]]] = ...) -> None: ...

class DelRecordsRequest(_message.Message):
    __slots__ = ("userName", "fileName", "filePath")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    userName: str
    fileName: str
    filePath: str
    def __init__(self, userName: _Optional[str] = ..., fileName: _Optional[str] = ..., filePath: _Optional[str] = ...) -> None: ...

class DelRecordsResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: statusType
    message: str
    def __init__(self, status: _Optional[_Union[statusType, str]] = ..., message: _Optional[str] = ...) -> None: ...
