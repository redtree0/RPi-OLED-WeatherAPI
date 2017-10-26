rpi-oled: rpi-oled.c
	cc -o $@ $< -lwiringPi

clean:
	rm -f sample
