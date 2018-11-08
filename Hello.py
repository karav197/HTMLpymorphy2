import flask
import pymorphy2

app = flask.Flask(__name__)
morph = pymorphy2.MorphAnalyzer()


@app.route('/')
def my_form():
    return flask.render_template('area.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = flask.request.form['text']
    return flask.render_template('area.html', text=count(normalized(text)))


def normalized(text):
    t = text.split()
    b = ""
    for word in t:
        p = morph.parse(word)[0]
        b = b + p.normal_form + " "
    return b


def count(normtext):
    t = normtext.split()
    d = dict()
    for word in t:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    c = ""
    for keys in d.keys():
        c += keys + " - " + str(d[keys]) + '\n'
    return c


if __name__ == '__main__':
    app.run()
