
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "SMCollection"
subject = "dataModel.SocialMedia"
groupedAt = "{'type': 'Property', 'value': {'@type': 'DateTime', '@value': '2020-12-24T12:00:00Z'}}"
attribute = "groupedAt"
value = groupedAt
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

hasAnalysis = [{'type': 'Relationship', 'object': 'urn:ngsi-ld:SMAnalysis:331', 'datasetId': 'urn:ngsi-ld:Dataset:SMAnalysis:331'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:SMAnalysis:332', 'datasetId': 'urn:ngsi-ld:Dataset:SMAnalysis:332'}]
attribute = "hasAnalysis"
value = hasAnalysis
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

hasPosts = [{'type': 'Relationship', 'object': 'urn:ngsi-ld:SMPost:125', 'datasetId': 'urn:ngsi-ld:Dataset:SMPost:125'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:SMPost:124', 'datasetId': 'urn:ngsi-ld:Dataset:SMPost:124'}]
attribute = "hasPosts"
value = hasPosts
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
