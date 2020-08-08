from typing import Callable, List, Optional, AsyncGenerator

from ovshell_fileman.api import (
    AutomountWatcher,
    RsyncRunner,
    RsyncStatusLine,
    BackupDirectory,
)


class AutomountWatcherStub(AutomountWatcher):
    stub_running = False
    mountpoint: str = ""

    _mount_handlers: List[Callable[[], None]]
    _unmount_handlers: List[Callable[[], None]]
    _device_in_handlers: List[Callable[[], None]]
    _device_out_handlers: List[Callable[[], None]]

    def __init__(self):
        self._mount_handlers = []
        self._unmount_handlers = []
        self._device_in_handlers = []
        self._device_out_handlers = []

    def on_device_in(self, handler: Callable[[], None]):
        self._device_in_handlers.append(handler)

    def on_device_out(self, handler: Callable[[], None]):
        self._device_out_handlers.append(handler)

    def on_unmount(self, handler: Callable[[], None]) -> None:
        self._unmount_handlers.append(handler)

    def on_mount(self, handler: Callable[[], None]) -> None:
        self._mount_handlers.append(handler)

    async def run(self) -> None:
        self.stub_running = True

    def stub_mount(self) -> None:
        for h in self._mount_handlers:
            h()

    def stub_unmount(self) -> None:
        for h in self._unmount_handlers:
            h()

    def stub_device_in(self) -> None:
        for h in self._device_in_handlers:
            h()

    def stub_device_out(self) -> None:
        for h in self._device_out_handlers:
            h()

    def get_mountpoint(self) -> str:
        return self.mountpoint


class RsyncRunnerStub(RsyncRunner):
    def __init__(self, progress: List[RsyncStatusLine] = None) -> None:
        self.progress = progress or []

    async def run(self, params: List[str]) -> AsyncGenerator[RsyncStatusLine, None]:
        for line in self.progress:
            yield line


class BackupDirectoryStub(BackupDirectory):
    def get_backed_up_files(self) -> List[str]:
        return []

    def ensure_backup_destination(self) -> str:
        return ""

    def get_backup_destination(self) -> str:
        return ""
