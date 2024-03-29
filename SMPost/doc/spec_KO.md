<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: SMPost    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **이 엔티티에는 소셜 미디어 도메인용으로 만들어진 일반 SMPost에 대한 조화로운 설명이 포함되어 있습니다.**    
버전: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `belongsToCollection[array]`: 이 게시물이 속해 있는 SMCollections의 ID는 다음과 같습니다.  - `createdBy[*]`: 이 게시물을 만든 SMUser의 아이디입니다.  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasAnalysis[array]`: 이 게시물을 분석하는 SMAnalyses의 ID  - `hasHashtags[array]`: 게시물의 해시태그  - `hasImages[array]`: 이미지 형식인 콘텐츠의 URL  - `hasInteractionCount[array]`: 이 게시물의 다양한 상호작용  - `hasLanguage[string]`: 게시물의 언어  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasMentions[array]`: 이 게시물에 언급된 SMU 사용자의 ID는 다음과 같습니다.  - `hasPostURL[string]`: 게시물의 URL  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasPrivacyLevel[string]`: 게시물의 개인정보 보호 설정  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasReferencedLocations[array]`: 이 게시물에 언급된 위치의 ID는 다음과 같습니다.  - `hasText[array]`: 텍스트 형식의 콘텐츠  - `hasThumbnails[array]`: 글의 썸네일 URL  - `hasVideos[array]`: 동영상 형식의 콘텐츠 URL  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `platform[string]`: 포스트 플랫폼  - `postCreatedAt[date-time]`: SMPost를 생성한 날짜 시간입니다.  - `postId[string]`: SMPost의 게시물 ID  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI-LD 엔티티 유형. SMPost와 같아야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SMPost:      
  description: This entity contains a harmonised description of a generic SMPost made for the Social Media domain.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    belongsToCollection:      
      description: 'The IDs of the SMCollections, which this post is a part of'      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    createdBy:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: The ID of the SMUser that created this post      
      x-ngsi:      
        model: ' https://schema.org/Text'      
        type: Relationship      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    hasAnalysis:      
      description: The IDs of the SMAnalyses that analyze this post      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    hasHashtags:      
      description: The hashtags of the post      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    hasImages:      
      description: The URLs of the content that is in image form      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    hasInteractionCount:      
      description: The different interactions of this post      
      items:      
        properties:      
          count:      
            type: number      
          interactionType:      
            enum:      
              - Comment      
              - Dislike      
              - Favorite      
              - Like      
              - Quote      
              - Reactions      
              - Reply      
              - Retweet      
              - Shares      
              - Views      
            type: string      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    hasLanguage:      
      description: The language of the post      
      type: string      
      x-ngsi:      
        model: ' https://schema.org/Text'      
        type: Property      
    hasMentions:      
      description: The IDs of the SMUsers mentioned in this post      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    hasPostURL:      
      description: The URL of the post      
      type: string      
      x-ngsi:      
        model: ' https://schema.org/Text'      
        type: Property      
    hasPrivacyLevel:      
      description: The privacy setting of the post      
      type: string      
      x-ngsi:      
        model: ' https://schema.org/Text'      
        type: Property      
    hasReferencedLocations:      
      description: The IDs of the locations referenced in this post      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    hasText:      
      description: The content that is in textual form      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    hasThumbnails:      
      description: The thumbnail URLs of the post      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    hasVideos:      
      description: The URLs of the content that is in video form      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    platform:      
      description: Platform of post      
      type: string      
      x-ngsi:      
        type: Property      
    postCreatedAt:      
      description: The datetime of the creation of the SMPost      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    postId:      
      description: The  post ID of the SMPost      
      type: string      
      x-ngsi:      
        model: ' https://schema.org/Text'      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It must be equal to SMPost      
      enum:      
        - SMPost      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - postCreatedAt      
    - postId      
    - platform      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.SocialMedia/blob/master/SMPost/LICENSE.md      
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/SMPost/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### SMPost NGSI-v2 키-값 예시    
다음은 JSON-LD 형식의 SMPost를 키-값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "SMPost.123",  
  "type": "SMPost",  
  "hasPostURL": "http://twt.com/121",  
  "postCreatedAt": "2020-12-24T12:00:00Z",  
  "postId": "21098319",  
  "hasLanguage": "en",  
  "platform": "Twitter",  
  "hasText": [  
    "This is a tweet",  
    "This is another tweet"  
  ],  
  "hasImages": [  
    "https://twt.com/image.png",  
    "https://twt.com/image2.png",  
    "https://twt.com/image3.png"  
  ],  
  "hasVideos": [  
    "https://twt.com/video.mp4",  
    "https://twt.com/video2.mp4"  
  ],  
  "hasPrivacyLevel": "public",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "hasHashtags": [  
    "#sample",  
    "#tag"  
  ],  
  "hasThumbnails": [  
    "https://twt.com/thumb.png",  
    "https://twt.com/thumb2.png"  
  ],  
  "hasInteractionCount": [  
    {  
      "interactionType": "Like",  
      "count": 750  
    },  
    {  
      "interactionType": "Views",  
      "count": 2150  
    }  
  ],  
  "hasReferencedLocations": [  
    "RefLocation.00",  
    "RefLocation.01"  
  ],  
  "hasMentions": [  
    "SMUser.154",  
    "SMUser.155",  
    "SMUser.156"  
  ],  
  "hasAnalysis": [  
    "Analysis.X",  
    "Analysis.X2"  
  ],  
  "createdBy": "SMUser.123",  
  "belongsToCollection": [  
    "SMCollection.001",  
    "SMCollection.002"  
  ]  
}  
```  
</details>    
#### SMPost NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SMPost의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "SMPost.123",  
  "type": "SMPost",  
  "hasPostURL": {  
    "type": "Text",  
    "value": "http://twt.com/121"  
  },  
  "postCreatedAt": {  
    "type": "DateTime",  
    "value": "2020-12-24T12:00:00Z"  
  },  
  "postId": {  
    "type": "Text",  
    "value": "21098319"  
  },  
  "hasLanguage": {  
    "type": "Text",  
    "value": "en"  
  },  
  "platform": {  
    "type": "Text",  
    "value": "Twitter"  
  },  
  "hasText": {  
    "type": "StructuredValue",  
    "value": [  
      "This is a tweet"  
    ]  
  },  
  "hasImages": {  
    "type": "StructuredValue",  
    "value": [  
      "https://twt.com/image.png"  
    ]  
  },  
  "hasVideos": {  
    "type": "StructuredValue",  
    "value": [  
      "https://twt.com/video.mp4"  
    ]  
  },  
  "hasPrivacyLevel": {  
    "type": "Text",  
    "value": "public"  
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
  "hasHashtag": {  
    "type": "StructuredValue",  
    "value": [  
      "#sample",  
      "#tag"  
    ]  
  },  
  "hasThumbnails": {  
    "type": "StructuredValue",  
    "value": [  
      "https://twt.com/thumb.png"  
    ]  
  },  
  "createdBy": {  
    "type": "Text",  
    "value": "SMUser.123"  
  },  
  "hasReferencedLocations": {  
    "type": "StructuredValue",  
    "value": [  
      "RefLocation.00"  
    ]  
  },  
  "hasMentions": {  
    "type": "StructuredValue",  
    "value": [  
      "SMUser.154"  
    ]  
  },  
  "belongsToCollection": {  
    "type": "StructuredValue",  
    "value": [  
      "SMCollection.001",  
      "SMCollection.002"  
    ]  
  }  
}  
```  
</details>    
#### SMPost NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 SMPost 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SMPost:123",  
  "type": "SMPost",  
  "belongsToCollection": [  
    "urn:ngsi-ld:SMCollection:001"  
  ],  
  "createdBy": "urn:ngsi-ld:SMUser:123",  
  "hasAnalysis": [  
    "urn:ngsi-ld:Analysis:X"  
  ],  
  "hasHashtags": [  
    "#sample",  
    "#tag"  
  ],  
  "hasImages": [  
    "https://twt.com/image.png"  
  ],  
  "hasInteractionCount": [  
    {  
      "interactionType": "Like",  
      "count": 762  
    }  
  ],  
  "hasLanguage": "en",  
  "hasMentions": [  
    "urn:ngsi-ld:SMUser:154"  
  ],  
  "hasPostURL": "http://twt.com/121",  
  "hasPrivacy": "public",  
  "hasReferencedLocations": [  
    "urn:ngsi-ld:RefLocation:00"  
  ],  
  "hasText": [  
    "This is a tweet"  
  ],  
  "hasThumbnails": [  
    "https://twt.com/thumb.png"  
  ],  
  "hasVideos": [  
    "https://twt.com/video.mp4"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.3,  
      25.5  
    ]  
  },  
  "platform": "Twitter",  
  "postCreatedAt": "2020-12-24T12:00:00Z",  
  "postId": "21098319",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SMPost NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SMPost의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:SMPost:123",  
    "type": "SMPost",  
    "belongsToCollection": [  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:SMCollection:001",  
            "datasetId": "urn:ngsi-ld:Dataset:SMCollection:001"  
        },  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:SMCollection:002",  
            "datasetId": "urn:ngsi-ld:Dataset:SMCollection:002"  
        }  
    ],  
    "createdBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SMUser:123"  
    },  
    "hasAnalysis": [  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Analysis:X",  
            "datasetId": "urn:ngsi-ld:Dataset:Analysis:X"  
        },  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Analysis:02",  
            "datasetId": "urn:ngsi-ld:Dataset:Analysis:02"  
        }  
    ],  
    "hasHashtags": [  
        {  
            "type": "Property",  
            "value": [  
                "#sample",  
                "#tag"  
            ]  
        },  
        {  
            "type": "Property",  
            "value": [  
                "#sample2",  
                "#tag2"  
            ]  
        }  
    ],  
    "hasImages": [  
        {  
            "type": "Property",  
            "value": "https://twt.com/image.png"  
        },  
        {  
            "type": "Property",  
            "value": "https://twt.com/image2.png"  
        }  
    ],  
    "hasInteractionCount": [  
        {  
            "type": "Property",  
            "value": {  
                "@interactionType": "Like",  
                "@count": "750"  
            }  
        },  
        {  
            "type": "Property",  
            "value": {  
                "@interactionType": "Views",  
                "@count": "2150"  
            }  
        }  
    ],  
    "hasLanguage": {  
        "type": "Property",  
        "value": "en"  
    },  
    "hasMentions": [  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:SMUser:154",  
            "datasetId": "urn:ngsi-ld:Dataset:SMUser:154"  
        },  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:SMUser:155",  
            "datasetId": "urn:ngsi-ld:Dataset:SMUser:155"  
        }  
    ],  
    "hasPostURL": {  
        "type": "Property",  
        "value": "http://twt.com/121"  
    },  
    "hasPrivacyLevel": {  
        "type": "Property",  
        "value": "public"  
    },  
    "hasReferencedLocations": [  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:RefLocation:00",  
            "datasetId": "urn:ngsi-ld:Dataset:RefLocation:00"  
        },  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:RefLocation:01",  
            "datasetId": "urn:ngsi-ld:Dataset:RefLocation:01"  
        }  
    ],  
    "hasText": [  
        {  
            "type": "Property",  
            "value": "This is a tweet."  
        },  
        {  
            "type": "Property",  
            "value": "This is another tweet."  
        }  
    ],  
    "hasThumbnails": [  
        {  
            "type": "Property",  
            "value": "https://twt.com/thumb.png"  
        },  
        {  
            "type": "Property",  
            "value": "https://twt.com/thumb2.png"  
        }  
    ],  
    "hasVideos": [  
        {  
            "type": "Property",  
            "value": "https://twt.com/video.mp4"  
        },  
        {  
            "type": "Property",  
            "value": "https://twt.com/video2.mp4"  
        }  
    ],  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                40.3,  
                25.5  
            ]  
        }  
    },  
    "platform": {  
        "type": "Property",  
        "value": "Twitter"  
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
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SocialMedia/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
