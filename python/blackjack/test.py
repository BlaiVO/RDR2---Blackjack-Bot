import pytesseract as tess
import pyautogui
from PIL import Image, ImageChops

tess.pytesseract.tesseract_cmd = r"C:\Users\blaix\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

thresh = 150
fn = lambda x : 255 if x > thresh else 0

img = pyautogui.screenshot(region=(435,1003,135,25))#.convert('L').point(fn, mode='1')
#img = ImageChops.invert(img)
text = tess.image_to_string(img)
img.save(r"test.png")
print (text)


# original: region=(420,990,50,50)
# all text: region=(420,990,135,50)
# just num: region=(435,1003,25,25)

