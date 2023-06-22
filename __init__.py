import time
import json
import http.client

class API:
    def __init__(this) -> None:
        this.__baseUrl = "www.1secmail.com"
        this.__getEmailsUrl = "/api/v1/?action=genRandomMailbox&count=10"
        this.__getMessagesUrl = "/api/v1/?action=getMessages&login={0}&domain={1}"
        this.__readMessageUrl = "/api/v1/?action=readMessage&login={0}&domain={1}&id={2}"

        this.__connection = http.client.HTTPSConnection(this.__baseUrl)
    
    def __sendRequest(this, url) -> None:
        this.__connection.request("GET", url)
        time.sleep(1)

    def __getresponse(this) -> str:
        return this.__connection.getresponse().read().decode("utf-8")

    def __doAPI(this, url) -> json:
        this.__sendRequest(url)
        return json.loads(this.__getresponse())

    def genRandomMailbox(this) -> json:
        return this.__doAPI(this.__getEmailsUrl)
    
    def getMessages(this, login, domain) -> list:
        return this.__doAPI(this.__getMessagesUrl.format(login, domain))
    
    def readMessage(this, login, domain, id) -> json:
        return this.__doAPI(this.__readMessageUrl.format(login, domain, id))

def filterMessageWhereSender(message, mail) -> str:
    return mail in message.get("from") and message

def getMessagesWhereSender(messages, mail) -> list:
    return list(filter(lambda seq: filterMessageWhereSender(seq, mail), messages))