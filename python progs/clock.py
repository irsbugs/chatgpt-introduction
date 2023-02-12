# ChatGPT response from:
# write a clock computer program

import time 

while True:
    currentTime = time.strftime("%H:%M:%S")
    print(currentTime)
    time.sleep(1)


"""
ian@hp:~/openai-quickstart-node/notes/python progs$ python clock.py
11:47:33
11:47:34
11:47:35

"""
