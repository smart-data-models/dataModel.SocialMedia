Entity: SMAnalysis  
==================  
[Open License](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMAnalysis/LICENSE.md)  

## List of properties  

Required properties  
- No required properties  ## Data Model description of properties  
Sorted alphabetically (click for details)  
## Example payloads    
#### SMAnalysis NGSI V2 key-values Example    
Here is an example of a SMAnalysis in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": 0.4,  
  "analyzedAt": "2020-12-24T12:00:00Z",  
  "hasAnalysisValue": "Anger",  
  "hasAnalysisType": "Sentiment",  
  "isAnalysisOf": "urn:ngsi-ld:SMCollection:001"  
}  
```  
Not available the example of a SMAnalysis in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a SMAnalysis in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### SMAnalysis NGSI-LD normalized Example    
Here is an example of a SMAnalysis in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "analyzedAt": {  
    "type": "Property",  
    "value": {  
			"@type": "DateTime",  
			"@value": "2020-12-24T12:00:00Z"  
			 }		  
  },  
  "hasAnalysisValue": {  
    "type": "Property",  
    "value": "Anger"  
  },  
  "hasAnalysisType": {  
    "type": "Property",  
    "value": "Sentiment"  
  },  
  "isAnalysisOf": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMCollection:001"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
