from PIL import Image, ImageDraw, ImageFont


base_image = Image.open('base_map.png')
w, h = base_image.size

# Define the size of the image and the hexagon
width = w
height = h
side = 30 # length of the hexagon side
radius = side / 2 * 3**0.5 # radius of the circumscribed circle

## MidPoint of hex? triangles out?


# Create a new image with white background
img = Image.new("RGBA", (width, height), (0,0,0,0))
draw = ImageDraw.Draw(img)

# Define the coordinates of a single hexagon
x0, y0 = 0, 0 # top left corner
x1, y1 = x0 + side, y0 # top right corner
x2, y2 = x1 + side / 2, y1 + radius # right corner
x3, y3 = x1, y2 + radius # bottom right corner
x4, y4 = x0, y3 # bottom left corner
x5, y5 = x0 - side / 2, y2 # left corner
hexagon = [(x0, y0), (x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

# Loop through the rows and columns of the image
for i in range(0, height, int(radius * 2)): ##rows
    for j in range(0, width, int(side * 1.5)): ##how many columns
        if j % 2 == 0:
            #move down slightly
            offset = radius
        else:
            offset = -radius 
        # Draw a hexagon with a random color
        draw.polygon(hexagon, outline="black")
        
        tmp = str(i//(int(radius*2))) + str(j//int(side*1.5))
        
        draw.text((hexagon[0][0] ,hexagon[0][1]), tmp,  font=ImageFont.truetype("arial"), fill=(255,255,255,255))
        # Translate the hexagon to the next position
        hexagon = [(x + side * 1.5, y+offset) for x, y in hexagon]
    # Reset the hexagon to the original position
    hexagon = [(x0, y0 + i + radius * 2), (x1, y1 + i + radius * 2), (x2, y2 + i + radius * 2), (x3, y3 + i + radius * 2), (x4, y4 + i + radius * 2), (x5, y5 + i + radius * 2)]

#img.show()
base_image.paste(img, (0,0), img)
base_image.show()

# Save the image
base_image.save("covered.png")