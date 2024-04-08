compile:
	cp spectralnorm.python3-5.python3 spectralnorm.python3-5.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO spectralnorm.python3-5.py 5500" Python spectral-norm

run:
	/usr/bin/python -OO spectralnorm.python3-5.py 5500

mem:
	/usr/bin/time -v /usr/bin/python -OO spectralnorm.python3-5.py 5500
