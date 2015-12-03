#-*- coding:utf-8 -*-
from adblockparser import AdblockRules


class AdUrlChecker(object):
    def __init__(self, *paths):
        raw_rules = list()
        for path in paths:
            print path
            with open(path) as f:
                txt = f.read()
                rows = txt.split('\n')
                raw_rules.extend(rows)
            self.rules = AdblockRules(raw_rules)

    def check_url(self, url):
        #adのurlに該当している場合にTrueを返します
        return self.rules.should_block(url)
