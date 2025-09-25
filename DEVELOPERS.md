# Developers 🛠️

This file contains information useful to Meergo Python SDK developers.

## How to test the SDK

1. Create the venv:

  ```
  python3 -m venv .venv
  ```

2. Activate the venv:

  ```
  source .venv/bin/activate
  ```

3. Install the dependencies from `requirements.txt`:

  ```
  python3 -m pip install -r ./requirements.txt
  ```

4. Start the testing server with:

  ```
  python3 meergo/analytics/test/test_server/server.py
  ```

5. **In another shell**, activate the venv:
  
  ```
  source .venv/bin/activate
  ```

6. Run the tests:

  ```
  python3 -m pytest -v .
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