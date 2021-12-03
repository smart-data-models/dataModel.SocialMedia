Entità: SMAnalysis  
==================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMAnalysis/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una generica SMAnalysis fatta per il dominio dei Social Media. Questa entità è principalmente associata al processo di analisi dei post delle applicazioni dei Social Media **.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `analyzedAt`: Il momento in cui l'analisi è finita  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `hasAnalysisType`: Il valore dell'analisi.  - `hasAnalysisValue`: Il tipo di analisi.  - `hasConfidence`: Rappresenta la fiducia dell'analisi. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  - `id`: Identificatore unico dell'entità  - `isAnalysisOf`: L'ID del post che è stato utilizzato nell'analisi.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI-LD. Deve essere uguale a SMAnalysis.    
Proprietà richieste  
- `analyzedAt`  - `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
    analyzedAt:    
      format: date-time    
      type: string    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    hasAnalysisType:    
      description: 'The value of the analysis.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
        units: 'No unit'    
    hasAnalysisValue:    
      description: 'The type of the analysis.'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
        units: 'No unit'    
    hasConfidence:    
      description: 'It represents the confidence of the analysis. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: 'No unit'    
    id:    
      anyOf: &smanalysis_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *smanalysis_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
      description: 'NGSI-LD Entity Type. It must be equal to SMAnalysis.'    
      enum:    
        - SMAnalysis    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - analyzedAt    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SocialMedia/blob/master/SMAnalysis/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/SMAnalysis/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## Esempio di payloads  
#### SMAnalysis NGSI-v2 valori chiave Esempio  
Ecco un esempio di una SMAnalysis in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### SMAnalysis NGSI-v2 normalizzato Esempio  
Ecco un esempio di una SMAnalysis in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### SMAnalysis NGSI-LD key-values Esempio  
Ecco un esempio di una SMAnalysis in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### SMAnalysis NGSI-LD normalizzato Esempio  
Ecco un esempio di una SMAnalysis in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza