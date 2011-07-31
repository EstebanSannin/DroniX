#!/system/bin/sh

echo Content-type: text/html
echo ""

echo "CPU Stats"
echo
echo "Time in state: "
echo
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state
echo
echo -n "Total Trans: "
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/stats/total_trans
echo
echo "Trans Table: "
echo
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/stats/trans_table
