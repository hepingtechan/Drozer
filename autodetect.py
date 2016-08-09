#!/usr/bin/env python
#coding:utf8
import sys, os
import pexpect
import time
import string

def autotest(drozer_path, file_package_names):
    os.chdir(drozer_path)
    #os.system('source ENVIRONMENT')
    os.system('adb forward tcp:31415 tcp:31415')
    child = pexpect.spawn('drozer console connect')
    child.expect('dz>')
    print "child.before: %s\n" % child.before
    
    commands = []
    with open(file_package_names) as file_package_names:
        for package_name in file_package_names.readlines():
            #package_name = package_name[0:-1] # 20160627 get rid of a carrige return at the end.
            package_name = package_name.rstrip()
            #print ('package name: %s' % package_name)
            commands.append('run apksec.activity.detect -a ' + package_name)
            commands.append('run apksec.broadcast.detect -a ' + package_name)
            commands.append('run apksec.service.detect -a ' + package_name)

    print ('commands : %s' % str(commands))
    for command in commands:
        print ('command : %s' % command)
        child.sendline(command)
        child.expect('dz>', timeout = None)
        print child.before

    child.sendline('exit()')


if __name__ == '__main__':
    drozer_path = sys.argv[1]
    file_package_names = sys.argv[2]
    autotest(drozer_path, file_package_names)


