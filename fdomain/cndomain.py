#!/usr/bin/env python
# coding=utf-8

"""
中文域名处理
"""


class CnDomain:

    def _en_domain(self, domain):
        domain_blocks = domain.split(".")
        ret = []
        for block in domain_blocks:
            if self.if_cn_word(block):
                block = "xn--" + block.decode("utf-8").encode("punycode")
            ret.append(block)
        return ".".join(ret)

    def _cn_domain(self, domain):
        domain = domain.lower()
        domain_blocks = domain.split(".")
        ret = []
        for block in domain_blocks:
            if block.find("xn--") == 0:
                block = block[4:].decode("punycode").encode("utf-8")
            ret.append(block)
        return ".".join(ret)

    def if_cn_word(self, word):
        """
        判断是否中文字符
        """
        ord0 = ord("0")
        ord9 = ord("9")
        orda = ord("a")
        ordz = ord("z")
        ord_ = ord("_")
        is_cn = False
        for w in word:
            ordw = ord(w)
            if not orda <= ordw <= ordz and not \
                    ord0 <= ordw <= ord9 and ordw != ord_:
                is_cn = True
                break
        return is_cn

    def if_cn_domain(self, domain):
        """
        判断是否中文域名
        """
        domain_blocks = domain.split(".")
        if_cn = False
        for block in domain_blocks:
            if self.if_cn_word(block):
                if_cn = True
                break
        return if_cn

    def format_domain(self, domain, to="en"):
        if to == "cn":
            domain = self._cn_domain(domain)
        else:
            domain = self._en_domain(domain)
        return domain
