from PIL import Image, ImageDraw

img = Image.open("white.gif")
new = Image.new("RGB", (500, 200))
draw = ImageDraw.Draw(new)
cx, cy = 0, 100
for frame in range(img.n_frames):
    img.seek(frame)
    left, upper, right, lower = img.getbbox()

    dx = left - 100
    dy = upper - 100

    if dx == dy == 0:
        cx += 50
        cy = 100
    cx += dx
    cy += dy
    draw.point([cx, cy])

new.show()