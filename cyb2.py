# PRODIGY_CS_02: Simple Image Encryption Tool

from PIL import Image

def swap_pixel_values(image):
    """
    Swaps the red and blue channels of an image.
    """
    r, g, b = image.split()
    return Image.merge("RGB", (b, g, r))

def apply_math_operation(image, operation="+", value=50):
    """
    Applies a basic mathematical operation to each pixel value.
    Default operation is addition with a value of 50.
    """
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if operation == "+":
                r = (r + value) % 256
                g = (g + value) % 256
                b = (b + value) % 256
            elif operation == "-":
                r = (r - value) % 256
                g = (g - value) % 256
                b = (b - value) % 256
            pixels[x, y] = (r, g, b)
    return image

def encrypt_image(input_path, output_path):
    """
    Encrypts an image by swapping pixel values and applying a mathematical operation.
    """
    try:
        original_image = Image.open(input_path)
        swapped_image = swap_pixel_values(original_image)
        encrypted_image = apply_math_operation(swapped_image, operation="+", value=50)
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path):
    """
    Decrypts an image by reversing the encryption process.
    """
    try:
        encrypted_image = Image.open(input_path)
        decrypted_image = apply_math_operation(encrypted_image, operation="-", value=50)
        original_image = swap_pixel_values(decrypted_image)
        original_image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = "example_image.png"
    encrypted_output_path = "encrypted_image.png"
    decrypted_output_path = "decrypted_image.png"

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_output_path)

    # Decrypt the image
    decrypt_image(encrypted_output_path, decrypted_output_path)
