#!/bin/sh
if [ -x /opt/kde3/bin/kdesu ]; then
    /opt/kde3/bin/kdesu /sbin/yast2 add-on cd:///
elif [ -x /usr/bin/gnomesu ]; then
    /usr/bin/gnomesu /sbin/yast2 add-on cd:///
elif [ -x /usr/bin/sudo ]; then
    /usr/bin/sudo /sbin/yast2 add-on cd:///
else
    /sbin/yast2 add-on cd:///
fi

