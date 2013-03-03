CREATE TABLE `questions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PostTypeId` int(11) DEFAULT NULL,
  `AcceptedAnswerId` int(11) DEFAULT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `CreationDate` datetime DEFAULT NULL,
  `Score` int(11) DEFAULT NULL,
  `ViewCount` int(11) DEFAULT NULL,
  `OwnerUserId` int(11) DEFAULT NULL,
  `Tags` varchar(45) DEFAULT NULL,
  `AnswerCount` int(11) DEFAULT NULL,
  `CommentCount` int(11) DEFAULT NULL,
  `FavouriteCount` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `accepted_answers` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PostTypeId` int(11) DEFAULT NULL,
  `AcceptedAnswerId` int(11) DEFAULT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `CreationDate` datetime DEFAULT NULL,
  `Score` int(11) DEFAULT NULL,
  `ViewCount` int(11) DEFAULT NULL,
  `OwnerUserId` int(11) DEFAULT NULL,
  `Tags` varchar(45) DEFAULT NULL,
  `AnswerCount` int(11) DEFAULT NULL,
  `CommentCount` int(11) DEFAULT NULL,
  `FavouriteCount` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `answers` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PostTypeId` int(11) DEFAULT NULL,
  `AcceptedAnswerId` int(11) DEFAULT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `CreationDate` datetime DEFAULT NULL,
  `Score` int(11) DEFAULT NULL,
  `ViewCount` int(11) DEFAULT NULL,
  `OwnerUserId` int(11) DEFAULT NULL,
  `Tags` varchar(45) DEFAULT NULL,
  `AnswerCount` int(11) DEFAULT NULL,
  `CommentCount` int(11) DEFAULT NULL,
  `FavouriteCount` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into `questions` 
select 
Id,PostTypeId,AcceptedAnswerId,ParentId,
CreationDate,Score,ViewCount,OwnerUserId,
Tags,AnswerCount,CommentCount,
FavouriteCount
from `posts` where `posttypeid`=1;

insert into `accepted_answers` 
select 
Id,PostTypeId,AcceptedAnswerId,ParentId,
CreationDate,Score,ViewCount,OwnerUserId,
Tags,AnswerCount,CommentCount,
FavouriteCount
from `posts` p where `posttypeid`=2 and `ParentId` is not null and (select id from posts p2 where p2.`AcceptedAnswerId` = p.id) is not null;

insert into `answers` 
select 
Id,PostTypeId,AcceptedAnswerId,ParentId,
CreationDate,Score,ViewCount,OwnerUserId,
Tags,AnswerCount,CommentCount,
FavouriteCount
from `posts` where `posttypeid`=2 and `ParentId` is not null;