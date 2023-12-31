import sys
import time

hbfuebfef = False

def loading_animation():
    while True:
        for i in range(1, 4):
            if condition_met(True):
                return

            sys.stdout.write("\rDownload {}  ".format("." * i))
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\r\033[K")  # ANSI escape code to clear the line

# Replace this function with your actual condition
def condition_met(iteration):
    if hbfuebfef == True:
        return iteration == True

loading_animation()
