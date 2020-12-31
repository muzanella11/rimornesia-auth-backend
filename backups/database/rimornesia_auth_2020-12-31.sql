# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.31)
# Database: rimornesia_auth
# Generation Time: 2020-12-31 04:51:28 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table access_climbing_post
# ------------------------------------------------------------

DROP TABLE IF EXISTS `access_climbing_post`;

CREATE TABLE `access_climbing_post` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `key_access` text,
  `user_id` int(11) DEFAULT NULL,
  `climbing_post_id` int(11) DEFAULT NULL,
  `is_active` int(5) DEFAULT '0',
  `is_owner` int(5) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `access_climbing_post` WRITE;
/*!40000 ALTER TABLE `access_climbing_post` DISABLE KEYS */;

INSERT INTO `access_climbing_post` (`id`, `key_access`, `user_id`, `climbing_post_id`, `is_active`, `is_owner`, `created_at`, `updated_at`)
VALUES
	(1,'BY9GGAYZ-5R9G9VNJ-BBNI82YU-WM5HCAIO-4ZUIIJXD-WAOMXNUD-YBTBQS85-JZUSCZRV',1,1,0,1,'2020-12-31 02:14:47','2020-12-31 02:19:51');

/*!40000 ALTER TABLE `access_climbing_post` ENABLE KEYS */;
UNLOCK TABLES;


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


# Dump of table user_identity_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_identity_types`;

CREATE TABLE `user_identity_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `label` varchar(20) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user_identity_types` WRITE;
/*!40000 ALTER TABLE `user_identity_types` DISABLE KEYS */;

INSERT INTO `user_identity_types` (`id`, `name`, `label`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'ktp','Kartu Tanda Penduduk','Kartu Tanda Penduduk','2020-11-20 05:54:05',NULL);

/*!40000 ALTER TABLE `user_identity_types` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_reset_password_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_reset_password_session`;

CREATE TABLE `user_reset_password_session` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `token` text,
  `user_id` int(11) DEFAULT NULL,
  `expired` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_reset_password_session` WRITE;
/*!40000 ALTER TABLE `user_reset_password_session` DISABLE KEYS */;

INSERT INTO `user_reset_password_session` (`id`, `token`, `user_id`, `expired`, `created_at`, `updated_at`)
VALUES
	(1,'Q0UWPFNK-WBDEY81X-LZMVSF7Y-9DNXZBOA-BHJRHH35-2ZW1F1PW-AE04RWWU-T9QVU4YQ',5,'1606892268000','2020-12-02 06:27:48','2020-12-02 06:27:48'),
	(2,'6K53FLOB-TETAY2QC-XVAO2NIV-QZUSZU42-UNYNTF3X-FUMNQ1GW-HVRJPCJD-ERMPVISZ',5,'1609317481000','2020-12-30 08:28:01','2020-12-30 08:28:01');

/*!40000 ALTER TABLE `user_reset_password_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_roles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_roles`;

CREATE TABLE `user_roles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `label` varchar(20) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;

INSERT INTO `user_roles` (`id`, `name`, `label`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'super-administrator','Super Administrator','Super Administrator','2020-05-20 14:28:18',NULL),
	(2,'administrator','Administrator','Administrator','2020-05-20 14:28:59',NULL),
	(3,'staff','Staff','Staff','2020-05-20 14:31:24',NULL),
	(4,'user','User','User','2020-05-20 14:31:41',NULL);

/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_types`;

CREATE TABLE `user_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user_types` WRITE;
/*!40000 ALTER TABLE `user_types` DISABLE KEYS */;

INSERT INTO `user_types` (`id`, `name`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'User','User','2020-07-08 07:14:56',NULL),
	(2,'Climbing Post','Climbing Post','2020-07-08 07:16:06',NULL);

/*!40000 ALTER TABLE `user_types` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_verification_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_verification_session`;

CREATE TABLE `user_verification_session` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `token` text,
  `expired` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_verification_session` WRITE;
/*!40000 ALTER TABLE `user_verification_session` DISABLE KEYS */;

INSERT INTO `user_verification_session` (`id`, `token`, `expired`, `created_at`, `updated_at`)
VALUES
	(1,'EZZQU4NY-OE0VYVII-XLQOSK3O-BSSQATCZ-QTDRKGGC-WZLXWQZK-5R9QWOFG-SLAXQNHW','1606201452000','2020-11-24 06:34:12','2020-11-24 06:34:12'),
	(2,'NSXH9BOB-3BHLVVWG-A4I3TATT-IK3SYWIB-AD3RTD5Q-FVK0X2KA-PYMARXA1-2IFJTINX','1606879573000','2020-12-02 02:56:13','2020-12-02 02:56:13'),
	(3,'MCJXWBAS-CU2FYYQP-UC9BM52W-XR0IJBQV-X2GIJKKX-DBCEJIAW-0OPILW04-NDGOZQWU','1606881749000','2020-12-02 03:32:29','2020-12-02 03:32:29'),
	(4,'IVSQME6U-XKMPIQQD-VBMIDC83-56QWGDL0-BKV2I7OV-B6CX3HP8-FUIUVZIY-UKKG3YF0','1606881889000','2020-12-02 03:34:49','2020-12-02 03:34:49'),
	(5,'2P5BQPGE-7BHZ7FSP-SCZJCFQK-X49GLU7A-0PBHAWUA-CJ2YDZTF-33SBUPCN-URWDPL6U','1606882003000','2020-12-02 03:36:43','2020-12-02 03:36:43'),
	(6,'8BPS5T5K-KTE7EWGJ-OMFR6J6U-VAZDPQPO-WPTSGAAY-AVQNQKPW-0FKJKT9M-WNQKA59E','1606882087000','2020-12-02 03:38:07','2020-12-02 03:38:07'),
	(7,'VMBDG3PW-VF204BWW-WUYMDS39-H9WJKWJN-X0KXTKOR-K6Z9AIGQ-RUKCGZSG-S2LRQHFW','1606882121000','2020-12-02 03:38:41','2020-12-02 03:38:41'),
	(8,'OJBZYN7H-588UQBAS-AD6G6QP6-9SBTNVZ5-FXW5JUAV-WRXW65EL-RMASLTZT-CM3WQ975','1609319653000','2020-12-30 08:44:13','2020-12-30 08:44:13'),
	(9,'BPU3FZ7V-NFEVC9AH-THWBMF8K-7ON0KOWA-HJOI2TA8-28U2Q2RR-DJVXH4LA-8ML7K1VT','1609319776000','2020-12-30 08:46:16','2020-12-30 08:46:16');

/*!40000 ALTER TABLE `user_verification_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `display_name` varchar(50) DEFAULT NULL,
  `email` text,
  `password` text,
  `username` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` int(1) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `identity` varchar(50) DEFAULT NULL,
  `identity_type` int(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `avatar` varchar(50) DEFAULT NULL,
  `cover_image` varchar(50) DEFAULT NULL,
  `status` int(1) DEFAULT NULL,
  `roles` int(11) DEFAULT '4',
  `is_verified` int(2) DEFAULT '0',
  `verification_token` text,
  `is_verified_account` int(2) DEFAULT '0',
  `completed` varchar(15) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`id`, `first_name`, `last_name`, `display_name`, `email`, `password`, `username`, `dob`, `age`, `gender`, `phone`, `identity`, `identity_type`, `address`, `avatar`, `cover_image`, `status`, `roles`, `is_verified`, `verification_token`, `is_verified_account`, `completed`, `created_at`, `updated_at`)
VALUES
	(1,'Super','Administrator','Super Administrator','super-admin@gmail.com','password','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,1,NULL,NULL,NULL,'2020-11-20 06:23:08','2020-12-02 08:23:22'),
	(2,'Super','Administrator','None','super-admin2@gmail.com','gAAAAABft2r7b8MG5Hoxh2hKYKCUfc8z7wm-ZCRPAFN4JgGFrYWUfuNF-xBOGW6-7n7XUcr9I7mFNjcWQuoDPSphAfWce9HaSA==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,0,NULL,NULL,NULL,'2020-11-20 07:06:35',NULL),
	(3,'Super','Administrator','None','super-admin3@gmail.com','gAAAAABft3C6080kjOZsSoBfTnJPI9WAor1cXT9SaeZAZ9unykRtnXHV-FQmK_iXk30uzgQYbsBsTQ_UWrGdL31FwKN2T8tY0w==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,0,NULL,0,NULL,'2020-11-20 07:31:06',NULL),
	(4,'Super','Administrator','None','super-admin4@gmail.com','gAAAAABfvKlkZ1Oz0mVLGfTy3B1Ag8rKx2iZ-8M1TAb3_sYzeVs6Iw5v-4si-S-Sf1SZSUUCWLEBGvkt9tag2gqb7Tc7C0si-A==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,0,'EZZQU4NY-OE0VYVII-XLQOSK3O-BSSQATCZ-QTDRKGGC-WZLXWQZK-5R9QWOFG-SLAXQNHW',0,NULL,'2020-11-24 06:34:12',NULL),
	(5,'Super','Administrator','None','super-admin5@gmail.com','gAAAAABf7Dr_BpRN6O2wIQzL65buJCQA94yVGVggRpdb6I-gMZBWO_b5WsRiRCtAMByzSKRwY473NRDP2TUAeTVYYy-J9VvZ2A==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,1,'VMBDG3PW-VF204BWW-WUYMDS39-H9WJKWJN-X0KXTKOR-K6Z9AIGQ-RUKCGZSG-S2LRQHFW',0,NULL,'2020-12-02 02:56:13','2020-12-30 08:31:59'),
	(6,'Super','Administrator 6','None','super-admin6@gmail.com','gAAAAABf7D5YLdtIZV648CB3jiNxmAxMOc7DIB-EahbBHKDpYN1ZUgRfUHHZAGI6fUv9sx6XYdIXeTva0RT1rBnUg1lQdDG3Mg==','super-admin-6','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,4,0,'BPU3FZ7V-NFEVC9AH-THWBMF8K-7ON0KOWA-HJOI2TA8-28U2Q2RR-DJVXH4LA-8ML7K1VT',0,NULL,'2020-12-30 08:46:16',NULL);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
