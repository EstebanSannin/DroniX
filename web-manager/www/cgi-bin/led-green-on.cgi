#!/system/bin/sh

echo Content-type: text/html
echo ""

echo "255" > /sys/devices/platform/rgb-leds.0/leds/green/brightness
echo "Led Green ON"
