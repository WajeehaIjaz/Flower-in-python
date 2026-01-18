from turtle import *
import colorsys

# Set turtle speed to fastest (0 = instant drawing)
speed(0)

bgcolor("Black")  # Set background color to black
h = 0     # h = hue value for colors (starts at 0 = red)

# Outer loop: repeats the pattern 16 times
for i in range(16):
    
    # Inner loop: draws 18 connected curves (creates one petal/section)
    for j in range(18):
        # Convert HSV color to RGB (h=hue, 1=full saturation, 1=full brightness)
        c = colorsys.hsv_to_rgb(h, 1, 1)
        
        color(c)            # Set the drawing color
        h += 0.005          # Gradually change the hue for rainbow effect
        rt(90)              # Turn right 90 degrees
        
        # Draw a curved arc (radius decreases as j increases, 90 degree arc)
        circle(150 - j*6, 90)
        
        lt(90)               # Turn left 90 degrees
        
        # Draw another curved arc (same radius, 90 degree arc)
        circle(150 - j*6, 90)
        
        
        rt(180)              # Turn around 180 degrees (face opposite direction)
    circle(40, 24)            # After completing one petal, rotate slightly for next petal
    # Small circle moves the turtle to a new position (24 degree rotation)

# Keep the window open until closed
done()