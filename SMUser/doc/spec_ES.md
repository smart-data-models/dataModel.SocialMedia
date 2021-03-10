Entidad: SMUser  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMUser/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un SMUser genérico realizada para el dominio de los Medios Sociales. Esta entidad está asociada principalmente a la descripción de un usuario de aplicaciones de medios sociales.**  

## Lista de propiedades  

- `address`: La dirección postal  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `createdPost`: El ID del puesto que el SMUser creó.  - `isMentionedBy`: El ID de un post que menciona al SMUser.  - `location`:   - `platform`: Descripción de la plataforma social del usuario.  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a SMUser.  - `userId`: El ID de usuario del SMUser.  - `userName`: El nombre de usuario del SMUser.    
Propiedades requeridas  
- `id`  - `platform`  - `type`  - `userId`  - `userName`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### SMUser NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un SMUser en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### SMUser NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un SMUser en formato JSON normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### SMUser NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un SMUser en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### SMUser NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un SMUser en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
