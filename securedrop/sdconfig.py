# -*- coding: utf-8 -*-

import config as _config

MYPY = False
if MYPY:
    from typing import List  # noqa: F401


class SDConfig(object):
    def __init__(self):
        # type: () -> None
        self.FlaskConfig = _config.FlaskConfig
        self.JournalistInterfaceFlaskConfig = \
            _config.JournalistInterfaceFlaskConfig
        self.SourceInterfaceFlaskConfig = _config.SourceInterfaceFlaskConfig

        self.ADJECTIVES = ""
        self.DATABASE_ENGINE = ""
        self.DEFAULT_LOCALE = ""
        self.GPG_KEY_DIR = ""
        self.JOURNALIST_KEY = ""
        self.JOURNALIST_TEMPLATES_DIR = ""
        self.NOUNS = ""
        self.SCRYPT_GPG_PEPPER = ""
        self.SCRYPT_ID_PEPPER = ""
        self.SCRYPT_PARAMS = ""
        self.SECUREDROP_DATA_ROOT = ""
        self.SECUREDROP_ROOT = ""
        self.SESSION_EXPIRATION_MINUTES = 120
        self.SOURCE_TEMPLATES_DIR = ""
        self.STORE_DIR = ""
        self.SUPPORTED_LOCALES = []  # type: List[str]
        self.TEMP_DIR = ""
        self.WORD_LIST = ""
        self.WORKER_PIDFILE = ""
        self.TRANSLATION_DIRS = ""
        # Below 4 attributes are only for non-sqlite env
        self.DATABASE_USERNAME = ""
        self.DATABASE_PASSWORD = ""
        self.DATABASE_HOST = ""
        self.DATABASE_NAME = ""
        # This is sqlite env
        self.DATABASE_FILE = ""
        # This by default is an empty string
        self.CUSTOM_HEADER_IMAGE = ""

        if _config.DATABASE_ENGINE != "sqlite":
            self.DATABASE_USERNAME = _config.DATABASE_USERNAME  # type: ignore
            self.DATABASE_PASSWORSD = \
                _config.DATABASE_PASSWORD   # type: ignore
            self.DATABASE_HOST = _config.DATABASE_HOST  # type: ignore
            self.DATABASE_NAME = _config.DATABASE_NAME  # type: ignore
        else:
            self.DATABASE_FILE = _config.DATABASE_FILE

        if hasattr(_config, 'CUSTOM_HEADER_IMAGE'):
            self.CUSTOM_HEADER_IMAGE = \
                _config.CUSTOM_HEADER_IMAGE  # type: ignore

        if hasattr(_config, 'SUPPORTED_LOCALES'):
            self.SUPPORTED_LOCALES = \
                _config.SUPPORTED_LOCALES  # type: ignore

        # Now we will fill up existing values from config.py
        # In future after moving out from the config.py to a
        # static configuration file, we should remove any dynamic
        # attribution set/get code like below.
        attributes = [
            'ADJECTIVES', 'DATABASE_ENGINE', 'DATABASE_FILE', 'DEFAULT_LOCALE',
            'GPG_KEY_DIR', 'JOURNALIST_KEY', 'JOURNALIST_TEMPLATES_DIR',
            'NOUNS', 'SCRYPT_GPG_PEPPER', 'SCRYPT_ID_PEPPER', 'SCRYPT_PARAMS',
            'SECUREDROP_DATA_ROOT', 'SECUREDROP_ROOT',
            'SESSION_EXPIRATION_MINUTES', 'SOURCE_TEMPLATES_DIR', 'STORE_DIR',
            'SUPPORTED_LOCALES', 'TEMP_DIR', 'WORD_LIST', 'WORKER_PIDFILE',
            'TRANSLATION_DIRS', 'env', 'os'
        ]
        for attr in attributes:
            if hasattr(_config, attr):
                self.__setattr__(attr, getattr(_config, attr))


config = SDConfig()  # type: SDConfig
