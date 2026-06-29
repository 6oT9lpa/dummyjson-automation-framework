from typing import Any

from pydantic import BaseModel, Field, field_validator


class LoggingConfig(BaseModel):
    enabled: bool = True
    level: str = "INFO"
    console_enabled: bool = True
    file_enabled: bool = True
    file_path: str = "logs/framework.log"
    max_bytes: int = Field(
        default=1_048_576,
        gt=0,
    )
    backup_count: int = Field(
        default=5,
        ge=0,
    )

    format: str = (
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    date_format: str = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LoggingConfig":
        return cls.model_validate(data)

    @field_validator("level")
    @classmethod
    def validate_level(cls, value: str) -> str:
        allowed_levels = {
            "INFO",
            "WARNING",
            "ERROR",
        }

        upper_value = value.upper()

        if upper_value not in allowed_levels:
            raise ValueError(
                f"Invalid log level: {value}"
            )

        return upper_value


class Config(BaseModel):
    base_url: str
    timeout: int = Field(default=10, gt=0)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
