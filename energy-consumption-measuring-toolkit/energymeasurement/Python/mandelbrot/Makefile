compile:
	cp mandelbrot.python3-7.python3 mandelbrot.python3-7.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO mandelbrot.python3-7.py 16000" Python mandelbrot 3500.0

run:
	/usr/bin/python -OO mandelbrot.python3-7.py 16000

mem:
	/usr/bin/time -v /usr/bin/python -OO mandelbrot.python3-7.py 16000
