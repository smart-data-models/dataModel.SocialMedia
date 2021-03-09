Entidad: SMRefLocation  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMRefLocation/LICENSE.md)  

## Lista de propiedades  

Propiedades requeridas  
- No hay propiedades requeridas  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
## Ejemplo de carga útil  
#### SMRefLocation NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un SMRefLocation en formato JSON como valores-clave. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RefLocation:00",  
  "type": "SMRefLocation",  
  "locationName": "Thessaloniki",  
  "location": {  
    "type": "Point",  
	"coordinates":   
	 [  
	  40.3,  
	  25.5  
	 ]  
	},  
  "locationReferencedBy": "urn:ngsi-ld:SMPost:123"  
}  
```  
No está disponible el ejemplo de un SMRefLocation en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una SMRefLocation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### SMRefLocation NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un SMRefLocation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RefLocation:00",  
  "type": "SMRefLocation",  
  "locationName": {  
    "type": "Property",  
    "value": "Thessaloniki"  
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
  "locationReferencedBy": {  
   "type": "Relationship",  
   "object": "urn:ngsi-ld:SMPost:123"  
   },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
