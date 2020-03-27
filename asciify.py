import numpy as np
import cv2
import sys

'''  
ascii level 참조
http://paulbourke.net/dataformats/asciiart/ 
'''
# 70단계의 회색값
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10단계의 회색값
gscale2 = '@%#*+=-:. '

def cam2ascii(cols, scale, level):
    global gscale1, gscale2

    vidcap = cv2.VideoCapture(0)
    if(vidcap.isOpened() == False):
        print('카메라 연결 안됨')
        sys.exit(1)
    else:
        size = [int(vidcap.get(3)), int(vidcap.get(4))]
    
    # filter의 width, height 계산
    w = size[0] / cols
    h = w / scale
    rows = int(size[1]/h)
    # cols = 특정 비율 출력을 원한다면 여기 코딩.
    # 80*24 기준 터미널창에 딱 맞게 출력하기 위해 cols는 계산하지 않음.

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
  
    # 이미지 크기가 너무 작으면 안됨.
    if cols > size[0] or rows > size[1]:
        print("너무 작은 이미지")
        exit(0)

    while True:
        ret, image = vidcap.read()
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ascii_image = ""
        for row in range(rows):
            y1 = int(row*h)
            y2 = int((row+1)*h)

            # 마지막 인덱스 처리
            if row == rows-1:
                y2 = size[1]
            
            for col in range(cols):
                x1 = int(col*w)
                x2 = int((col+1)*w)

                # 마지막 인덱스 처리
                if col == cols-1:
                    x2 = size[0]
                
                crop = image[y1:y2, x1:x2]
                avg = crop.mean()
                if level:
                    gsval = gscale1[int((avg*69)/255)]
                else:
                    gsval = gscale2[int((avg*9)/255)]
                
                ascii_image+=gsval
            ascii_image+='\n'
        print(ascii_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return ascii_image

def image2ascii(filename, cols, scale, level): 
    global gscale1, gscale2
  
    # 이미지 열어서 grayscale 형식으로 바꿈. 
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    try:
        size = [len(image[0]), len(image)]
    except:
        print('영상 정보 획득 실패')
        sys.exit(1)

    print("input image dims: %d x %d" % (size[0], size[1])) 
  
    # filter의 width, height 계산
    w = size[0] / cols 
    h = w / scale 
    rows = int(size[1] / h)
      
    print("cols: %d, rows: %d" % (cols, rows)) 
    print("tile dims: %d x %d" % (w, h)) 
  
    # 이미지 크기가 너무 작으면 안됨.
    if cols > size[0] or rows > size[1]:
        print("너무 작은 이미지")
        exit(0)
  
    ascii_image = ""
    for row in range(rows):
        y1 = int(row*h)
        y2 = int((row+1)*h)

        # 마지막 인덱스 처리
        if row == rows-1:
            y2 = size[1]
        
        for col in range(cols):
            x1 = int(col*w)
            x2 = int((col+1)*w)

            # 마지막 인덱스 처리
            if col == cols-1:
                x2 = size[0]
            
            crop = image[y1:y2, x1:x2]
            avg = crop.mean()
            if level:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            
            ascii_image+=gsval
        ascii_image+='\n'
    print(ascii_image)
    return ascii_image


def video2ascii(filename, cols, scale, level): 
    global gscale1, gscale2
  
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    # 이미지 크기 확인
    if success:
        size = [len(image[0]), len(image)]
    else:
        print('영상 정보 획득 실패')
        sys.exit(1)

    # filter의 width, height 계산
    w = size[0] / cols
    h = w / scale
    rows = int(size[1]/h)
    # cols = 특정 비율 출력을 원한다면 여기 코딩.
    # 80*24 기준 터미널창에 딱 맞게 출력하기 위해 cols는 계산하지 않음.

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
  
    # 이미지 크기가 너무 작으면 안됨.
    if cols > size[0] or rows > size[1]:
        print("너무 작은 이미지")
        exit(0)

    while success:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ascii_image = ""
        for row in range(rows):
            y1 = int(row*h)
            y2 = int((row+1)*h)

            # 마지막 인덱스 처리
            if row == rows-1:
                y2 = size[1]
            
            for col in range(cols):
                x1 = int(col*w)
                x2 = int((col+1)*w)

                # 마지막 인덱스 처리
                if col == cols-1:
                    x2 = size[0]
                
                crop = image[y1:y2, x1:x2]
                avg = crop.mean()
                if level:
                    gsval = gscale1[int((avg*69)/255)]
                else:
                    gsval = gscale2[int((avg*9)/255)]
                
                ascii_image+=gsval
            ascii_image+='\n'
        print(ascii_image)
        success, image = vidcap.read()

    return ascii_image    
