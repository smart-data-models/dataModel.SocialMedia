Entität: SMUser  
===============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMUser/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen SMUsers, die für den Bereich der sozialen Medien erstellt wurde. Diese Entität ist in erster Linie mit der Beschreibung eines Nutzers von Social-Media-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `createdPosts`: Die ID des Beitrags, den der SMUser erstellt hat.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `isMentionedBy`: Die ID eines Beitrags, in dem der SMUser erwähnt wird.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `platform`: Beschreibung der sozialen Plattform des Nutzers.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-LD-Entitätstyp. Er muss gleich SMUser sein.  - `userId`: Die Benutzer-ID des SMUsers.  - `userName`: Der Benutzername des SMUsers. Datenschutz:'Niedrig'    
Erforderliche Eigenschaften  
- `id`  - `platform`  - `type`  - `userName`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &smuser_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smuser_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    platform:    
      description: 'Description of the  social platform of the user.'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to SMUser.'    
      enum:    
        - SMUser    
      type: string    
      x-ngsi:    
        type: Property    
    userId:    
      description: 'The User ID of the SMUser.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
    userName:    
      description: 'The username of the SMUser. Privacy:''Low'''    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
  required:    
    - id    
    - type    
    - platform    
    - userName    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SocialMedia/blob/master/SMUser/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/SMUser/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## Beispiel-Nutzlasten  
#### SMUser NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen SMUser im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SMUser NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen SMUser im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SMUser NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen SMUser im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SMUser NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen SMUser im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht