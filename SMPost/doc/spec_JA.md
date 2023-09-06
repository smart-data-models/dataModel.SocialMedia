<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティSMPost  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.SocialMedia/blob/master/SMPost/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**このエンティティには、ソーシャルメディア領域用に作成された一般的な SMPost の調和された記述が含まれる。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `belongsToCollection[array]`: この投稿が属するSMCollectionsのID  - `createdBy[*]`: この投稿を作成したSMUserのID  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `hasAnalysis[array]`: この投稿を分析するSMAnalysesのID  - `hasHashtags[array]`: 投稿のハッシュタグ  - `hasImages[array]`: 画像形式のコンテンツのURL  - `hasInteractionCount[array]`: この記事のさまざまなやり取り  - `hasLanguage[string]`: ポストの言葉  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasMentions[array]`: この投稿で言及されたSMUsersのID  - `hasPostURL[string]`: 投稿のURL  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasPrivacyLevel[string]`: 投稿のプライバシー設定  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `hasReferencedLocations[array]`: この投稿で参照した場所のID  - `hasText[array]`: テキスト形式のコンテンツ  - `hasThumbnails[array]`: 投稿のサムネイルURL  - `hasVideos[array]`: ビデオ形式のコンテンツのURL  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `platform[string]`: ポストのプラットフォーム  - `postCreatedAt[date-time]`: SMPostが作成された日時。  - `postId[string]`: SMPostのポストID  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSI-LD エンティティタイプ。SMPost と等しくなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `platform`  - `postCreatedAt`  - `postId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### SMPost NGSI-v2 キー値の例  
SMPostをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### SMPost NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のSMPostの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "SMPost.123",  
  "type": "SMPost",  
  "hasPostURL": {  
    "type": "Property",  
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
    "type": "array",  
    "value": [  
      "This is a tweet"  
    ]  
  },  
  "hasImages": {  
    "type": "array",  
    "value": [  
      "https://twt.com/image.png"  
    ]  
  },  
  "hasVideos": {  
    "type": "array",  
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
    "type": "array",  
    "value": [  
      "#sample",  
      "#tag"  
    ]  
  },  
  "hasThumbnails": {  
    "type": "array",  
    "value": [  
      "https://twt.com/thumb.png"  
    ]  
  },  
  "createdBy": {  
    "type": "Relationship",  
    "object": "SMUser.123"  
  },  
  "hasReferencedLocations": {  
    "type": "Relationship",  
    "object": [  
      "RefLocation.00"  
    ]  
  },  
  "hasMentions": {  
    "type": "Relationship",  
    "object": [  
      "SMUser.154"  
      ]  
  },  
  "belongsToCollection": {  
    "type": "Relationship",  
    "object": [  
      "SMCollection.001",  
      "SMCollection.002"  
    ]  
  }  
}  
```  
</details>  
#### SMPost NGSI-LD キー値の例  
SMPostをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### SMPost NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のSMPostの例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
