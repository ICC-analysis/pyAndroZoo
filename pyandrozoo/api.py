#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from urllib.parse import urlparse, urlunparse, urlencode, parse_qs

import grequests  # type: ignore[import-untyped]

ANDROZOO_URL = 'https://androzoo.uni.lu/api/download'

def exception_handler(request, exception):
    print('Request failed: {}'.format(request.url))

class pyAndroZoo():
    def __init__(self, apikey=None, url=ANDROZOO_URL):
        self.root_url = url
        self.apikey = apikey or os.getenv('androzoo_api_key', default=None)
        self.payload = {'apikey': self.apikey}

    def __write_file(self, r, **kwargs):
        sha256 = parse_qs(urlparse(r.url).query)['sha256'][0]
        if r.status_code == 200:
             with open(sha256+'.apk', "wb") as apk_file:
                 apk_file.write(r.content)
        else:
            print('Request failed for: {}'.format(sha256))
        return r

    def get(self, sha256_list):
        reqs = []
        parts = urlparse(self.root_url)
        for sha256 in sha256_list:
            payload = {'sha256': sha256}
            payload.update(self.payload)
            url = urlunparse(parts[:4] + (urlencode(payload),) + parts[5:])
            reqs.append(grequests.get(url,
                                    hooks={'response': [self.__write_file]}))
        grequests.map(reqs, size=30, exception_handler=exception_handler)
