# imports functions
import json
import templates
import os
import pdfkit

# installed at: https://wkhtmltopdf.org/downloads.html
# is needed for pdfkit to work / because fuck python and it working fine one day and not the next
path_to_wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# declares filepaths for code to run
directory = os.path.abspath("")
iamge_dir = os.path.join(directory,"images")
templates_dir = os.path.join(directory,"templates")
static = os.path.join(directory,"static")

# opens the json file to be read
with open((f"{directory}\\Labelinfo.json"), 'r') as f:
    data = json.load(f)


# gets information from the database to be turned into output.html
def pull_from_database(entryname):
    """Gets the data from the json file"""
    with open((f"{directory}\\Labelinfo.json"), 'r') as f:
        data = json.load(f)

    if entryname in data:
        return data[entryname]
    else:
        return "error-404"

# def convert_pdf(entryname):
    # grab the html information and conver it to pdf for system printing

def create_html(entryname):
    databaseInfo = pull_from_database(entryname)

    for entry in databaseInfo:
        client = entry.get("client")
        attribute = entry.get("attribute")
        duedate = entry.get("duedate")
        ticketno = entry.get("ticketno")
        serialno = entry.get("serialno")
        ettag = entry.get("ettag")
        addnotes = entry.get("addnotes")
        ticketType = entry.get("type")

    if ticketType == "build":
        formatted_html = templates.buildLabel(client,attribute,duedate,ticketno,serialno,ettag,addnotes)
    elif ticketType == "stock":
        formatted_html = templates.stockLabel(client,attribute,duedate,ettag,ticketno,serialno,addnotes)
    elif ticketType == "repair":
        formatted_html = templates.repairLabel(client,ticketno,duedate,ettag,attribute,serialno,addnotes)
    elif ticketType == "dispose":
        formatted_html = templates.disposalLabel(client,ticketno,duedate,attribute,ettag,serialno,addnotes)
        
    file = open(f"{static}\\output.html", "w")
    file.writelines(formatted_html)
    file.close()

# adds information pushed from flask to the json file for storage
def add_to_database(client, attrib, duedate, ticketno, serialno, ettag, addnotes, ticketType):
    """client: client name
    attrib: Make/model | new/used | user
    duedate: date the device is due to ship out
    ticketno: Ticket Number
    serialno: Device serial number
    ettag: Device ET Tag
    addnotes: Additional notes
    """
    new_entry = {
        "client":client,
        "attribute":attrib,
        "duedate":duedate,
        "ticketno":ticketno,
        "serialno":serialno,
        "ettag":ettag,
        "addnotes":addnotes,
        "type":ticketType
    }

    if ticketno in data:
        counter = 1
        new_ticketno = f"{ticketno}_{counter}"
        while new_ticketno in data:
            counter += 1
            new_ticketno = f"{ticketno}_{counter}"
        entryname = new_ticketno
    else:
        entryname = ticketno
        
    data[entryname] = []
    data[entryname].append(new_entry)

    with open((f"{directory}\\Labelinfo.json"),"w") as f:
        json.dump(data,f,indent=4)

    create_html(entryname)

def printpdf():
    html_file = os.path.join(static,"output.html")
    pdf_file = "out.pdf"
    pdfkit.from_file(html_file,pdf_file, options={"load-error-handling":"ignore","enable-local-file-access":""}, configuration=config)
    os.startfile(pdf_file,"print")


# pulling information out of the json file #
#
# for entry in data[ticketno]:
#     client = entry.get("client")
#     attribute = entry.get("attribute")
#     duedate = entry.get("duedate")
#     ticketno = entry.get("ticketno")
#     serialno = entry.get("serialno")
#     ettag = entry.get("ettag")
#     addnotes = entry.get("addnotes")
#     ticketType = entry.get("type")

# ticketno = input("What is the ticket no: ")
# client = input("what is the client name: ")
# attribute = input("What is the user/new or used: ")
# duedate = input("what is the duedate: ")
# serialno = input("What is the serial number: ")
# ettag = input("what is the ET Tag: ")
# addnotes = input("any additional notes: ")


# converts the html file to pdf. need to see if we can pass the information through #
# direct from HTML code to avoid creating html files where not nessasary            #
#
# pdfkit.from_file(printpath, "out.pdf", options={"load-error-handling": "ignore", "enable-local-file-access": ""})