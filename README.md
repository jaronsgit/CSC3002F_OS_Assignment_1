# CSC3002F OS Assignment 1

The FIFO, LRU and OPT page replacement algorithms have been implemented in a python file called paging.py

## How to use the program

### The structure of the command line execution is as follows:

```bash
python3 paging.py number_of_frames [number_of_pages]
```

#### number_of_frames

This is a required argument and refers to the number of frames in memory.

#### number_of_pages

This is an optional argument and refers to the number of pages in the random page-reference string.

Examples and explanations:

```bash
python3 paging.py 4
```

The above command will execute the program with a memory of 4 frames and will randomly generate a page-reference string between the number_of_frames and 100

Navigate to the folder in Terminal and utilise the provided Makefile to run the program using the command:

The following command will invoke the program with

```bash
make run
```
