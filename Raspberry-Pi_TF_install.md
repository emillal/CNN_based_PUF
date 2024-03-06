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

Run commmand ```sudo nano ~/.bashrc``` <br />
Add the following three lines to the botton of the .bashrc file:<br />
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
<br />
Save and close bashrc.<br />
Restart terminal with the command ```exec $SHELL``` <br />

Install extra packages:<br />
```
sudo apt-get install --yes libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libgdbm-dev lzma lzma-dev tcl-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev wget curl make build-essential openssl
```
<br />



