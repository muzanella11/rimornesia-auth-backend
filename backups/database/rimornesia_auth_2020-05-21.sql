# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.30)
# Database: rimornesia_auth
# Generation Time: 2020-05-21 00:08:09 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table access_controls
# ------------------------------------------------------------

DROP TABLE IF EXISTS `access_controls`;

CREATE TABLE `access_controls` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `role_id` int(11) DEFAULT NULL,
  `apps_permission` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `access_controls` WRITE;
/*!40000 ALTER TABLE `access_controls` DISABLE KEYS */;

INSERT INTO `access_controls` (`id`, `role_id`, `apps_permission`, `created_at`, `updated_at`)
VALUES
	(1,1,'1','2020-05-21 00:06:10','2020-05-21 00:06:28');

/*!40000 ALTER TABLE `access_controls` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table applications
# ------------------------------------------------------------

DROP TABLE IF EXISTS `applications`;

CREATE TABLE `applications` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  `env` varchar(50) DEFAULT NULL,
  `key` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;

INSERT INTO `applications` (`id`, `name`, `description`, `url`, `env`, `key`)
VALUES
	(1,'rimornesia-mountain','Rimornesia Mountain','http://localhost:5000/','development','gAAAAABexUt6tfz6MiF4w_Ws79t2cX7QRNg7qEnF620TK2hdxyJO0Ob39E7ZPLwTb2wXH7hxUZ1Wsajgm2O6edqbojAgBRNXYYZ2WAPXDsNzNoxZUut69jY=');

/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_roles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_roles`;

CREATE TABLE `user_roles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;

INSERT INTO `user_roles` (`id`, `name`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'Super Administrator','Super Administrator','2020-05-20 14:28:18',NULL),
	(2,'Administrator','Administrator','2020-05-20 14:28:59',NULL),
	(3,'Staff','Staff','2020-05-20 14:31:24',NULL),
	(4,'User','User','2020-05-20 14:31:41',NULL);

/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_fname` varchar(50) DEFAULT NULL,
  `user_lname` varchar(50) DEFAULT NULL,
  `user_display_name` varchar(50) DEFAULT NULL,
  `user_display_alias` varchar(20) DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  `user_password` varchar(75) DEFAULT NULL,
  `user_username` varchar(50) DEFAULT NULL,
  `user_dob` date DEFAULT NULL,
  `user_age` int(11) DEFAULT NULL,
  `user_gender` int(1) DEFAULT NULL,
  `user_phone` varchar(20) DEFAULT NULL,
  `user_identity` varchar(50) DEFAULT NULL,
  `user_address` varchar(50) DEFAULT NULL,
  `user_avatar` varchar(50) DEFAULT NULL,
  `user_cover_image` varchar(50) DEFAULT NULL,
  `user_status` int(1) DEFAULT NULL,
  `user_role` int(11) DEFAULT NULL,
  `is_verified` int(2) DEFAULT NULL,
  `completed` varchar(15) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
