import unittest

import meergo.analytics.request
meergo.analytics.request.verify_ssl_requests = False

import meergo.analytics as analytics

test_endpoint = "https://127.0.0.1:8000"

class TestModule(unittest.TestCase):

    # def failed(self):
    #     self.failed = True

    def setUp(self):
        self.failed = False
        analytics.write_key = 'testsecret'
        analytics.endpoint = test_endpoint
        analytics.on_error = self.failed

    def test_no_write_key(self):
        analytics.write_key = None
        analytics.endpoint = test_endpoint
        self.assertRaises(Exception, analytics.track)

    @unittest.skip("Currently the default endpoint is just a placeholder and cannot be fetched")
    def test_no_endpoint(self):
        analytics.endpoint = None
        self.assertRaises(Exception, analytics.track)

    def test_track(self):
        analytics.endpoint = test_endpoint
        analytics.track('userId', 'python module event')
        analytics.flush()

    def test_identify(self):
        analytics.endpoint = test_endpoint
        analytics.identify('userId', {'email': 'user@email.com'})
        analytics.flush()

    def test_group(self):
        analytics.endpoint = test_endpoint
        analytics.group('userId', 'groupId')
        analytics.flush()

    def test_alias(self):
        analytics.endpoint = test_endpoint
        analytics.alias('previousId', 'userId')
        analytics.flush()

    def test_page(self):
        analytics.endpoint = test_endpoint
        analytics.page('userId')
        analytics.flush()

    def test_screen(self):
        analytics.endpoint = test_endpoint
        analytics.screen('userId')
        analytics.flush()

    def test_flush(self):
        analytics.endpoint = test_endpoint
        analytics.flush()
