from flask import Flask, request, render_template
from flask_cors import cross_origin
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
import pandas as pd
import pyodbc


#connection to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-4RMDURAD;'
                      'Database=TourismManagement;'
                      'Trusted_Connection=yes;');

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/datareport", methods = ["GET", "POST"])
@cross_origin()
def data():
    option = request.form['exampleRadios']
    if option == 'option1':
        data = pd.read_sql("SELECT * FROM users", conn)
        result=data.to_html()
        sns.countplot(x='gender',data=data,palette="BuPu")
        plt.xlabel('gender')
        plt.ylabel('No of users')
        plt.savefig('static/gender.jpg') 
        result=append_html(result,['gender.jpg'])

        sns.countplot(x='address',data=data,palette="BuPu")
        plt.xlabel('address')
        plt.ylabel('No of users')
        plt.savefig('static/address.jpg')
        result=append_html(result,['address.jpg'])

    elif option == 'option2':
        data = pd.read_sql("SELECT * FROM locations", conn)
        result=data.to_html()
        sns.barplot(x='loc_name',y='loc_expense',data=data,palette="BuPu")
        plt.xlabel('loc_name')
        plt.ylabel('loc_expense')
        plt.title('Locations Name and Expense')
        plt.savefig('static/loc.jpg')
        result=append_html(result,['loc.jpg'])

    elif option == 'option3':
        data = pd.read_sql("SELECT * FROM hotels", conn)
        result=data.to_html()
        sns.barplot(x='htl_name',y='htl_rent',data=data,palette="BuPu")
        plt.xlabel('htl_name')
        plt.ylabel('htl_rent')
        plt.title('Hotel Name and Rent')
        plt.savefig('static/htl_rent.jpg')
        result=append_html(result,['htl_rent.jpg'])

    elif option == 'option4':
        data = pd.read_sql("SELECT * FROM package", conn)
        result=data.to_html()
        sns.barplot(x='pac_title',y='pac_ppl',data=data,palette="BuPu")
        plt.xlabel('pac_title')
        plt.ylabel('pac_ppl')
        plt.title('No. of people per package')
        plt.savefig('static/pac_ppl.jpg')
        result=append_html(result,['pac_ppl.jpg'])

        sns.barplot(x='pac_title',y='pac_days',data=data,palette="BuPu")
        plt.xlabel('pac_title')
        plt.ylabel('pac_days')
        plt.title('No. of days per package')
        plt.savefig('static/pac_days.jpg')
        result=append_html(result,['pac_days.jpg'])

        sns.barplot(x='pac_title',y='pac_cost',data=data,palette="BuPu")
        plt.xlabel('pac_title')
        plt.ylabel('pac_cost')
        plt.title('Cost per package')
        plt.savefig('static/pac_cost.jpg')
        result=append_html(result,['pac_cost.jpg'])

    return result



def append_html(result,image_names):
    for i in image_names:
        result=result+" <img src=\"static/"+i+"\" width=\"400\" height=\"300\">"
    return result


if __name__ == "__main__":
    app.run(debug=True)
