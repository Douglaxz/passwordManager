-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: db_passwordmanager
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `tb_passwordtype`
--

DROP TABLE IF EXISTS `tb_passwordtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_passwordtype` (
  `cod_passwordtype` int NOT NULL AUTO_INCREMENT,
  `desc_passwordtype` varchar(45) NOT NULL,
  `status_passwordtype` int NOT NULL,
  `icon_passwordtype` varchar(45) NOT NULL,
  PRIMARY KEY (`cod_passwordtype`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_passwordtype`
--

LOCK TABLES `tb_passwordtype` WRITE;
/*!40000 ALTER TABLE `tb_passwordtype` DISABLE KEYS */;
INSERT INTO `tb_passwordtype` VALUES (1,'Facebook',0,'bi bi-facebook'),(2,'Twitter',0,'bi bi-twitter'),(3,'Instagram',0,'bi bi-instagram'),(4,'Twitch',0,'bi bi-twitch'),(5,'GitHub',0,'bi bi-github'),(6,'Google',0,'i class=\"bi bi-google'),(7,'Facebook Messenger',0,'bi bi-messenger'),(8,'Youtube',0,'bi bi-youtube'),(9,'Wordpress',0,'bi bi-wordpress'),(10,'Whatsapp',0,'bi bi-whatsapp'),(11,'Telegram',0,'bi bi-telegram'),(12,'Stack overflow',0,'bi bi-stack-overflow'),(13,'Spotify',0,'bi bi-spotify'),(14,'Snapchat',0,'bi bi-snapchat'),(15,'Skype',0,'bi bi-skype'),(16,'Reddit',0,'bi bi-reddit'),(17,'Pinterest',0,'bi bi-pinterest'),(18,'Paypall',0,'bi bi-paypal'),(19,'Microsoft Teams',0,'bi bi-microsoft-teams'),(20,'Discord',0,'bi bi-discord');
/*!40000 ALTER TABLE `tb_passwordtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_user` (
  `cod_user` int NOT NULL AUTO_INCREMENT,
  `name_user` varchar(45) NOT NULL,
  `password_user` varchar(70) NOT NULL,
  `status_user` int NOT NULL,
  `email_user` varchar(45) NOT NULL,
  `lastlogin_user` datetime DEFAULT NULL,
  `login_user` varchar(45) NOT NULL,
  `cod_usertype` int NOT NULL,
  PRIMARY KEY (`cod_user`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES (1,'Douglas Amaral','$2b$12$ZWrw9mT75lR3EQlpoVhICuyk8z4iB/9N/2nmO.jBL82/ZLGxTIkUu',0,'douglaxz@hotmail.com',NULL,'douglas',1),(2,'Francieli Amaral','$2b$12$8JSLecf6J0MsBDhh.cu9zuGkuIbz20aP4fB90co2cW7UtxcOUllYS',0,'fran_mma@hotmail.com',NULL,'francieli',2),(3,'Admin temp 2','$2b$12$EYOzSTTDSYPNn0cu70k7OezlS7.oRX0pCIXV7aOK9oOLD/OXrtWau',0,'sadsd',NULL,'admintemp',1),(7,'Lila Amaral','$2b$12$a8GaZv4X47h1wqNXsVPXZ.9TkH/P1AVrIqv5p9EN77Ncs/pw2U1.C',0,'lila@amaralcorp.com.br',NULL,'lila',2),(8,'Melvim Amaral','$2b$12$FfnF6W9gujK/Bd12RvCsaOIIJy2wLDA9M3sjHXJMI/oRw/01bzwn6',0,'melvim@amaralcorp.com.br',NULL,'melvim',2),(9,'Leonor','$2b$12$qkInaNkoJs0xpaZWV14Y6OXNn0FZdgWQ3VwAMo72uzKL3LjMZ3py6',0,'leonor@teste.com.br',NULL,'leonor',2);
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_userpassword`
--

DROP TABLE IF EXISTS `tb_userpassword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_userpassword` (
  `cod_userpassword` int NOT NULL AUTO_INCREMENT,
  `cod_passwordtype` int NOT NULL,
  `username_userpassword` varchar(45) DEFAULT NULL,
  `password_userpassword` varchar(70) NOT NULL,
  `date_userpassword` datetime NOT NULL,
  `cod_user` int NOT NULL,
  PRIMARY KEY (`cod_userpassword`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_userpassword`
--

LOCK TABLES `tb_userpassword` WRITE;
/*!40000 ALTER TABLE `tb_userpassword` DISABLE KEYS */;
INSERT INTO `tb_userpassword` VALUES (1,5,'usuarioteste2','ganwvinmt','2023-01-01 00:00:00',1),(2,1,'usuarioFace','senhaFace','2023-01-27 00:00:00',1),(3,2,'usuarioTwitter','senhaTwitter','2023-01-27 00:00:00',1),(4,10,'userWhatsapp','senhawhats123','2023-01-27 00:00:00',1),(5,15,'usuarioSkype','testeSkype123','2023-01-27 00:00:00',1),(6,19,'usuisduoisa','dssf','2023-01-27 00:00:00',1),(7,3,'teste11111','111111','2023-01-27 00:00:00',2),(8,15,'melvimgato','zhpwf','2023-01-29 00:00:00',8),(9,12,'qualquer','$2b$12$dAiu7KDs8cX39.0vr7FwOu4.zrwFFfn1GybFxHG2KTpzbLb/nNKwm','2023-01-29 00:00:00',1),(10,10,'userwhats','$2b$12$NBicIGG2IwktSiTO5BKCgOJ1ubusmORciQ4W45c.3QA7SaeyZ3x7q','2023-01-29 00:00:00',9),(11,11,'usuario teste','12345','2023-01-30 00:00:00',1);
/*!40000 ALTER TABLE `tb_userpassword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_usertype`
--

DROP TABLE IF EXISTS `tb_usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_usertype` (
  `cod_usertype` int NOT NULL AUTO_INCREMENT,
  `desc_usertype` varchar(45) NOT NULL,
  `status_usertype` int NOT NULL,
  PRIMARY KEY (`cod_usertype`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_usertype`
--

LOCK TABLES `tb_usertype` WRITE;
/*!40000 ALTER TABLE `tb_usertype` DISABLE KEYS */;
INSERT INTO `tb_usertype` VALUES (1,'Administrador',0),(2,'Usuario simples',1);
/*!40000 ALTER TABLE `tb_usertype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-31  8:18:31
