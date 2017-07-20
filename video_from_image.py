import argparse
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os

def main():
    parser = argparse.ArgumentParser(description='Create driving video.')
    parser.add_argument(
        '--fps',
        type=int,
        default=60,
        help='FPS (Frames per second) setting for the video.')
    args = parser.parse_args()

    img_root = "/home/qtz/Downloads/packages/dataset/driving_data/IMG/"
    # Edit each frame's appearing time!
    fps = 5
    fourcc = VideoWriter_fourcc(*"XVID")    # fourcc = VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter("/home/qtz/Downloads/packages/dataset/driving_data/vedio/driving.avi", fourcc, fps=args.fps, frameSize=(320, 160))

    im_names = os.listdir(img_root)
    print(im_names)
    for im_name in range(len(im_names)):
        frame = cv2.imread(img_root + str(im_name) + '.jpg')
        print(im_name)
        videoWriter.write(frame)

    videoWriter.release()


if __name__ == '__main__':
    main()
