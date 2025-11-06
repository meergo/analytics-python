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

### Necessary knowledge

Before proceeding with publishing, it's important to have a general understanding of how publishing to PyPi works (and possibly to TestPyPi for preliminary testing).

It's therefore recommended to read at least this:

https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

### Steps

It is recommended that you release a new version of the repository: while this is not required for publishing to PyPi, it is recommended as it clarifies the version history in the repository.

Then:

Install the latest version of [Twine](https://twine.readthedocs.io/en/stable/) with:

```bash
pip3 install twine
```

Install the latest version of [build](https://build.pypa.io/en/stable/) with:

```bash
pip3 install build
```

Compile the Pure Python Wheel:

```bash
python3 -m build --wheel
```

Upload the Wheel to PyPI:

> For detailed information, see https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#upload-your-distributions.

```bash
twine upload dist/*
```