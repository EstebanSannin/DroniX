#!/system/bin/sh

EXE=/system/xbin
echo Content-type: text/html
echo ""

echo ""
echo ""
$EXE/cat <<EOF
<table border="0">
EOF
CURRENT=`$EXE/cat logTheme`
WHITE=white
BLACK=black
if [ $CURRENT = $BLACK ]; then
$EXE/cat <<EOF
<tr><td>White Theme</td><td></td>
<td><input type="button" name="memory" value="ENABLE" OnClick="javascript:stop(); cgiRequest('cgi-bin/themeChangerWhite.cgi', 'result')"></td>
</tr>
<tr><td><br><br><br><img src="/image/whiteTheme.png"></img></td></tr>
EOF
elif [ $CURRENT = $WHITE ]; then
$EXE/cat <<EOF
<tr><td>Black Theme</td><td></td>
<td><input type="button" name="memory" value="ENABLE" OnClick="javascript:stop(); cgiRequest('cgi-bin/themeChangerBlack.cgi', 'result')"></td>
</tr>
<tr><td></td></tr>
<tr><td><br><br><br><img src="/image/blackTheme.png"></img></td></tr>
EOF
fi
echo "</table>"
