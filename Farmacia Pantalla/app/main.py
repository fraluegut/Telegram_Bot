import os
from json import dumps
from datetime import datetime, date
from flask import Flask, render_template, url_for, request
import gspread
import webbrowser

#url = https://docs.google.com/spreadsheets/d/1TOfdUNW5hLqS14wXHKMEfRtVFfjIh1p2s8UhtdmPhmc/edit#gid=0



gc = gspread.service_account(filename="/home/linuxpc/PycharmProjects/pythonProject/Farmacia Pantalla/app/static/test-2-323510-c9244d2915b2.json")
sh = gc.open_by_key("1TOfdUNW5hLqS14wXHKMEfRtVFfjIh1p2s8UhtdmPhmc")
worksheet = sh.sheet1


# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, static_folder="/home/linuxpc/PycharmProjects/pythonProject/Farmacia Pantalla/app/static")



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            option = request.form['stars']
            print(option)
            now = datetime.now()
            date=str(now.strftime("%d/%m/%Y"))

            time = str(now.strftime("%H:%M:%S"))
            registro = [date, time, option]
            worksheet.append_row(registro)
        except:
            print("Ya le han dado mal")
            pass


    else:
        print("Problema")
        pass

    return render_template("index.html")





webbrowser.open('http://0.0.0.0:5011/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
    datas = [('./resources/*.png', 'resources')],
