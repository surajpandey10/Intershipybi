from PIL import Image, ImageDraw, ImageFont
import textwrap
import pytesseract # type: ignore
import PIL.Image as Image

# Path to the Tesseract executable 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image file containing handwritten text
image_path = 'text4.jpg'

# Open the image file
image = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Initialize image parameters
width, height = 480, 700
background_color = "white"
text_color = "black"

# Create a blank image with white background
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load a handwriting-style font
font_path = "1.ttf"  
font_size = 20
font = ImageFont.truetype(font_path, font_size)

# Wrap text
lines = textwrap.wrap(text, width=50)
y_text = 15
for line in lines:
    line_width, line_height = font.getbbox(line)[2:]
    draw.text(((width - line_width) / 2, y_text), line, font=font, fill=text_color)
    y_text += line_height

# Save the image
image.save("handwritten_text6.png")
