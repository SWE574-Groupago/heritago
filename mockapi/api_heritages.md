FORMAT: 1A

# Heritago Api
This is the Api Blueprint version of the heritago rest api design.
[Wiki Page](https://github.com/SWE574-Groupago/heritago/wiki/REST-API)

**Note:** This file may need updates

For more info on Api Blueprint [Docs](https://apiblueprint.org/documentation/)


# GET /heritages/{id}
+ Parameters
  + id (string)

+ Response 200 (application/json)

        {
          "id": 1,
          "description": "",
          "title": "",
          "createdAt": "2017-01-19 11:11:11+3",
          "basicInformation": [
            {
              "key": "completed",
              "value": "1991"
            },
            {
              "key": "author",
              "value": "Namik Kemal"
            }
          ],
          "origins": [
            "Turkish",
            "Hittit"
          ],
          "tags": [
            "building",
            "history",
            "food"
          ],
          "annotationCount": 32,
          "owner": {
            "id": 1,
            "name": "Suzan U."
          },
          "multimedia": [
            {
              "type": "image",
              "id": 132,
              "url": "http://www.heritago.com/heritages/1/images/132.png",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "video",
              "id": 51,
              "url": "http://www.heritago.com/heritages/1/videos/51.mp4",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "audio",
              "id": 22,
              "url": "http://www.heritago.com/heritages/1/audio/22.mp3",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "location",
              "id": 61,
              "url": "http://www.heritago.com/heritages/1/videos/51.png",
              "createdAt": "2017-01-19 11:11:12+3",
              "selector": {
                "type": "polygon",
                "value": {
                  "latlongs": [
                    [
                      12.2,
                      58.7
                    ],
                    [
                      71.5,
                      95.4
                    ]
                  ]
                }
              }
            }
          ]
        }


# GET /heritages?{title,owner}

+ Parameters
  + title (string)
  + owner (string)

+ Response 200 (application/json)

      [
        {
          "id": 2,
          "description": "",
          "title": "",
          "createdAt": "2017-01-19 11:11:11+3",
          "basicInformation": [
            {
              "key": "completed",
              "value": "1991"
            },
            {
              "key": "author",
              "value": "Namik Kemal"
            }
          ],
          "origins": [
            "Turkish",
            "Hittit"
          ],
          "tags": [
            "building",
            "history",
            "food"
          ],
          "annotationCount": 32,
          "owner": {
            "id": 1,
            "name": "Suzan U."
          },
          "multimedia": [
            {
              "type": "image",
              "id": 132,
              "url": "http://www.heritago.com/heritages/1/images/132.png",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "video",
              "id": 51,
              "url": "http://www.heritago.com/heritages/1/videos/51.mp4",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "audio",
              "id": 22,
              "url": "http://www.heritago.com/heritages/1/audio/22.mp3",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "location",
              "id": 61,
              "url": "http://www.heritago.com/heritages/1/videos/51.png",
              "createdAt": "2017-01-19 11:11:12+3",
              "selector": {
                "type": "polygon",
                "value": {
                  "latlongs": [
                    [
                      12.2,
                      58.7
                    ],
                    [
                      71.5,
                      95.4
                    ]
                  ]
                }
              }
            }
          ]
        },
        {
          "id": 1,
          "description": "",
          "title": "",
          "createdAt": "2017-01-19 11:11:11+3",
          "basicInformation": [
            {
              "key": "completed",
              "value": "1991"
            },
            {
              "key": "author",
              "value": "Namik Kemal"
            }
          ],
          "origins": [
            "Turkish",
            "Hittit"
          ],
          "tags": [
            "building",
            "history",
            "food"
          ],
          "annotationCount": 32,
          "owner": {
            "id": 1,
            "name": "Suzan U."
          },
          "multimedia": [
            {
              "type": "image",
              "id": 132,
              "url": "http://www.heritago.com/heritages/1/images/132.png",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "video",
              "id": 51,
              "url": "http://www.heritago.com/heritages/1/videos/51.mp4",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "audio",
              "id": 22,
              "url": "http://www.heritago.com/heritages/1/audio/22.mp3",
              "createdAt": "2017-01-19 11:11:12+3"
            },
            {
              "type": "location",
              "id": 61,
              "url": "http://www.heritago.com/heritages/1/videos/51.png",
              "createdAt": "2017-01-19 11:11:12+3",
              "selector": {
                "type": "polygon",
                "value": {
                  "latlongs": [
                    [
                      12.2,
                      58.7
                    ],
                    [
                      71.5,
                      95.4
                    ]
                  ]
                }
              }
            }
          ]
        }
      ]

# GET /heritages/{id}/annotations
+ Parameters
  + id (string)

+ Response 200 (application/json)

      {
        "heritageId": 1,
        "votes": {
          "http://example.org/anno11": {
            "up": 9,
            "down": 4,
            "you": -1
          },
          "http://example.org/anno12": {
            "up": 5,
            "down": 7,
            "you": 0
          },
          "http://example.org/anno13": {
            "up": 9,
            "down": 5,
            "you": 1
          }
        },
        "annotations": [
          {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": "http://example.org/anno11",
            "type": "Annotation",
            "creator": "http://574heritago.com/users/25/",
            "created": "2017-01-02T17:00:00Z",
            "body": {
              "type": "Text",
              "value": "The gate was built in 1829.",
              "format": "text/plain"
            },
            "target": {
              "id": "http://574heritago.com/heritages/3#description",
              "type": "Text",
              "format": "text/plain",
              "selector": {
                "type": "substring",
                "value": {
                  "starts": 10,
                  "length": 30
                }
              }
            }
          },
          {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": "http://example.org/anno11",
            "type": "Annotation",
            "creator": "http://574heritago.com/users/25/",
            "created": "2017-01-02T17:00:00Z",
            "body": {
              "type": "Image",
              "format": "image/png",
              "source": "http://574heritago.com/resources/images/2/"
            },
            "target": {
              "id": "http://574heritago.com/heritages/3#description",
              "type": "Text",
              "format": "text/plain",
              "selector": {
                "type": "substring",
                "value": {
                  "starts": 10,
                  "length": 30
                }
              }
            }
          },
          {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": "http://example.org/anno11",
            "type": "Annotation",
            "creator": "http://574heritago.com/users/25/",
            "created": "2017-01-02T17:00:00Z",
            "body": {
              "type": "Video",
              "format": "audio/mpeg",
              "source": "http://574heritago.com/resources/videos/2/"
            },
            "target": {
              "id": "http://574heritago.com/heritages/3#description",
              "type": "Text",
              "format": "text/plain",
              "selector": {
                "type": "substring",
                "value": {
                  "starts": 10,
                  "length": 30
                }
              }
            }
          },
          {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": "http://example.org/anno11",
            "type": "Annotation",
            "creator": "http://574heritago.com/users/25/",
            "created": "2017-01-02T17:00:00Z",
            "body": {
              "type": "Location",
              "format": "text/plain",
              "source": "http://map.com/?someselection"
            },
            "target": {
              "id": "http://574heritago.com/heritages/3#description",
              "type": "Text",
              "format": "text/plain",
              "selector": {
                "type": "substring",
                "value": {
                  "starts": 10,
                  "length": 30
                }
              }
            }
          },
          {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "id": "http://example.org/anno11",
            "type": "Annotation",
            "creator": "http://574heritago.com/users/25/",
            "created": "2017-01-02T17:00:00Z",
            "body": {
              "type": "Audio",
              "format": "audio/mp3",
              "source": "http://574heritago.com/resources/90/"
            },
            "target": {
              "id": "http://574heritago.com/heritages/3#description",
              "type": "Text",
              "format": "text/plain",
              "selector": {
                "type": "substring",
                "value": {
                  "starts": 10,
                  "length": 30
                }
              }
            }
          }
        ]
      }

# POST /heritages/{id}/annotations

+ Parameters
  + id (string)
  + @context (json)
  + type (string)
  + body (json)
  + target (json)

+ Response 200 (application/json)

        {
          "@context": "http://www.w3.org/ns/anno.jsonld",
          "type": "Annotation",
          "creator": "http://574heritago.com/users/25/",
          "created": "2017-01-02T17:00:00Z",
          "id": "http://574heritago.com/heritages/1/annotations/4",
          "body": {
            "type": "Text",
            "value": "The gate was built in 1829.",
            "format": "text/plain"
          },
          "target": {
            "id": "http://574heritago.com/heritages/3#description",
            "type": "Text",
            "format": "text/plain",
            "selector": {
              "type": "substring",
              "value": {
                "starts": 10,
                "length": 30
              }
            }
          }
        }

# POST /heritages/{id}/annotations/{annotationId}/votes

+ Parameters
  + id (string)
  + annotationId (string)
  + vote (number)

+ Response 200
