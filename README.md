# OffAPI

[![PyPI](https://img.shields.io/pypi/v/offapi.svg)](https://pypi.org/project/offapi/)

OpenAPI template files for offline usage.

This package will download the related files during the build time, and package them into the final distribution.

## Supports

- Swagger
- Redoc
- Scalar

## Installation

```bash
pip install offapi
```

## Usage

```python
from offapi import OpenAPITemplate

swagger_template = OpenAPITemplate.SWAGGER.value
swagger_template.format(spec_url="your_path_to_the_spec.json")
```

## Used by

- [spectree](https://github.com/0b01001001/spectree): API spec validator and OpenAPI document generator for Python web frameworks.
- [defspec](https://github.com/kemingy/defspec/): Create the OpenAPI spec and document from dataclass, attrs, etc.

