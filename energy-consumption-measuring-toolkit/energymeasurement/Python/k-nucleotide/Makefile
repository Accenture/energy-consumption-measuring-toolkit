compile:
	cp knucleotide.python3-3.python3 knucleotide.python3-3.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO knucleotide.python3-3.py 0 < ../../knucleotide-input25000000.txt" Python k-nucleotide 1900.0
        
run:
	/usr/bin/python -OO knucleotide.python3-3.py 0 < ../../knucleotide-input25000000.txt

mem:
	/usr/bin/time -v /usr/bin/python -OO knucleotide.python3-3.py 0 < ../../knucleotide-input25000000.txt
