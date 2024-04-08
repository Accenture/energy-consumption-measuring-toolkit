compile:
	cp binarytrees.python3 binarytrees.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO binarytrees.py 21" Python binary-trees 700.0

run:
	/usr/bin/python -OO binarytrees.py 21

mem:
	/usr/bin/time -v /usr/bin/python -OO binarytrees.py 21
