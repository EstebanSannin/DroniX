#!/system/bin/sh

EXE=/system/xbin
echo Content-type: text/html
echo ""

echo "<h3>DroniX Theme Information</h3>"
echo "<pre>"
$EXE/cat /etc/themeChanger.conf
echo "</pre>"
