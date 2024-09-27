from flask import Flask, render_template, request

app = Flask(__name__)


quiz_questions = [
    {'question': 'Apa itu perubahan iklim?', 'choices': ['Perubahan iklim adalah perubahan suhu rata-rata global.', 'Perubahan iklim adalah perubahan pada pola cuaca.', 'Perubahan iklim adalah perubahan pada iklim lokal.'], 'answer': 'Perubahan iklim adalah perubahan suhu rata-rata global.'},
    {'question': 'Seberapa serius masalah ini?', 'choices': ['Tidak serius', 'Cukup serius', 'Sangat serius'], 'answer': 'Sangat serius'},
    {'question': 'Apa yang memicu perubahan iklim?', 'choices': ['aktivitas manusia seperti pembakaran bahan bakar fosil.', 'pergerakan benua.', 'rotasi bumi.'], 'answer': 'aktivitas manusia seperti pembakaran bahan bakar fosil.'},
    {'question': 'Bagaimana kita dapat menghambat perubahan iklim?', 'choices': ['Mengurangi emisi karbon', 'Mengabaikan kebijakan lingkungan', 'Meningkatkan penggunaan bahan bakar fosil'], 'answer': 'Mengurangi emisi karbon'}
]

@app.route('/')  #page links to each sections
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    for question in quiz_questions:
        selected = request.form.get(question['question'])
        if selected == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(quiz_questions))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
