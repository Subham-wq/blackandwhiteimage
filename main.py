from PIL import Image

# Open an image file
input_image_path = "image.jpg"
output_image_path = "output_image.jpg"

try:
    image = Image.open(input_image_path)

    # Convert the image to grayscale (black and white)
    bw_image = image.convert("L")

    # Save the black and white image
    bw_image.save(output_image_path)

    print(f"Image converted to black and white and saved as {output_image_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
