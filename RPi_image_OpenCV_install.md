# Raspberry Pi OpenCV installation

## Steps to install Open CV to RPi 3B

1. For best practice create a seperate folder for OpenCV
2. I have intalled Python 3.9.2 locally in the folder. [Refer here](https://github.com/mrdunker/CNN_based_PUF/blob/main/Raspberry-Pi_TF_install.md)
3. Install OpenCV in same folder. Good to Go.

### Do the following commands to install opencv

1. Make Directory :
  ```
  cd Desktop/
  mkdir opencv
  cd opencv/
  ```
2. Install python locally :
Follow the [link](https://github.com/mrdunker/CNN_based_PUF/blob/main/Raspberry-Pi_TF_install.md).Instead of ```pyenv install 3.7.12``` do the following command.
```
pyenv install 3.9.2
```
3. Run following commands: 
```
sudo apt update
pip install --upgrade pip setuptools wheel
sudo apt-get install -y libhdf5-dev libhdf5-serial-dev python3-pyqt5 libatlas-base-dev libjasper-dev
```

4. Install OpenCV
```
pip install opencv-contrib-python==4.5.3.56
```
The Installation should be done very quick.<br />

![image](https://github.com/mrdunker/CNN_based_PUF/assets/38190245/5bd23db9-d913-4fe9-9a50-9a0e24b03cc0)

