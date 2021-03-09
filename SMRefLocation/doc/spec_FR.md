Entité : SMRefLocation  
======================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMRefLocation/LICENSE.md)  

## Liste des biens  

Propriétés requises  
- Aucune propriété requise  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
## Exemples de charges utiles  
#### SMRefLocation NGSI V2 Exemple de valeurs clés  
Voici un exemple de SMRefLocation au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Non disponible l'exemple d'une SMRefLocation en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une SMRefLocation au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### SMRefLocation NGSI-LD normalisé Exemple  
Voici un exemple de SMRefLocation au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
