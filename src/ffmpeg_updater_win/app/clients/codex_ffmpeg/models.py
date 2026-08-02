from io import BytesIO

from pydantic import BaseModel, ConfigDict


class ByteResponse(BaseModel):
    model_config = ConfigDict(strict=True, extra='forbid', arbitrary_types_allowed=True)

    bytes_data: BytesIO
    headers: dict
    url: str
