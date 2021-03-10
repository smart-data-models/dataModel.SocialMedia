Entity: SMUser  
==============  
[Open License](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMUser/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic SMUser made for the Social Media domain. This entity is primarily associated with the description of a user of Social Media applications.**  

## List of properties  

- `address`: The mailing address  - `areaServed`: The geographic area where a service or offered item is provided  - `createdPost`: The ID of the post that the SMUser created.  - `isMentionedBy`: The ID of a post that mentions the SMUser.  - `location`:   - `platform`: Description of the  social platform of the user.  - `type`: NGSI-LD Entity Type. It must be equal to SMUser.  - `userId`: The User ID of the SMUser.  - `userName`: The username of the SMUser.    
Required properties  
- `id`  - `platform`  - `type`  - `userId`  - `userName`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SMUser:    
  description: 'This entity contains a harmonised description of a generic SMUser made for the Social Media domain. This entity is primarily associated with the description of a user of Social Media applications.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    createdPost:    
      description: 'The ID of the post that the SMUser created.'    
      items:    
        format: uri    
        type: string    
      type: Relationship    
    isMentionedBy:    
      description: 'The ID of a post that mentions the SMUser.'    
      items:    
        format: uri    
        type: string    
      type: Relationship    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    platform:    
      description: 'Description of the  social platform of the user.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to SMUser.'    
      enum:    
        - SMUser    
      type: Property    
    userId:    
      description: 'The User ID of the SMUser.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    userName:    
      description: 'The username of the SMUser.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
  required:    
    - id    
    - type    
    - userId    
    - platform    
    - userName    
  type: object    
```  
</details>    
## Example payloads    
#### SMUser NGSI V2 key-values Example    
Here is an example of a SMUser in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:SMUser:123",  
  "type": "SMUser",  
  "userId": "21098319",  
  "platform": "Twitter",  
  "userName": "Jsmith2",  
  "createdPost": "urn:ngsi-ld:SMPost:123",  
  "isMentionedBy": "urn:ngsi-ld:SMPost:123"  
}  
```  
#### SMUser NGSI V2 normalized Example    
Here is an example of a SMUser in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:SMUser:123",  
  "type": "SMUser",  
  "userId": {  
    "type": "Property",  
    "value": "21098319"  
  },  
  "platform": {  
    "type": "Property",  
    "value": "Twitter"  
  },  
  "userName": {  
    "type": "Property",  
    "value": "Jsmith2"  
  },  
  "createdPost": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   },  
   "isMentionedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   }  
}  
```  
#### SMUser NGSI-LD key-values Example    
Here is an example of a SMUser in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:SMUser:123",  
  "type": "SMUser",  
  "userId": "21098319",  
  "platform": "Twitter",  
  "userName": "Jsmith2",  
  "createdPost": "urn:ngsi-ld:SMPost:123",  
  "isMentionedBy": "urn:ngsi-ld:SMPost:123",  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  
#### SMUser NGSI-LD normalized Example    
Here is an example of a SMUser in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:SMUser:123",  
  "type": "SMUser",  
  "userId": {  
    "type": "Property",  
    "value": "21098319"  
  },  
  "platform": {  
    "type": "Property",  
    "value": "Twitter"  
  },  
  "userName": {  
    "type": "Property",  
    "value": "Jsmith2"  
  },  
  "createdPost": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   },  
   "isMentionedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
