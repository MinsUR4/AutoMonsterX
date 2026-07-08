class ExecutionFlag(Exception):
    pass


class AutoMonsterXXError(Exception):
    pass


class DeviceError(AutoMonsterXXError):
    pass


class OpenGameError(AutoMonsterXXError):
    pass


class CloseGameError(AutoMonsterXXError):
    pass


class ScreenShotError(AutoMonsterXXError):
    pass


class WaitError(AutoMonsterXXError):
    pass


class FollowSequenceError(AutoMonsterXXError):
    pass


class ClickError(AutoMonsterXXError):
    pass


class GoToError(AutoMonsterXXError):
    pass


class BattleError(AutoMonsterXXError):
    pass


class InvalidTeamError(AutoMonsterXXError):
    pass


class PVPError(AutoMonsterXXError):
    pass


class InputError(AutoMonsterXXError):
    pass


class PlayAdsError(AutoMonsterXXError):
    pass


class SkipAdError(AutoMonsterXXError):
    pass


class ConnectError(AutoMonsterXXError):
    pass

class SliderError(AutoMonsterXXError):
    pass