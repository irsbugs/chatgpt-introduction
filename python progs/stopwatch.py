# Command given to ChatGPT ChatGPT (chat generative pre-trained transformer)...
# write a stopwatch program in python

import time

# define the start time
start = time.time()

# keep looping until user presses 'q'
while True:
    # print the elapsed time
    print('Elapsed Time: {:.2f}s'.format(time.time() - start))
    
    # prompt user to quit
    user_input = input('Press "q" to quit: ')
    
    if user_input == 'q':
        break
        
"""
ian@hp:~/openai-quickstart-node/notes/python progs$ python stopwatch.py
Elapsed Time: 0.00s
Press "q" to quit: #  <--- pressed return key after 30 seconds
Elapsed Time: 32.53s
Press "q" to quit: 
Elapsed Time: 35.73s

"""
