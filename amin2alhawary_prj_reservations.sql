-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: amin2alhawary_prj
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `BookingRef` int NOT NULL AUTO_INCREMENT,
  `BookingDate` date DEFAULT NULL,
  `CheckIn` date DEFAULT NULL,
  `CheckOut` date DEFAULT NULL,
  `USER` varchar(60) DEFAULT NULL,
  `ROOMNUM` int NOT NULL,
  `HOTEL` varchar(5) NOT NULL,
  `ROOMTYPE` varchar(20) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Guests` int NOT NULL,
  `Ongoing` tinyint DEFAULT NULL,
  `cancelFee` int DEFAULT NULL,
  `Notes` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`BookingRef`),
  KEY `HOTEL` (`HOTEL`),
  KEY `ROOMTYPE` (`ROOMTYPE`),
  KEY `USER` (`USER`),
  KEY `ROOMNUM` (`ROOMNUM`),
  CONSTRAINT `RESERVATIONS_ibfk_2` FOREIGN KEY (`ROOMTYPE`) REFERENCES `room_types` (`TYPE`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `RESERVATIONS_ibfk_3` FOREIGN KEY (`USER`) REFERENCES `accounts` (`email`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT=' ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES (23,'2022-05-08','2022-05-14','2022-05-22',NULL,28,'EDN','Double',1536,1,1,NULL,NULL),(24,'2022-05-08','2022-05-14','2022-05-21',NULL,1,'LDN','Standard',1400,1,1,NULL,NULL),(25,'2022-05-08','2022-05-14','2022-05-22',NULL,73,'BRS','Family',1680,1,0,NULL,NULL);
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-08 13:47:59
