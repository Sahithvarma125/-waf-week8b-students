from flask import Flask, render_template, request

app = Flask(__name__)
students = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        roll = request.form.get('roll', '').strip()
        name = request.form.get('name', '').strip()
        department = request.form.get('department', '').strip()
        if roll and name and department:
            students.append({'roll': roll, 'name': name, 'department': department})
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
