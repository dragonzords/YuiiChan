from YuiiChan import (
    DEV_USERS,
    SUDO_USERS,
    SUPPORT_USERS,
    TIGER_USERS,
    WHITELIST_USERS,
    telethn,
)

IMMUNE_USERS = SUDO_USERS + WHITELIST_USERS + SUPPORT_USERS + TIGER_USERS + DEV_USERS

IMMUNE_USERS = (
    list(SUDO_USERS)
    + list(WHITELIST_USERS)
    + list(SUPPORT_USERS)
    + list(TIGER_USERS)
    + list(DEV_USERS)
)