#!/system/bin/sh

echo Content-type: test/html
echo ""

echo "Battery Information:"
echo
echo -n "Level: "
/system/xbin/cat /sys/devices/platform/huawei_battery/power_supply/battery/level
echo -n "Temperature: "
/system/xbin/cat /sys/devices/platform/huawei_battery/power_supply/battery/batt_temp
echo -n "Voltage: "
/system/xbin/cat /sys/devices/platform/huawei_battery/power_supply/battery/batt_vol

