##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
_uucp:*:4:4::0:0:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13::0:0:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24::0:0:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25::0:0:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26::0:0:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27::0:0:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31::0:0:Service Configuration Service:/var/empty:/usr/bin/false
_ces:*:32:32::0:0:Certificate Enrollment Service:/var/empty:/usr/bin/false
_mcxalr:*:54:54::0:0:MCX AppLaunch:/var/empty:/usr/bin/false
_appleevents:*:55:55::0:0:AppleEvents Daemon:/var/empty:/usr/bin/false
_geod:*:56:56::0:0:Geo Services Daemon:/var/db/geod:/usr/bin/false
_serialnumberd:*:58:58::0:0:Serial Number Daemon:/var/empty:/usr/bin/false
_devdocs:*:59:59::0:0:Developer Documentation:/var/empty:/usr/bin/false
_sandbox:*:60:60::0:0:Seatbelt:/var/empty:/usr/bin/false
_mdnsresponder:*:65:65::0:0:mDNSResponder:/var/empty:/usr/bin/false
_ard:*:67:67::0:0:Apple Remote Desktop:/var/empty:/usr/bin/false
_www:*:70:70::0:0:World Wide Web Server:/Library/WebServer:/usr/bin/false
_eppc:*:71:71::0:0:Apple Events User:/var/empty:/usr/bin/false
_cvs:*:72:72::0:0:CVS Server:/var/empty:/usr/bin/false
_svn:*:73:73::0:0:SVN Server:/var/empty:/usr/bin/false
_mysql:*:74:74::0:0:MySQL Server:/var/empty:/usr/bin/false
_sshd:*:75:75::0:0:sshd Privilege separation:/var/empty:/usr/bin/false
_qtss:*:76:76::0:0:QuickTime Streaming Server:/var/empty:/usr/bin/false
_cyrus:*:77:6::0:0:Cyrus Administrator:/var/imap:/usr/bin/false
_mailman:*:78:78::0:0:Mailman List Server:/var/empty:/usr/bin/false
_appserver:*:79:79::0:0:Application Server:/var/empty:/usr/bin/false
_clamav:*:82:82::0:0:ClamAV Daemon:/var/virusmails:/usr/bin/false
_amavisd:*:83:83::0:0:AMaViS Daemon:/var/virusmails:/usr/bin/false
_jabber:*:84:84::0:0:Jabber XMPP Server:/var/empty:/usr/bin/false
_appowner:*:87:87::0:0:Application Owner:/var/empty:/usr/bin/false
_windowserver:*:88:88::0:0:WindowServer:/var/empty:/usr/bin/false
_spotlight:*:89:89::0:0:Spotlight:/var/empty:/usr/bin/false
_tokend:*:91:91::0:0:Token Daemon:/var/empty:/usr/bin/false
_securityagent:*:92:92::0:0:SecurityAgent:/var/empty:/usr/bin/false
_calendar:*:93:93::0:0:Calendar:/var/empty:/usr/bin/false
_teamsserver:*:94:94::0:0:TeamsServer:/var/teamsserver:/usr/bin/false
_update_sharing:*:95:-2::0:0:Update Sharing:/var/empty:/usr/bin/false
_installer:*:96:-2::0:0:Installer:/var/empty:/usr/bin/false
_atsserver:*:97:97::0:0:ATS Server:/var/empty:/usr/bin/false
_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
_unknown:*:99:99::0:0:Unknown User:/var/empty:/usr/bin/false
_softwareupdate:*:200:200::0:0:Software Update Service:/var/empty:/usr/bin/false
_coreaudiod:*:202:202::0:0:Core Audio Daemon:/var/empty:/usr/bin/false
_screensaver:*:203:203::0:0:Screensaver:/var/empty:/usr/bin/false
_locationd:*:205:205::0:0:Location Daemon:/var/db/locationd:/usr/bin/false
_trustevaluationagent:*:208:208::0:0:Trust Evaluation Agent:/var/empty:/usr/bin/false
_timezone:*:210:210::0:0:AutoTimeZoneDaemon:/var/empty:/usr/bin/false
_lda:*:211:211::0:0:Local Delivery Agent:/var/empty:/usr/bin/false
_cvmsroot:*:212:212::0:0:CVMS Root:/var/empty:/usr/bin/false
_usbmuxd:*:213:213::0:0:iPhone OS Device Helper:/var/db/lockdown:/usr/bin/false
_dovecot:*:214:6::0:0:Dovecot Administrator:/var/empty:/usr/bin/false
_dpaudio:*:215:215::0:0:DP Audio:/var/empty:/usr/bin/false
_postgres:*:216:216::0:0:PostgreSQL Server:/var/empty:/usr/bin/false
_krbtgt:*:217:-2::0:0:Kerberos Ticket Granting Ticket:/var/empty:/usr/bin/false
_kadmin_admin:*:218:-2::0:0:Kerberos Admin Service:/var/empty:/usr/bin/false
_kadmin_changepw:*:219:-2::0:0:Kerberos Change Password Service:/var/empty:/usr/bin/false
_devicemgr:*:220:220::0:0:Device Management Server:/var/empty:/usr/bin/false
_webauthserver:*:221:221::0:0:Web Auth Server:/var/empty:/usr/bin/false
_netbios:*:222:222::0:0:NetBIOS:/var/empty:/usr/bin/false
_warmd:*:224:224::0:0:Warm Daemon:/var/empty:/usr/bin/false
_dovenull:*:227:227::0:0:Dovecot Authentication:/var/empty:/usr/bin/false
_netstatistics:*:228:228::0:0:Network Statistics Daemon:/var/empty:/usr/bin/false
_avbdeviced:*:229:-2::0:0:Ethernet AVB Device Daemon:/var/empty:/usr/bin/false
_krb_krbtgt:*:230:-2::0:0:Open Directory Kerberos Ticket Granting Ticket:/var/empty:/usr/bin/false
_krb_kadmin:*:231:-2::0:0:Open Directory Kerberos Admin Service:/var/empty:/usr/bin/false
_krb_changepw:*:232:-2::0:0:Open Directory Kerberos Change Password Service:/var/empty:/usr/bin/false
_krb_kerberos:*:233:-2::0:0:Open Directory Kerberos:/var/empty:/usr/bin/false
_krb_anonymous:*:234:-2::0:0:Open Directory Kerberos Anonymous:/var/empty:/usr/bin/false
_assetcache:*:235:235::0:0:Asset Cache Service:/var/empty:/usr/bin/false
_coremediaiod:*:236:236::0:0:Core Media IO Daemon:/var/empty:/usr/bin/false
_xcsbuildagent:*:237:237::0:0:Xcode Server Build Agent:/var/empty:/usr/bin/false
_xcscredserver:*:238:238::0:0:Xcode Server Credential Server:/var/empty:/usr/bin/false
_launchservicesd:*:239:239::0:0:_launchservicesd:/var/empty:/usr/bin/false