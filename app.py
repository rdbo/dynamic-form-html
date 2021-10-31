from flask import Flask, render_template, redirect, url_for, request

app = Flask("test")

@app.route("/", methods=["GET", "POST"])
@app.route("/<largest_num>", methods=["GET", "POST"])
def index(largest_num=""):
	if request.method == "POST":
		numbers = request.form.getlist("numbers[]")
		if numbers is None:
			return redirect(url_for("index"))
		numbers = [int(i) for i in numbers]
		largest_idx = 0
		for i in range(1, len(numbers)):
			if numbers[i] > numbers[largest_idx]:
				largest_idx = i
		return redirect(url_for("index", largest_num=numbers[largest_idx]))
	return render_template("index.html", largest_num=largest_num)

if __name__ == "__main__":
	app.run("localhost", 1337)
