from flask import Flask,render_template,request
myweb=Flask(__name__)


@myweb.route('/')
def landingpage():
    return render_template('LandingPage.html')

@myweb.route('/Home')
def home():
    return render_template('Home.html')

@myweb.route("/AboutMe")
def About():
    return render_template('AboutMe.html')



@myweb.route("/Hobbies")
def hobbies():
    return render_template('Hobbies.html')

@myweb.route("/MoreAbout")
def moreabouteducation():
    return render_template('MoreAbout.html')


@myweb.route("/Skills")
def Myskills():
    return render_template('Skills.html')













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
@myweb.route("/Contact")
def sample11():
    return render_template('Contact.html')


@myweb.route("/successfull", methods=('GET','POST'))
def sample12():
    YourName= request.form.get('name')
    Email  = request.form.get('e-mail')
    PhoneNumber= request.form.get('phone')
    message = request.form.get('message')
    a={"Your Name":YourName,"Your E-mail Address":Email,"Your Phone Number":PhoneNumber,"Your Message":message}
    ContactFormDetails.insert_one(a)
    return render_template('ContactThanku.html')



@myweb.route("/Feedback")
def feedback():
    return render_template('Feedback.html')

@myweb.route('/Feedback', methods=('GET','POST'))
def submit_feedback():
    Name=request.form.get('name')
    EMail=request.form.get('email')
    Rate=request.form.get('rate')
    Feedback=request.form.get('feedback')
    b = {"Name": Name, "E-mail Address": EMail, "Rating": Rate, "Your Message": Feedback}
    FeedbackFormDetails.insert_one(b)
    return render_template('FeedbackThanku.html')












if __name__ == "__main__":
    myweb.run()
