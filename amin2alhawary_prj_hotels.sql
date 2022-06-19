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
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `hid` varchar(5) NOT NULL,
  `HName` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `Feat` tinyint(1) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `pricePeak` int DEFAULT NULL,
  `priceOff` int DEFAULT NULL,
  `hotelDesc` varchar(200) DEFAULT NULL,
  `region` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES ('ABR','Horizon Hotels Aberdeen','Aberdeen',NULL,NULL,80,140,60,NULL,'Scotland'),('BLF','Horizon Hotels Belfast','Belfast',NULL,NULL,80,130,60,NULL,'Northern Ireland'),('BRM','Horizon Hotels Birmingham','Birmingham',NULL,NULL,90,150,70,NULL,'West Midlands'),('BRS','Horizon Hotels Bristol','Bristol',NULL,NULL,90,140,70,NULL,'South West England'),('CDF','Horizon Hotels Cardiff','Cardiff',NULL,NULL,80,120,60,NULL,'Wales'),('EDN','Horizon Hotels Edinburgh','Edinburgh',NULL,NULL,90,160,70,NULL,'Scotland'),('GLS','Horizon Hotels Glasgow','Glasgow',NULL,NULL,100,150,70,NULL,'Scotland'),('LDN','Horizon Hotels London','London',NULL,1,120,200,80,NULL,'London'),('MNC','Horizon Hotels Manchester','Manchester',NULL,1,110,180,80,NULL,'North West England'),('NEW','Horizon Hotels Newcastle','Newcastle',NULL,NULL,80,100,60,NULL,'North East England'),('NOR','Horizon Hotels Norwich','Norwich',NULL,1,80,100,60,NULL,'East of England'),('NOT','Horizon Hotels Nottingham','Nottingham',NULL,NULL,100,120,70,NULL,'East Midlands'),('OXF','Horizon Hotels Oxford','Oxford',NULL,NULL,80,180,70,NULL,'South East England'),('PLY','Horizon Hotels Plymouth','Plymouth',NULL,NULL,80,180,50,NULL,'South West England'),('SWA','Horizon Hotels Swansea','Swansea',NULL,NULL,80,120,50,NULL,'Wales');
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
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
