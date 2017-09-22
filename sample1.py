"""
Python support for Azure automation is now public preview!

Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

# Emotion analysis

########### Python 3.2 #############
# import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
#
# headers = {
#     # Request headers. Replace the placeholder key below with your subscription key.
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': '13hc77781f7e4b19b5fcdd72a8df7156',
# }
#
# params = urllib.parse.urlencode({
# })
#
# # Replace the example URL below with the URL of the image you want to analyze.
# body = "{ 'url': 'http://example.com/picture.jpg' }"
#
# try:
#     # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
#     #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
#     #   URL below with "westcentralus".
#     conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print(e.args)
# ####################################

"""
Python support for Azure automation is now public preview!

Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

# Emotion analysis

########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e257b9e881914b878039b41fc101e870'
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'http://dreamatico.com/data_images/face/face-1.jpg' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
