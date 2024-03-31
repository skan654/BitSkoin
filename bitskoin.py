#Import necessary libraries
from tkinter import *
from time import strftime
from pandas import Series, DataFrame
from PIL import ImageTk, Image
from flask import Flask, jsonify

import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
import pandas as pd
import random
import json
import hashlib
import requests
import csv
import PIL.Image

#creér une fenetre
window = Tk() 
mainmenu = Menu(window)
window.config(menu=mainmenu)

#personnaliser la fenetre 
window.title("BitSkoin")

#taille de la fenetre
window.geometry("1080x720")
window.minsize(480,360)

window.configure(borderwidth="1")
window.configure(relief="sunken")
window.configure(cursor="arrow")

window.grid_columnconfigure((0,1), weight=1)

#couleur du background de la fenetre 
window.config(background='#DCDCDC')

#Create frame for logo's position
frame = Frame(window, width=50, height=50)
frame.pack()
frame.place(anchor='n', relx=0.5)

# Create an object of tkinter ImageTk
img= PIL.Image.open("/Users/emansarahafi/Downloads/bitskoin.png")

#Resize the Image using resize method
resized_image= img.resize((200,200), PIL.Image.Resampling.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

# Create a Label Widget to display the text or Image
label = Label(frame, image = new_image)
label.pack()

#Add the window's icon 
window.iconbitmap("/Users/emansarahafi/Downloads/bitskoin.ico")

# Create Label to display the Date
w = Label(window, text=f"{dt.datetime.now():%a, %b %d %Y}", foreground="black", background='#DCDCDC', font=("helvetica", 14))
w.place(relx = 0.0,rely = 0.0, anchor ='nw')

def time():
    string = strftime('%H:%M:%S %p')
    lblo.config(text = string)
    lblo.after(1000, time)
    
lblo = Label(window,foreground="black",background='#DCDCDC', font=("helvetica", 14))
lblo.place(relx = 1.0,rely = 0.0, anchor ='ne')
time()

#labels and entries for inputs

Label0 = Label(window, text="Network: ")
Label0.configure(background='#DCDCDC')
Label0.place(anchor='n', relx=0.30, rely=0.25)

Label1 = Label(window, text="Address: ")
Label1.configure(background='#DCDCDC')
Label1.place(anchor='n', relx=0.30, rely=0.30)

Label2 = Label(window, text="r_transaction: ")
Label2.configure(background='#DCDCDC')
Label2.place(anchor='n', relx=0.30, rely=0.35)

Label3 = Label(window, text="nc: ")
Label3.configure(background='#DCDCDC')
Label3.place(anchor='n', relx=0.30, rely=0.40)

Label4 = Label(window, text="Is confirmed: ")
Label4.configure(background='#DCDCDC')
Label4.place(anchor='n', relx=0.30, rely=0.45)

Label5 = Label(window, text="Value: ")
Label5.configure(background='#DCDCDC')
Label5.place(anchor='n', relx=0.30, rely=0.50)

Entry0 = Entry(window, width=60)
Entry0.place(anchor='n', relx=0.65, rely=0.25)

Entry1 = Entry(window, width=60)
Entry1.place(anchor='n', relx=0.65, rely=0.30)

Entry2 = Entry(window, width=60)
Entry2.place(anchor='n', relx=0.65, rely=0.35)

Entry3 = Entry(window, width=60)
Entry3.place(anchor='n', relx=0.65, rely=0.40)

Entry4 = Entry(window, width=60)
Entry4.place(anchor='n', relx=0.65, rely=0.45)

Entry5 = Entry(window, width=60)
Entry5.place(anchor='n', relx=0.65, rely=0.50)


#defintion of the function
# network is a variable describing the nature of cryptocurrency
# for example network can be : 'BTC' or 'DOGE' OR 'ETH'
# try to test for example bitskan ('BTC')
def bitskoin ():
    #to extract the inputs
    network = Entry0.get()
    address = Entry1.get()
    r_transaction = Entry2.get()
    nc = Entry3.get()
    is_confirmed = Entry4.get()
    value = Entry5.get()

    url1 = 'https://chain.so/api/v2/get_info/'
    url2=url1+network
    x= requests.get(url2)
    y= x.text
    print (y)
    url3='https://chain.so/api/v2/get_address_received/'+network+'/'+address
    y= requests.get(url3)
    z= y.text
    print (z)
    url4= 'https://chain.so/api/v2/get_tx_inputs/'+ network + '/' +address + '/' + r_transaction
    z= requests.get(url4)
    a= z.text
    print (a)
    url5= 'https://chain.so/api/v2/get_tx_outputs/'+ network + '/' + r_transaction+ '/' + 'nc'
    a= requests.get(url5)
    b= a.text
    print (b)
    url6= 'https://chain.so/api/v2/is_tx_confirmed/'+ network+ '/'+  address+ '/'+ r_transaction+ '/'+ 'nc'+ '/'+ is_confirmed
    b= requests.get(url6)
    c= b.text
    print (c)
    url7= 'https://chain.so/api/v2/tx/'+ network+ '/'+  address+ '/'+ r_transaction+ '/'+ 'nc'+ '/'+ is_confirmed + '/' + 'value'
    c= requests.get(url7)
    d= c.text
    print (d)

    #affichage des resultats
    res1= y
    mytext=StringVar()   
    mytext.set(res1)
    Label1 = Label(window, bg='#DCDCDC', text="The first result :").place(anchor='n', relx=0.30, rely=0.70)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.70)

    res2= z
    mytext=StringVar()   
    mytext.set(res2)
    Label2 = Label(window, bg='#DCDCDC', text="The second result :").place(anchor='n', relx=0.30, rely=0.725)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.725)

    res3= a
    mytext=StringVar()   
    mytext.set(res3)
    Label3 = Label(window, bg='#DCDCDC', text="The third result :").place(anchor='n', relx=0.30, rely=0.75)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.75)

    res4= b
    mytext=StringVar()   
    mytext.set(res4)
    Label4 = Label(window, bg='#DCDCDC', text="The fourth result :").place(anchor='n', relx=0.30, rely=0.775)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.775)

    res5= c
    mytext=StringVar()   
    mytext.set(res5)
    Label5 = Label(window, bg='#DCDCDC', text="The fifth result :").place(anchor='n', relx=0.30, rely=0.80)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.80)

    res6= d
    mytext=StringVar()   
    mytext.set(res6)
    Label6 = Label(window, bg='#DCDCDC', text="The sixth result :").place(anchor='n', relx=0.30, rely=0.825)
    result=Label(window, text="", textvariable=mytext).place(anchor='n', relx=0.65, rely=0.825)

def curvefulltime():
    raw_data = pd.read_csv("/Users/emansarahafi/Downloads/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
    df = raw_data.dropna()
    df.reset_index(inplace=True, drop=True)
    pd.options.mode.chained_assignment = None
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

    df.drop([0,1,2,3], inplace=True)
    df.reset_index(inplace=True, drop=True)

    fig = px.line(df, x="Timestamp",y="Weighted_Price")
    fig.show()

def diffcurvefulltime():
    raw_data = pd.read_csv("/Users/emansarahafi/Downloads/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
    df = raw_data.dropna()
    df.reset_index(inplace=True, drop=True)
    pd.options.mode.chained_assignment = None
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

    df.drop([0,1,2,3], inplace=True)
    df.reset_index(inplace=True, drop=True)
    
    df["closeDiff"] = df["Close"].diff()

    fig = px.line(df, x="Timestamp",y="closeDiff")
    fig.show() 

def curve2019():
    raw_data = pd.read_csv("/Users/emansarahafi/Downloads/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
    df = raw_data.dropna()
    df.reset_index(inplace=True, drop=True)
    pd.options.mode.chained_assignment = None
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df["year"] = pd.DatetimeIndex(df["Timestamp"]).year

    df.drop([0,1,2,3], inplace=True)
    df.reset_index(inplace=True, drop=True)

    df19 =  df[df["year"] == 2019]
    df19.reset_index(inplace=True, drop=True)

    fig = px.line(df19, x="Timestamp",y="Weighted_Price")
    fig.show()

    df19.to_csv('/Users/emansarahafi/Downloads/btc19.csv', index=False)

def diffcurve2019():
    raw_data = pd.read_csv("/Users/emansarahafi/Downloads/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
    df = raw_data.dropna()
    df.reset_index(inplace=True, drop=True)
    pd.options.mode.chained_assignment = None
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df["year"] = pd.DatetimeIndex(df["Timestamp"]).year

    df.drop([0,1,2,3], inplace=True)
    df.reset_index(inplace=True, drop=True)

    df["closeDiff"] = df["Close"].diff()

    df19 =  df[df["year"] == 2019]
    df19.reset_index(inplace=True, drop=True)
    fig = px.line(df19, x="Timestamp",y="closeDiff")
    fig.show()

    df19.to_csv('/Users/emansarahafi/Downloads/btc19.csv', index=False)

def links():
    # This is the class to initaite building the blockchain
    class Blockchain:
    # The _init_ method allows us to build the genesis block
       def __init__(self):
           self.chain = []
           self.create_blockchain(proof=1, previous_hash='0')

    #The create_blockchain() method will allow us to create our Genesis block on instantiation of the class.
       def create_blockchain(self, proof, previous_hash):
            block = {
           'index': len(self.chain) + 1,
           'timestamp': str(dt.datetime.now()),
           'proof': proof,
           'previous_hash': previous_hash
       }

            self.chain.append(block)
            return block

    #This method fetches the previous block in the chain
       def get_previous_block(self):
        last_block = self.chain[-1]
        return last_block

    #This method allows the miners to sucessfully mine a block
       def proof_of_work(self, previous_proof):
       # miners proof submitted
        new_proof = 1
       # status of proof of work
        check_proof = False
        while check_proof is False:
           # problem and algorithm based off the previous proof and new proof
           hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
           # check miners solution to problem, by using miners proof in cryptographic encryption
           # if miners proof results in 4 leading zero's in the hash operation, then:
           if hash_operation[:4] == '0000':
               check_proof = True
           else:
               # if miners solution is wrong, give mine another chance until correct
               new_proof += 1
        return new_proof
    #4 leading zeroes are required to mine the block better and faster
    # to generate a hash of an entire block
       def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    # verify the chain's validity
       def is_chain_valid(self, chain):
       # get the first block in the chain and it serves as the previous block
        previous_block = chain[0]
       # an index of the blocks in the chain for iteration
        block_index = 1
        while block_index < len(chain):
           # get the current block
            block = chain[block_index]
           # check if the current block link to previous block has is the same as the hash of the previous block
            if block["previous_hash"] != self.hash(previous_block):
                return False

           # get the previous proof from the previous block
            previous_proof = previous_block['proof']

           # get the current proof from the current block
            current_proof = block['proof']

           # run the proof data through the algorithm
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
           # check if hash operation is invalid
            if hash_operation[:4] != '0000':
               return False
           # set the previous block to the current block after running validation on current block
            previous_block = block
            block_index += 1
        return True

    app = Flask(__name__)
    blockchain = Blockchain()

    @app.route('/mine_block', methods=['GET'])
    def mine_block():
    # get the data we need to create a block
       previous_block = blockchain.get_previous_block()
       previous_proof = previous_block['proof']
       proof = blockchain.proof_of_work(previous_proof)
       previous_hash = blockchain.hash(previous_block)

       block = blockchain.create_blockchain(proof, previous_hash)
       response = {'message': 'Block mined!',
                   'index': block['index'],
                   'timestamp': block['timestamp'],
                   'proof': block['proof'],
                   'previous_hash': block['previous_hash']}
       return jsonify(response), 200


    @app.route('/get_chain', methods=['GET'])
    # Here is the method to get the chain
    def get_chain():
         response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}
         return jsonify(response), 200



    app.run(host='0.0.0.0', port=5000)

#Create labels
lbl = Label(window, bg='#DCDCDC', text="Show Bitcoin Graphs :").place(anchor='n', relx=0.30, rely=0.60)
lbl1 = Label(window, bg='#DCDCDC', text="Generate blockchain link(s) on Debugger with instructions:").place(anchor='n', relx=0.30, rely=0.65)

#Create a Button
btn = Button(window, text = 'RESULT',command=(bitskoin))
btn.place(anchor='n', relx=0.65, rely=0.55)
btn0 = Button(window, text = 'GENERATE LINK(S)',command=(links))
btn0.place(anchor='n', relx=0.65, rely=0.65)
btn1 = Menubutton(window,
                   text="Access the graphs",
                   width=20,height=2)
btn1.place(anchor='n', relx=0.65, rely=0.60)
btn1.menu = Menu(btn1)

#Personalize drop down menu for websites
btn1["menu"] = btn1.menu
btn1.menu.add_checkbutton(label="SHOW BITCOIN GRAPH 2012-2021", command=(curvefulltime))
btn1.menu.add_checkbutton(label="SHOW BITCOIN DIFF GRAPH 2012-2021", command=(diffcurvefulltime))
btn1.menu.add_checkbutton(label="SHOW BITCOIN GRAPH 2019", command=(curve2019))
btn1.menu.add_checkbutton(label="SHOW BITCOIN DIFF GRAPH 2019", command=(diffcurve2019))

#Create a footer
# Create bottom label for company's name
def callback(url):
    webbrowser.open_new(url)

pwr = Label(window, text="""Powered by
Tashfeen Engineering Solutions (2022)""", cursor="hand2", fg = "blue")
pwr.configure(background='#DCDCDC',underline=True)
pwr.place(relx = 0.5,rely = 1.00, anchor ='s')
pwr.bind("<Button-1>", lambda e: callback("https://tashfeen.tech/"))

 
#afficher la fenetre 
window.mainloop()
