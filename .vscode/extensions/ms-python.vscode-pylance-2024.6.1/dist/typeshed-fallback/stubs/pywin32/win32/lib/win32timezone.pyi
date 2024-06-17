import datetime
from _typeshed import Incomplete

log: Incomplete

class _SimpleStruct:
    def __init__(self, *args, **kw) -> None: ...
    def field_names(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class SYSTEMTIME(_SimpleStruct): ...
class TIME_ZONE_INFORMATION(_SimpleStruct): ...
class DYNAMIC_TIME_ZONE_INFORMATION(_SimpleStruct): ...

class TimeZoneDefinition(DYNAMIC_TIME_ZONE_INFORMATION):
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, attr: str): ...
    @classmethod
    def current(cls): ...
    def set(self) -> None: ...
    def copy(self): ...
    def locate_daylight_start(self, year): ...
    def locate_standard_start(self, year): ...

class TimeZoneInfo(datetime.tzinfo):
    tzRegKey: str
    timeZoneName: Incomplete
    fixedStandardTime: Incomplete
    def __init__(self, param: Incomplete | None = ..., fix_standard_time: bool = ...) -> None: ...
    def tzname(self, dt): ...
    def getWinInfo(self, targetYear): ...
    def utcoffset(self, dt): ...
    def dst(self, dt): ...
    def GetDSTStartTime(self, year): ...
    def GetDSTEndTime(self, year): ...
    def __cmp__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    def local(cls): ...
    @classmethod
    def utc(cls): ...
    @staticmethod
    def get_sorted_time_zone_names(): ...
    @staticmethod
    def get_all_time_zones(): ...
    @staticmethod
    def get_sorted_time_zones(key: Incomplete | None = ...): ...

def utcnow(): ...
def now(): ...
def GetTZCapabilities(): ...

class DLLHandleCache:
    def __getitem__(self, filename): ...

DLLCache: Incomplete

def resolveMUITimeZone(spec): ...

class RangeMap(dict[int, str]):
    sort_params: Incomplete
    match: Incomplete
    def __init__(self, source, sort_params=..., key_match_comparator=...) -> None: ...
    def __getitem__(self, item): ...
    def get(self, key, default: Incomplete | None = ...): ...
    def bounds(self): ...
    undefined_value: Incomplete

    class Item(int): ...
    first_item: Incomplete
    last_item: Incomplete
