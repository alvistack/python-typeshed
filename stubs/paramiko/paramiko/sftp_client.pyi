from _typeshed import Self
from logging import Logger
from typing import IO, Any, Callable, Iterator
from typing_extensions import TypeAlias

from paramiko.channel import Channel
from paramiko.sftp import BaseSFTP
from paramiko.sftp_attr import SFTPAttributes
from paramiko.sftp_file import SFTPFile
from paramiko.transport import Transport
from paramiko.util import ClosingContextManager

_Callback: TypeAlias = Callable[[int, int], Any]

b_slash: bytes

class SFTPClient(BaseSFTP, ClosingContextManager):
    sock: Channel
    ultra_debug: bool
    request_number: int
    logger: Logger
    def __init__(self, sock: Channel) -> None: ...
    @classmethod
    def from_transport(
        cls: type[Self], t: Transport, window_size: int | None = ..., max_packet_size: int | None = ...
    ) -> Self | None: ...
    def close(self) -> None: ...
    def get_channel(self) -> Channel | None: ...
    def listdir(self, path: str = ...) -> list[str]: ...
    def listdir_attr(self, path: str = ...) -> list[SFTPAttributes]: ...
    def listdir_iter(self, path: bytes | str = ..., read_aheads: int = ...) -> Iterator[SFTPAttributes]: ...
    def open(self, filename: bytes | str, mode: str = ..., bufsize: int = ...) -> SFTPFile: ...
    file = open
    def remove(self, path: bytes | str) -> None: ...
    unlink = remove
    def rename(self, oldpath: bytes | str, newpath: bytes | str) -> None: ...
    def posix_rename(self, oldpath: bytes | str, newpath: bytes | str) -> None: ...
    def mkdir(self, path: bytes | str, mode: int = ...) -> None: ...
    def rmdir(self, path: bytes | str) -> None: ...
    def stat(self, path: bytes | str) -> SFTPAttributes: ...
    def lstat(self, path: bytes | str) -> SFTPAttributes: ...
    def symlink(self, source: bytes | str, dest: bytes | str) -> None: ...
    def chmod(self, path: bytes | str, mode: int) -> None: ...
    def chown(self, path: bytes | str, uid: int, gid: int) -> None: ...
    def utime(self, path: bytes | str, times: tuple[float, float] | None) -> None: ...
    def truncate(self, path: bytes | str, size: int) -> None: ...
    def readlink(self, path: bytes | str) -> str | None: ...
    def normalize(self, path: bytes | str) -> str: ...
    def chdir(self, path: None | bytes | str = ...) -> None: ...
    def getcwd(self) -> str | None: ...
    def putfo(
        self, fl: IO[bytes], remotepath: bytes | str, file_size: int = ..., callback: _Callback | None = ..., confirm: bool = ...
    ) -> SFTPAttributes: ...
    def put(
        self, localpath: bytes | str, remotepath: bytes | str, callback: _Callback | None = ..., confirm: bool = ...
    ) -> SFTPAttributes: ...
    def getfo(self, remotepath: bytes | str, fl: IO[bytes], callback: _Callback | None = ..., prefetch: bool = ...) -> int: ...
    def get(
        self, remotepath: bytes | str, localpath: bytes | str, callback: _Callback | None = ..., prefetch: bool = ...
    ) -> None: ...

class SFTP(SFTPClient): ...
