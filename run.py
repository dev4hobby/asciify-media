import argparse
import asciify

def main():
    # argv 파싱
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    
    # 파싱할 것들
    parser.add_argument('--file', dest='name', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='out', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='level',action='store_true')
  
    # 파싱한거 쓰는부분
    args = parser.parse_args()
    name = args.name
  
    # set output file
    out = 'out.txt'
    if args.out:
        out = args.out
  
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
  
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
  
    print('processing ...')
    # convert image to ascii txt
    ext = name.split('.')[-1]
    if ext in ['jpg','png','jpeg','bmp']:
        aimg = asciify.image2ascii(name, cols, scale, args.level)
        f = open(out, 'w')
        f.write(aimg)
        print("ASCII art written to %s" % out)
    elif ext in ['mp4', ]: # 원한다면 다른 확장자 추가 가능.
        _ = asciify.video2ascii(name, cols, scale, args.level)
    else:
        _ = asciify.cam2ascii(cols, scale, args.level)

# main 시작
if __name__ == '__main__':
    main()
