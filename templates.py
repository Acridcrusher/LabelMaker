import os

def buildLabel(client,user,dueDate,ticket,serial,ETTag, additionalNotes):
    """Client, user, due date, ticket number, serial number, ET Tag, additional notes"""
    websiteText =f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=380.5 height=574.4 initial-scale=1.0">
    <link rel="stylesheet" href="history_stylesheet.css">
    <title>Build Label</title>
</head>
<body>
    <div class="logo">
        <img src="enable-logo.png">
    </div>
    <div class="parent">
        <div class="child" id="fixedInfo">
            <li id="fixedChild">Client :</lt>
            <li id="fixedChild">User :</li>
            <li id="fixedChild">Due Date :</li>
            <li id="fixedChild">Ticket No :</li>
            <li id="fixedChild">Serial Number :</li>
            <li id="fixedChild">ET Tag :</li>
        </div>
        <div class="child" id="editedInfo">
            <li id="editedChild">{client}<!-- client --></li>
            <li id="editedChild">{user}<!-- user --></li>
            <li id="editedChild">{dueDate}<!-- due date --></li>
            <li id="editedChild">{ticket}<!-- ticket number --></li>
            <li id="editedChild">{serial}<!-- serial number --></li>
            <li id="editedChild">{ETTag}<!-- et tag --></li>
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
    file = open(f"./history/{ticket}.html", "w")
    file.writelines(websiteText)
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
