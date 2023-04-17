from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def square_root():
    n = int(request.args.get('n'))
    return f"squre root is equal to: {n**0.5}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
