import numpy as np
import cv2
import sys

def scaling(image, size, cols, scale, level):
    '''  
    ascii level 참조
    http://paulbourke.net/dataformats/asciiart/ 
    '''
    # 회색이미지 레벨 (70 단계)
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # 회색이미지 레벨 (10 단계)
    gscale2 = '@%#*+=-:. '
    
    # filter의 width, height 계산
    w = size[0] / cols
    h = w / scale
    rows = int(size[1]/h)
    # cols = 특정 비율 출력을 원한다면 여기 코딩.
    # 80*24 기준 터미널창에 딱 맞게 출력하기 위해 cols는 계산하지 않음.

    ''' 이미지 정보 출력필요할경우 코멘트 해제
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
    '''
    # 이미지 크기가 너무 작으면 안됨.
    if cols > size[0] or rows > size[1]:
        print("너무 작은 이미지")
        exit(0)

    ascii_image = ''
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
    return ascii_image

def cam2ascii(cols, scale, level):
    vidcap = cv2.VideoCapture(0)
    if(vidcap.isOpened() == False):
        print('카메라 연결 안됨')
        sys.exit(1)
    else:
        size = [int(vidcap.get(3)), int(vidcap.get(4))]

    while True:
        ret, image = vidcap.read()
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ascii_image = scaling(image, size, cols, scale, level)
        print(ascii_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return ascii_image

def image2ascii(filename, cols, scale, level): 
    # 이미지 열어서 grayscale 형식으로 바꿈. 
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    try:
        size = [len(image[0]), len(image)]
    except:
        print('영상 정보 획득 실패')
        sys.exit(1)

    ascii_image = scaling(image, size, cols, scale, level)
    print(ascii_image)
    return ascii_image

def video2ascii(filename, cols, scale, level): 
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    # 이미지 크기 확인
    if success:
        size = [len(image[0]), len(image)]
    else:
        print('영상 정보 획득 실패')
        sys.exit(1)

    while success:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ascii_image = scaling(image, size, cols, scale, level)
        print(ascii_image)
        success, image = vidcap.read()

    return ascii_image    
