from framework.core.singleton import SingletonMeta
from framework.models.config import Config
from framework.models.test_data import TestData
from framework.utils.json_data_loader import JsonDataLoader


class ConfigManager(metaclass=SingletonMeta):
    CONFIG_FILE_NAME = "config.json"

    def __init__(self) -> None:
        self.config = Config.model_validate(
            JsonDataLoader().load(self.CONFIG_FILE_NAME)
        )


class TestDataManager(metaclass=SingletonMeta):
    __test__ = False

    TEST_DATA_FILE_NAME = "test_data.json"

    def __init__(self) -> None:
        self._data = TestData.model_validate(
            JsonDataLoader().load(self.TEST_DATA_FILE_NAME)
        )

    @property
    def data(self) -> TestData:
        return self._data

    def __getattr__(self, item):
        return getattr(self._data, item)
