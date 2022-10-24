<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SMPost  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description harmonisée d'un SMPost générique réalisé pour le domaine des médias sociaux.**  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `belongsToCollection[array]`: Les ID des SMCollections, dont ce post fait partie.  - `createdBy[*]`: L'ID du SMUser qui a créé ce message.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `hasAnalysis[array]`: Les ID des SMAnalyses qui analysent ce poste.  - `hasHashtags[array]`: Les hashtags de la publication.  - `hasImages[array]`: Les URLs du contenu qui est sous forme d'image.  - `hasInteractionCount[array]`: Les différentes interactions de ce poste.  - `hasLanguage[string]`: La langue du poste.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasMentions[array]`: Les ID des SMUsers mentionnés dans ce post.  - `hasPostURL[string]`: L'URL de l'article.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasPrivacyLevel[string]`: Le paramètre de confidentialité du message.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasReferencedLocations[array]`: Les ID des lieux référencés dans ce post.  - `hasText[array]`: Le contenu qui est sous forme textuelle.  - `hasThumbnails[array]`: Les URL des vignettes de l'article.  - `hasVideos[array]`: Les URLs du contenu qui est sous forme de vidéo.  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `platform[string]`: Plate-forme du poste.  - `postCreatedAt[string]`: La date de création de la SMPost.  - `postId[string]`: L'ID du poste du SMPost.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI-LD. Il doit être égal à SMPost.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        model: ' https://schema.org/Text'    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    hasHashtags:    
      description: 'The hashtags of the post.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    hasImages:    
      description: 'The URLs of the content that is in image form.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    hasInteractionCount:    
      description: 'The different interactions of this post.'    
      items:    
        properties:    
          count:    
            type: number    
          interactionType:    
            enum:    
              - Comment    
              - Dislike    
              - Favorite    
              - Like    
              - Quote    
              - Reactions    
              - Reply    
              - Retweet    
              - Shares    
              - Views    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    hasLanguage:    
      description: 'The language of the post.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    hasPostURL:    
      description: 'The URL of the post.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
    hasPrivacyLevel:    
      description: 'The privacy setting of the post.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    hasText:    
      description: 'The content that is in textual form.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    hasThumbnails:    
      description: 'The thumbnail URLs of the post.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    hasVideos:    
      description: 'The URLs of the content that is in video form.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
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
        anyOf: *smpost_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    platform:    
      description: 'Platform of post.'    
      type: string    
      x-ngsi:    
        type: Property    
    postCreatedAt:    
      description: 'The datetime of the creation of the SMPost.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    postId:    
      description: 'The  post ID of the SMPost.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
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
      description: 'NGSI-LD Entity Type. It must be equal to SMPost.'    
      enum:    
        - SMPost    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - postCreatedAt    
    - postId    
    - platform    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SocialMedia/blob/master/SMPost/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/SMPost/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### SMPost NGSI-v2 key-values Exemple  
Voici un exemple d'un SMPost au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SMPost NGSI-v2 normalisé Exemple  
Voici un exemple d'un SMPost au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SMPost NGSI-LD key-values Exemple  
Voici un exemple d'un SMPost au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SMPost:123",  
    "type": "SMPost",  
    "belongsToCollection": [  
        "urn:ngsi-ld:SMCollection:001"  
    ],  
    "createdBy": "urn:ngsi-ld:SMUser:123",  
    "hasAnalysis": [  
        "urn:ngsi-ld:Analysis:X"  
    ],  
    "hasHashtags": [  
        "#sample",  
        "#tag"  
    ],  
    "hasImages": [  
        "https://twt.com/image.png"  
    ],  
    "hasInteractionCount": [  
        {  
            "interactionType": "Like",  
            "count": 762  
        }  
    ],  
    "hasLanguage": "en",  
    "hasMentions": [  
        "urn:ngsi-ld:SMUser:154"  
    ],  
    "hasPostURL": "http://twt.com/121",  
    "hasPrivacy": "public",  
    "hasReferencedLocations": [  
        "urn:ngsi-ld:RefLocation:00"  
    ],  
    "hasText": [  
        "This is a tweet"  
    ],  
    "hasThumbnails": [  
        "https://twt.com/thumb.png"  
    ],  
    "hasVideos": [  
        "https://twt.com/video.mp4"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            40.3,  
            25.5  
        ]  
    },  
    "platform": "Twitter",  
    "postCreatedAt": "2020-12-24T12:00:00Z",  
    "postId": "21098319",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SMPost NGSI-LD normalisé Exemple  
Voici un exemple d'un SMPost au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SMPost:123",  
    "type": "SMPost",  
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
    "createdBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SMUser:123"  
    },  
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
    "hasLanguage": {  
        "type": "Property",  
        "value": "en"  
    },  
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
    "hasPostURL": {  
        "type": "Property",  
        "value": "http://twt.com/121"  
    },  
    "hasPrivacyLevel": {  
        "type": "Property",  
        "value": "public"  
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
    "platform": {  
        "type": "Property",  
        "value": "Twitter"  
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
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
