
# Decompiled by #SSX3l | Hussain Yacoub
# Github : https://github.com/kanekikon
#---------------------------------------

import os
import sys
import time
import colorama
from colorama import *

def tm():
    time.sleep(1)


def pt():
    print ''


def clr():
    os.system('clear')


def author():
    print '\x1b[1;92m'
    print Fore.RED + 'Loading scripts Information...'


def logo():
    pt()
    time.sleep(0.3)
    print Fore.RED + 'Loading scripts Info...'
    time.sleep(2)
    pt()
    os.system('clear')
    print '\x1b[1;96m'
    print '         ___   ___  __ _  _ __   _ __    ___  _ __ '
    print "        / __| / __|/ _` || '_ \ | '_ \  / _ \| '__|"
    print '        \__ \| (__| (_| || | | || | | ||  __/| |   '
    print '        |___/ \___|\__,_||_| |_||_| |_| \___||_|  v1.0 '
    print ''
    print '  \x1b[1;95m -:;-\x1b[1;97m I do not tolerate bad use , written By @SSX3l \x1b[1;95m-:;-'
    print ' '


def again():
    pp = raw_input('\x1b[1;91m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80[\x1b[1;96mContinue|Exit=[c/e]\x1b[1;91m]\n\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\xba\x1b[1;92m ')
    if pp == 'e':
        time.sleep(1)
        print '\x1b[1;91m            <-----\ Exiting /----->'
        print ''
    else:
        print '                    >-----\ launching /-----<'
        time.sleep(1)
        os.system('clear')
        logo()
        main()


def main():
    print '\x1b[1;91m[\x1b[1;93m01\x1b[1;91m] \x1b[1;92mFTP-Backdoor      \x1b[1;91m[\x1b[1;93m02\x1b[1;91m] \x1b[1;92mFirewall Detection '
    pt()
    print '\x1b[1;91m[\x1b[1;93m03\x1b[1;91m] \x1b[1;92mOS Detection      \x1b[1;91m[\x1b[1;93m04\x1b[1;91m] \x1b[1;92mHeartBleed'
    pt()
    print '\x1b[1;91m[\x1b[1;93m05\x1b[1;91m] \x1b[1;92mfirewall-bypass   \x1b[1;91m[\x1b[1;93m06\x1b[1;91m] \x1b[1;92mssl-poodle'
    pt()
    print '\x1b[1;91m[\x1b[1;93m07\x1b[1;91m] \x1b[1;92mwordpress-users   \x1b[1;91m[\x1b[1;93m08\x1b[1;91m] \x1b[1;92mXSS-stored '
    pt()
    print '\x1b[1;91m[\x1b[1;93m09\x1b[1;91m] \x1b[1;92mcookie Flags      \x1b[1;91m[\x1b[1;93m10\x1b[1;91m] \x1b[1;92mCSRF'
    pt()
    print '\x1b[1;91m[\x1b[1;93m11\x1b[1;91m] \x1b[1;92mphpself XSS       \x1b[1;91m[\x1b[1;93m12\x1b[1;91m] \x1b[1;92mphpmyadmin traversal'
    pt()
    print '\x1b[1;91m[\x1b[1;93m13\x1b[1;91m] \x1b[1;92mDlink Backdoor    \x1b[1;91m[\x1b[1;93m14\x1b[1;91m] \x1b[1;92mshellshock'
    pt()
    print '\x1b[1;91m[\x1b[1;93m15\x1b[1;91m] \x1b[1;92mSQL injection     \x1b[1;91m[\x1b[1;93m16\x1b[1;91m] \x1b[1;92msmtp [cve2011-1764]'
    pt()
    print '\x1b[1;91m[\x1b[1;93m17\x1b[1;91m] \x1b[1;92mMy-SQL            \x1b[1;91m[\x1b[1;93m18\x1b[1;91m] \x1b[1;92mBotnet channels'
    pt()
    print '\x1b[1;91m[\x1b[1;93m19\x1b[1;91m] \x1b[1;92mMacOS-X AFP       \x1b[1;91m[\x1b[1;93m20\x1b[1;91m] \x1b[1;92mFtp libopie '
    pt()
    print '\x1b[1;91m[\x1b[1;93m21\x1b[1;91m] \x1b[1;92mDos site ?        \x1b[1;91m[\x1b[1;93m00\x1b[1;91m] \x1b[1;92mExit '
    pt()
    op = raw_input('\x1b[1;91m\xe2\x94\x8c\xe2\x94\x80[\x1b[1;96mscanner\x1b[1;91m]\n|\n\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\xba\x1b[1;92m ')
    pt()
    if op == '1':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap --script ftp-proftpd-backdoor -p 21 ' + t)
        again()
    elif op == '2':
        tm()
        t = raw_input('\x1b[1;91m Target Ip : \x1b[1;92m')
        os.system('nmap -sA ' + t)
        again()
    elif op == '3':
        tm()
        t = raw_input('\x1b[1;91m Target Ip : \x1b[1;92m')
        os.system('nmap -O ' + t)
        again()
    elif op == '4':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p 443 --script ssl-heartbleed ' + t)
        again()
    elif op == '5':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap --script firewall-bypass ' + t)
        again()
    elif op == '6':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV --version-light --script ssl-poodle -p 443 ' + t)
        again()
    elif op == '7':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p80 --script http-wordpress-users ' + t)
        again()
    elif op == '8':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p80 --script http-stored-xss.nse ' + t)
        again()
    elif op == '9':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p 443 --script http-cookie-flags ' + t)
        again()
    elif op == '10':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p80 --script http-csrf.nse ' + t)
        again()
    elif op == '11':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap --script=http-phpself-xss -p80 ' + t)
        again()
    elif op == '12':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p80 --script http-phpmyadmin-dir-traversal ' + t)
        again()
    elif op == '13':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV --script http-dlink-backdoor ' + t)
        again()
    elif op == '14':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV -p- --script http-shellshock ' + t)
        again()
    elif op == '15':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV --script=http-sql-injection ' + t)
        again()
    elif op == '16':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap --script=smtp-vuln-cve2011-1764 -pT:25,465,587 ' + t)
        again()
    elif op == '17':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p3306 --script mysql-vuln-cve2012-2122 ' + t)
        again()
    elif op == '18':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -p 6667 --script=irc-botnet-channels ' + t)
        again()
    elif op == '19':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV --script=afp-path-vuln ' + t)
        again()
    elif op == '20':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap -sV --script=ftp-libopie ' + t)
        again()
    elif op == '21':
        tm()
        t = raw_input('\x1b[1;91m Target : \x1b[1;92m')
        os.system('nmap --script dos -Pn ' + t)
        again()
    elif op == '00':
        time.sleep(1)
        print '                    <-----\ Exiting /----->'
        print ''
        time.sleep(1)
    else:
        os.system('clear')
        logo()
        main()

logo()
main()