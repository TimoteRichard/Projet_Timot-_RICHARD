from animation import (f , animator)

def main():
    animator(x = [0,10], t = [0,3], path = "data/animation.gif", f = f)

if __name__=="__main__":
    main()
    
"""This will create an animation.gif file in the data directory showing the wave function evolving over time, representing the patient's heart rate model.
The animation will show:
        A wave packet moving from left to right
        The amplitude modulated by the Gaussian envelope
        Smooth transition between frames
        Total duration of 3 seconds as specified in the time range
The resulting animation will help visualize how the heart rate model changes over both position (x) and time (t).
"""
