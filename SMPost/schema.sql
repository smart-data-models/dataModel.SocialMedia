/* (Beta) Export of data model SMPost of the subject dataModel.SocialMedia for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SMPost_type AS ENUM ('SMPost');
CREATE TABLE SMPost (address json, alternateName text, areaServed text, belongsToCollection json, createdBy text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasAnalysis json, hasHashtags json, hasImages json, hasInteractionCount json, hasLanguage text, hasMentions json, hasPostURL text, hasPrivacyLevel text, hasReferencedLocations json, hasText json, hasThumbnails json, hasVideos json, id text, location json, name text, owner json, platform text, postCreatedAt timestamp, postId text, seeAlso json, source text, type SMPost_type);