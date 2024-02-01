from flask import Flask,render_template,request, redirect, url_for
app=Flask(__name__)


@app.route('/')
def landingpage():
    return render_template('LandingPage.html')

@app.route('/Home')
def home():
    return render_template('Home.html')

@app.route("/AboutMe")
def About():
    return render_template('AboutMe.html')



@app.route("/Hobbies")
def hobbies():
    return render_template('Hobbies.html')

@app.route("/MoreAbout")
def moreabouteducation():
    return render_template('MoreAbout.html')


@app.route("/Skills")
def Myskills():
    return render_template('Skills.html')


@app.route("/Achievements")
def myachive():
    return render_template('Achievements.html')










# mongodb connection
from pymongo import MongoClient
#instance creation
client=MongoClient("mongodb://127.0.0.1:27017")
#Database Creation
db=client["studentss"]
#collection creation
ContactFormDetails= db.contact

#creating collection for feedback
FeedbackFormDetails= db.feedback
@app.route("/Contact")
def sample11():
    return render_template('Contact.html')


@app.route("/Contact", methods=('GET','POST'))
def sample12():
    YourName= request.form.get('name')
    Email  = request.form.get('e-mail')
    PhoneNumber= request.form.get('phone')
    message = request.form.get('message')
    a={"Your Name":YourName,"Your E-mail Address":Email,"Your Phone Number":PhoneNumber,"Your Message":message}
    ContactFormDetails.insert_one(a)
    return render_template('ContactThanku.html')




# @myweb.route('/Contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['e-mail']
#         phone = request.form['phone']
#         message = request.form['message']
#
#         # Store data in MongoDB
#         ContactFormDetails.insert_one({'name': name, 'email': email, 'phone': phone, 'message': message})
#
#         # Redirect to a thank you page or any other page
#
#
#     return render_template('Contact.html')






@app.route("/Feedback")
def feedback():
    return render_template('Feedback.html')

@app.route('/Feedback', methods=('GET','POST'))
def submit_feedback():
    Name=request.form.get('name')
    EMail=request.form.get('email')
    Feedback=request.form.get('message')
    b = {"Name": Name, "E-mail Address": EMail, "Your Message": Feedback}
    FeedbackFormDetails.insert_one(b)
    return render_template('FeedbackThanku.html')












if __name__ == "__main__":
    app.run()
