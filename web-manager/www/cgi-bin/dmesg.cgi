#!/system/bin/sh

echo Content-type: text/html
echo ""

/system/xbin/dmesg | /system/xbin/tail -n12

