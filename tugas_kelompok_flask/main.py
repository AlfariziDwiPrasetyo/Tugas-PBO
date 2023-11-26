from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/penghitungan", methods=['POST'])
def penghitungan():
    nama = request.form['name']
    tinggi = request.form['height']
    berat = request.form['weight']
    umur = request.form['age']
    gender = request.form['gender']
    aktivitas = request.form['activity']

    # penghitungan BMR
    if gender.lower() == 'male':
        bmr = 10 * float(berat) + 6.25 * float(tinggi) - 5 * float(umur) + 5
    elif gender.lower() == 'female':
        bmr = 10 * float(berat) + 6.25 * float(tinggi) - 5 * float(umur) - 161
    else:
        raise ValueError("Invalid value for 'gender'. Use 'male' or 'female'.")

    # penghitungan Kebutuhan Kalori
    if aktivitas.lower() == 'not-active':
        kalori = bmr * 1.2
    elif aktivitas.lower() == 'lightly-active':
        kalori = bmr * 1.375
    elif aktivitas.lower() == 'moderately-active':
        kalori = bmr * 1.55
    elif aktivitas.lower() == 'very-active':
        kalori = bmr * 1.725
    else:
        raise ValueError("Invalid value for 'activity'")

    return redirect(url_for("result", nama=nama, bmr=round(bmr, 2), kalori=round(kalori, 2)))


@app.route("/result/<nama>/<bmr>/<kalori>")
def result(nama, bmr, kalori):
    return render_template("result.html", nama=nama, bmr=bmr, kalori=kalori)


if __name__ == "__main__":
    app.run(debug=True)
