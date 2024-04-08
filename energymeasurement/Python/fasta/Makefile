compile:
	cp fasta.python3-3.python3 fasta.python3-3.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO fasta.python3-3.py 25000000" Python fasta

run:
	/usr/bin/python -OO fasta.python3-3.py 25000000

make mem:
	/usr/bin/time -v  /usr/bin/python -OO fasta.python3-3.py 25000000
