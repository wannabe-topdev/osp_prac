from flask import Flask, render_template, request
import sys

application = Flask(__name__)

@application.route("/")
def hello():
 return render_template("index.html")

@application.route("/list")
def view_list():
 return render_template("list.html")

@application.route("/review")
def view_review():
 return render_template("review.html")


@application.route("/reg_reviews")
def reg_review():
 return render_template("reg_reviews.html")

if __name__ == "__main__":
 application.run(host='0.0.0.0')

@application.route("/reg_items")
def reg_item_submit():
    name=request.args.get("name")
    seller=request.args.get("seller")
    addr=request.args.get("addr")
    email=request.args.get("email")
    category=request.args.get("category")
    card=request.args.get("card")
    status=request.args.get("status")
    phone=request.args.get("phone")
    print(name,seller,addr,email,category,card,status,phone)
    
    return render_template("reg_items.html")
    
    
@application.route("/submit_item_result", methods=['POST'])
def reg_item_submit_post():
    
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    
    return render_template("submit_item_result.html", data=data, img_path="static/image/{}".format(image_file.filename))

    
    
    


#return render_template("reg_item.html")
