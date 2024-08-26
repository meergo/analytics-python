from datetime import datetime, date
import unittest
import json
import requests

import meergo.analytics.request
meergo.analytics.request.verify_ssl_requests = False

from meergo.analytics.request import post, DatetimeSerializer

test_endpoint = 'https://127.0.0.1:8000'

class TestRequests(unittest.TestCase):

    def test_valid_request(self):
        res = post('testsecret', endpoint=test_endpoint, batch=[{
            'userId': 'userId',
            'event': 'python event',
            'type': 'track'
        }])
        self.assertEqual(res.status_code, 200)

    def test_invalid_request_error(self):
        self.assertRaises(Exception, post, 'testsecret',
                         False, '[{]', endpoint=test_endpoint)

    def test_invalid_endpoint(self):
        self.assertRaises(Exception, post, 'testsecret',
                          endpoint=test_endpoint, batch=[])

    def test_datetime_serialization(self):
        data = {'created': datetime(2012, 3, 4, 5, 6, 7, 891011)}
        result = json.dumps(data, cls=DatetimeSerializer)
        self.assertEqual(result, '{"created": "2012-03-04T05:06:07.891011"}')

    def test_date_serialization(self):
        today = date.today()
        data = {'created': today}
        result = json.dumps(data, cls=DatetimeSerializer)
        expected = '{"created": "%s"}' % today.isoformat()
        self.assertEqual(result, expected)

    def test_should_not_timeout(self):
        res = post('testsecret', endpoint=test_endpoint, batch=[{
            'userId': 'userId',
            'event': 'python event',
            'type': 'track'
        }], timeout=15)
        self.assertEqual(res.status_code, 200)

    def test_should_timeout(self):
        with self.assertRaises(requests.ReadTimeout):
            post('testsecret', endpoint=test_endpoint, batch=[{
                'userId': 'userId',
                'event': 'python event',
                'type': 'track'
            }], timeout=0.0001)

    def test_proxies(self):
        res = post('testsecret', endpoint=test_endpoint, batch=[{
            'userId': 'userId',
            'event': 'python event',
            'type': 'track',
            'proxies': '203.243.63.16:80'
        }])
        self.assertEqual(res.status_code, 200)
