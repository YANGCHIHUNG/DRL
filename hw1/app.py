from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # 預設網格尺寸為 5
    n = 5
    if request.method == "POST":
        try:
            n = int(request.form.get("grid_size"))
            # 限制範圍在 5 至 9
            if n < 5 or n > 9:
                n = 5
        except (ValueError, TypeError):
            n = 5
    return render_template("index.html", n=n)

if __name__ == "__main__":
    app.run(debug=True)
