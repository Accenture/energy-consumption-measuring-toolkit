compile:
	cp nbody.python3 nbody.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO nbody.py 50000000" Python n-body

run:
	/usr/bin/python -OO nbody.py 50000000

mem:
	/usr/bin/time -v /usr/bin/python -OO nbody.py 50000000
