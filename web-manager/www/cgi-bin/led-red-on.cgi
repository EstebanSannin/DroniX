#!/system/bin/sh

echo Content-type: text/html
echo ""

echo "255" > /sys/devices/platform/rgb-leds.0/leds/red/brightness
echo "Led RED ON"
