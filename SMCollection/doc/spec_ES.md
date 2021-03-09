Entidad: SMCollection  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMCollection/LICENSE.md)  

## Lista de propiedades  

Propiedades requeridas  
- No hay propiedades requeridas  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
## Ejemplo de carga útil  
#### SMCollection NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de una SMCollection en formato JSON como valores-clave. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SMCollection:001",  
  "type": "SMCollection",  
  "description": "this is a collection of posts",  
  "location": {  
    "type": "Point",  
    "coordinates":   
	 [  
	  40.3,  
	  25.5  
	 ]  
	},  
  "hasPosts": ["urn:ngsi-ld:SMPost:125","urn:ngsi-ld:SMPost:124"],  
  "isAnalyzedBy": "urn:ngsi-ld:Analysis:331"  
}  
```  
No está disponible el ejemplo de una SMCollection en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SMCollection en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### SMCollection NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de una SMCollection en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
   "datasetId": "urn:ngsi-ld:Dataset:01"  
  },  
  {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:124",  
   "datasetId": "urn:ngsi-ld:Dataset:camera:01"  
  }  
  ],  
   "isAnalyzedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:Analysis:331"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
