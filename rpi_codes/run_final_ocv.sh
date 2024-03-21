
#!/bin/bash

# Take a picture using fswebcam
fswebcam -d /dev/video0 -r 1920x1080 -S 30 -F 5 /home/pi/Desktop/opencv/image-dataset/frame.jpg

# Check if fswebcam command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to take a picture."
    exit 1
fi

# cd to opencv directory
cd /home/pi/Desktop/opencv/image-dataset/

# Run the Python script to process image with opencv
python pi_image_process_image.py

# Check if  execution was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to execute pi_image_process_image.py."
    exit 1
fi

cd /home/pi/Desktop/opencv/processed-image/


# Move frame.jpg to project directory
mv -f processed_image.jpg /home/pi/Desktop/project/

# Check if file is not moved
if [ $? -ne 0 ]; then
    echo "Error: Failed to move processed_image.jpg."
    exit 1
fi

# Change directory to Desktop/project
cd /home/pi/Desktop/project

# Activate the virtual environment
source env/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment."
    exit 1
fi

# Run the Python script run.py
python run.py

# Check if run.py execution was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to execute run.py."
    exit 1
fi

echo "All scripts executed successfully."
exit 0
