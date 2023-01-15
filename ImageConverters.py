from PIL import ImageTk, Image
import os


def ICSayoriTurned(image, strings):
    characterString = strings[-1]
    r = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_{strings[0].get()}.png").resize((480, 480))
    l = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_{strings[1].get()}.png").resize((480, 480))
    head = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_{strings[2].get()}.png").resize(
        (480, 480))
    mouth = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_mouth_{strings[3].get()}.png").resize(
        (480, 480))
    nose = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_nose_{strings[4].get()}.png").resize(
        (480, 480))
    eyes = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_eyes_{strings[5].get()}.png").resize(
        (480, 480))
    eyebrows = Image.open(
        os.getcwd() + f"/assets/{characterString.get().lower()}/sayori_turned_eyebrows_{strings[6].get()}.png").resize(
        (480, 480))
    imager = ImageTk.getimage(image)
    imager.paste(im=l, box=(0, 0), mask=l)
    imager.paste(im=r, box=(0, 0), mask=r)
    imager.paste(im=head, box=(0, 0), mask=head)
    imager.paste(im=mouth, box=(0, 0), mask=mouth)
    imager.paste(im=nose, box=(0, 0), mask=nose)
    imager.paste(im=eyes, box=(0, 0), mask=eyes)
    imager.paste(im=eyebrows, box=(0, 0), mask=eyebrows)
    return imager
