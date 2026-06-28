print("A")
from flask import Flask, request, render_template

print("B")
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

print("C")

application = Flask(__name__)
app = application

print("D")

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

print("E")

# Prediction Route
@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():

    print("F - Entered predict_datapoint")

    if request.method == "GET":
        print("G - GET Request")
        return render_template("home.html")

    else:
        print("H - POST Request")

        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score"))
        )

        print("I - CustomData Created")

        pred_df = data.get_data_As_data_frame()

        print("J - DataFrame Created")
        print(pred_df)

        predict_pipeline = PredictPipeline()

        print("K - PredictPipeline Created")

        results = predict_pipeline.predict(pred_df)

        print("L - Prediction Completed")

        return render_template(
            "home.html",
            results=results[0]
        )

print("M")

if __name__ == "__main__":
    print("N - Starting Flask")

    app.run(
    host="127.0.0.1",
    port=8000,
    debug=False
)

    print("O - Flask Stopped")