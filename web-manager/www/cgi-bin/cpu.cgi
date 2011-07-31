#!/system/bin/sh

echo Content-type: text/html
echo ""

echo "CPU Monitoring"
echo
echo -n "Frequenza attuale: "
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
echo -n "Frequenza minima: "
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
echo -n "Frequenza massima: "
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
echo -n "Governor usato: "
/system/xbin/cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 
