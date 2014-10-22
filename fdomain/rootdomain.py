#!/usr/bin/env python
# coding=utf-8

"""
根域名处理
"""

from suffixs import SUFFIXS


class Domain:

    def url_format(self, url):
        """
        return http(s)://www.example.com
        """
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        if url.endswith("/"):
            url = url[:-1]
        return url

    def get_domain(self, url):
        url = url.replace("https://", "")
        url = url.replace("http://", "")
        domain = url[:url.index("/")+1] if "/" in url else url
        return domain

    def get_root_domain(self, url):
        domain = self.get_domain(url)
        domain_blocks = domain.split(".")
        index = -2
        suffix = ".".join(domain_blocks[index:])
        if_match = False
        if suffix in SUFFIXS:
            index -= 1
            if_match = True
        else:
            index += 1
            suffix = ".".join(domain_blocks[index:])
            if suffix in SUFFIXS:
                index -= 1
                if_match = True
        root_domain = ""
        if if_match:
            root_domain = ".".join(domain_blocks[index:])
        return root_domain

fd = Domain()
