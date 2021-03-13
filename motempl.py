#!/usr/bin/env python
import numpy as np
import cv2 as cv

MHI_DURATION = 0.5
DEFAULT_THRESHOLD = 32
MAX_TIME_DELTA = 0.1
MIN_TIME_DELTA = 0.05
SWIPE_THRESH = 7


# (empty) trackbar callback
def nothing(dummy):
    pass

def draw_motion_comp(vis, rect, angle, color):
    x, y, w, h = rect
    cv.rectangle(vis, (x, y), (x+w, y+h), (0, 255, 0))
    r = min(w//2, h//2)
    cx, cy = x+w//2, y+h//2
    angle = angle*np.pi/180
    cv.circle(vis, (cx, cy), r, color, 3)
    cv.circle(vis, (cx, cy), 3, (0, 255, 0), 3)
    cv.line(vis, (cx, cy), (int(cx+np.cos(angle)*r), int(cy+np.sin(angle)*r)), color, 3)

if __name__ == '__main__':
    import sys
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    cv.namedWindow('motempl')
    visuals = ['input', 'frame_diff', 'motion_hist', 'grad_orient']
    cv.createTrackbar('visual', 'motempl', 2, len(visuals)-1, nothing)
    cv.createTrackbar('threshold', 'motempl', DEFAULT_THRESHOLD, 255, nothing)

    cam = cv.VideoCapture(video_src)
    if not cam.isOpened():
        print("could not open video_src " + str(video_src) + " !\n")
        sys.exit(1)
    ret, frame = cam.read()
    if ret == False:
        print("could not read from " + str(video_src) + " !\n")
        sys.exit(1)
    h, w = frame.shape[:2]
    prev_frame = frame.copy()
    motion_history = np.zeros((h, w), np.float32)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[:,:,1] = 255

    left = 0
    right = 0
    up = 0
    down = 0

    while True:
        ret, frame = cam.read()
        if ret == False:
            break
        frame_diff = cv.absdiff(frame, prev_frame)
        gray_diff = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)
        thrs = cv.getTrackbarPos('threshold', 'motempl')
        ret, motion_mask = cv.threshold(gray_diff, thrs, 1, cv.THRESH_BINARY)
        timestamp = cv.getTickCount() / cv.getTickFrequency()
        cv.motempl.updateMotionHistory(motion_mask, motion_history, timestamp, MHI_DURATION)
        mg_mask, mg_orient = cv.motempl.calcMotionGradient( motion_history, MAX_TIME_DELTA, MIN_TIME_DELTA, apertureSize=5 )
        seg_mask, seg_bounds = cv.motempl.segmentMotion(motion_history, timestamp, MAX_TIME_DELTA)

        visual_name = visuals[cv.getTrackbarPos('visual', 'motempl')]
        if visual_name == 'input':
            vis = frame.copy()
        elif visual_name == 'frame_diff':
            vis = frame_diff.copy()
        elif visual_name == 'motion_hist':
            vis = np.uint8(np.clip((motion_history-(timestamp-MHI_DURATION)) / MHI_DURATION, 0, 1)*255)
            vis = cv.cvtColor(vis, cv.COLOR_GRAY2BGR)
        elif visual_name == 'grad_orient':
            hsv[:,:,0] = mg_orient/2
            hsv[:,:,2] = mg_mask*255
            vis = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

        for i, rect in enumerate(list(seg_bounds)):
            x, y, rw, rh = rect
            area = rw*rh
            if area < 400**2:
                continue
            silh_roi   = motion_mask   [y:y+rh,x:x+rw]
            orient_roi = mg_orient     [y:y+rh,x:x+rw]
            mask_roi   = mg_mask       [y:y+rh,x:x+rw]
            mhi_roi    = motion_history[y:y+rh,x:x+rw]
            if cv.norm(silh_roi, cv.NORM_L1) < area*0.05:
                continue
            angle = cv.motempl.calcGlobalOrientation(orient_roi, mask_roi, mhi_roi, timestamp, MHI_DURATION)
            print(angle)
            if ((angle < 10.0) or (angle > 350.0)):
              right += 1
              left=up=down = 0
            elif ((angle < 190) and (angle > 170)):
              right=up=down = 0
              left += 1
            elif ((angle > 260) and (angle < 280)):
              down=left=right = 0
              up += 1
            elif ((angle > 80) and (angle < 100)):
              up=left=right = 0
              down += 1
            else:
              up=down=left=right = 0

            if right >= SWIPE_THRESH:
              print("Swipe RIGHT detected!")
              right = 0
            elif left >= SWIPE_THRESH:
              print("Swipe LEFT detected!")
              left = 0
            elif up >= SWIPE_THRESH:
              print("Swipe UP detected!")
              up = 0
            elif down >= SWIPE_THRESH:
              print("Swipe DOWN detected!")
              down = 0
            # color = ((255, 0, 0), (0, 0, 255))[i == 0]
            color = (255, 0, 0)
            draw_motion_comp(vis, rect, angle, color)
            break
        
        cv.putText(vis, visual_name, (20, 20), cv.FONT_HERSHEY_PLAIN, 1.0, (200,0,0))
        cv.imshow('motempl', vis)

        prev_frame = frame.copy()
        if 0xFF & cv.waitKey(5) == 27:
            break
    # cleanup the camera and close any open windows
    cam.release()
    cv.destroyAllWindows()