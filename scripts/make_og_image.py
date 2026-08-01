from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#0a5d65")
draw = ImageDraw.Draw(img)

# Diagonal gradient approximation using layered rectangles
top = (10, 93, 158)     # unused placeholder
c1 = (14, 124, 134)   # teal
c2 = (37, 99, 235)    # blue
for y in range(H):
    t = y / H
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# logo mark circle
cx, cy, r = 120, 120, 60
draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 255, 255, 255))
draw.polygon([(cx-32, cy+14), (cx+40, cy-24), (cx+20, cy+30), (cx+2, cy+8), (cx-14, cy+18)], fill=(255, 107, 74))

font_bold = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", 80)
font_reg = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf", 34)

draw.text((220, 90), "TravelConcurrent", font=font_bold, fill="white")
draw.text((224, 190), "Beste aanbieders, beste deals, reisinspiratie", font=font_reg, fill=(230, 245, 243))

img.save("/home/claude/travelconcurrent/public/afbeeldingen/og-default.png")
print("saved")
