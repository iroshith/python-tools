#-*- coding:utf-8 -*-
from libs.parser import AdUrlChecker
import sys


def list_parser(path):
    with open(path, 'rb') as f:
        line = f.read()
        rows = line.split('\n')
        return rows


def main():
    resourse_path = '/Users/HiroshitakatoH/PycharmProjects/python-tools/adblock_parser/resourse/EasyList.txt'
    resourse_path2 = '/Users/HiroshitakatoH/PycharmProjects/python-tools/adblock_parser/resourse/abp_jp.txt'

    url_list_path = sys.argv[1]
    urls = list_parser(url_list_path)

    checker = AdUrlChecker(resourse_path, resourse_path2)

    for url in urls:
        if checker.check_url(url):
            print url

if __name__ == '__main__':
    main()
