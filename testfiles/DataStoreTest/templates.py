import os

def buildLabel(client,user,dueDate,ticket,serial,ETTag, additionalNotes):
    """Client, user, due date, ticket number, serial number, ET Tag, additional notes"""
    websiteText = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=380.5 height=574.4 initial-scale=1.0">
    <title>Build Label</title>
    <style>
        /* -- image details -- */
        .logo {{
            display: grid;
            align-items: center;
            justify-content: space-evenly;
            size: 250px;
        }}

        img {{
            width: 50%;
            display: block;
            height: auto;
            position: relative;
            margin-left: auto;
            margin-right: auto;
        }}

        /* -- List items -- */
        .parent {{
            display: table;
            width: 100%;
            table-layout: fixed;
        }}

        .child {{
            display: table-cell;
            vertical-align: top;
            list-style-type: none; /* Remove bullet points */
            padding: 0; /* Remove default padding */
            margin: 0; /* Remove default margin */
        }}

        #fixedInfo {{
            text-align: right;
            padding-right: 5px; /* Adjust padding as needed */
        }}

        #editedInfo {{
            text-align: left;
            padding-left: 5px; /* Adjust padding as needed */
        }}

        li {{
            align-items: right;
        }}

        #fixedChild, #editedChild {{
            height: 20px;
        }}

        /* -- additional information -- */
        .addNotes {{
            overflow: hidden;
        }}

        #title {{
            padding-left: 20px;
        }}

        #textbox {{
            border: 2px solid black;
            margin-left: 1rem;
            margin-right: 1rem;
            border-color: black;
            width: 90%;
            height: 75px;
        }}

        /* -- main html details -- */
        html {{
            width: 380.5px;
            height: 570.4px;
        }}

        .foldbar {{
            position: relative;
            bottom: 225;
            width: 100%;
            position: absolute;
        }}

        #footbar {{
            width: 95%;
            background-color: black;
        }}

        body {{
            display: block;
            position: relative;
        }}
    </style>
</head>
<body>
    <div class="logo">
        <img src="enable-logo.png">
    </div>
    <div class="parent">
        <ul class="child" id="fixedInfo">
            <li id="fixedChild">Client :</li>
            <li id="fixedChild">User :</li>
            <li id="fixedChild">Due Date :</li>
            <li id="fixedChild">Ticket No :</li>
            <li id="fixedChild">Serial Number :</li>
            <li id="fixedChild">ET Tag :</li>
        </ul>
        <ul class="child" id="editedInfo">
            <li id="editedChild">{client}<!-- client --></li>
            <li id="editedChild">{user}<!-- user --></li>
            <li id="editedChild">{dueDate}<!-- due date --></li>
            <li id="editedChild">{ticket}<!-- ticket number --></li>
            <li id="editedChild">{serial}<!-- serial number --></li>
            <li id="editedChild">{ETTag}<!-- et tag --></li>
        </ul>
    </div>
    <hr>
    <div class="addNotes">
        <p id="title">Additional Notes</p>
        <div id="textbox">
            <p contenteditable="true">{additionalNotes}<!-- note field --></p>
        </div>
    </div>
    <div class="foldbar">
        <hr id="footbar">
    </div>
</body>
<script>window.print()</script>
</html>
"""
    variables = {
        "client":client,
        "user":user,
        "dueDate":dueDate,
        "ticket":ticket,
        "serial":serial,
        "ETTag":ETTag,
        "additionalNotes":additionalNotes
    }
    formatted_html = websiteText.format(**variables)
    file = open(f"./history/{ticket}.html", "w")
    file.writelines(formatted_html)
    file.close()

def stockLabel(client,newused,dateReceived,ettag,makeModel,serial,additionalNotes): #client, NorU,date,device,serialno,addnote
    """Client, new or used, date received, make model, serial number, additional notes"""
    websiteText =f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=358.5 height=574.4 initial-scale=1.0">
    <link rel="stylesheet" href="history_stylesheet.css">
    <title>Stock Label</title>
</head>
<body>
    <div class="logo">
        <img src="enable-logo.png">
    </div>
    <div class="parent">
        <div class="child" id="fixedInfo">
            <li id="fixedChild">Client :</lt>
            <li id="fixedChild">New | Used :</li>
            <li id="fixedChild">Date Received :</li>
            <li id="fixedChild">ET Tag :</li>
            <li id="fixedChild">Make / Model :</li>
            <li id="fixedChild">Serial Number :</li>
        </div>
        <div class="child" id="editedInfo">
            <li id="editedChild">{client}<!-- client --></li>
            <li id="editedChild">{newused}<!-- New | Used --></li>
            <li id="editedChild">{dateReceived}<!-- Date Received--></li>
            <li id="editedChild">{ettag}</li>
            <li id="editedChild">{makeModel}<!-- Make / Model --></li>
            <li id="editedChild">{serial}<!-- Serial Number --></li>
        </div>
    </div>
    <hr>
    <div class="addNotes">
        <p1 id="title">Additional Notes</p1>
        <div id="textbox">
            <p1 contenteditable="true">{additionalNotes}<!-- note field --></p1>
        </div>
    </div>
    <div class="foldbar">
        <hr id="footbar">
    </div>
</body>
<script>window.print()</script>
</html>"""
    file = open(f"./history/stock-{client}.html", "w")
    file.writelines(websiteText)
    file.close()


def repairLabel(client,ticketno,dateReceived,ettag,makeModel,serial,additionalNotes): #client,ticketno,date,makemodel,serialno,addnotes
    """Client, new or used, date received, make model, serial number, additional notes"""
    websiteText =f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=358.5 height=574.4 initial-scale=1.0">
    <link href="../history-style/stylesheet.css" rel="stylesheet" type="text/css" />
    <title>Repair Label</title>
</head>
<body>
    <div class="logo">
        <img src="../history-style/enable-logo.png">
    </div>
    <div class="parent">
        <div class="child" id="fixedInfo">
            <li id="fixedChild">Client :</lt>
            <li id="fixedChild">Ticket No :</lt>
            <li id="fixedChild">Date Received :</li>
            <li id="fixedChild">ET Tag :</li>
            <li id="fixedChild">Make / Model :</li>
            <li id="fixedChild">Serial Number :</li>
        </div>
        <div class="child" id="editedInfo">
            <li id="editedChild">{client}<!-- client --></li>
            <li id="editedChild">{ticketno}<!-- Ticket number --></li>
            <li id="editedChild">{dateReceived}<!-- Date Received--></li>
            <li id="editedChild">{ettag}</li>
            <li id="editedChild">{makeModel}<!-- Make / Model --></li>
            <li id="editedChild">{serial}<!-- Serial Number --></li>
        </div>
    </div>
    <hr>
    <div class="addNotes">
        <p1 id="title">Additional Notes</p1>
        <div id="textbox">
            <p1 contenteditable="true">{additionalNotes}<!-- note field --></p1>
        </div>
    </div>
    <div class="foldbar">
        <hr id="footbar">
    </div>
</body>
<script>window.print()</script>
</html>"""
    file = open(f"./history/{ticketno}.html", "w")
    file.writelines(websiteText)
    file.close()

def disposalLabel(client,ticket,date,device,AssetTag,serialNo,addnotes):
    """Client, user, due date, ticket number, serial number, ET Tag, additional notes"""
    websiteText =f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=358.5 height=574.4 initial-scale=1.0">
    <link href="../history-style/stylesheet.css" rel="stylesheet" type="text/css" />
    <title>disposal label</title>
</head>
<body>
    <div class="logo">
        <img src="../history-style/enable-logo.png">
    </div>
    <div class="parent">
        <div class="child" id="fixedInfo">
            <li id="fixedChild">Client :</lt>
            <li id="fixedChild">Ticket No :</li>
            <li id="fixedChild">Date :</li>
            <li id="fixedChild">Device :</li>
            <li id="fixedChild">Serial Number :</li>
            <li id="fixedChild">ET Tag :</li>
        </div>
        <div class="child" id="editedInfo">
            <li id="editedChild">{client}<!-- client --></li>
            <li id="editedChild">{ticket}<!-- ticket number --></li>
            <li id="editedChild">{date}<!-- due date --></li>
            <li id="editedChild">{device}<!-- device --></li>
            <li id="editedChild">{serialNo}<!-- serial number --></li>
            <li id="editedChild">{AssetTag}<!-- et tag --></li>
        </div>
    </div>
    <hr>
    <div class="addNotes">
        <p1 id="title">Additional Notes</p1>
        <div id="textbox">
            <p1 contenteditable="true">{addnotes}<!-- note field --></p1>
        </div>
    </div>
    <div class="foldbar">
        <hr id="footbar">
    </div>
</body>
<script>window.print()</script>
</html>"""
    file = open(f".\history\{ticket}.html", "w")
    file.writelines(websiteText)
    file.close()
