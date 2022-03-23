import cv2
import rclpy
from flask import Flask, render_template, Response
from mrdc_msgs.msg import Motors

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)
lastpacket = {"left_motor": 0, "right_motor": 0}


def gen():
    while True:
        didRead, image = video_capture.read()
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        didEncode, encimg = cv2.imencode('.jpg', image, encode_param)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytes(encimg) + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/details')
def details():
    return {
        "left_motor": lastpacket["left_motor"],
        "right_motor": lastpacket["right_motor"]
    }


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def onSerialMessage(d: Motors):
    global lastpacket
    lastpacket = {
        "left_motor": d.left_motor,
        "right_motor": d.right_motor
    }


def main(args=None):
    app.run()

    rclpy.init(args=args)

    node = rclpy.create_node('mrdc_serial')
    node.create_subscription(
        Motors, '/mrdc/serial', lambda msg: onSerialMessage(msg), 20
    )

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
