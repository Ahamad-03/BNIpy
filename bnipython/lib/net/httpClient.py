import http.client
import json
import ssl
import base64
import requests
from bnipython.lib.util.utils import getTimestamp, generateTokenSignature


class HttpClient():
    def __init__(self):
        self.httpClient = http.client.HTTPSConnection('')

    def tokenRequest(self, options={'url', 'path', 'username', 'password'}):
        url = str(options['url']).replace(
            'http://', '').replace('https://', '')
        httpClient = http.client.HTTPSConnection(url)
        username = options['username']
        password = options['password']
        authorize = base64.b64encode(f'{username}:{password}'.encode('utf-8'))
        headers = {
            'User-Agent': 'bni-python/0.1.0',
            'Authorization': f'Basic {authorize.decode()}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = 'grant_type=client_credentials'

        httpClient.request('POST', options['path'], payload, headers)
        res = httpClient.getresponse()
        data = res.read()
        return json.loads(str(data.decode('utf-8')))

    def request(self, options={'method', 'apiKey', 'accessToken', 'url', 'path', 'data'}):
        url = str(options['url']).replace(
            'http://', '').replace('https://', '')
        httpClient = http.client.HTTPSConnection(url)
        accessToken = options['accessToken']
        path = options['path']
        url = f'{path}?access_token={accessToken}'
        payload = json.dumps(options['data'])
        headers = {
            'User-Agent': 'bni-python/0.1.0',
            'x-api-key': options['apiKey'],
            'Content-Type': 'application/json'
        }
        httpClient.request(options['method'], url, payload, headers)
        res = httpClient.getresponse()
        data = res.read()
        return json.loads(str(data.decode('utf-8')))

    def tokenRequestSnapBI(self, options={'url', 'clientId', 'privateKeyPath'}):
        timeStamp = getTimestamp()
        payload = "{\n\"grantType\":\"client_credentials\",\n\"additionalInfo\": {}\n}"
        headers = {
            'Content-Type': 'application/json',
            'X-SIGNATURE': generateTokenSignature({
                'privateKeyPath': options['privateKeyPath'],
                'clientId': options['clientId'],
                'timeStamp': timeStamp
            }),
            'X-TIMESTAMP': timeStamp,
            'X-CLIENT-KEY': options['clientId']
        }

        response = requests.request("POST", options['url'], headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))

    def requestSnapBI(self, options={'method', 'apiKey', 'accessToken', 'url', 'data', 'additionalHeader'}):
        accessToken = options['accessToken']
        header = {
            'content-type': 'application/json',
            'user-agent': 'bni-python/0.1.0',
            'Authorization': f'Bearer {accessToken}',
        }
        header.update(options['additionalHeader'])
        payload = json.dumps(options['data'])
        response = requests.request(
            "POST", options['url'], headers=header, data=payload)
        return json.loads(response.text.encode('utf8'))
    
    def requestV2(self, options={'method', 'apiKey', 'accessToken', 'url', 'path', 'data', 'signature', 'timestamp'}):
        url = str(options['url']).replace(
            'http://', '').replace('https://', '')
        httpClient = http.client.HTTPSConnection(url)
        accessToken = options['accessToken']
        path = options['path']
        url = f'{path}?access_token={accessToken}'
        payload = json.dumps(options['data'])
        headers = {
            'User-Agent': 'bni-python/0.1.0',
            'x-api-key': options['apiKey'],
            'x-signature': options['signature'],
            'x-timestamp': options['timestamp'],
            'Content-Type': 'application/json'
        }
        httpClient.request(options['method'], url, payload, headers)
        res = httpClient.getresponse()
        data = res.read()
        return json.loads(str(data.decode('utf-8')))
    
    # def requestOtr(self, options={'method', 'RequestId', 'ChannelId', 'url', 'path', 'data', 'timestamp'}):
    #     url = str(options['url']).replace(
    #         'http://', '').replace('https://', '')
    #     httpClient = http.client.HTTPSConnection(url)
    #     path = options['path']
    #     url = f'{path}'
    #     payload = json.dumps(options['data'])
    #     headers = {
    #         'User-Agent': 'bni-python/0.8.5',
    #         'Content-Type': 'application/json',
    #         'RequestId': options['RequestId'],
    #         'RequestDateTime': options['timestamp'],
    #         'ChannelId': options['ChannelId'],
    #     }
    #     print({'method': options['method'], 'url': url, 'headers': headers})
    #     # method is Get
    #     httpClient.request(options['method'], url, headers)
    #     res = httpClient.getresponse()
    #     data = res.read()
    #     return json.loads(str(data.decode('utf-8')))\
    def requestOtr(self, options=None):
        if options is None:
            options = {}
        
        # Validate necessary options
        if 'url' not in options or 'path' not in options:
            print("Error: URL and path must be provided in options.")
            return None

        # Prepare the URL
        base_url = str(options['url']).replace('http://', '').replace('https://', '')
        path = options['path']

        # Prepare the headers
        headers = {
            'User-Agent': 'bni-python/0.8.5',
            'Content-Type': 'application/json',
            'RequestId': options.get('RequestId', ''),
            'RequestDateTime': options.get('timestamp', ''),
            'ChannelId': options.get('ChannelId', ''),
        }

        # Prepare the payload
        payload = json.dumps(options.get('data', {})) if options.get('method', 'GET') != 'GET' else None  

        print('base_url', base_url)
        print('path', path)
        print('payload', payload)
        print('headers', headers)

        # Create HTTP client and make the request
        httpClient = http.client.HTTPSConnection(base_url)
        try:
            httpClient.request(options.get('method', 'GET'), path, body=payload, headers=headers)
            res = httpClient.getresponse()
            print('HTTP Status:', res.status)
            raw_data = res.read()
            print('Raw response data:', raw_data)
            
            if res.status == 204 or not raw_data:
                print("No content to decode.")
                return None
            
            return json.loads(raw_data.decode('utf-8'))
        except json.JSONDecodeError:
            print("Failed to decode JSON from response.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
