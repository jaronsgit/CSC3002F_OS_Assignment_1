"""
A Python implementation of the FIFO, LRU and OPT page replacement algorithms.

Author: Jaron Cohen 
Student Number: CHNJAR003

Sources:
[CSC3002F, 2020] CSC3002F (2020). A Comparison of Three Page Replacement Algorithms:
FIFO, LRU and Optimal. Department of Computer Science, University of Cape Town,
South Africa.
[Silberschatz et al., 2018] Silberschatz, A., Galvin, P., and Gagne, G. (2018). Operating Sys-
tem Concepts - 10th Edition. John Wiley & Sons, New York, USA.

"""

import sys
import random
from collections import deque

"""
Performs the FIFO algorithm on an array of integer page references in the range of 0 to 9 for a given memory size.
parameters:
size - integer number in range 1 to 7 of number of frames in memory
pages - array of integer page references with each element in the range of 0 to 9
"""


def FIFO(size, pages):
    memory = []
    queue = deque([])
    numPageFaults = 0

    for page in pages:
        if len(memory) < size:
            memory.append(page)
            queue.append(page)
            numPageFaults += 1
        else:
            if page not in memory:
                pageToRemove = queue.popleft()
                indexOfPageToRemove = memory.index(pageToRemove)
                memory.remove(pageToRemove)
                memory.insert(indexOfPageToRemove, page)
                queue.append(page)
                numPageFaults += 1
    return numPageFaults


"""
Performs the LRU algorithm on an array of integer page references in the range of 0 to 9 for a given memory size.
parameters:
size - integer number in range 1 to 7 of number of frames in memory
pages - array of integer page references with each element in the range of 0 to 9
"""


def LRU(size, pages):
    memory = []
    stack = deque()
    numPageFaults = 0

    for page in pages:
        if len(memory) < size:
            memory.append(page)
            stack.appendleft(page)
            numPageFaults += 1

        else:
            if page in memory:  # If page is referenced, remove and place on top of stack

                pageStackIndex = stack.index(page)

                del stack[pageStackIndex]
                stack.appendleft(page)

            else:

                minPage = stack.pop()

                indexOfPageToRemove = memory.index(minPage)

                memory.remove(minPage)
                memory.insert(indexOfPageToRemove, page)
                stack.appendleft(page)
                numPageFaults += 1

    return numPageFaults


"""
Performs the OPT algorithm on an array of integer page references in the range of 0 to 9 for a given memory size.
parameters:
size - integer number in range 1 to 7 of number of frames in memory
pages - array of integer page references with each element in the range of 0 to 9
"""


def OPT(size, pages):
    memory = []
    numPageFaults = 0
    for i in range(len(pages)):

        if len(memory) < size:
            memory.append(pages[i])
            numPageFaults += 1

        else:

            if pages[i] not in memory:

                lastToBeUsed = -1
                # Find page in memory that is never referenced in the future
                for frame in memory:
                    # If there is a page in a frame in memory that doesn't appear in the rest of the pages sequence
                    if frame not in pages[i+1:]:
                        lastToBeUsed = frame
                        break

                # If found page not referenced in future, replace it
                if lastToBeUsed != -1:

                    indexOfPageToRemove = memory.index(lastToBeUsed)

                    memory.remove(lastToBeUsed)
                    memory.insert(indexOfPageToRemove, pages[i])
                    numPageFaults += 1
                else:  # If all pages in memory are referenced in future, find farthest in future

                    farthestIndex = pages[i+1:].index(memory[0])
                    pageWithFarthestIndex = memory[0]
                    # Iterate through memory frames and find farthest one in sequence
                    for frameIndex in range(1, len(memory)):
                        newIndex = pages[i+1:].index(memory[frameIndex])
                        if newIndex > farthestIndex:
                            farthestIndex = newIndex
                            pageWithFarthestIndex = memory[frameIndex]
                    indexOfPageToRemove = memory.index(pageWithFarthestIndex)

                    memory.remove(pageWithFarthestIndex)
                    memory.insert(indexOfPageToRemove, pages[i])
                    numPageFaults += 1

    return numPageFaults


def main():

    if len(sys.argv) == 2:
        numFrames = int(sys.argv[1])
        numPages = random.randint(10, 100)
        pages = [random.randint(0, 9) for ranNum in range(numPages)]
        print('Random Page References: ', pages)
        print('Number of Page References: ', len(pages))
        print('Number of Frames: ', numFrames)
        print('FIFO', FIFO(numFrames, pages), 'page faults.')
        print('LRU', LRU(numFrames, pages), 'page faults.')
        print('OPT', OPT(numFrames, pages), 'page faults.')
    else:
        numFrames = int(sys.argv[1])
        try:
            numPages = int(sys.argv[2])
        except:
            print("Invalid second argument provided.")

        pages = [random.randint(0, 9) for ranNum in range(numPages)]
        print('Random Page References: ', pages)
        print('Number of Page References: ', len(pages))
        print('Number of Frames: ', numFrames)
        print('FIFO', FIFO(numFrames, pages), 'page faults.')
        print('LRU', LRU(numFrames, pages), 'page faults.')
        print('OPT', OPT(numFrames, pages), 'page faults.')


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Usage: python3 paging.py number_of_frames [number_of_pages]')
        print('Refer to README for additional information.')
    elif len(sys.argv) >= 2 and len(sys.argv) <= 3:

        numFrames = int(sys.argv[1])
        if numFrames in range(1, 8):
            main()
        else:
            print("Invalid number of frames entered. Provide integer from 1 to 7.")

    else:
        print(
            'Too many arguments provided. Refer to README for valid command line arguments.')
