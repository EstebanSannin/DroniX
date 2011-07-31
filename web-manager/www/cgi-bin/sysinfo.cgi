#!/system/bin/sh

echo Content-type: text/html
echo ""

echo -n "<font color=red>ROM Version: </font>"
echo "DroniX 0.4"
echo "<br>"
echo -n  "<font color=red>KERNEL: </font>"
/system/xbin/uname -a
echo "<br>"
echo -n "<font color=red>UPTIME: </font>"
/system/xbin/uptime
echo "<br><br>"
echo -n "<font color=red>IP eth0: </font>"
/system/xbin/ifconfig eth0 | /system/xbin/grep "inet a" | /system/xbin/awk '{print $2}' | /system/xbin/cut -d: -f2
