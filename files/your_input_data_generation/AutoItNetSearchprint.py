#!/usr/bin/env python
"""
    python codeCreationAutomation.py

    TODO: Add usage information here.
"""
import sys
# TODO: Uncomment or add imports here.
import os
#import re
#import time
#import subprocess
from argparse import ArgumentParser

def execute_codeCreationAutomation(searchphrase, area, name, searchphrase2, area2, name2, searchphrase3, area3, name3, searchphrase4, area4, name4, serachphrase5, area5, name5, searchphrase6, area6, name6, name7):
    """ TODO: Add docstring here. """
    # TODO: Add or delete code here.
    # Dump all passed argument values.
    print 'searchphrase = %s' % (repr(searchphrase))
    print 'area = %s' % (repr(area))
    print 'name = %s' % (repr(name))
    print 'searchphrase2 = %s' % (repr(searchphrase2))
    print 'area2 = %s' % (repr(area2))
    print 'name2 = %s' % (repr(name2))
    print 'searchphrase3 = %s' % (repr(searchphrase3))
    print 'area3 = %s' % (repr(area3))
    print 'name3 = %s' % (repr(name3))
    print 'searchphrase4 = %s' % (repr(searchphrase4))
    print 'area4 = %s' % (repr(area4))
    print 'name4 = %s' % (repr(name4))
    print 'serachphrase5 = %s' % (repr(serachphrase5))
    print 'area5 = %s' % (repr(area5))
    print 'name5 = %s' % (repr(name5))
    print 'searchphrase6 = %s' % (repr(searchphrase6))
    print 'area6 = %s' % (repr(area6))
    print 'name6 = %s' % (repr(name6))
    print 'name7 = %s' % (repr(name7))
    return 0

# Start of main program.
def main(argv=None):
    # Initialize the command line parser.
    parser = ArgumentParser(description='TODO: Text to display before the argument help.',
                            epilog='Copyright (c) 2017 TODO: your-name-here.',
                            add_help=True,
                            argument_default=None, # Global argument default
                            usage=__doc__)
    parser.add_argument(action='store', dest='searchphrase', help='TODO: Give first searchphrase')
    parser.add_argument(action='store', dest='area', help='TODO: Give area where in search results you want to copy')
    parser.add_argument(action='store', dest='name', help='TODO: Give au3 file name for automation file')
    parser.add_argument(action='store', dest='searchphrase2', help='TODO: Give second searchphrase')
    parser.add_argument(action='store', dest='area2', help='TODO: Give area where in search result you want to copy ')
    parser.add_argument(action='store', dest='name2', help='TODO: Give Generated java or other language name')
    parser.add_argument(action='store', dest='searchphrase3', help='TODO: Dive third searchphrase')
    parser.add_argument(action='store', dest='area3', help='TODO: Give area in where you want to copy')
    parser.add_argument(action='store', dest='name3', help='TODO: Give generated java or other language name')
    parser.add_argument(action='store', dest='searchphrase4', help='TODO: Give fourth searchphrase')
    parser.add_argument(action='store', dest='area4', help='TODO: Give fourth copy area')
    parser.add_argument(action='store', dest='name4', help='TODO: Give generated java or other language name ')
    parser.add_argument(action='store', dest='searchphrase5', help='TODO: Give fifth searchphrase')
    parser.add_argument(action='store', dest='area5', help='TODO: Give area where to copy')
    parser.add_argument(action='store', dest='name5', help='TODO: Give generated java or other language name')
    parser.add_argument(action='store', dest='searchphrase6', help='TODO: Give sixth searchphrase')
    parser.add_argument(action='store', dest='area6', help='TODO: Give area where to copy')
    parser.add_argument(action='store', dest='name6', help='TODO: Give generated java or other language name')
    parser.add_argument(action='store', dest='name7', help='TODO: Give generated java or other language name')

    # Parse the command line.
    arguments = parser.parse_args(args=argv)
    searchphrase = arguments.searchphrase
    area = arguments.area
    name = arguments.name
    searchphrase2 = arguments.searchphrase2
    area2 = arguments.area2
    name2 = arguments.name2
    searchphrase3 = arguments.searchphrase3
    area3 = arguments.area3
    name3 = arguments.name3
    searchphrase4 = arguments.searchphrase4
    area4 = arguments.area4
    name4 = arguments.name4
    searchphrase5 = arguments.searchphrase5
    area5 = arguments.area5
    name5 = arguments.name5
    searchphrase6 = arguments.searchphrase6
    area6 = arguments.area6
    name6 = arguments.name6
    name7 = arguments.name7
    status = 0
    try:

        f = open(arguments.name, 'w')
        f.write(
""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area) + ""')'"" +
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+
""'\nMouseClick("left", 200, 300)'""+ 
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nSend('"" + "'" + "{}".format(arguments.name2)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase2) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area2) + ""')'"" +
""'\nSleep(1500)'""+
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+
""'\nMouseClick("left", 200, 300)'""+ 
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nSend('"" + "'" + "{}".format(arguments.name3)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase3) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area3) + ""')'"" +
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+
""'\nMouseClick("left", 200, 300)'""+ 
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nSend('"" + "'" + "{}".format(arguments.name4)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase4) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area4) + ""')'"" +
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+
""'\nMouseClick("left", 200, 300)'""+ 
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nSend('"" + "'" + "{}".format(arguments.name5)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase5) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area5) + ""')'"" +
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+ 
""'\nMouseClick("left", 200, 300)'""+ 
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nSend('"" + "'" + "{}".format(arguments.name6)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+""'\nMouseClick("left", 360,900)'""+ 
""'\nsleep(6000)'""+ 
""'\nMouseClick("left", 1330,20)'"" + 
""'\nMouseClick("left", 650, 150)'""+ 
""'\nSleep(3000)'""+
""'\nSend('"" + ""'"{}"'"".format(arguments.searchphrase6) + ""')'"" +
""'\nSend("{Enter}")'""+ 
""'\nSleep(3000)'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nMouseClick("left", 300,300)'""+ 
""'\nSleep(700)'""+ ""'\nSleep(1500)'"" +
""'\nMouseClickDrag("left",'"" "{}".format(arguments.area6) + ""')'"" +
""'\nSend("^c")'""+
""'\nSleep(1500)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 1420, 20)'""+
""'\nMouseClick("left", 400, 250)'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'""+
"MouseClick(\"right\", 50,20)\r\n" +
"Sleep(500)\r\n" +
"MouseClick(\"left\", 100,50)\r\n" +
"Sleep(6000)\r\n" +
"MouseClick(\"left\", 200, 300)\r\n" +
"WinActivate ( \"C:\\\\Python27\\python.exe\" , \"Enter @class name\" )\r\n" +
"WinSetState ( \"\",\"\", @SW_MAXIMIZE )\r\n" +
"Sleep(100)\r\n" +
"MouseClick(\"left\", 150, 25)\r\n" +
"Sleep(150)\r\n" +
"MouseClick(\"left\", 150, 100)\r\n"+
""'\nSleep(2000)'""+ 
""'\nSend("^v")'""+ 
""'\nSend("{")'""+ 
""'\nSleep(100)'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend("public void")'""+ 
""'\nSend("^v")'""+
""'\nSend("}")'""+ 
""'\nSend("{Enter}")'""+ 
""'\nSleep(6000)'""+ 
""'\nSend('"" + "'" + "{}".format(arguments.name7)+ "'" +  ""')'""+ 
""'\nSleep(1000)'""+ 
""'\nSend("{Enter}")'""+
""'\nSend("{LWINDOWN}")'""+
""'\nSend("{PRINTSCREEN}")'""+
""'\nSend("{LWINUP}")'""+
""'\nWinActivate ( "C:\Python27\python.exe" , "Enter @class name" )'""+
""'\nWinSetState ( "","", @SW_MAXIMIZE )'""+
""'\nWinSetState ( "","", @SW_MINIMIZE )'"")
        f.close()

        execute_codeCreationAutomation(searchphrase, area, name, searchphrase2, area2, name2, searchphrase3, area3, name3, searchphrase4, area4, name4, searchphrase5, area5, name5, searchphrase6, area6, name6, name7)
    
    except ValueError, value_error:
        print value_error
        status = -1
    except EnvironmentError, environment_error:
        print environment_error
        status = -1
    return status


    



if __name__ == "__main__":
    sys.exit(main())
