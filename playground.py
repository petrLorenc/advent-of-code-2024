
from dataclasses import dataclass
from enum import Enum
from typing import Any


class LogoSource(str, Enum):
    """Enum representing logo detection methods.
    CUSTOM_MODEL: Detection using trained ML model
    LLM: Detection using Large Language Model
    KEYWORDS: Detection using keyword/text matching
    """

    CUSTOM_MODEL = "custom_model"
    KEYWORDS = "keywords"
    LLM = "llm"

    def __str__(self) -> str:
        """Return the string representation of the enum."""
        return self.value


@dataclass(frozen=True)
class LogoMetadata:
    """Container for logo detection metadata.
    Attributes:
        path: S3 or MinIO path to the JSON file containing logo detection results
        source: Method used for logo detection (custom model or keyword matching)
    """

    path: str
    source: LogoSource

    def __post_init__(self) -> None:
        """Validate the inputs after initialization."""
        valid_prefixes = ("s3://", "minio://")
        if not any(self.path.startswith(prefix) for prefix in valid_prefixes):
            raise ValueError(f"Path must start with one of {valid_prefixes}")

        if not isinstance(self.source, LogoSource):
            # Handle the case where a string is passed instead of enum
            object.__setattr__(
                self,
                "source",
                (
                    LogoSource(self.source)
                    if isinstance(self.source, str)
                    else self.source
                ),
            )

    def to_dict(self) -> dict[str, Any]:
        """Convert the metadata to a dictionary format."""
        return {"path": self.path, "source": str(self.source)}

print(LogoMetadata("s3://", "custom_model").to_dict())