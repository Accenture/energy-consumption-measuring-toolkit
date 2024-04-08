compile:
	cp mergeSort.python3 mergeSort.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO mergeSort.py 21" Python binary-trees 700.0

run:
	/usr/bin/python -OO mergeSort.py 21

mem:
	/usr/bin/time -v /usr/bin/python -OO mergeSort.py 21
