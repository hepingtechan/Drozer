#!/usr/bin/env python
#coding:utf8
import sys, os
import string

def auto_uninstall(path_file_package_names):
    failed_count = 0
    with open('uninstall_failed.txt', 'w') as file_uninstall_log:
        with open(path_file_package_names) as file_package_names:
            package_names = file_package_names.readlines()
            for package_name in package_names:
                package_name = package_name.rstrip()
                os.system('adb forward tcp:31415 tcp:31415')
                try:
                    ret = os.popen('adb uninstall ' + package_name).read()
                    if 'Failure' in ret:
                        print 'Failure'
                        failed_count += 1
                        file_uninstall_log.write('No%d: %s\n' % (failed_count, package_name))
                    else:
                        print 'Success'
                except Exception as e:
                    pass

if __name__ == '__main__':
    path_file_package_names = sys.argv[1]
    auto_uninstall(path_file_package_names)


