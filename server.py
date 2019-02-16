import urllib

from openalpr import Alpr
from flask import Flask, jsonify, request

alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
alpr.set_top_n(20)

app = Flask(__name__)

@app.errorhandler(400)
def invalid_params(error):
    return jsonify(error=400, text=str(error)), 400

@app.route('/v2/identify/plate', methods = ['GET'])
def get_v2_identify_plate():
    image_url = request.args.get('image_url')

    if not image_url:
        return invalid_params('Image URL was not provided')

    url_response = urllib.urlopen(image_url)
    jpeg_bytes = url_response.read()

    if len(jpeg_bytes) <= 0:
        return invalid_params('Image is empty')

    results = alpr.recognize_array(jpeg_bytes)
    return jsonify(results)

@app.route('/v2/identify/plate', methods = ['POST'])
def post_v2_identify_plate():
    if 'image' not in request.files:
        return invalid_params('Image parameter not provided')

    jpeg_bytes = request.files['image'].read()

    if len(jpeg_bytes) <= 0:
        return invalid_params('Image is empty')

    results = alpr.recognize_array(jpeg_bytes)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
