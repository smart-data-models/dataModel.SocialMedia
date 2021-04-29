Entidad: SMAnalysis  
===================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMAnalysis/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un SMAnalysis genérico realizado para el dominio de los Medios Sociales. Esta entidad está asociada principalmente al proceso de análisis de las publicaciones de las aplicaciones de los medios sociales.**  

## Lista de propiedades  

- `address`: La dirección postal  - `analyzedAt`:   - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `hasAnalysisType`: El valor del análisis.  - `hasAnalysisValue`: El tipo de análisis.  - `hasConfidence`: Representa la confianza del análisis. Todas las unidades se aceptan en código [CEFACT](https://www.unece.org/cefact.html).  - `isAnalysisOf`: El ID del puesto que se utilizó en el análisis.  - `location`:   - `type`: Tipo de entidad NGSI-LD. Debe ser igual a SMAnalysis.    
Propiedades requeridas  
- `analyzedAt`  - `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SMAnalysis:    
  description: 'This entity contains a harmonised description of a generic SMAnalysis made for the Social Media domain. This entity is primarily associated with the process of analysis of Social Media applications'' posts.'    
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
    analyzedAt:    
      format: date-time    
      type: string    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hasAnalysisType:    
      description: 'The value of the analysis.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasAnalysisValue:    
      description: 'The type of the analysis.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    hasConfidence:    
      description: 'It represents the confidence of the analysis. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: 'No unit'    
    isAnalysisOf:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID of the post that was used in the analysis.'    
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
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to SMAnalysis.'    
      enum:    
        - SMAnalysis    
      type: Property    
  required:    
    - id    
    - type    
    - analyzedAt    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### SMAnalysis NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un SMAnalysis en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": 0.4,  
  "analyzedAt": "2020-12-24T12:00:00Z",  
  "hasAnalysisValue": "Anger",  
  "hasAnalysisType": "Sentiment",  
  "isAnalysisOf": "urn:ngsi-ld:SMCollection:001"  
}  
```  
#### SMAnalysis NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un SMAnalysis en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "analyzedAt": {  
    "type": "DateTime",  
    "value": "2020-12-24T12:00:00Z"  
  },  
  "hasAnalysisValue": {  
    "type": "Text",  
    "value": "Anger"  
  },  
  "hasAnalysisType": {  
    "type": "Text",  
    "value": "Sentiment"  
  },  
  "isAnalysisOf": {  
    "type": "Relationship",  
    "object": "SMCollection.001"  
  }  
}  
```  
#### SMAnalysis NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un SMAnalysis en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": 0.4,  
  "analyzedAt": "2020-12-24T12:00:00Z",  
  "hasAnalysisValue": "Anger",  
  "hasAnalysisType": "Sentiment",  
  "isAnalysisOf": "urn:ngsi-ld:SMCollection:001",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SMAnalysis NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un SMAnalysis en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Analysis:X",  
  "type": "SMAnalysis",  
  "hasConfidence": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "analyzedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "hasAnalysisValue": {  
    "type": "Property",  
    "value": "Anger"  
  },  
  "hasAnalysisType": {  
    "type": "Property",  
    "value": "Sentiment"  
  },  
  "isAnalysisOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SMCollection:001"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
