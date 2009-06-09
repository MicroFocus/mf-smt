-- MySQL dump 10.10
--
-- Host: localhost    Database: smt
-- ------------------------------------------------------
-- Server version	5.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
CREATE TABLE `Clients` (
  `GUID` char(50) NOT NULL,
  `HOSTNAME` varchar(100) default '',
  `TARGET` varchar(100) default NULL,
  `DESCRIPTION` varchar(500) default '',
  `LASTCONTACT` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`GUID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
INSERT INTO `Clients` VALUES ('4f6d81cabd5343548dda08f425b0ceea','srv64','sles-10-x86_64','','2009-01-07 13:06:51');
INSERT INTO `Clients` VALUES ('f7ef7ef5a8be4884991a9f7b153515f9','e200','sle-11-i586','','2009-03-13 14:11:54');
INSERT INTO `Clients` VALUES ('65f411b03c4e4009867c316a798b960c','mctest','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd1','restest1','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd2','restest2','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd3','restest3','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd4','restest4','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd5','restest5','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd6','restest6','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('abcd7','restest7','sle-11-i586','','2009-03-05 08:50:36');

INSERT INTO `Clients` VALUES ('xyz1','slestest1','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('xyz2','slestest1','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('xyz3','slestest1','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('xyz4','slestest1','sle-11-i586','','2009-03-05 08:50:36');
INSERT INTO `Clients` VALUES ('xyz5','slestest1','sle-11-i586','','2009-03-05 08:50:36');
/*!40000 ALTER TABLE `Clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Registration`
--

DROP TABLE IF EXISTS `Registration`;
CREATE TABLE `Registration` (
  `GUID` char(50) NOT NULL,
  `PRODUCTID` int(11) NOT NULL,
  `REGDATE` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `NCCREGDATE` timestamp NULL default NULL,
  `NCCREGERROR` int(11) default '0',
  PRIMARY KEY  (`GUID`,`PRODUCTID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Registration`
--

LOCK TABLES `Registration` WRITE;
/*!40000 ALTER TABLE `Registration` DISABLE KEYS */;
INSERT INTO `Registration` VALUES ('4f6d81cabd5343548dda08f425b0ceea',1021,'2009-01-07 13:06:51',NULL,1);
INSERT INTO `Registration` VALUES ('4f6d81cabd5343548dda08f425b0ceea',824,'2009-01-07 13:06:51',NULL,1);
INSERT INTO `Registration` VALUES ('f7ef7ef5a8be4884991a9f7b153515f9',1226,'2009-01-15 15:53:42',NULL,1);
INSERT INTO `Registration` VALUES ('65f411b03c4e4009867c316a798b960c',1226,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('65f411b03c4e4009867c316a798b960c',1240,'2009-03-04 15:12:26',NULL,1);


INSERT INTO `Registration` VALUES ('xyz1',1226,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('xyz2',1226,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('xyz3',1226,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('xyz4',1226,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('xyz5',1226,'2009-03-04 15:12:26',NULL,1);

INSERT INTO `Registration` VALUES ('abcd1',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd2',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd3',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd4',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd5',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd6',1322,'2009-03-04 15:12:26',NULL,1);
INSERT INTO `Registration` VALUES ('abcd7',1322,'2009-03-04 15:12:26',NULL,1);

/*!40000 ALTER TABLE `Registration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-06-05 10:28:51
