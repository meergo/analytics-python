# Meergo Python SDK

The Meergo Python SDK lets you send customer event data from your Python applications to your specified destinations.

## SDK setup requirements

- Set up a Meergo account.
- Set up a Python source in the dashboard.
- Copy the write key and the endpoint.

## Using the SDK

```python
import segment.analytics as analytics

analytics.write_key = 'YOUR_WRITE_KEY'
analytics.endpoint = 'YOUR_ENDPOINT'

analytics.track('Order Completed', { price: 99.84 })
```

## Sending events

Refer to the Meergo events documentation for more information on the supported event types.

## License

The Meergo Python SDK is released under the [MIT license](License.md).
