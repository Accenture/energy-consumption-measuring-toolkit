compile:
	cp pidigits.python3-2.python3 pidigits.python3-2.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO pidigits.python3-2.py 10000" Python pidigits

run:
	/usr/bin/python -OO pidigits.python3-2.py 10000
mem:
	/usr/bin/time -v /usr/bin/python -OO pidigits.python3-2.py 10000
