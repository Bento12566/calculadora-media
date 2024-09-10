from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

@app.route('/', methods=['GET', 'POST'])
def index():
    media = None
    if request.method == 'POST':
        entrada = request.form['numeros']
        numeros_str = entrada.split()
        try:
            numeros = [float(num) for num in numeros_str]
            media = calcular_media(numeros)
        except ValueError:
            media = "Por favor, insira apenas números válidos."
    return render_template('index.html', media=media)

if __name__ == "__main__":
    app.run(debug=True)
