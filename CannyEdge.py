import cv2
import numpy as np
import imutils

# detect circles in the image
# circles = cv2.HoughCircles(grayNEW, cv2.HOUGH_GRADIENT, 1.2, 100)


def main():

    video = cv2.imread("green2.jpg")
    video = imutils.resize(video, width = 600)

    greenLower = (33, 90, 56)
    greenUpper = (118, 255, 255)

    while True:
        #_, video = videoFeed.read()
        hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, np.array(greenLower, dtype = "uint8"), np.array(greenUpper, dtype = "uint8"))

        output = cv2.bitwise_and(hsv, hsv, mask=mask)
        grayNEW = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

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

            print(len(cnts))

            # for greenAreas in cnts:
            #     (x, y, w, h) = cv2.boundingRect(greenAreas)
            #
            #
            #     cv2.rectangle(video, (x,y), (x+w, y+h), (0, 0 ,255), -1)

                # circles = cv2.HoughCircles(subFrame, cv2.HOUGH_GRADIENT, 1.2, 100)
                #
                # if (len(circles) == 1):
                #     ((xCircle, yCircle), radius) = cv2.minEnclosingCircle(greenAreas)
                #     M = cv2.moments(greenAreas)
                #
                #     try:
                #         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                #     except:
                #         center = (0, 0)
                #
                #     # only proceed if the radius meets a minimum size
                #     if radius > 15:
                #         # draw the circle and centroid on the frame,
                #         # then update the list of tracked points
                #         cv2.circle(video, (x + int(xCircle), y + int(yCircle)), int(radius),
                #                        (0, 255, 255), 2)
                #         cv2.circle(video, center, 5, (0, 0, 255), -1)
                #
                # else:
                #     continue


        cv2.imshow("gray", grayNEW)
        cv2.imshow("green detector", output)
        cv2.imshow("video", video)

        if cv2.waitKey(1) == ord('q'):
            break



if __name__ == "__main__":
    main()