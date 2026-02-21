import traceback

from flask import Flask, render_template, request
from PIL import Image
from classifier import predict_image


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            file = request.files["file"]

            if file:
                image = Image.open(file)
                prediction, confidence = predict_image(image)

                return render_template(
                    "result.html",
                    prediction=prediction,
                    confidence=confidence
                )
        except Exception as e:
            print(f"! ERROR ! {e}")
            traceback.print_exc()
            return render_template(
                "result.html",
                prediction="Error occurred.",
                confidence=0
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
