# OffAPI

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
