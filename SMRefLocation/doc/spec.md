Entity: SMRefLocation  
=====================  
[Open License](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMRefLocation/LICENSE.md)  

## List of properties  

Required properties  
- No required properties  ## Data Model description of properties  
Sorted alphabetically (click for details)  
## Example payloads    
#### SMRefLocation NGSI V2 key-values Example    
Here is an example of a SMRefLocation in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:RefLocation:00",  
  "type": "SMRefLocation",  
  "locationName": "Thessaloniki",  
  "location": {  
    "type": "Point",  
	"coordinates":   
	 [  
	  40.3,  
	  25.5  
	 ]  
	},  
  "locationReferencedBy": "urn:ngsi-ld:SMPost:123"  
}  
```  
Not available the example of a SMRefLocation in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a SMRefLocation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### SMRefLocation NGSI-LD normalized Example    
Here is an example of a SMRefLocation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:RefLocation:00",  
  "type": "SMRefLocation",  
  "locationName": {  
    "type": "Property",  
    "value": "Thessaloniki"  
  },  
  "location": {  
    "type": "GeoProperty",  
	"value": {  
	 "type": "Point",  
	 "coordinates":   
	 [  
	  40.3,  
	  25.5  
	 ]  
	}  
  },  
  "locationReferencedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
