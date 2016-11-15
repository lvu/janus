from typing import Generic, TypeVar, Optional, Generator, Any
import asyncio

_T = TypeVar('_T')


class Queue(Generic[_T]):
    def __init__(self, maxsize: int=0, *, loop: Optional[asyncio.AbstractEventLoop]=None) -> None: ...

    def close(self) -> None: ...

    @asyncio.coroutine
    def wait_closed(self) -> Generator[Any, None, None]: ...

    @property
    def maxsize(self) -> int: ...

    @property
    def sync_q(self) -> _SyncQueueProxy[_T]: ...

    @property
    def async_q(self) -> _AsyncQueueProxy[_T]: ...


class _SyncQueueProxy(Generic[_T]):

    @property
    def maxsize(self) -> int: ...

    def task_done(self) -> None: ...

    def join(self) -> None: ...

    def qsize(self) -> int: ...

    def empty(self) -> bool: ...

    def full(self) -> bool: ...

    def put(self, item: _T, block: bool=True, timeout: Optional[float]=None) -> None: ...

    def get(self, block: bool=True, timeout: Optional[float]=None) -> _T: ...


    def put_nowait(self, item: _T) -> None: ...

    def get_nowait(self) -> _T: ...


class _AsyncQueueProxy(Generic[_T]):

    @property
    def maxsize(self) -> int: ...

    def task_done(self) -> None: ...

    @asyncio.coroutine
    def join(self) -> Generator[Any, None, None]: ...

    def qsize(self) -> int: ...

    def empty(self) -> bool: ...

    def full(self) -> bool: ...

    @asyncio.coroutine
    def put(self, item: _T) -> Generator[Any, None, None]: ...

    @asyncio.coroutine
    def get(self) -> Generator[Any, None, _T]: ...


    def put_nowait(self, item: _T) -> None: ...

    def get_nowait(self) -> _T: ...


class PriorityQueue(Queue[_T], Generic[_T]): ...


class LifoQueue(Queue[_T], Generic[_T]): ...