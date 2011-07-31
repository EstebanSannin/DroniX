#!/system/bin/sh

echo Content-type: text/html
echo ""

if [ -e /system/etc/ssh/passwd ]; then
PASSWD=`/system/xbin/cat /etc/ssh/passwd`
/system/xbin/dropbear -A -N root -U 0 -G 0 -C $PASSWD -r /etc/rsa_key -p 22
echo "SSH Server Enabled!"
echo ""
echo "Use passwd: $PASSWD"
else
echo "Password File not exist!"
fi 
