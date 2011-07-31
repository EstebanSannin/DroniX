#!/system/bin/sh


PASSWD=`echo "$QUERY_STRING" | /system/xbin/grep -oE "(^|[?&])passwd=[^&]+" | /system/xbin/sed "s/%20/ /g" | /system/xbin/cut -f 2 -d "="`
#USER=`echo "$QUERY_STRING" | grep -oE "(^|[?&])user=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`

echo Content-type: text/html
echo ""

/system/xbin/mount -o rw,remount -t yaffs2 /dev/block/mtdblock4 /system
echo $PASSWD > /system/etc/ssh/passwd
/system/xbin/mount -o ro,remount -t yaffs2 /dev/block/mtdblock4 /system

/system/xbin/cat << EOF
<html>
<link rel='stylesheet' href='style.css' type='text/css'>
<head>
<title>Monitor Tools</title>
<script src="js/ajaxsbmt.js" type="text/javascript"></script>
<script language="javascript" src="dinamic.js" type=text/javascript></script>
</head>
<body>
<!-- onload="setInterval(mostraOra, 1000);"> -->

<div id='footer'><font color=red>DroniX Web Manager</font> by <font color=yellow><a href='http://esteban.homelinux.org'>Stefano Viola (EstebanSannin)</a></font></div>

<div id='header'><img src="image/dronixlogo2.png">
<table border="0"><tr>
<td class="headitem"><a href="index.html">home</a></td>
<td class="headitem"><a href="versionNote.html">versionNote</a></td>
<td class="headitem"><a href="modules.html">modules</a></td>
<td class="headitem"><a href="sdcard">SD-Card</a></td>
<td class="headitem"><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ZCZJMRK7UGHH6&lc=GB&item_name=DroniX%20Development&currency_code=EUR&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted">donate</a></td></tr></table>
</div>
<div id='content'>
<br><br>
<h3>SSH Password Changed!</h3>
<br>
New Password is: `echo $PASSWD`
</div>
</body>
</html>
EOF
