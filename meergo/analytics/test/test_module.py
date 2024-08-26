import unittest

import meergo.analytics.request
meergo.analytics.request.verify_ssl_requests = False

import meergo.analytics as analytics

class TestModule(unittest.TestCase):

    # def failed(self):
    #     self.failed = True

    def setUp(self):
        self.failed = False
        analytics.write_key = 'testsecret'
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.on_error = self.failed

    @unittest.skip
    def test_no_write_key(self):
        analytics.write_key = None
        self.assertRaises(Exception, analytics.track)

    @unittest.skip
    def test_no_endpoint(self):
        analytics.endpoint = None
        self.assertRaises(Exception, analytics.track)

    def test_track(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.track('userId', 'python module event')
        analytics.flush()

    def test_identify(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.identify('userId', {'email': 'user@email.com'})
        analytics.flush()

    def test_group(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.group('userId', 'groupId')
        analytics.flush()

    def test_alias(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.alias('previousId', 'userId')
        analytics.flush()

    def test_page(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.page('userId')
        analytics.flush()

    def test_screen(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.screen('userId')
        analytics.flush()

    def test_flush(self):
        analytics.endpoint = 'https://127.0.0.1:8000'
        analytics.flush()
