#!/usr/bin/env python3

# author: greyshell
# description: extract the dwl links

# setup Imports
from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse


# Class BurpExtender (Required) contaning all functions used to interact with Burp Suite API
class BurpExtender(IBurpExtender, IHttpListener, IHttpRequestResponse):
    # define registerExtenderCallbacks: From IBurpExtender Interface

    def registerExtenderCallbacks(self, callbacks):
        # keep a reference to our callbacks object (Burp Extensibility Feature)
        self._callbacks = callbacks
        # obtain an extension helpers object (Burp Extensibility Feature)
        # http://portswigger.net/burp/extender/api/burp/IExtensionHelpers.html
        self._helpers = callbacks.getHelpers()
        # set our extension name that will display in Extender Tab
        self._callbacks.setExtensionName("get URL")
        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)

    # define processHttpMessage: From IHttpListener Interface
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # determine what tool we would like to pass though our extension:
        if toolFlag == 4:  # if tool is Proxy Tab
            # determine if request or response:

            if not messageIsRequest:  # only handle responses
                response = messageInfo.getResponse()  # get Response from IHttpRequestResponse instance
                analyzedResponse = self._helpers.analyzeResponse(response)  # returns IResponseInfo
                headerList = analyzedResponse.getHeaders()  # get Headers from IResponseInfo Instance

                jsondata = response.tostring()
                videourl = jsondata.find('"url":"https://embed-ssl.wistia.com/deliveries/')
                created = jsondata.find('","created_at"')
                if videourl > 0:
                    download_link = jsondata[videourl + 7:created]
                    print(download_link)
                    with open("results.txt", "a") as f:
                        f.write(download_link)
                        f.write("\n")
                    messageInfo.setHighlight("blue")  # set Highlight Color to blue
