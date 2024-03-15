from PIL import Image
import os

# Function to process the extracted frame
def process_frame(source_directory, destination_directory):
    # Desired dimensions for the processed image
    desired_width, desired_height = 100, 100  # Example dimensions
    margin = 35  # Example margin

    # Read the image
    image_path = os.path.join(source_directory, "frame.jpg")
    image = Image.open(image_path)

    # Convert to grayscale
    grayscale_image = image.convert('L')

    # Create a mask for green color
    green_mask = grayscale_image.point(lambda x: 255 if 80 < x < 120 else 0)

    # Find bounding box of the LED region
    bbox = green_mask.getbbox()

    if bbox:
        # Expand the bounding box by margin
        bbox = (max(0, bbox[0] - margin),
                max(0, bbox[1] - margin),
                min(image.width, bbox[2] + margin),
                min(image.height, bbox[3] + margin))

        # Extract the LED region
        led_region = image.crop(bbox)

        # Resize the LED region
        led_region_resized = led_region.resize((desired_width, desired_height))

        # Save the processed image
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        destination_path = os.path.join(destination_directory, "processed_image.jpg")
        led_region_resized.save(destination_path)

    print("Image processing complete.")

# Main function
def main():
    destination_directory_frames = "image-dataset"
    destination_directory_process = "processed-image"

    # Process the extracted frame
    process_frame(destination_directory_frames, destination_directory_process)

# Entry point of the program
if __name__ == "__main__":
    main()

