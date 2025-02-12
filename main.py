import select
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,  # Диалог открытия файлов (и папок)
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout, QMessageBox, QInputDialog
)
from PyQt5.QtCore import Qt  # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap, QImage
import os
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from PIL import ImageFilter
from PIL.ImageFilter import *
from account import *
from qss import *
import io
import json

app = QApplication([])
win = QWidget()
win.resize(700, 700)
win.setWindowTitle("Photo Redactor")
win.setStyleSheet(QSS1)
win.setStyleSheet('''background-color: rgb(238, 187, 136);''')
list = QListWidget()
list.setStyleSheet('''background-color: rgb(186, 85, 54);''')
list_btns = QListWidget()
im_label = QLabel('Image🖼 (Click buttons, when you choice a photo)')
system_btn = QPushButton('Files📂')
system_btn.setStyleSheet('''color: white;
	background-color: rgb(186, 85, 54);
	border-radius: 10px;
	width: 200 px; height: 30;''')
contrast_btn = QPushButton('Contrast')
contrast_btn.setStyleSheet('''color: white;
	background-color: rgb(15, 255, 27);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
mirror_btn = QPushButton("Mirror")
mirror_btn.setStyleSheet('''color: white;
	background-color: rgb(135, 135, 135);;
	border-radius: 10px;
	width: 110 px; height: 25px;''')
left_btn = QPushButton('Left')
left_btn.setStyleSheet('''color: white;
	background-color: rgb(141, 35, 15);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
right_btn = QPushButton('Right')
right_btn.setStyleSheet('''color: white;
	background-color: rgb(246, 71, 71);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
blur_btn = QPushButton('Blur')
blur_btn.setStyleSheet('''color: white;
	background-color: rgb(127, 75, 75);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
wh_bl_btn = QPushButton("B/W")
wh_bl_btn.setStyleSheet('''
	color: white;
	background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.995, y2:1, stop:0 rgba(218, 218, 218, 255), stop:0.305419 rgba(0, 7, 11, 255), stop:0.935961 rgba(2, 11, 18, 255), stop:1 rgba(240, 240, 240, 255));
	border: 1px solid black;
	border-radius: 10px;
	width: 110 px; height: 25px;;''')
smooth_btn = QPushButton("Smooth")
smooth_btn.setStyleSheet('''color: white;
	background-color: rgb(110, 103, 2);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
add_text_btn = QPushButton("Add text")
add_text_btn.setStyleSheet('''color: white;
	background-color: rgb(58, 134, 255);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
imgs_btn = QPushButton("2 images")
imgs_btn.setStyleSheet('''color: white;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 190, 11, 255), stop:1 rgba(251, 86, 7, 255));
	border-radius: 10px;
	width: 110 px; height: 25px;''')
inverse_btn = QPushButton("Inverse")
inverse_btn.setStyleSheet('''color: white;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 190, 11, 255), stop:1 rgba(251, 86, 7, 255));
	border-radius: 10px;
	width: 110 px; height: 25px;''')
#inverse_btn.setStyleSheet()
cut_btn = QPushButton("Cut✂")
cut_btn.setStyleSheet('''color: white;
	background-color: rgb(255, 165, 119);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
crop_btn = QPushButton("Crop")
crop_btn.setStyleSheet('''color: white;
	background-color: rgb(255, 165, 119);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
save_btn = QPushButton("Save image")
save_btn.setStyleSheet('''color: white;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));
	width: 100 px; height: 30;
	border-radius: 10px;''')
info_btn = QPushButton("Info")
info_btn.setStyleSheet('''color: white;
	background-color: rgb(251, 86, 7);
	border-radius: 10px;
	width: 110 px; height: 25px;''')
cancel_btn = QPushButton("Result")
cancel_btn.setStyleSheet('''background-color: rgb(230, 62, 62);
	color: white;
	border-radius: 10px;
	width: 110 px; height: 30px;''')
encane_btn = QPushButton('Encane')
encane_btn.setStyleSheet('''background-color: rgb(168, 104, 104);
	color: white;
	border-radius: 10px;
	width: 110 px; height: 25px;''')

v1 = QVBoxLayout()
v1.addWidget(system_btn)
v1.addWidget(list)
v2 = QVBoxLayout()
v2.addWidget(im_label)
h1 = QHBoxLayout()
h1.addWidget(wh_bl_btn)
h1.addWidget(inverse_btn)
h1.addWidget(contrast_btn)
h1.addWidget(smooth_btn)
h1.addWidget(encane_btn)
h1.addWidget(mirror_btn)
h1.addWidget(blur_btn)
h1.addWidget(left_btn)
h1.addWidget(right_btn)

h2 = QHBoxLayout()
h2.addWidget(wh_bl_btn)
h2.addWidget(cut_btn)
h2.addWidget(crop_btn)
h2.addWidget(add_text_btn)
h2.addWidget(imgs_btn)
h2.addWidget(info_btn)
h2.addWidget(cancel_btn)
h2.addWidget(save_btn)


v2.addLayout(h1)
v2.addLayout(h2)
main_layout = QHBoxLayout()
main_layout.addLayout(v1, 1)
main_layout.addLayout(v2, 5)
win.setLayout(main_layout)


def sucess():  #
    message = QMessageBox()
    message.setText("Operation succesful!")
    message.setIcon(QMessageBox.Information)
    message.exec()

def error():  #
    message = QMessageBox()
    message.setText("Error! Stop programm!")
    message.setIcon(QMessageBox.Warning)
    message.exec()

#  class
class Image_Process():
    def __init__(self):
        self.image = None
        self.dir = None  # ()
        self.filename = None
        self.save_dir = "ChangeFile"
        self.picture = []
        self.imageo = None

    def save_image(self, dir, filename):
        self.dir = dir  # ()
        self.filename = filename
        file_path = os.path.join(dir, filename)
        self.image = Image.open(file_path)
        self.picture.append(self.image)

    def show_image(self, file_path):
        im_label.hide()
        file_path = os.path.join(self.dir, self.filename)
        pix = QPixmap(file_path)
        w, h = im_label.width(), im_label.height()

        pix = pix.scaled(w, h, Qt.KeepAspectRatio)
        im_label.setPixmap(pix)

        im_label.show()

    def save_image1(self):
        self.workdir = QFileDialog.getExistingDirectory()
        try:
            # self.filename = filename
            path = os.path.join(self.workdir, self.filename)
            self.image.save(path)
            self.show_image(path)
            self.picture.append(self.image)
            sucess()
        except:
            error()

    def information(self):
        print("Image open")
        print("Size:", self.image.size)
        print("Format", self.image.format)
        print("Type:", self.image.mode)
        self.picture.append(self.image)

    def left(self):
        try:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.picture.append(self.image)
            self.save_image1()
            self.image.show()
        except:
            error()

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def b_w(self):
        self.image = self.image.convert("L")
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def inverse(self):
        try:
            r, g, b = self.image.split()
            self.image = Image.merge("RGB", (b, g, r))
            self.picture.append(self.image)
            self.save_image1()
            self.image.show()
        except:
            print("EROR")

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(1.5)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def cut(self):
        self.image.thumbnail((500, 600))
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def crop (self):
        self.image = self.image.crop((1,2,300,300))
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()
    def smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()
    def encane(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.picture.append(self.image)
        self.save_image1()
        self.image.show()

    def two_images(self):
        try:
            # Відкриваємо діалогове вікно для вибору файлу
            url2Img, _ = QFileDialog.getOpenFileName()
            if not url2Img:
                raise Exception("No file selected")
            image_size = self.image.size
            self.imageo = Image.open(url2Img)
            # Створюємо нове зображення з потрібними розмірами
            images = Image.new('RGB', (image_size[0] + self.imageo.size[0], image_size[1]), (250, 250, 250))
            images.paste(self.image, (0, 0))
            images.paste(self.imageo, (image_size[0], 0))
            self.image = images
            # Зберігаємо результат
            self.picture.append(self.image)
            self.save_image1()
            # Показуємо зображення
            self.image.show()
        except Exception as e:
            print(f"Error: {e}")


    def add_text(self):
        draw = ImageDraw.Draw(self.image)
        input_text, ok = QInputDialog.getText(win, 'Add text', 'Text:')
        if ok:
            try:
                font = ImageFont.truetype('arial.ttf', 36)

                width, height = self.image.size
                textbbox = draw.textbbox((0, 0), input_text, font=font)
                textwidth = textbbox[2] - textbbox[0]
                textheight = textbbox[3] - textbbox[1]

                # calculate the x,y coordinates of the text
                margin = 10
                x = width - textwidth - margin
                y = height - textheight - margin

                # draw watermark in the bottom right corner
                draw.text((x, y), input_text, font=font)
                self.image.show()
                self.picture.append(self.image)
                self.save_image1()
            except Exception as e:
                print(f"An error occurred: {e}")
                error()

    def pil_to_qpixmap(self, pil_image):
        # Convert the PIL image to a byte array
        byte_array = io.BytesIO()
        pil_image.save(byte_array, format='PNG')
        byte_array.seek(0)
        qimage = QImage()

        # Load QImage from the byte array
        qimage.loadFromData(byte_array.read())

        # Convert QImage to QPixmap
        qpixmap = QPixmap.fromImage(qimage)

        return qpixmap

    def cancel(self):
        if len(self.picture) > 0:
            self.image = self.picture[-1]
            pix = self.pil_to_qpixmap(self.image)
            w, h = im_label.width(), im_label.height()

            pix = pix.scaled(w, h, Qt.KeepAspectRatio)
            im_label.setPixmap(pix)
            self.picture.remove(self.picture[-1])
            cancel_btn.setText('Cancel')
        else:
            cancel_btn.setText('Result')


workdir = ""

workImage = Image_Process()


def showImageItem():
    if list.selectedItems():
        filename = list.currentItem().text()
        workImage.save_image(workdir, filename)
        workImage.show_image(os.path.join(workdir, filename))
        workImage.picture = []


def filter_images(filenames, extensions):
    result = []
    for name in filenames:
        for ext in extensions:
            if name.endswith(ext):
                result.append(name)
                break
    return result


def system_files():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    try:
        filenames = os.listdir(workdir)
        extensions = [".png", ".jpg", ".bmp", ".jpeg", ".gif", "AVIF"]
        filenames = filter_images(filenames, extensions)
        list.clear()
        list.addItems(filenames)
        sucess()
    except:
        error()

# JSON
users = {"admin":  "admin1"}
with open('accounts.json', 'r', encoding='UTF-8') as file:
    users = json.load(file)

def show_sign_up():
    win_account.close()
    win_sign_up.show()
    app2.exec_()

def sign_up():
    if field_login1.text() and field_password1.text() != "":
        if field_login1.text() != field_password1.text():
            if field_login1.text() not in users:
                with open('accounts.json', 'w', encoding='UTF-8') as file:
                    users[field_login1.text()] = field_password1.text()
                    json.dump(users, file, ensure_ascii=False)
                    sucess()
                    win_sign_up.close()
                    win.show()
                    app.exec_()
            else:
                print("This login is in program!")
        else:
            print("Login is NOT = password")
    else:
        print('Enter login and password!')

def sign_in():
    if field_login.text() != "":
        if field_password.text() != "":
            if field_login.text() != field_password.text():
                if field_login.text() in users:
                    if field_password.text() == users[field_login.text()]:
                        sucess()
                        win_account.close()
                        win.show()
                        app.exec_()
                    else:
                        print("Error... password")
                else:
                    print("Error... login")
            else:
                print("Login NOT = password")
    else:
        print('Enter login and password!')

sign_in_btn.clicked.connect(sign_in)
sign_up_btn.clicked.connect(show_sign_up)
sign_up_btn1.clicked.connect(sign_up)
system_btn.clicked.connect(system_files)
list.currentRowChanged.connect(showImageItem)
wh_bl_btn.clicked.connect(workImage.b_w)
save_btn.clicked.connect(workImage.save_image1)
smooth_btn.clicked.connect(workImage.smooth)
inverse_btn.clicked.connect(workImage.inverse)
contrast_btn.clicked.connect(workImage.contrast)
crop_btn.clicked.connect(workImage.crop)
cut_btn.clicked.connect(workImage.cut)
mirror_btn.clicked.connect(workImage.mirror)
blur_btn.clicked.connect(workImage.blur)
left_btn.clicked.connect(workImage.left)
right_btn.clicked.connect(workImage.right)
info_btn.clicked.connect(workImage.information)
encane_btn.clicked.connect(workImage.encane)
add_text_btn.clicked.connect(workImage.add_text)
imgs_btn.clicked.connect(workImage.two_images)
cancel_btn.clicked.connect(workImage.cancel)
win_account.show()
app1.exec_()