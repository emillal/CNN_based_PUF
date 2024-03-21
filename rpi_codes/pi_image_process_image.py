import cv2
import os
import numpy as np

# Function to process the extracted frame
def process_frame(source_directory, destination_directory):
    # Desired dimensions for the processed image
    desired_width, desired_height = 100, 100  # Example dimensions

    # Read the image
    image_path = os.path.join(source_directory, "frame.jpg")
    image = cv2.imread(image_path)

    # Convert to HSV and create a mask for green color
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

    # Find contours and extract the LED region
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Assuming the largest contour is the LED
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        led_region = image[y:y+h, x:x+w]

        # Resize the LED region
        led_region_resized = cv2.resize(led_region, (desired_width, desired_height))

        # Save the processed image
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        destination_path = os.path.join(destination_directory, "processed_image.jpg")
        cv2.imwrite(destination_path, led_region_resized)

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

