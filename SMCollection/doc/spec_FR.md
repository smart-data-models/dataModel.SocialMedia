Entité : SMCollection  
=====================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMCollection/LICENSE.md)  

## Liste des biens  

Propriétés requises  
- Aucune propriété requise  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
## Exemples de charges utiles  
#### SMCollection NGSI V2 valeurs clés Exemple  
Voici un exemple de collection SMC au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Non disponible l'exemple d'une collection SMC en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une collection SMC au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### SMCollection NGSI-LD normalisé Exemple  
Voici un exemple de collection SMC au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
