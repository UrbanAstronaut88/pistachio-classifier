from flask import Flask, render_template, request
from PIL import Image
from classifier import predict_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            image = Image.open(file)
            prediction, confidence = predict_image(image)

            return render_template(
                "result.html",
                prediction=prediction,
                confidence=confidence
            )

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
