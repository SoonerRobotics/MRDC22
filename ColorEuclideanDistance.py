<<<<<<< HEAD
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

def euclideanDistance(array, color):
    distance = math.sqrt(
        math.pow((array[0] - color[0]), 2) +
        math.pow((array[1] - color[1]), 2) +
        math.pow((array[2] - color[2]), 2))


    return distance

def determineColor(array):
    # accepts RGB

    colorArray = array

    #colorArray = array[::-1]
    #print(colorArray)

    distanceColor = {}

    for color in colors:
        distanceColor[color] = euclideanDistance(colorArray, colors[color])

    sortedColor = sorted(distanceColor.items(), key = operator.itemgetter(1))

    color = sortedColor[0][0]

    if color == "red1" or color == "red2":
        color = "red"

    return color


def main():
    # 121, 19, 31 [red]
    # 136, 33, 24 [orange]
    # 129, 115, 10 [yellow]
    # 14, 74, 40 [green]
    # 24, 43, 119 [blue]
    # 68, 25, 70 [purple]

    global colors
    # BGR for opencv
    # colors = {
    #     "red" : (31, 19, 121),
    #     "orange" : (24, 33, 136),
    #     "yellow" : (10, 115, 129),
    #     "green" : (40, 74, 14),
    #     "blue" : (119, 43, 24),
    #     "purple" : (70, 25, 68)
    # }

    # HSV values for colors
    colors = {
        "red1" : (5, 255, 255),
        "orange" : (15, 255, 255),
        "yellow" : (30, 255, 255),
        "green" : (55, 255, 255),
        "blue" : (120, 255, 255),
        "purple" : (145, 255, 255),
        "red2" : (170, 255, 255)
    }

    videoFeed = cv2.VideoCapture(0)

    while True:

        _, video = videoFeed.read()
        smallVideo = video[200:375, 200:375]
        #hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

        # print(video.shape[:2])

        averageBGR = smallVideo.mean(axis=0).mean(axis=0)
        #averageHSV = hsv.mean(axis=0).mean(axis=0)

        #cv2.line(video, (200, 200), (375, 375), (255, 0, 0), 5)



        # pixels = np.float32(video.reshape(-1, 3))
        #
        # n_colors = 5
        # criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        # flags = cv2.KMEANS_RANDOM_CENTERS
        #
        # _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        # _, counts = np.unique(labels, return_counts=True)

        hsvConverted = BGRtoHSV(averageBGR)

        guessColor = determineColor(hsvConverted)

        cv2.putText(video, guessColor, (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)

        print("\nBGR: " + str(averageBGR) + " " + guessColor)
        #print("HSV: " + str(averageHSV))
        cv2.imshow("small test", smallVideo)
        cv2.imshow("test", video)

        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
=======
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

def euclideanDistance(array, color):
    distance = math.sqrt(
        math.pow((array[0] - color[0]), 2) +
        math.pow((array[1] - color[1]), 2) +
        math.pow((array[2] - color[2]), 2))


    return distance

def determineColor(array):
    # accepts RGB

    colorArray = array

    #colorArray = array[::-1]
    #print(colorArray)

    distanceColor = {}

    for color in colors:
        distanceColor[color] = euclideanDistance(colorArray, colors[color])

    sortedColor = sorted(distanceColor.items(), key = operator.itemgetter(1))

    color = sortedColor[0][0]

    if color == "red1" or color == "red2":
        color = "red"

    return color


def main():
    # 121, 19, 31 [red]
    # 136, 33, 24 [orange]
    # 129, 115, 10 [yellow]
    # 14, 74, 40 [green]
    # 24, 43, 119 [blue]
    # 68, 25, 70 [purple]

    global colors
    # BGR for opencv
    # colors = {
    #     "red" : (31, 19, 121),
    #     "orange" : (24, 33, 136),
    #     "yellow" : (10, 115, 129),
    #     "green" : (40, 74, 14),
    #     "blue" : (119, 43, 24),
    #     "purple" : (70, 25, 68)
    # }

    # HSV values for colors
    colors = {
        "red1" : (5, 255, 255),
        "orange" : (15, 255, 255),
        "yellow" : (30, 255, 255),
        "green" : (55, 255, 255),
        "blue" : (120, 255, 255),
        "purple" : (145, 255, 255),
        "red2" : (170, 255, 255)
    }

    videoFeed = cv2.VideoCapture(0)

    while True:

        _, video = videoFeed.read()
        smallVideo = video[200:375, 200:375]
        #hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

        # print(video.shape[:2])

        averageBGR = smallVideo.mean(axis=0).mean(axis=0)
        #averageHSV = hsv.mean(axis=0).mean(axis=0)

        #cv2.line(video, (200, 200), (375, 375), (255, 0, 0), 5)
        cv2.putText()


        # pixels = np.float32(video.reshape(-1, 3))
        #
        # n_colors = 5
        # criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        # flags = cv2.KMEANS_RANDOM_CENTERS
        #
        # _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        # _, counts = np.unique(labels, return_counts=True)

        hsvConverted = BGRtoHSV(averageBGR)

        guessColor = determineColor(hsvConverted)

        #cv2.putText(video, guessColor, (50,50), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), -1)

        print("\nBGR: " + str(averageBGR) + " " + guessColor)
        #print("HSV: " + str(averageHSV))
        cv2.imshow("small test", smallVideo)
        cv2.imshow("test", video)

        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
>>>>>>> 8f6dfd4064e317b295a94a03ad7928eeda6cec4d
     main()