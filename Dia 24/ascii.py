from PIL import Image
import sys

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width * 0.55)  
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def main():
    if len(sys.argv) < 2:
        print("Uso: python ascii_art.py imagen.jpg")
        return

    path = sys.argv[1]

    try:
        image = Image.open(path)
    except:
        print("No se pudo abrir la imagen.")
        return

    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)

    ascii_art = "\n".join(
        ascii_str[i:i+image.width] for i in range(0, len(ascii_str), image.width)
    )

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ascii_art)

    print("✔ Arte ASCII generado en output.txt")

if __name__ == "__main__":
    main()
