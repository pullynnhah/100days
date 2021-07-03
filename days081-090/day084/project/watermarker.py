# ------------------------------------------------------- IMPORTS ---------------------------------------------------- #
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

# ------------------------------------------------------ CONSTANTS --------------------------------------------------- #
MARGIN = 15
FONT_UI = 'Emilio 20'
DEEP_PINK = (255, 20, 147)
FONT_WATERMARK = ImageFont.truetype('fonts/Sacramento-Regular.ttf', 40)


# ------------------------------------------------------ FUNCTIONS --------------------------------------------------- #
def check_images(images):
    files = os.listdir('images')
    for image in images:
        if image not in files:
            messagebox.showerror(title="Image not found!", message="Some image isn't on the images folder.")
            return False
    return True


def make_watermark(image, watermark):
    img = Image.open(f'images/{image}')
    img_copy = img.copy()
    width, height = img_copy.size

    draw = ImageDraw.Draw(img_copy)
    text_width, text_height = draw.textsize(watermark, FONT_WATERMARK)

    # calculate the x,y coordinates of the text
    x = width - text_width - MARGIN
    y = height - text_height - MARGIN

    # draw watermark in the bottom right corner
    draw.text((x, y), watermark, DEEP_PINK, font=FONT_WATERMARK)
    img_copy.save(f'watermarks/{image}')


def watermark_images():
    images = images_text.get("1.0", END).split()
    watermark = watermark_entry.get()
    if check_images(images):
        for image in images:
            make_watermark(image, watermark)
        messagebox.showinfo(title='Watermarked',
                            message='All your images have been watermarked. Check watermarks folder to see them.')


# ------------------------------------------------------ UI SETUP ---------------------------------------------------- #
window = Tk()
window.title('💦 WaterMarker 💦')
window.config(padx=25, pady=25)

title_label = Label(window, text='WaterMarker', font=(FONT_UI, 30))
title_label.config(pady=20)
title_label.grid(column=0, row=0, columnspan=2)
images_label = Label(window, text='Images:', font=(FONT_UI, 12))
images_label.grid(column=0, row=1)

images_text = Text(window, width=20, height=10)
images_text.grid(column=1, row=1)

watermark_label = Label(window, text='Watermark:', font=(FONT_UI, 12))
watermark_label.grid(column=0, row=2)

watermark_entry = Entry(window)
watermark_entry.grid(column=1, row=2)

add_watermark = Button(window, width=23, text='Watermark', font=(FONT_UI, 14), command=watermark_images)
add_watermark.grid(column=0, row=3, columnspan=2)

window.mainloop()
