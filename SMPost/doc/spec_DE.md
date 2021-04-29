Entität: SMPost  
===============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen SMPosts, der für die Social-Media-Domäne erstellt wurde.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `belongsToCollection`: Die IDs der SMCollections, von denen dieser Beitrag ein Teil ist.  - `createdBy`: Die ID des SMUsers, der diesen Beitrag erstellt hat.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `hasAnalysis`: Die IDs der SMAnalysen, die diesen Beitrag analysieren.  - `hasHashtags`: Die Hashtags des Beitrags.  - `hasImages`: Die URLs der Inhalte, die in Bildform vorliegen.  - `hasInteractionCount`:   - `hasLanguage`: Die Sprache des Beitrags.  - `hasMentions`: Die IDs der in diesem Beitrag erwähnten SMUsers.  - `hasPostURL`: Die URL des Beitrags.  - `hasPrivacyLevel`: Die Datenschutzeinstellung des Beitrags.  - `hasReferencedLocations`: Die IDs der Orte, auf die in diesem Beitrag verwiesen wird.  - `hasText`: Der Inhalt, der in Textform vorliegt.  - `hasThumbnails`: Die Miniatur-URLs des Beitrags.  - `hasVideos`: Die URLs der Inhalte, die in Videoform vorliegen.  - `id`: Eindeutiger Bezeichner der Entität  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `platform`: Plattform der Stelle.  - `postCreatedAt`:  Der Zeitpunkt der Erstellung des SMPosts.  - `postId`: Die Post-ID des SMPosts.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI-LD Entity Type. Er muss gleich SMPost sein.    
Erforderliche Eigenschaften  
- `id`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SMPost:    
  description: 'This entity contains a harmonised description of a generic SMPost made for the Social Media domain.'    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    belongsToCollection:    
      description: 'The IDs of the SMCollections, which this post is a part of.'    
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
    createdBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID of the SMUser that created this post.'    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    hasAnalysis:    
      description: 'The IDs of the SMAnalyses that analyze this post.'    
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
    hasHashtags:    
      description: 'The hashtags of the post.'    
      items:    
        type: string    
      type: Property    
    hasImages:    
      description: 'The URLs of the content that is in image form.'    
      items:    
        type: string    
      type: Property    
    hasInteractionCount:    
      items:    
        properties:    
          count:    
            type: number    
          interactionType:    
            enum:    
              - Quote    
              - Reply    
              - Retweet    
              - Favorite    
              - Shares    
              - Reactions    
              - Views    
              - Like    
              - Dislike    
              - Favorite    
              - Comment    
            type: string    
        type: object    
      type: array    
    hasLanguage:    
      description: 'The language of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    hasMentions:    
      description: 'The IDs of the SMUsers mentioned in this post.'    
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
    hasPostURL:    
      description: 'The URL of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    hasPrivacyLevel:    
      description: 'The privacy setting of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    hasReferencedLocations:    
      description: 'The IDs of the locations referenced in this post.'    
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
    hasText:    
      description: 'The content that is in textual form.'    
      items:    
        type: string    
      type: Property    
    hasThumbnails:    
      description: 'The thumbnail URLs of the post.'    
      items:    
        type: string    
      type: Property    
    hasVideos:    
      description: 'The URLs of the content that is in video form.'    
      items:    
        type: string    
      type: Property    
    id:    
      anyOf: &smpost_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smpost_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    platform:    
      description: 'Platform of post.'    
      type: Property    
    postCreatedAt:    
      description: ' The datetime of the creation of the SMPost.'    
      format: date-time    
      type: string    
    postId:    
      description: 'The  post ID of the SMPost.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to SMPost.'    
      enum:    
        - SMPost    
      type: Property    
  required:    
    - id    
    - type    
    - postCreatedAt    
    - postId    
    - platform    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### SMPost NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen SMPost im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "id": "SMPost.123",  
  "type": "SMPost",  
  "hasPostURL": "http://twt.com/121",  
  "postCreatedAt": "2020-12-24T12:00:00Z",  
  "postId": "21098319",  
  "hasLanguage": "en",  
  "platform": "Twitter",  
  "hasText": [  
    "This is a tweet",  
    "This is another tweet"  
  ],  
  "hasImages": [  
    "https://twt.com/image.png",  
    "https://twt.com/image2.png",  
    "https://twt.com/image3.png"  
  ],  
  "hasVideos": [  
    "https://twt.com/video.mp4",  
    "https://twt.com/video2.mp4"  
  ],  
  "hasPrivacyLevel": "public",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "hasHashtags": [  
    "#sample",  
    "#tag"  
  ],  
  "hasThumbnails": [  
    "https://twt.com/thumb.png",  
    "https://twt.com/thumb2.png"  
  ],  
  "hasInteractionCount": [  
    {  
      "interactionType": "Like",  
      "count": 750  
    },  
    {  
      "interactionType": "Views",  
      "count": 2150  
    }  
  ],  
  "hasReferencedLocations": [  
    "RefLocation.00",  
    "RefLocation.01"  
  ],  
  "hasMentions": [  
    "SMUser.154",  
    "SMUser.155",  
    "SMUser.156"  
  ],  
  "hasAnalysis": [  
    "Analysis.X",  
    "Analysis.X2"  
  ],  
  "createdBy": "SMUser.123",  
  "belongsToCollection": [  
    "SMCollection.001",  
    "SMCollection.002"  
  ]  
}  
```  
#### SMPost NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen SMPost im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "SMPost:.23",  
  "type": "SMPost",  
  "hasPostURL": {  
    "type": "Property",  
    "value": "http://twt.com/121"  
  },  
  "postCreatedAt": {  
    "type": "DateTime",  
    "value": "2020-12-24T12:00:00Z"  
  },  
  "postId": {  
    "type": "Text",  
    "value": "21098319"  
  },  
  "hasLanguage": {  
    "type": "Text",  
    "value": "en"  
  },  
  "platform": {  
    "type": "Text",  
    "value": "Twitter"  
  },  
  "hasText": {  
    "type": "Text",  
    "value": "This is a tweet"  
  },  
  "hasImage": {  
    "type": "Text",  
    "value": "https://twt.com/image.png"  
  },  
  "hasVideo": {  
    "type": "Text",  
    "value": "https://twt.com/video.mp4"  
  },  
  "hasPrivacy": {  
    "type": "Text",  
    "value": "public"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        40.3,  
        25.5  
      ]  
    }  
  },  
  "hasHashtag": {  
    "type": "Text",  
    "value": ["#sample","#tag"]  
  },  
  "hasThumbnail": {  
    "type": "Text",  
    "value": "https://twt.com/thumb.png"  
  },  
  "likes": {  
    "type": "Number",  
    "value": 762  
  },  
  "createdBy": {  
    "type": "Relationship",  
    "object": "SMUser.123"  
  },  
  "hasReferencedLocation": {  
    "type": "Relationship",  
    "object": "RefLocation.00"  
  },  
  "hasMentions": {  
    "type": "Relationship",  
    "object": "SMUser.154"  
  },  
  "isAnalyzedBy": {  
    "type": "Relationship",  
    "object": "Analysis.X"  
  },  
  "belongsToCollection": {  
    "type": "Relationship",  
    "object": "SMCollection.001"  
  }  
}  
```  
#### SMPost NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen SMPost im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:SMPost:123",  
  "type": "SMPost",  
  "hasPostURL": "http://twt.com/121",  
  "postCreatedAt": "2020-12-24T12:00:00Z",  
  "postId": "21098319",  
  "hasLanguage": "en",  
  "platform": "Twitter",  
  "hasText": [  
    "This is a tweet"  
  ],  
  "hasImages": [  
    "https://twt.com/image.png"  
  ],  
  "hasVideos": [  
    "https://twt.com/video.mp4"  
  ],  
  "hasPrivacy": "public",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "hasHashtags": [  
    "#sample",  
    "#tag"  
  ],  
  "hasThumbnails": [  
    "https://twt.com/thumb.png"  
  ],  
  "hasInteractionCount": [  
    {  
      "interactionType": "Like",  
      "count": 762  
    }  
  ],  
  "createdBy": "urn:ngsi-ld:SMUser:123",  
  "hasReferencedLocations": [  
    "urn:ngsi-ld:RefLocation:00"  
  ],  
  "hasMentions": [  
    "urn:ngsi-ld:SMUser:154"  
  ],  
  "hasAnalysis": [  
    "urn:ngsi-ld:Analysis:X"  
  ],  
  "belongsToCollection": ["urn:ngsi-ld:SMCollection:001"],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SMPost NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen SMPost im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:SMPost:123",  
  "type": "SMPost",  
  "hasPostURL": {  
    "type": "Property",  
    "value": "http://twt.com/121"  
  },  
  "postCreatedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "postId": {  
    "type": "Property",  
    "value": "21098319"  
  },  
  "hasLanguage": {  
    "type": "Property",  
    "value": "en"  
  },  
  "platform": {  
    "type": "Property",  
    "value": "Twitter"  
  },  
  "hasText": [  
    {  
      "type": "Property",  
      "value": "This is a tweet."  
    },  
    {  
      "type": "Property",  
      "value": "This is another tweet."  
    }  
  ],  
  "hasImages": [  
    {  
      "type": "Property",  
      "value": "https://twt.com/image.png"  
    },  
    {  
      "type": "Property",  
      "value": "https://twt.com/image2.png"  
    }  
  ],  
  "hasVideos": [  
    {  
      "type": "Property",  
      "value": "https://twt.com/video.mp4"  
    },  
    {  
      "type": "Property",  
      "value": "https://twt.com/video2.mp4"  
    }  
  ],  
  "hasPrivacyLevel": {  
    "type": "Property",  
    "value": "public"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        40.3,  
        25.5  
      ]  
    }  
  },  
  "hasHashtags": [  
    {  
      "type": "Property",  
      "value": [  
        "#sample",  
        "#tag"  
      ]  
    },  
    {  
      "type": "Property",  
      "value": [  
        "#sample2",  
        "#tag2"  
      ]  
    }  
  ],  
  "hasThumbnails": [  
    {  
      "type": "Property",  
      "value": "https://twt.com/thumb.png"  
    },  
    {  
      "type": "Property",  
      "value": "https://twt.com/thumb2.png"  
    }  
  ],  
  "createdBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SMUser:123"  
  },  
  "hasReferencedLocations": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:RefLocation:00",  
      "datasetId": "urn:ngsi-ld:Dataset:RefLocation:00"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:RefLocation:01",  
      "datasetId": "urn:ngsi-ld:Dataset:RefLocation:01"  
    }  
  ],  
  "hasMentions": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMUser:154",  
      "datasetId": "urn:ngsi-ld:Dataset:SMUser:154"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMUser:155",  
      "datasetId": "urn:ngsi-ld:Dataset:SMUser:155"  
    }  
  ],  
  "hasAnalysis": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Analysis:X",  
      "datasetId": "urn:ngsi-ld:Dataset:Analysis:X"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Analysis:02",  
      "datasetId": "urn:ngsi-ld:Dataset:Analysis:02"  
    }  
  ],  
  "belongsToCollection": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMCollection:001",  
      "datasetId": "urn:ngsi-ld:Dataset:SMCollection:001"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:SMCollection:002",  
      "datasetId": "urn:ngsi-ld:Dataset:SMCollection:002"  
    }  
  ],  
  "hasInteractionCount": [  
    {  
      "type": "Property",  
      "value": {  
        "@interactionType": "Like",  
        "@count": "750"  
      }  
    },  
    {  
      "type": "Property",  
      "value": {  
        "@interactionType": "Views",  
        "@count": "2150"  
      }  
    }  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
