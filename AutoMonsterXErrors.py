class ExecutionFlag(Exception):
    pass


class AutoMonsterXError(Exception):
    pass


class DeviceError(AutoMonsterXError):
    pass


class OpenGameError(AutoMonsterXError):
    pass


class CloseGameError(AutoMonsterXError):
    pass


class ScreenShotError(AutoMonsterXError):
    pass


class WaitError(AutoMonsterXError):
    pass


class FollowSequenceError(AutoMonsterXError):
    pass


class ClickError(AutoMonsterXError):
    pass


class GoToError(AutoMonsterXError):
    pass


class BattleError(AutoMonsterXError):
    pass


class InvalidTeamError(AutoMonsterXError):
    pass


class PVPError(AutoMonsterXError):
    pass


class InputError(AutoMonsterXError):
    pass


class PlayAdsError(AutoMonsterXError):
    pass


class SkipAdError(AutoMonsterXError):
    pass


class ConnectError(AutoMonsterXError):
    pass

class SliderError(AutoMonsterXError):
    pass