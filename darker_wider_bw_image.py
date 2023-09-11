from PIL import Image, ImageEnhance

input_image_path = "bw_image.jpg"
output_image_path = "darker_wider_bw_image.jpg"

try:
    # Open the black and white image
    image = Image.open(input_image_path)
    
    # Adjust contrast to make it darker
    enhancer = ImageEnhance.Contrast(image)
    darkened_image = enhancer.enhance(0.5)  # Decrease contrast to darken
    
    # Resize the image to make it wider while keeping the same dimensions
    wider_bw_image = darkened_image.resize(image.size)
    
    # Save the darker and wider black and white image
    wider_bw_image.save(output_image_path)
    
    print(f"Darker and wider black and white image saved as {output_image_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
