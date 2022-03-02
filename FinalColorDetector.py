import math
import operator
import cv2
import numpy as np

#https://i.stack.imgur.com/gyuw4.png

def BGRtoHSV(bgrArray):
    (b, g, r) = bgrArray

    b = b / 255.0
    g = g / 255.0
    r = r / 255.0

    v = max([b, g, r])

    if v is 0:
        s = 0
    else:
        s = (v - min([b, g, r])) / v

    if v is r:
        h = 60.0 * (g - b) / (v - min([b, g, r]))
    elif v is g:
        h = 120 + 60.0 * (b - r) / (v - min([b, g, r]))
    elif v is b:
        h = 240 + 60.0 * (r - g) / (v - min([b, g, r]))

    if h < 0:
        h = h + 360

    v = np.round(255.0 * v).astype(int)
    s = np.round(255.0 * s).astype(int)
    h = np.round(h / 2.0).astype(int)

    return((h, s, v))


def determineColor(array):
    colorArray = array

    distanceColor = {}

    for color in colors:
        distanceColor[color] = abs(colorArray - colors[color])

    sortedColor = sorted(distanceColor.items(), key = operator.itemgetter(1))

    # sortedColor[0] gets first element of "color:value," in ascending order
    # sortedColor[0][0] gets color of first element
    color = sortedColor[0][0]

    if color == "red1" or color == "red2":
        color = "red"

    return color


def main():

    global colors

    # HSV values for colors (only using Hue)
    colors = {
        "red1" : 5,
        "orange" : 15,
        "yellow" : 30,
        "green" : 55,
        "blue" : 120,
        "purple" : 145,
        "red2" : 170
    }

    videoFeed = cv2.VideoCapture(0)

    while True:

        _, video = videoFeed.read()
        
        # only uses video feed from small portion of screen
        # can delete if we're using full camera feed
        smallVideo = video[200:375, 200:375]

        # average color of frame
        averageBGR = smallVideo.mean(axis=0).mean(axis=0)

        # converts BGR to HSV, gets Hue
        hsvConverted = BGRtoHSV(averageBGR)
        hue = hsvConverted[0]

        guessColor = determineColor(hue)

        cv2.putText(video, guessColor, (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)

        print("\nBGR: " + str(averageBGR) + " " + guessColor)

        cv2.imshow("small test", smallVideo)
        cv2.imshow("test", video)

        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
     main()
