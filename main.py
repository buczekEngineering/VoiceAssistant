from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def health():
    return render_template("index.html")

@app.route("/test-speech-recognition", methods=["POST"])
def test_speech_recgnition():
    text = request.form.get('text')
    # start the transcription server
    result = ""

    return render_template("transcription_result.html", result=result,)




if __name__ =="__main__":
    app.run(debug=True, port=5000)