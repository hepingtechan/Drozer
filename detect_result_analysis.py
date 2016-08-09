#!/usr/bin/env python
#coding:utf8
import sys, os
import string

def analysis_detect_result(detect_result_path):
    filenames = os.listdir(detect_result_path)
    filenames.sort()
    print 'filenames: %s\n' % str(filenames)
    components = ['Activity', 'BroadcastReceiver', 'Service']

    count = 0
    with open('detect_result_consolidation.txt', 'w') as file_detect_result:
        if len(filenames) > 0:
            for filename in filenames:
                if count == 0:
                    underline_index = filename.find('_')
                    package_name = filename[0:underline_index]
                    file_detect_result.write('%s:\nActivity: ' % package_name)
                if count == 1:
                    file_detect_result.write('BroadcastReceiver: ')

                if count == 2:
                    file_detect_result.write('Service: ')

                full_filename = os.path.join(detect_result_path, filename)
                with open(full_filename) as origin_detect_result:
                    detect_result = origin_detect_result.readlines()
                    detect_result_line2 = detect_result[1]
                    detect_result_line_last = detect_result[-1]
                file_detect_result.write('%d/%d\n' % (int(detect_result_line_last.rstrip()), int(detect_result_line2.rstrip())))

                if count == 2:
                    file_detect_result.write('\n')

                count += 1
                count %= 3

if __name__ == '__main__':
    detect_result_path = sys.argv[1]
    analysis_detect_result(detect_result_path)
