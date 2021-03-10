Entidad: SMPost  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un SMPost genérico realizado para el dominio de los medios sociales.**  

## Lista de propiedades  

- `address`: La dirección postal  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `belongsToCollection`: El ID de la SMCollection, de la que forma parte este puesto.  - `createdBy`: El ID del SMUser que creó esta entrada.  - `hasHashtag`: Los hashtags del post.  - `hasImage`: La URL de la imagen de la entrada.  - `hasLanguage`: El lenguaje del puesto.  - `hasMentions`: El ID del SMUser que tiene menciones en este post.  - `hasPostURL`: La URL del puesto.  - `hasPrivacy`: La configuración de privacidad del puesto.  - `hasReferencedLocation`: El ID de la ubicación referenciada de este puesto.  - `hasText`: El texto del puesto.  - `hasThumbnail`: La URL en miniatura de la entrada.  - `hasVideo`: La URL del vídeo del puesto.  - `isAnalyzedBy`: El ID del SMAnalysis que analiza este puesto.  - `likes`: El número de "likes" de la publicación. Todas las unidades se aceptan en código [CEFACT](https://www.unece.org/cefact.html).  - `location`:   - `platform`: Plataforma del puesto.  - `postCreatedAt`:   - `postId`: El ID del puesto de SMPost.  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a SMPost.    
Propiedades requeridas  
- `id`  - `location`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### SMPost NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un SMPost en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
No está disponible el ejemplo de un SMPost en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un SMPost en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### SMPost NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un SMPost en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
