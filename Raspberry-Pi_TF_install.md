## Installation attempts of Tensorflow

### Attempt 1:

Material   : ```https://www.youtube.com/watch?v=9fEnvDgxwbI&t=1s``` <br />
VNC viewer : ```https://www.realvnc.com/en/connect/download/viewer/```
  1. Normal installation of Rasbian OS(32-bit) Legacey for Pi-3B with the installed done with imager v1.8.5.
  2. SSH done 
  3. VCN Remote Desktop

```
ping raspberrypi   //check if connection is proper
ssh pi@raspberrypi //ssh into pi remotely
sudo raspi-config  //set VCN
```
<br />
Direct installation deoes not work: https://github.com/samjabrahams/tensorflow-on-raspberry-pi
<br />
Approch as per : https://www.youtube.com/watch?v=QLZWQlg-Pk0&t=241s <br />

## Need to downgrade to Python 3.7.12

### Working with pyenv inside raspberry pi terminal

Download pyenv: ```curl https://pyenv.run | bash``` <br />

Run commmand : ```sudo nano ~/.bashrc``` <br />
Add the following three lines to the botton of the .bashrc file:<br />
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
<br />
Save and close bashrc<br />

Restart terminal with the command: ```exec $SHELL```
<br />

Install extra packages:<br />
```
sudo apt-get install --yes libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libgdbm-dev lzma lzma-dev tcl-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev wget curl make build-essential openssl
```
<br />

Update pyenv using command: ```pyenv update```
<br />
We can choose from the list of python versions availible. We are going to install 3.7.12 using :
```
pyenv install --list
pyenv install 3.7.12
```
<br />
<br />

Making this(pyenv) the local or global python:
```
pyenv local 3.7.12  // sets the python version a given particular folder(directory)
or
pyenv shell 3.7.12  // not reccomended to use
or
pyenv global 3.7.12 // sets this version as global
```
<br />

If we want to revert this action we can uninstall it.<br />
Run command: ```rm -fr ~/.pyenv```
<br />
Then remove lines from .bashrc (sudo nano ~/.bashrc). <br />
<br />
## Comming back to TensorFlow

To know Processor architecture ```uname -m```
<br />
To know Pi OS details ``` cat /etc/os-release```
<br />
<br />
Find proper tensorflow file from github : https://github.com/PINTO0309/Tensorflow-bin/tree/main/previous_versions
<br />
Based on Processor Architecture(armv7l) and Python version(3.7)
<br />
<br />
Make your project directory:
```
cd Desktop
mkdir project
cd project
```
<br />
Now, to make a virtual enviornment :

```
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate
```
(Recomended since package versioning matters in tools like TF)
<br />

Run below pacakge,These are system y packages plus some python packages:
```
sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev
```

Run the following also : ```pip install -U wheel mock six```

<br />
Find proper tensorflow file from github : https://github.com/PINTO0309/Tensorflow-bin/tree/main/previous_versions
<br />
<br />
We select "download_tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195.sh" <br />
Raw file link :
https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/main/previous_versions/download_tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195.sh
<br />
<br />

Run command :```wget 'the above url'```
<br />
Make the .sh as executable file with ```sudo chmod +x 'filename'```
<br />
Run the command to exceute : ```./'filename'```
<br />
Now a .whl file will be made in the directory.
<br />
If any pre-existing tensorflow exits, Uninstall :

```
sudo pip uninstall tensorflow
pip uninstall tensorflow
```
<br />


Install the .whl filein the directory.Install with the command below :
```
pip install  tensorflow-'version'.whl
```
### ***UPDATE: wget direct will not work

1. Remove the the existing tensorflow.whl file
2. Download manually from https://github.com/PINTO0309/Tensorflow-bin/blob/main/previous_versions/download_tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195.sh
3. Install Ninite WinSCP
4. Follow : https://www.youtube.com/watch?v=WIOpNuQc068
5. Transfer downloaded .whl file from PC to Raspberry Pi through WSCP (to the projects folder)
6. now do ``` pip install  tensorflow-'version'.whl```

Now, Tensorflow should be installed.<br />
Restart the shell ```exec $SHELL```
<br />
Run command:
```
cd Desktop
cd project
source env/bin/activate
python
  >>>import tensorflow
  >>>tensorflow.__version__
```

<br />
It's installed.

![image](https://github.com/mrdunker/CNN_based_PUF/assets/38190245/abbae9e1-6ff7-4fd6-ab8d-b6a2f6a32df3)

<br />
To fix the 'HDF5' warning:

```
pip uninstall h5py
HDF5_VERSION=1.10.6 pip install --no-binary=h5py h5py==3.1.0 // might not work
```

Reference: https://docs.h5py.org/en/stable/build... 
<br />


