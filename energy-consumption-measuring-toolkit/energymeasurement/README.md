# Energy Measurement in Python Applications

The folder contains applications written in python language. The application energy is calculated with RAPL and saved in .csv file.

#### The Folder Structure
The main folder elements: 
1. Python folders containing applications of algorithms.
2. A `Python` script `compile_all.py`, capable of building, running and measuring the energy and memory usage of every application in python language.
3. A `RAPL` sub-folder, containing the code of the energy measurement framework.
4. A `Bash` script `gen-input.sh`, used to generate the input files for algorithms: `bubbleSort`, `heapSort`, `mergeSort`.

#### The Operations

Each application sub-folder, included in a Python folder, contains a `Makefile`.
This is the file where is stated how to perform the 4 supported operations: *(1)* **compilation**, *(2)* **execution**, *(3)* **energy measuring** and *(4)* **memory peak detection**.

Basically, each `Makefile` **must** contains 4 rules, one for each operations:

| Rule | Description |
| -------- | -------- |
| `compile` | This rule specifies how the applications should be compiled in the python language. |
| `run` | This rule specifies how the applications should be executed; It is used to test whether the applications runs with no errors, and the output is the expected. |
| `measure` | This rule shows how to use the framework included in the `RAPL` folder to measure the energy of executing the task specified in the `run` rule. |
| `mem` | Similar to `measure`, this rule executes the task specified in the `run` rule but with support for memory peak detection. |

### Running an example.

Give sudo access to the energy registers for RAPL to access
```
sudo modprobe msr
```
and then generate the input files, like this
```Makefile
./gen-input.sh
```
This will generate the necessary input files, and are valid for python language.

We included a main Python script, `compile_all.py`, that you can either call from the main folder or from inside a language folder, and it can be executed as follows:

```PowerShell
python compile_all.py [rule]
```

The default rule is `compile`, which means that if you run it with no arguments provided (`python compile_all.py`) the script will try to compile all applications.

The results of the energy measurements will be stored in files with the name `python.csv`.

python.csv will contain a line with the following: 

```application-name ; PKG (Joules) ; CPU (J) ; GPU (J) ; DRAM (J) ; Time (ms)```

Do note that the availability of GPU/DRAM measurements depend on your machine's architecture. These are requirements from RAPL itself.