# Energy Consumption Measuring Toolkit in Python Programming Language

The way software is designed, developed, and deployed can have a major impact on energy consumption. Accordingly, companies should include software in their sustainability efforts.
 
While running applications on-premises or in the cloud, the main consumers of power on a server will be the CPU, the GPU, the memory, and the Tech Stack. Estimating how much each consumes will give an estimate of how much power your server, or your application on a server, consumes.

Key considerations on measuring energy consumption of software applications:

First, a baseline for energy consumption of software is that any hardware will consume power when idle. For absolute numbers, subtract the baseline consumption measurement from the overall consumption measured when running the application.
 
Second, the development of software can be extremely energy intensive. For example, sorting operation takes a significant amount time when the size of the given input increases. Hence critical to capture the execution time at a more fine grained level. The goals are saving time, decreasing power consumption, and saving money.


## Overview

This repo contains the following two projects to measure and benchmark Energy Consumption Measuring Toolkit in Python Programming Language.

#### Measuring Energy Consumption in Software Appliation using RAPL

Sorting – Process of rearrangement of a list of elements to the correct order for efficient handling of the elements.
The following sorting algorithms were considered for energy consumption analysis, MergeSort and BubbleSort.
•	MergeSort: An efficient, general-purpose, and comparison-based sorting algorithm. Works on Divide and Conquer Approach.
•	BubbleSort: The simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 

The Energy Profiler records how much energy each server component uses. The Energy Profiler also shows occurrences of system events (sleep) that can affect energy consumption.

Running Average Power Limit (RAPL) is a feature of recent intel processors that provide the energy consumption of the processor and provides interfaces for reporting the accumulated energy consumption of various power domains.

Identified program for energy efficiency calculation using RAPL technology:
•	pyJoules: Monitors energy consumption of python code, pyJoules support energy consumption calculation of intel cpu and code snippets using the RAPL technology. This module has been leveraged in our application.

energymeasurement: This is a custom “RAPL Enhancement” application.

1.	Collect energy data of the software application.
    a.	Call rapl.h application energy measurement.
2.	Helps in removal of Hardware Energy Data.
    a.	rapl_before() and rapl_after() captures CPU and GPU energy measurement. 
    b.	We need to configure which CPU socket to monitor (applications are deployed on specific CPU). This is achieved through RAPL setup function. 
    c.	The above data needs to be subtracted from data gathered in Step 1. This ensures only energy data related to application is captured. 
3.	The last step is to omit the sleep time of a multithreaded application, or the delay time captured in an application.
    a.	We leverage the EnergyContext package to add “breakpoint” in specific class/functions.
    b.	Start_tag parameter in EnergyContext package with each function name is used to capture energy data for the time when the application is executed.
    c.	Energy calculation using tagging omits the sleep time set in between the two functions. 


#### Generate Graph to benchmark the Energy Consumed by Software Appliation vs Time Taken for python applications.

Generate a benchmark comparison of the energy consumed vs time taken by the software applications.The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:

Parameters:

x_axis_data: Energy Consumed in Joules by Software Applications.
y_axis_data: Total execution time of Software Application.