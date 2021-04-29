Entité : SMUser  
===============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMUser/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un SMUser générique faite pour le domaine des médias sociaux. Cette entité est principalement associée à la description d'un utilisateur d'applications de médias sociaux**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `createdPosts`: L'ID du message que le SMUser a créé.  - `isMentionedBy`: L'ID d'un message qui mentionne le SMUser.  - `location`:   - `platform`: Description de la plateforme sociale de l'utilisateur.  - `type`: Type d'entité NGSI-LD. Il doit être égal à SMUser.  - `userId`: L'ID de l'utilisateur du SMUser.  - `userName`: Le nom d'utilisateur du SMUser. Confidentialité : 'Low' (faible)    
Propriétés requises  
- `id`  - `platform`  - `type`  - `userName`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
    createdPosts:    
      description: 'The ID of the post that the SMUser created.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: Relationship    
    isMentionedBy:    
      description: 'The ID of a post that mentions the SMUser.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
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
    userName:    
      description: 'The username of the SMUser. Privacy:''Low'''    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
  required:    
    - id    
    - type    
    - platform    
    - userName    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### SMUser NGSI-v2 valeurs-clés Exemple  
Voici un exemple de SMUser au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "SMUser.123",  
  "type": "SMUser",  
  "userId": "21098319",  
  "platform": "Twitter",  
  "userName": "Jsmith2",  
  "createdPosts": [  
    "SMPost.123",  
    "SMPost.124"  
  ],  
  "isMentionedBy": [  
    "SMPost.123",  
    "SMPost.124"  
  ]  
}  
```  
#### SMUser NGSI-v2 normalisé Exemple  
Voici un exemple d'un SMUser au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "SMUser.123",  
  "type": "SMUser",  
  "userId": {  
    "type": "Text",  
    "value": "21098319"  
  },  
  "platform": {  
    "type": "Text",  
    "value": "Twitter"  
  },  
  "userName": {  
    "type": "Text",  
    "value": "Jsmith2"  
  },  
  "createdPosts": [  
    {  
      "type": "Relationship",  
      "value": "SMPost.123"  
    }  
  ],  
  "isMentionedBy": [  
    {  
      "type": "Relationship",  
      "value": "SMPost.123"  
    }  
  ]  
}  
```  
#### SMUser NGSI-LD valeurs-clés Exemple  
Voici un exemple de SMUser au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SMUser:123",  
  "type": "SMUser",  
  "userId": "21098319",  
  "platform": "Twitter",  
  "userName": "Jsmith2",  
  "createdPosts": [  
    "urn:ngsi-ld:SMPost:123"  
  ],  
  "isMentionedBy": [  
    "urn:ngsi-ld:SMPost:123"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SMUser NGSI-LD normalisé Exemple  
Voici un exemple d'un SMUser au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
  "createdPosts": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMPost:123",  
      "datasetId": "urn:ngsi-ld:Dataset:SMPost:123"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMPost:124",  
      "datasetId": "urn:ngsi-ld:Dataset:SMPost:124"  
    }  
  ],  
  "isMentionedBy": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMPost:123",  
      "datasetId": "urn:ngsi-ld:Dataset:SMPost:123"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMPost:124",  
      "datasetId": "urn:ngsi-ld:Dataset:SMPost:124"  
    }  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
