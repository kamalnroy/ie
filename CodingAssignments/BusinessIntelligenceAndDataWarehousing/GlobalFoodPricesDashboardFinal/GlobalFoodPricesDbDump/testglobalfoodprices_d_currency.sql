CREATE DATABASE  IF NOT EXISTS `testglobalfoodprices` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `testglobalfoodprices`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: localhost    Database: testglobalfoodprices
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `d_currency`
--

DROP TABLE IF EXISTS `d_currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `d_currency` (
  `currency_id` int(11) NOT NULL,
  `currency_name` varchar(64) DEFAULT NULL,
  `country` varchar(64) DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `d_currency`
--

LOCK TABLES `d_currency` WRITE;
/*!40000 ALTER TABLE `d_currency` DISABLE KEYS */;
INSERT INTO `d_currency` VALUES (22,'TZS','United Republic of Tanzania',NULL),(23,'SZL','Swaziland',NULL),(24,'HTG','Haiti',NULL),(25,'BDT','Bangladesh',NULL),(26,'XOF','Benin',NULL),(26,'XOF','Burkina Faso',NULL),(26,'XOF','Cote d\'Ivoire',NULL),(26,'XOF','Guinea-Bissau',NULL),(26,'XOF','Mali',NULL),(26,'XOF','Niger',NULL),(26,'XOF','Nigeria',NULL),(26,'XOF','Senegal',NULL),(27,'CDF','Democratic Republic of the Congo',NULL),(28,'USD','Costa Rica',NULL),(28,'USD','El Salvador',NULL),(28,'USD','Honduras',NULL),(28,'USD','Panama',NULL),(28,'USD','Timor-Leste',NULL),(28,'USD','Zimbabwe',NULL),(29,'PHP','Philippines',NULL),(30,'KES','Kenya',NULL),(31,'YER','Yemen',NULL),(32,'BIF','Burundi',NULL),(33,'PEN','Peru',NULL),(34,'IDR','Indonesia',NULL),(35,'GHS','Ghana',NULL),(36,'AZN','Azerbaijan',NULL),(37,'AMD','Armenia',NULL),(38,'EGP','Egypt',NULL),(39,'UGX','Uganda',NULL),(40,'LRD','Liberia',NULL),(42,'GMD','Gambia',NULL),(45,'PKR','Pakistan',NULL),(46,'BOB','Bolivia',NULL),(47,'ETB','Ethiopia',NULL),(48,'XAF','Cameroon',NULL),(48,'XAF','Central African Republic',NULL),(48,'XAF','Chad',NULL),(48,'XAF','Congo',NULL),(49,'TJS','Tajikistan',NULL),(50,'GEL','Georgia',NULL),(51,'MZN','Mozambique',NULL),(54,'GNF','Guinea',NULL),(55,'LKR','Sri Lanka',NULL),(56,'LSL','Lesotho',NULL),(57,'CVE','Cape Verde',NULL),(58,'JOD','Jordan',NULL),(59,'DJF','Djibouti',NULL),(60,'KHR','Cambodia',NULL),(61,'KGS','Kyrgyzstan',NULL),(62,'NPR','Nepal',NULL),(63,'LAK','Lao People\'s Democratic Republic',NULL),(64,'MRO','Mauritania',NULL),(65,'MGA','Madagascar',NULL),(66,'MWK','Malawi',NULL),(67,'COP','Colombia',NULL),(68,'INR','India',NULL),(73,'NIS','State of Palestine',NULL),(74,'MMK','Myanmar',NULL),(75,'SDG','Sudan',NULL),(76,'BTN','Bhutan',NULL),(77,'RWF','Rwanda',NULL),(78,'SYP','Syrian Arab Republic',NULL),(79,'SOS','Somalia',NULL),(81,'Somaliland Shilling','Somalia',NULL),(82,'GTQ','Guatemala',NULL),(83,'SSP','South Sudan',NULL),(84,'IQD','Iraq',NULL),(87,'AFN','Afghanistan',NULL),(88,'TRY','Turkey',NULL),(89,'IRR','Iran  (Islamic Republic of)',NULL),(90,'LBP','Lebanon',NULL),(91,'DZD','Algeria',NULL),(93,'UAH','Ukraine',NULL),(94,'ZMW','Zambia',NULL);
/*!40000 ALTER TABLE `d_currency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 23:48:26
