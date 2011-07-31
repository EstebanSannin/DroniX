#!/system/bin/sh

EXE=/system/xbin
echo Content-type: text/html
echo ""

echo "<pre>Theme Changer DroniX"
echo ""
echo ""
echo "Plese wait"
echo "<!--"
$EXE/mountrw
echo "-->"
echo "Install theme..."
echo "<!--"
$EXE/cp /cust/white/* /system/framework/
echo "-->"
echo ""
echo "white" > /data/www/cgi-bin/logTheme
echo "<!--"
$EXE/mountro
echo "-->"
echo "Restarting Framework...</pre>"

echo "<!--"
$EXE/kill -9 `/system/xbin/ps | $EXE/grep zygot | $EXE/awk '{print $1}' | $EXE/head -n1`
echo "-->"
