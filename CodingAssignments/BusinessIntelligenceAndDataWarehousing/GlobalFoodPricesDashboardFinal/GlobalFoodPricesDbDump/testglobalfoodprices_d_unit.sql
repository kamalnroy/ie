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
-- Table structure for table `d_unit`
--

DROP TABLE IF EXISTS `d_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `d_unit` (
  `unit_id` int(11) NOT NULL,
  `unit_name` varchar(64) DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `d_unit`
--

LOCK TABLES `d_unit` WRITE;
/*!40000 ALTER TABLE `d_unit` DISABLE KEYS */;
INSERT INTO `d_unit` VALUES (5,'KG',NULL),(9,'100 KG',NULL),(14,'Marmite',NULL),(15,'L',NULL),(16,'45 KG',NULL),(17,'90 KG',NULL),(18,'MT',NULL),(19,'385 G',NULL),(20,'100 Tubers',NULL),(21,'Bunch',NULL),(22,'50 KG',NULL),(23,'91 KG',NULL),(24,'400 G',NULL),(25,'500 ML',NULL),(27,'Gallon',NULL),(28,'500 G',NULL),(29,'Cuartilla',NULL),(30,'Pound',NULL),(31,'Sack',NULL),(33,'Unit',NULL),(35,'Dozen',NULL),(36,'12.5 KG',NULL),(37,'Loaf',NULL),(38,'750 ML',NULL),(40,'85 G',NULL),(41,'380 G',NULL),(42,'150 G',NULL),(43,'25 KG',NULL),(44,'60 KG',NULL),(46,'1.8 KG',NULL),(47,'3.5 KG',NULL),(48,'3 KG',NULL),(49,'650 G',NULL),(50,'Libra',NULL),(51,'Day',NULL),(52,'1.5 KG',NULL),(55,'Course',NULL),(56,'USD/LCU',NULL),(57,'2 KG',NULL),(58,'Month',NULL),(61,'Head',NULL),(63,'200 G',NULL),(65,'160 G',NULL),(67,'5 L',NULL),(69,'30 pcs',NULL),(72,'185 G',NULL),(74,'125 G',NULL),(75,'Packet',NULL),(76,'18 KG',NULL),(81,'10 pcs',NULL),(83,'10 KG',NULL),(86,'11.5 KG',NULL),(87,'5 KG',NULL),(90,'12 KG',NULL),(95,'168 G',NULL),(96,'350 G',NULL),(97,'115 G',NULL);
/*!40000 ALTER TABLE `d_unit` ENABLE KEYS */;
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
