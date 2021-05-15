Entité : SMCollection  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMCollection/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une SMCollection générique réalisée pour le domaine des médias sociaux. Cette entité est principalement associée au processus de collecte de messages de médias sociaux (principalement Twitter).**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Description générale de la collection SMC.  - `groupedAt`: La date et l'heure auxquelles la collection a été construite / regroupée.  - `hasAnalysis`: Les ID des SMAnalyses qui analysent ce SMCollection.  - `hasPosts`: Les ID des SMPost qui appartiennent à cette SMCollection.  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI-LD. Il doit être égal à SMCollection.    
Propriétés requises  
- `description`  - `hasPosts`  - `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SMCollection:    
  description: 'This entity contains a harmonised description of a generic SMCollection made for the Social Media domain. This entity is primarily associated with the process of collection of Social Media posts (primarily Twitter).'    
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
      description: 'General description of the SMCollection.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    groupedAt:    
      description: 'The date and time of when the collection was constructed / grouped.'    
      format: date-time    
      type: Property    
    hasAnalysis:    
      description: 'The IDs of the SMAnalyses that analyze this SMCollection.'    
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
      x-ngsi:    
        model: ' https://schema.org/Text'    
    hasPosts:    
      description: 'The IDs of the SMPost that belong in this SMCollection.'    
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
      x-ngsi:    
        model: ' https://schema.org/Text'    
    id:    
      anyOf: &smcollection_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *smcollection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to SMCollection.'    
      enum:    
        - SMCollection    
      type: Property    
  required:    
    - id    
    - type    
    - description    
    - hasPosts    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### SMCollection NGSI-v2 key-values Exemple  
Voici un exemple d'une collection SMCollection au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "SMCollection.001",  
  "type": "SMCollection",  
  "description": "this is a collection of posts",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "hasPosts": [  
    "SMPost.125",  
    "SMPost.124"  
  ],  
  "hasAnalysis": [  
    "Analysis.331",  
    "Analysis.334"  
  ]  
}  
```  
#### SMCollection NGSI-v2 normalisé Exemple  
Voici un exemple de SMCollection au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SMCollection:001",  
  "type": "SMCollection",  
  "description": {  
    "type": "Text",  
    "value": "this is a collection of posts"  
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
  "hasPosts": [  
    {  
      "type": "Relationship",  
      "object": "SMPost.125"  
    },  
    {  
      "type": "Relationship",  
      "object": "SMPost.124"  
    }  
  ],  
  "isAnalyzedBy": {  
    "type": "Relationship",  
    "object": "Analysis.331"  
  }  
}  
```  
#### SMCollection Valeurs-clés NGSI-LD Exemple  
Voici un exemple de SMCollection au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SMCollection:001",  
  "type": "SMCollection",  
  "description": "this is a collection of posts",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "hasPosts": [  
    "urn:ngsi-ld:SMPost:125",  
    "urn:ngsi-ld:SMPost:124"  
  ],  
  "isAnalyzedBy": ["urn:ngsi-ld:Analysis:331"],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SMCollection NGSI-LD normalisé Exemple  
Voici un exemple de SMCollection au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SMCollection:001",  
  "type": "SMCollection",  
  "description": {  
    "type": "Property",  
    "value": "this is a collection of posts"  
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
  "hasPosts": [  
  {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:125",  
   "datasetId": "urn:ngsi-ld:Dataset:SMPost:125"  
  },  
  {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:124",  
   "datasetId": "urn:ngsi-ld:Dataset:SMPost:124"  
  }  
  ],  
   "hasAnalysis": [  
   {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMAnalysis:331"  
   "datasetId": "urn:ngsi-ld:Dataset:SMAnalysis:331"	     
   },  
   {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMAnalysis:332"  
   "datasetId": "urn:ngsi-ld:Dataset:SMAnalysis:332"	     
   }],  
    "groupedAt": {  
    "type": "Property",  
    "value": {  
			"@type": "DateTime",  
			"@value": "2020-12-24T12:00:00Z"  
			 }		  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
