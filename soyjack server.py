from flask import Flask, request, send_file
from PIL import Image, ImageFont, ImageDraw
import os

app = Flask(__name__)

image = Image.open(r'soy100%.png')
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50) 

@app.route("/")
def hello_world():
	ip = request.remote_addr
	draw.text((200,50), ("Your IP:\n" + ip), font = font, align = "center")
	path = "soyIP-" + ip + ".png"
	image.save(path)
	return send_file(path, mimetype="image/png")
	os.remove(path)

if __name__ == "__main__":
	app.run()