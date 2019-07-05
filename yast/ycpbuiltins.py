from syslog import *

def y2milestone(*args):
    syslog(LOG_NOTICE, *args)

def y2warning(*args):
    syslog(LOG_WARNING, *args)

def y2error(*args):
    syslog(LOG_ERR, *args)

def y2debug(*args):
    syslog(LOG_DEBUG, *args)

def y2internal(*args):
    syslog(LOG_INFO, *args)

def y2security(*args):
    syslog(LOG_ALERT, *args)
