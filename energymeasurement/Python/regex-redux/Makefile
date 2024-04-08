compile:
	cp regexredux.python3 regexredux.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/python -OO regexredux.py 0 < ../../regexredux-input5000000.txt" Python regex-redux

run:
	/usr/bin/python -OO regexredux.py 0 < ../../regexredux-input5000000.txt

mem:
	/usr/bin/time -v /usr/bin/python -OO regexredux.py 0 < ../../regexredux-input5000000.txt
