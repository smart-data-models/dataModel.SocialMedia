Entité : SMPost  
===============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un SMPost générique réalisé pour le domaine des médias sociaux.**  

## Liste des biens  

- `address`: L'adresse postale  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `belongsToCollection`: L'identifiant de la collection SMC, dont ce poste fait partie.  - `createdBy`: L'identifiant de l'utilisateur qui a créé ce poste.  - `hasHashtag`: Les hashtags du poste.  - `hasImage`: L'URL de l'image du billet.  - `hasLanguage`: La langue du poste.  - `hasMentions`: L'identifiant de l'utilisateur qui est mentionné dans ce post.  - `hasPostURL`: L'URL du poste.  - `hasPrivacy`: Le paramètre de confidentialité du poste.  - `hasReferencedLocation`: L'ID de l'emplacement référencé de ce poste.  - `hasText`: Le texte du poste.  - `hasThumbnail`: La vignette URL de l'article.  - `hasVideo`: L'URL de la vidéo du poste.  - `isAnalyzedBy`: L'ID de la SMAnalyse qui analyse ce billet.  - `likes`: Le nombre d'articles similaires au poste. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `location`:   - `platform`: Plate-forme de poste.  - `postCreatedAt`:   - `postId`: Le numéro de poste du SMPost.  - `type`: Type d'entité NGSI-LD. Il doit être égal à SMPost.    
Propriétés requises  
- `id`  - `location`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    belongsToCollection:    
      description: 'The ID of the SMCollection, which this post is a part of.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    createdBy:    
      description: 'The ID of the SMUser that created this post.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasHashtag:    
      description: 'The hashtags of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasImage:    
      description: 'The image URL of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasLanguage:    
      description: 'The language of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasMentions:    
      description: 'The ID of the SMUser that has mentions in this post.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasPostURL:    
      description: 'The URL of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasPrivacy:    
      description: 'The privacy setting of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasReferencedLocation:    
      description: 'The ID of the referenced location of this post.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasText:    
      description: 'The text of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasThumbnail:    
      description: 'The thumbnail URL of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasVideo:    
      description: 'The video URL of the post.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    isAnalyzedBy:    
      description: 'The ID of the SMAnalysis that analyzes this post.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    likes:    
      description: 'The number of likes of the post. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: 'No unit'    
    location:    
      $id: https://geojson.org/schema/Point.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
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
    platform:    
      description: 'Platform of post.'    
      type: Property    
    postCreatedAt:    
      format: date-time    
      type: string    
    postId:    
      description: 'The  post ID of the SMPost.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
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
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### SMPost NGSI V2 valeurs clés Exemple  
Voici un exemple de SMPost au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SMPost:123",  
  "type": "SMPost",  
  "hasPostURL": "http://twt.com/121",  
  "postCreatedAt": "2020-12-24T12:00:00Z",  
  "postId": "21098319",  
  "hasLanguage": "en",  
  "platform": "Twitter",  
  "hasText": "This is a tweet",  
  "hasImage": "https://twt.com/image.png",  
  "hasVideo": "https://twt.com/video.mp4",  
  "hasPrivacy": "public",  
  "location": {  
    "type": "Point",  
	"coordinates":   
	 [  
	  40.3,  
	  25.5  
	 ]  
	},  
  "hasHashtag": "[#sample,#tag]",  
  "hasThumbnail": "https://twt.com/thumb.png",  
  "likes": 762,  
  "createdBy": "urn:ngsi-ld:SMUser:123",  
  "hasReferencedLocation": "urn:ngsi-ld:RefLocation:00",  
  "hasMentions": "urn:ngsi-ld:SMUser:154",  
  "isAnalyzedBy": "urn:ngsi-ld:Analysis:X",  
  "belongsToCollection": "urn:ngsi-ld:SMCollection:001"  
}  
```  
Non disponible l'exemple d'un SMPost en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un SMPost en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### SMPost NGSI-LD normalisé Exemple  
Voici un exemple de SMPost au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
  "hasText": {  
    "type": "Property",  
    "value": "This is a tweet"  
  },  
  "hasImage": {  
    "type": "Property",  
    "value": "https://twt.com/image.png"  
  },  
  "hasVideo": {  
    "type": "Property",  
    "value": "https://twt.com/video.mp4"  
  },  
  "hasPrivacy": {  
    "type": "Property",  
    "value": "public"  
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
  "hasHashtag": {  
    "type": "Property",  
    "value": "[#sample,#tag]"  
  },  
  "hasThumbnail": {  
    "type": "Property",  
    "value": "https://twt.com/thumb.png"  
  },  
  "likes": {  
    "type": "Property",  
    "value": 762  
  },  
  "createdBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMUser:123"  
   },  
   "hasReferencedLocation": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:RefLocation:00"  
   },  
   "hasMentions": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMUser:154"  
   },  
   "isAnalyzedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:Analysis:X"  
   },  
   "belongsToCollection": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMCollection:001"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
