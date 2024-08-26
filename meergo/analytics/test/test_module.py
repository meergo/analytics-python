import unittest

import meergo.analytics.request
meergo.analytics.request.verify_ssl_requests = False

import meergo.analytics as analytics

test_endpoint='https://127.0.0.1:8000'

class TestModule(unittest.TestCase):

    # def failed(self):
    #     self.failed = True

    def setUp(self):
        self.failed = False
        analytics.write_key = 'testsecret'
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
        analytics.track('userId', 'python module event', endpoint=test_endpoint)
        analytics.flush()

    def test_identify(self):
        analytics.identify('userId', {'email': 'user@email.com'}, endpoint=test_endpoint)
        analytics.flush()

    def test_group(self):
        analytics.group('userId', 'groupId', endpoint=test_endpoint)
        analytics.flush()

    def test_alias(self):
        analytics.alias('previousId', 'userId', endpoint=test_endpoint)
        analytics.flush()

    def test_page(self):
        analytics.page('userId', endpoint=test_endpoint)
        analytics.flush()

    def test_screen(self):
        analytics.screen('userId', endpoint=test_endpoint)
        analytics.flush()

    def test_flush(self):
        analytics.flush()
