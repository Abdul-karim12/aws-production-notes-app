from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)
        return redirect('/')

    return render_template_string('''
        <h1>My Notes App</h1>
        <form method="POST">
            <input name="note" placeholder="Write a note">
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for note in notes %}
                <li>{{ note }}</li>
            {% endfor %}
        </ul>
    ''', notes=notes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
