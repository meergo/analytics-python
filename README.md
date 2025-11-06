# Meergo Python SDK

The Meergo Python SDK lets you send customer event data from your Python applications to your specified destinations.

## Install the Meergo SDK

```bash
pip install git+https://github.com/meergo/analytics-python
```

## Using the SDK

💡 We recommend referring to the [Meergo documentation](https://meergo.com) for information on using this SDK.

It's more comprehensive and provides a general overview as well as a step-by-step guide on how to use this SDK.

```python
import meergo.analytics as analytics

analytics.write_key = '<write key>'
analytics.endpoint = '<endpoint>'

analytics.track('er56789012', 'Product added to cart', {
    'price': 32.50
})
```

## Report an issue

To file an issue about the Python SDK for Meergo, please refer to the issues in the main Meergo repository:

[🐞 https://github.com/meergo/meergo/issues?q=is%3Aissue%20state%3Aopen%20label%3Apython-sdk](https://github.com/meergo/meergo/issues?q=is%3Aissue%20state%3Aopen%20label%3Apython-sdk)

## License

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

(The MIT License)

Copyright (c) 2024 Open2b

Copyright (c) 2013 Segment Inc. <friends@segment.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.