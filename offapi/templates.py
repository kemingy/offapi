from string import Template

SwaggerTemplate = Template("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%221em%22 font-size=%2280%22>📄</text></svg>">
    <meta
      name="description"
      content="SwaggerUI"
    />
    <title>SwaggerUI</title>
    <style>$swagger_style</style>
  </head>
  <body>
  <div id="swagger-ui"></div>
  <script>$swagger_bundle</script>
  <script>$swagger_preset</script>
  <script>
    window.onload = () => {{
      window.ui = SwaggerUIBundle({{
        url: '{spec_url}',
        dom_id: '#swagger-ui',
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset,
        ],
        layout: "StandaloneLayout",
      }});
    }};
  </script>
  </body>
</html>
""")

ReDocTemplate = Template("""
<!DOCTYPE html>
<html>
    <head>
        <title>ReDoc</title>
        <!-- needed for adaptive design -->
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%221em%22 font-size=%2280%22>📄</text></svg>">
        <link href=
        "https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700"
        rel="stylesheet">

        <!--
        ReDoc doesn't change outer page styles
        -->
        <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        </style>
    </head>
    <body>
        <redoc spec-url='{spec_url}'></redoc>
        <script>$redoc</script>
    </body>
</html>
""")

ScalarTemplate = Template("""
<!doctype html>
<html>
  <head>
    <title>API Reference</title>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%221em%22 font-size=%2280%22>📄</text></svg>">
    <style>
      body {{
        margin: 0;
      }}
    </style>
  </head>
  <body>
    <script
      id="api-reference"
      data-url="{spec_url}">
    </script>
    <script>
      var configuration = {{
        theme: 'purple',
      }}

      var apiReference = document.getElementById('api-reference')
      apiReference.dataset.configuration = JSON.stringify(configuration)
    </script>
    <script>$scalar</script>
  </body>
</html>
""")
