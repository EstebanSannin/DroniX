#!/system/bin/sh

EXE=/system/xbin
echo Content-type: text/html
echo ""

echo "<pre>Theme Changer DroniX"
echo ""
echo ""
$EXE/mountrw
echo "Install theme..."
$EXE/cp /cust/black/* /system/framework/
echo ""
echo "black" > /data/www/cgi-bin/logTheme
$EXE/mountro
echo "Restarting Framework...</pre>"

$EXE/kill -9 `/system/xbin/ps | $EXE/grep zygot | $EXE/awk '{print $1}' | $EXE/head -n1`
echo "Plese wait"
