a=0
y=0
b=0
d=0
f=0
m=0
c=0
x = input("введите номер задания:")

#7.1
def f1():
    from PIL import image
    c = "sobaken.jpg"
    with Image.open(c) as img:
        img.load()
    img.show()
    width, heigt = img.size
    f = img.format
    m = img.mode
    print("Ширина: ", width)
    print("Высота: ", heigt)
    print("Формат: ", f)
    print("Цветовая модель: ", m)
if x==1:
    f1()

#7.2
def f1():
    from PIL import image
    c = "sobaken.jpg"
    with Image.open(c) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_sobaken.jpg")
    c_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    c_img.save("img_flipsobaken_top.jpg")
    c_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    c_img.save("img_flipsobaken_left.jpg")
if x==2:
    f2()

#7.3
def f3():
    from PIL import image
    c = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in c:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(Image.Filter.CONTOUR)
            new_img.show()
            new_img.save("new_" + file)
if x==3:
    f3()

#7.4
def f4():
    import cv2
    image = cv2.imread('img.jpg')
    watermark = cv2.imread('watermark.jpg', cv2.IMREAD_UNCHANGED)

    (wH, wW) = watermark.shape[:2]
    weight = 1 - watermark[:, :, 3] / 255
    num1 = 1250
    num2 = 50

    image[num1:num1 + wH, num2:num2 + wW, 0] = np.multiply(image[num1:num1 + wH, num2:num2 + wW, 0], weight).astype(
        np.uint8)
    image[num1:num1 + wH, num2:num2 + wW, 1] = np.multiply(image[num1:num1 + wH, num2:num2 + wW, 1], weight).astype(
        np.uint8)
    image[num1:num1 + wH, num2:num2 + wW, 2] = np.multiply(image[num1:num1 + wH, num2:num2 + wW, 2], weight).astype(
        np.uint8)
    output = cv2.addWeighted(image[num1:num1 + wH, num2:num2 + wW], 1, watermark[:, :, 0:3], 1, 1)
    image[num1:num1 + wH, num2:num2 + wW] = output
    cv2.imwrite("watermark3.jpg", image)
if x==4:
    f4()
if x< 0 or x > 4:
    print("Такой задачи нет(")