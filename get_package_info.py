#!/usr/bin/env python
#coding:utf8
import sys, os
import string

def get_package_info(packages_path):
    with open('packages_info.txt', 'w') as file_package_info:
        os.chdir(packages_path)
        filenames = os.listdir(packages_path)
        filenames.sort()
        for filename in filenames:
            ret = os.popen('aapt dump badging ' + filename).readlines()
            output = filename+'\n'
            sys.stdout.write(output)
            file_package_info.write(output)
            output = "%s%s%s\n" % (ret[0], ret[2], ret[3])
            sys.stdout.write(output)
            file_package_info.write(output)
        
if __name__ == '__main__':
    packages_path = sys.argv[1]
    get_package_info(packages_path)
