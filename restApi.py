from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello, world"
@app.route('/armstrong/<int:num>')
def armstrogFind(num):
    length = len(str(num))
    copy = num
    newNum = 0
    for i in range(length):
        single_num = num%10 
        newNum += single_num**length
        # num = int(num/10) # or use num = num//10
        num = num//10
    if newNum == copy:
        result = {
            'Number' : copy,
            'Armstrong' : True,
            'Server' : "192.168.1.1" 
        }
    else:
        result = {
            'Number' : copy,
            'Armstrong' : False,
            'Server' : "192.168.1.1" 
        }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug = True)