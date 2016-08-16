#!/usr/bin/env python
#coding:utf8

import sys, os

def get_package_names(file_packages_info):
    with open(file_packages_info) as file_packages_info, open('package_names.txt', 'w') as file_package_names:
        for package_info in file_packages_info.readlines():
            if package_info.find("package: name='") != -1:
                start = len("package: name='")
                end = package_info.find("'", start)
                package_name = package_info[start:end]
                print package_name
                file_package_names.write(package_name+'\n')

if __name__ == '__main__':
    packages_info_path = sys.argv[1]
    get_package_names(packages_info_path)
