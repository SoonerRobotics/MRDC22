import cv2
import numpy as np
import imutils

def detect(camera, colorName):
    colorArray = colors[colorName]

    lower = colorArray[0]
    upper = colorArray[1]

    while True:
        _, video = camera.read()

        blurred = cv2.GaussianBlur(video, (11, 11), 0)

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # video -> blurred

        mask = cv2.inRange(hsv, np.array(lower, dtype = "uint8"), np.array(upper, dtype = "uint8"))

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        output = cv2.bitwise_and(hsv, hsv, mask=mask)

        #grayNEW = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)


        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid

            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            # calculates moment
            try:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            except:
                center = (0, 0)

            # only proceed if the radius meets a minimum size
            if radius > 15: # and radius < 100 [for max radius allowed]

                # draw the circle and centroid on the frame
                cv2.circle(video, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(video, center, 5, (0, 0, 255), -1)

        # inserts name of color on video
        cv2.putText(video, colorName, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        #cv2.imshow("gray", grayNEW)
        cv2.imshow("color", output)
        cv2.imshow("video", video)

        # q to skip to next color
        if cv2.waitKey(1) == ord('q'):
            break

def main():
    # allows file-wide usage of colors dictionary
    global colors
    colors = {
        "blue" : [(81, 46, 81), (125, 255, 255)],
        "green" : [(42, 47, 81), (81, 255, 255)],
        "yellow" : [(21, 88, 137), (36, 255, 255)],
        "purple" : [(120, 88, 116), (171, 255, 255)],
        "orange" : [(11, 84, 185), (21, 255, 255)],
        "red" : [(0, 77, 162), (5, 255, 255)]
    }

    video = cv2.VideoCapture(0)

    #cv2.namedWindow('gray')
    cv2.namedWindow('color')
    cv2.namedWindow('video')

    while True:
        for colorName in colors.keys():
            detect(video, colorName)


if __name__ == "__main__":
    main()