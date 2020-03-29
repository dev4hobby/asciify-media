# 'ASCII'fy media

![test_drive](./test_drive.gif)  

---

## Requirement

- Python 3.6 or high
- PIP packages
  - opencv-python==4.2.0.32
  - numpy==1.18.2

## How to run

### Quick start

#### image -> ascii image
`python3 run.py --file $ImageFile`

#### video -> ascii streaming
`python3 run.py --file $VideoFile`

#### webcam or whatever someting to streaming as ascii
`python3 run.py --file webcam`

### with Options

- `--file` : file name (*.jpg, *.png, *.mp4 or webcam)
- `--scale` : default scale is `0.34`
- `--out` : output file name (support only image i/o)
- `--cols` : recommend `80`. it's default and fit with terminal cols
- `--morelevels` : support 2 mode (True or False)
  - `True` : your source will be displayed as a grayscale image with 70 levels
  - `False` : your source will be displayed as a grayscale image with 10 levels

#### example
- `python3 run.py --file test.jpg --cols 120 --out result`  
- `python3 run.py --file test.mp4 --scale 0.8 --cols 150`
- `python3 run.py --file webcam --cols 120`

# Have fun
New contributions are always welcome. feel free to PR  
