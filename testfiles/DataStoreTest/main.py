import json
import templates
import os
import pdfkit

filepath = "C:\\Temp\\VS_Code\\Python\\personal\\DataStoreTest\\Labelinfo.json"


with open(filepath, 'r') as f:
    data = json.load(f)

# ticketno = input("What is the ticket no: ")
# client = input("what is the client name: ")
# attribute = input("What is the user/new or used: ")
# duedate = input("what is the duedate: ")
# serialno = input("What is the serial number: ")
# ettag = input("what is the ET Tag: ")
# addnotes = input("any additional notes: ")

# new_entry = {
#     "client":client,
#     "attribute":attribute,
#     "duedate":duedate,
#     "ticketno":ticketno,
#     "serialno":serialno,
#     "ettag":ettag,
#     "addnotes":addnotes
# }

# if ticketno not in data:
#     data[ticketno] = []

# data[ticketno].append(new_entry)

# with open(filepath,"w") as f:
#     json.dump(data,f,indent=4)
#     print(f)
#     print(data[ticketno])

ticketno = "T20241231.0001"

for entry in data[ticketno]:
    client = entry.get("client")
    attribute = entry.get("attribute")
    duedate = entry.get("duedate")
    ticketno = entry.get("ticketno")
    serialno = entry.get("serialno")
    ettag = entry.get("ettag")
    addnotes = entry.get("addnotes")

printpath = f"C:\\Temp\\VS_Code\\Python\\personal\\DataStoreTest\\history\\{ticketno}.html"    

templates.buildLabel(client,attribute,duedate,ticketno,serialno,ettag,addnotes)

pdfkit.from_file(printpath, "out.pdf", options={"load-error-handling": "ignore", "enable-local-file-access": ""})
os.startfile("out.pdf","print")