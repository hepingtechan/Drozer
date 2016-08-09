from pydiesel.reflection import ReflectionException
from drozer.modules import Module, common
from drozer.modules.common.package_manager import PackageManager
from drozer import android
from drozer.modules.apksec.logcat_logs import read_shell, cutoff_system_print
from drozer.modules.apksec.config import START_ACTIVITY
import os
import sys
import traceback
import time
import string

class Detect(Module, common.Filters, common.PackageManager, common.IntentFilter):
    name = "Detect Activity Security Hole"
    description = "Detect the activites, find the security holes"
    examples = "run apksec.activity.detect -a com.mwr.example.sieve"
    date = "2016-08-08"
    author = "Xiaofang Huang"
    licence = "MWR Code Licence"
    path = ["apksec", "activity"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

    def add_arguments(self, parser):
        parser.add_argument("-a", "--package", default = None, help = "specify the package to inspect")
        parser.add_argument("-c", "--component", default = None, help = "specify the component to inspect")

    def execute(self, arguments):
        reload(sys)
        sys.setdefaultencoding("utf-8")

        shell = self.new("com.mwr.jdiesel.util.Shell")
        shell.write("su\n") # added 20160612
        """
        shell.write("logcat ContextImplcheckPermission:E IntentExtra:E AndroidRuntime:E *:S")
        shell.write("logcat -d")#20160607
        shell.write("logcat -c")#20160612
        logs = read_shell(shell, 1)
        #self.stdout.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!logs before detecting is...\n%s\n" % logs)
        """
        if arguments.package != None and arguments.component != None:
            self.stdout.write("activity detecting starts...\n")
            activity_detect_result = {}#20160317
            shell.write("logcat ContextImplcheckPermission:E IntentExtra:E AndroidRuntime:E *:S")#20160607
            logs = read_shell(shell, 1)#20160607

            time.sleep(1)
            # Serializable added 20151113
            start_components = self.new("com.mwr.dz.apksec.StartComponents")
            try:
                start_components.startcomponent(arguments.package, arguments.component, START_ACTIVITY, self.getContext())
            except Exception as e:
                pass

            shell.write("logcat -d")#20160607
            logs = read_shell(shell, 1)
            logs = cutoff_system_print(logs)

            if logs != '':
                self.stdout.write("++++++++++++++++++++++++++++++++++++++++LOGS of %s++++++++++++++++++++++++++++++++++++++++\n%s\n" % (arguments.component, logs))
                self.stdout.flush() #added 20151116
                shell.write("logcat -c")#20160612


        else:
            self.stdout.write("package could not be None!\n")

        shell.close()


    def __get_activities(self, package):
        exported_activities = self.match_filter(package.activities, 'exported', True)
        hidden_activities = self.match_filter(package.activities, 'exported', False )
        return exported_activities


