#!/usr/bin/env python
#coding:utf8
import sys, os
import string

def get_apk_name_list(apk_path):
    apk_name_list = []
    filenames = os.listdir(apk_path)

    if (len(filenames) > 0):
        for filename in filenames:
            if ('.apk' in filename):
                full_filename = os.path.join(apk_path, filename)
                full_filename_new = full_filename.replace(' ', '_')
                os.rename(full_filename, full_filename_new)
                #print 'full_filename : %s' % full_filename
                apk_name_list.append(full_filename_new)
    return apk_name_list

def auto_install_app(apk_name_list):
    count_install_failed = 0
    with open('install_failed.txt', 'w') as file_install_log:
        for apk_name in apk_name_list:
            try:
                print 'apk name : %s' % apk_name
                ret = os.popen('adb install ' + apk_name).read()
                if 'Failure' in ret:
                    print ret
                    count_install_failed += 1
                    file_install_log.write('No.%d : %s\n%s\n' % (count_install_failed, apk_name, ret))
                else:
                    print 'Success'
                    pass
            except Exception as e:
                pass

if __name__ == '__main__':
    apk_path = sys.argv[1]
    apk_name_list = get_apk_name_list(apk_path)
    auto_install_app(apk_name_list)


