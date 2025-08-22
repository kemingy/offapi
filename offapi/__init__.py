import json
from enum import Enum
from importlib import resources
from pathlib import PurePath

from offapi.templates import ReDocTemplate, ScalarTemplate, SwaggerTemplate

__all__ = ["OpenAPITemplate"]


with (resources.files("offapi") / "url.json").open(encoding="utf-8") as f:
    urls = json.load(f)


def load_resource_file(filename: str) -> str:
    content = (resources.files("offapi") / filename).read_text(encoding="utf-8")
    # escape curly braces
    return content.replace("{", "{{").replace("}", "}}")


class OpenAPITemplate(Enum):
    SWAGGER = SwaggerTemplate.safe_substitute(
        {
            PurePath(key).stem: load_resource_file(key)
            for key in urls
            if key.startswith("swagger")
        }
    )
    REDOC = ReDocTemplate.safe_substitute(
        {
            PurePath(key).stem: load_resource_file(key)
            for key in urls
            if key.startswith("redoc")
        }
    )
    SCALAR = ScalarTemplate.safe_substitute(
        {
            PurePath(key).stem: load_resource_file(key)
            for key in urls
            if key.startswith("scalar")
        }
    )
