#!/system/bin/sh

echo Content-type: text/html
echo ""

echo "Stopping SSH Server..."
/system/xbin/kill -9 `/system/xbin/ps | /system/xbin/grep -v "grep" | /system/xbin/grep dropbear | /system/xbin/awk '{print $1}'` > /dev/null

