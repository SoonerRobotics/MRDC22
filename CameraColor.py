import cv2
import numpy as np
import imutils


def main():

    videoFeed = cv2.VideoCapture(0)

    #greenLower = (1, 33, 47)
    #greenUpper = (61, 179, 143)

    #greenLower = (42, 25, 8)
    #greenUpper = (101, 225, 214)

    greenLower = (33, 90, 56)
    greenUpper = (118, 255, 255)
    #greenUpper = (105, 206, 225)

    while True:
        _, video = videoFeed.read()
        hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

        #gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        #thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

        mask = cv2.inRange(hsv, np.array(greenLower, dtype = "uint8"), np.array(greenUpper, dtype = "uint8"))

        output = cv2.bitwise_and(hsv, hsv, mask=mask)
        grayNEW = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

        # detect circles in the image
        circles = cv2.HoughCircles(grayNEW, cv2.HOUGH_GRADIENT, 1.2, 100)

        cnts = cv2.findContours(grayNEW.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # ensure at least some circles were found
        #if circles is not None:
        #    # convert the (x, y) coordinates and radius of the circles to integers
        #    circles = np.round(circles[0, :]).astype("int")
        #    # loop over the (x, y) coordinates and radius of the circles
        #
        #    for (x, y, r) in circles:
        #        # draw the circle in the output image, then draw a rectangle
        #        # corresponding to the center of the circle
        #        cv2.circle(video, (x, y), r, (0, 255, 0), 4)
        #        cv2.rectangle(video, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid


            # SINGLE BALL

            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            try:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            except:
                center = (0, 0)

            # only proceed if the radius meets a minimum size
            if radius > 15:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(video, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(video, center, 5, (0, 0, 255), -1)

        cv2.imshow("gray", grayNEW)
        cv2.imshow("green detector", output)
        cv2.imshow("video", video)

        if cv2.waitKey(1) == ord('q'):
            break



if __name__ == "__main__":
    main()