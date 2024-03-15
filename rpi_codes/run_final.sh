
#!/bin/bash

# Take a picture using fswebcam
fswebcam -d /dev/video0 -r 1920x1080 -S 30 -F 5 /home/pi/Desktop/project/image-dataset/frame.jpg

# Check if fswebcam command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to take a picture."
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

# Run the Python script new_process_pil.py
python new_process_pil.py

# Check if new_process_pil.py execution was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to execute new_process_pil.py."
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
