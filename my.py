import time 
from colorama import Fore,Back 
import sys
from playsound import playsound
zig_zag_art=['''
               \\
                \\
                 \\
                  \\
                  /
                 /
                /
               /
               \\
                \\ 
                 \\ 
                 /
                /
               /
              /''','''
                               \\
                                \\
                                 \\
                                  \\
                                  /
                                 /
                                /
                               /
                               \\
                                \\ 
                                 \\ 
                                 /
                                /
                               /
                              /      ''','''
                                              \\
                                               \\
                                                \\
                                                 \\
                                                 /
                                                /
                                               /
                                              /
                                              \\
                                               \\ 
                                                \\ 
                                                /
                                               /
                                              /
                                             /   ''','''
                            \\
                             \\
                              \\
                               \\
                               /
                              /
                             /
                            /
                             \\
                              \\ 
                               \\ 
                               /
                              /
                             /
                            /
                            |
                            |''']
#Creating a function that loops over a subscriptable sequence and prints it out horizontially in the output stream 
def loop_over(sequence,color,delay_time):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{Fore.RESET}')
        
loop_over(sequence='Lightning...',color=Fore.YELLOW,delay_time=0.01)
time.sleep(1)
print(f'{Back.BLACK}')
for n in range(20):
    loop_over(sequence=zig_zag_art[0:-1],color=Fore.YELLOW,delay_time=0.1)
else:
    time.sleep(1)
    loop_over(sequence=zig_zag_art[-1],color=Fore.YELLOW,delay_time=0.000001)
    time.sleep(0.1)
    playsound('thunder.mp3')
