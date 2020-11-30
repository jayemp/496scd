import sounddevice as sd
# import numpy as np

def dot(v1, v2):
    return sum(x*y for x,y in zip(v1,v2))

def print_sound(indata, outdata, frames, time, status):
    # volume_norm = np.linalg.norm(indata)*10
    volume_norm = dot(indata, indata) * 10
    print ("|" * int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(10000)
