
import subprocess
import socket

'''
@brief Encapsulation of open ocd

Do konstruktoru se preda konfiguracni slovnik

je treba umet ocd
 - spusti zastavit a yrestartovat pri padu
 - callback pri nenulovem navratove hodnote
 - telnet spojeni a nebo tcl ?

je treba umet
 - flashovat
 - mazat
 - halt
 - reset
 - reset halt

'''

class Oocd(object):
    pass

    def __init__(self, oocd_executable, gdb_port, cmd_port):
        self.__oocd_executable = oocd_executable
        self.__gdb_port = gdb_port
        self.__cmd_port = cmd_port
        self.__oocd_proc = None
        self.__oocd_cmd_sock = None
        self.__oocd_gdb_sock = None

    def __proc_watch(self):
        pass

    def __sock_watch(self, s):
        self.__proc_watch()
        
    def __cmd_sock_watch(self):
        pass

    def __gdb_sock_watch(self):
        pass

    def __launch_oocd(self):
        self.__oocd_proc = subprocess.Popen(self.__oocd_executable, stdout=subprocess.PIPE)

    def get_oocd_stdout(self):
        return self.__oocd_proc.stdout

    def oocd_exit_code(self):
        return self.__oocd_proc.poll()

    def __open_cmd_sock(self):
        if self.__oocd_cmd_socks is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("localhost", self.__cmd_port))
            self.__cmd_port = s

    def __open_gdb_sock(self):
        if self.__oocd_gdb_socks is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("localhost", self.__gdb_port))
            self.__gdb_port = s

    @property
    def gdb_sock(self):
        return self.__oocd_gdb_sock

    def do_cmd(self, cmd, timeout=10):
        pass

