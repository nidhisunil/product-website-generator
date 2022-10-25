from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

import json
import time
import openai
import ipywidgets as widgets
import textwrap as tw
openai.api_key = "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"
import re

app = Flask(__name__)


#global variables
productID = ''
productName = ''
productTagline = ''
productParagraph = ''
productColour = ''
productSSColour = ''
websiteCode = ''



@app.route('/')
def hello():

    return render_template("index.html")

@app.route('/name')
def name():
    global productID
    prompt = f"make up a numbered list of 10 cool and trendy new brand names for selling {productID}."
    completion = openai.Completion.create(engine="text-davinci-002",max_tokens=256,prompt=prompt)
    result = completion.choices[0].text.strip()
    item_to_return = {'product_id': productID, 'numbered_product_names': result}

    return render_template("name.html",data=item_to_return)

@app.route('/tagline')
def tagline():
    global productID
    global productName
    prompt = f"make up a numbered list of 5 taglines for a brand called {productName}. It's a store that sells {productID}."
    completion = openai.Completion.create(engine="text-davinci-002",max_tokens=256,prompt=prompt)
    result = completion.choices[0].text.strip()
    item_to_return = {'product_id': productID, 'product_name': productName, 'numbered_product_taglines': result}
    return render_template("tagline.html",data=item_to_return)

@app.route('/paragraph')
def paragraph():
    global productID
    global productName
    global productTagline
    global productParagraph
    prompt = f"{productID} is a business that sells {productID}. Their tagline is {productTagline}. Write three paragraphs for the business explaining why they have the best {productID} and why you should buy from them."
    completion = openai.Completion.create(engine="text-davinci-002",max_tokens=256,prompt=prompt)
    result = completion.choices[0].text.strip()
    colour_prompt = f"{productName} is a company that sells {productID}. Give me a numbered list of 5 colours for its website:"
    completion2 = openai.Completion.create(engine="text-davinci-002",max_tokens=256,prompt=colour_prompt)
    colour_result = completion2.choices[0].text.strip()
    productParagraph = result
    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline':productTagline, 'product_paragraph': result, 'numbered_product_colours': colour_result}
    return render_template("paragraph.html",data=item_to_return)


@app.route('/secondarycolour')
def secondarycolour():
    global productID
    global productName
    global productTagline
    global productParagraph
    global productColour
    prompt = f"Give me a numbered list of 5 complimentary colours for {productColour}:"
    completion = openai.Completion.create(engine="text-davinci-002",max_tokens=256,prompt=prompt)
    result = completion.choices[0].text.strip()
    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline':productTagline, 'product_paragraph': productParagraph, 'product_colour':productColour,'numbered_product_seccolours': result}
    return render_template("secondarycolour.html",data=item_to_return)

@app.route('/final_template')
def final_template():
    global productID
    global productName
    global productTagline
    global productParagraph
    global productColour
    global productSSColour
    global websiteCode
    websiteCode = f'<!DOCTYPE html><html lang="en"> <head><link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUProduct Website GeneratorcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><script src =""></script> </head> <body> <div class="brand-name" style="background-color:{productColour};"> <h1>{productName}</h1> <h2>{productTagline}</h2 style="color:{productSSColour};"> </div> <div class="brand-paragraph" style="background-color:white;"> <p>{productParagraph}</p> </div> </body></html>'

    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline':productTagline, 'product_paragraph': productParagraph, 'product_colour':productColour,'product_sscolour': productSSColour, 'website-code': websiteCode}
    return render_template("final_template.html",data=item_to_return)

@app.route('/test_website')
def test_website():
    global productID
    global productName
    global productTagline
    global productParagraph
    global productColour
    global productSSColour
    global websiteCode

    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline':productTagline, 'product_paragraph': productParagraph, 'product_colour':productColour,'product_sscolour': productSSColour}
    return render_template("test_website.html",data=item_to_return)



@app.route('/save_product', methods=['GET', 'POST'])
def save_product():
    global productID
    json_data = request.get_json()
    productID = json_data["product_id"]
    item_to_return = {'product_id': productID}
    return jsonify(item_to_return)

@app.route('/save_productname', methods=['GET', 'POST'])
def save_productname():

    global productID
    global productName
    json_data = request.get_json()
    productName = json_data["product_name"]
    item_to_return = {'product_id': productID, 'product_name': productName}
    return jsonify(item_to_return)

@app.route('/save_producttagline', methods=['GET', 'POST'])
def save_producttagline():

    global productID
    global productName
    global productTagline
    json_data = request.get_json()
    productTagline = json_data["product_tagline"]
    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline': productTagline}
    return jsonify(item_to_return)

@app.route('/save_productcolour', methods=['GET', 'POST'])
def save_productcolour():

    global productID
    global productName
    global productTagline
    global productColour
    global productParagraph
    json_data = request.get_json()
    productColour = json_data["product_colour"]
    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline': productTagline, 'product_colour': productColour, 'product_paragraph': productParagraph}
    return jsonify(item_to_return)

@app.route('/save_productsscolour', methods=['GET', 'POST'])
def save_productsscolour():

    global productID
    global productName
    global productTagline
    global productColour
    global productParagraph
    global productSSColour
    json_data = request.get_json()
    productSSColour = json_data["product_sscolour"]
    item_to_return = {'product_id': productID, 'product_name': productName, 'product_tagline': productTagline, 'product_colour': productColour, 'product_paragraph': productParagraph, 'product_sscolour': productSSColour}
    return jsonify(item_to_return)
