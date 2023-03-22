import re
from flask import Flask, request, render_template

app = Flask(__name__)


def find_pattern(str_, pattern):
    print(f"Given String: {str_}")
    print(f"Given String: {pattern}")
    count = 0
    final_list = []
    for s in str_:
        final = re.findall(pattern, s)
        final = ''.join(final)
        if len(final) == 0:
            continue
        else:
            count += 1
            # print(count, ": ", final.strip())
            final_list.append(final.strip())
            # print(final_list)
            # print(f"Matches : {count}")
    print(f"count: {count}")
    return count


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        str_ = request.form.get('text1')
        pattern = request.form.get('text2')
        result = find_pattern(str_, pattern)
    return render_template("home.html", result=[str_, pattern, result])


if __name__ == "__main__":
    app.run(debug=True)
