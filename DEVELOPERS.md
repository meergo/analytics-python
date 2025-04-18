# Developers 🛠️

This file contains information useful to Meergo Python SDK developers.

## How to test the SDK

1. Start the testing server with:

  ```
  python meergo/analytics/test/test_server/server.py
  ```

2. Launch the tests with:
  
  ```
  pytest . -v
  ```

## How to publish the Meergo Python SDK on PyPI

> For detailed information on the entire publishing process of the Meergo Python SDK, see https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#pure-python-wheels

### Compiling the Pure Python Wheel

```
python3 -m build --wheel
```

### Upload the Wheel to PyPI

> For detailed information, see https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#upload-your-distributions.

```
twine upload dist/*
```