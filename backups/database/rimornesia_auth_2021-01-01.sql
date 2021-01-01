# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.31)
# Database: rimornesia_auth
# Generation Time: 2021-01-01 00:09:40 +0000
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
	(1,'VJTDTZXL-C1MJ71M0-EJHHJDFE-OTVSWDC1-ILLNQ1PN-JSKBKFCF-3DK7DY9Q-D8LVTPVV',1,1,1,1,'2020-12-31 08:24:03',NULL);

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


# Dump of table user_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_session`;

CREATE TABLE `user_session` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `token` text,
  `expired` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_session` WRITE;
/*!40000 ALTER TABLE `user_session` DISABLE KEYS */;

INSERT INTO `user_session` (`id`, `token`, `expired`, `created_at`, `updated_at`)
VALUES
	(1,'KMS5TNCL-WDBSQUTN-CLLR09MW-WC5JZIOU-6VZBI3WI-MKE4ZCSW-CMDVVH1O-PV4AMYXS','1609452578000','2020-12-31 21:39:38','2020-12-31 21:39:38'),
	(2,'O67Q8AF9-QRGDMXYA-RGO01JHU-FOFEHA9B-WNKIIE0I-CVJW1ZN2-LCYL117S-WILPRVLB','1609450890000','2020-12-31 21:41:30','2020-12-31 21:41:30'),
	(3,'KXAI8YYX-04J83XAW-OHMISEDD-KGFL2ZIE-OJA7JG7T-KRVA1SL8-HITAG7SF-HAXSLIAR','1609453061000','2020-12-31 22:17:41','2020-12-31 22:17:41'),
	(4,'JSQUB1TQ-68BNZMFJ-HCZ04IBE-8PBWXQYJ-TVYVXST9-IVQJS7RK-LYGBYYNP-A54B8EKC','1609453378000','2020-12-31 22:22:58','2020-12-31 22:22:58'),
	(5,'F8ZCFZKB-EP1RALOK-DUE8MCMI-ZMVMF0CW-5IPZASPT-JBYANILS-2ZKUAN4L-BFKWNEXV','1609453394000','2020-12-31 22:23:14','2020-12-31 22:23:14'),
	(6,'LGMWODDY-J46EBFCE-FFTLKCEW-KYJJMKK1-A8P71URG-NKNOIOXF-LDSPCVZ4-TXMA4AHV','1609453845000','2020-12-31 22:29:45','2020-12-31 22:29:45'),
	(7,'AZIRO8MN-LKN9IURI-HASO6IZS-VRN9HBRM-X1XR7NPX-UF6T777V-S3C3G7HU-FJCA9BS2','1609454724000','2020-12-31 22:44:24','2020-12-31 22:44:24'),
	(8,'FTTNDCBY-4AS8L2TP-CBZVNXCI-VZVAH08P-UUM2M4IN-BS1TKHMN-URGBPJYZ-HO3RJXWO','1609455453000','2020-12-31 22:56:33','2020-12-31 22:56:33'),
	(9,'NVQ4JZOC-GU812MDM-S4CDE432-SMAYXWES-HZYOLLIY-SMEBQU7X-G7BMT5QP-I6CKEUHI','1609455634000','2020-12-31 22:59:34','2020-12-31 22:59:34'),
	(10,'FPXOEBFX-PBCMU0T1-NFGQQ4FB-BEWOWNVZ-Y3PLUIKL-Q7HBBSGJ-OLUDDWNZ-FX1COIPW','1609455748000','2020-12-31 23:01:28','2020-12-31 23:01:28'),
	(11,'8GJQT4UL-C3NFJ483-7BD82ZEK-GOO0K3PU-3AZMVFWT-PZYWGOBZ-KALWU62T-NO4ACVR0','1609457644000','2020-12-31 23:33:04','2020-12-31 23:33:04'),
	(12,'B8AOEYSY-XIPR9RAK-YA0FT8TH-YM261HWL-3BVWDBDR-S5OQ18ML-YZQDEQDF-WEOPCCMS','1609630843000','2020-12-31 23:40:43','2020-12-31 23:40:43'),
	(13,'7MBYGWRH-WAFY2BDL-UA6V8CVT-WVWGHKFK-CC7NZNYW-1G5LDNPH-QWFPR5LJ-WV1VP5PO','1609631655000','2020-12-31 23:54:15','2020-12-31 23:54:15'),
	(14,'FUOI1FNY-OWMPOVLA-1X40C9TM-KSISUFA5-OET4UV01-KP9POWLZ-AN7Q5K2P-FOKRYXHU','1609631711000','2020-12-31 23:55:11','2020-12-31 23:55:11'),
	(15,'5DY19Y0F-OMUBOODD-RMEOWQD1-HCOA7KS3-KJFSGQOV-UG05PR3G-72NCQ9EB-KO7Z6G3B','1609631816000','2020-12-31 23:56:56','2020-12-31 23:56:56'),
	(16,'BOEPWY9C-TAG9Z3BF-IAJ709WD-Q3KFFAOB-CEBXRUTC-6DEN9UJW-7ALWTO31-SBBAFHWO','1609631873000','2020-12-31 23:57:53','2020-12-31 23:57:53'),
	(17,'A9B4VHPO-8TPD7AY6-UEB4IMFA-5NIQZYGD-MOYICP1F-PRUUSRYZ-ZZPCECTI-3RSHDZYM','1609632060000','2021-01-01 00:01:00','2021-01-01 00:01:00'),
	(18,'UK9DGVIL-W3Z9WW82-2YBSCD9G-KJDFK4GH-AELAFAFJ-JZIZJIN2-ZUKL6XEZ-OQQTUKYT','1609632140000','2021-01-01 00:02:20','2021-01-01 00:02:20');

/*!40000 ALTER TABLE `user_session` ENABLE KEYS */;
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
  `key_access_climbing_post` text,
  `is_verified` int(2) DEFAULT '0',
  `verification_token` text,
  `is_verified_account` int(2) DEFAULT '0',
  `completed` varchar(15) DEFAULT NULL,
  `session_token` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`id`, `first_name`, `last_name`, `display_name`, `email`, `password`, `username`, `dob`, `age`, `gender`, `phone`, `identity`, `identity_type`, `address`, `avatar`, `cover_image`, `status`, `roles`, `key_access_climbing_post`, `is_verified`, `verification_token`, `is_verified_account`, `completed`, `session_token`, `created_at`, `updated_at`)
VALUES
	(1,'Super','Administrator','Super Administrator','super-admin@gmail.com','gAAAAABft2r7b8MG5Hoxh2hKYKCUfc8z7wm-ZCRPAFN4JgGFrYWUfuNF-xBOGW6-7n7XUcr9I7mFNjcWQuoDPSphAfWce9HaSA==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,'VJTDTZXL-C1MJ71M0-EJHHJDFE-OTVSWDC1-ILLNQ1PN-JSKBKFCF-3DK7DY9Q-D8LVTPVV',1,NULL,NULL,NULL,'','2020-11-20 06:23:08','2021-01-01 00:02:49'),
	(2,'Super','Administrator','None','super-admin2@gmail.com','gAAAAABft2r7b8MG5Hoxh2hKYKCUfc8z7wm-ZCRPAFN4JgGFrYWUfuNF-xBOGW6-7n7XUcr9I7mFNjcWQuoDPSphAfWce9HaSA==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,NULL,0,NULL,NULL,NULL,'KXAI8YYX-04J83XAW-OHMISEDD-KGFL2ZIE-OJA7JG7T-KRVA1SL8-HITAG7SF-HAXSLIAR','2020-11-20 07:06:35','2020-12-31 22:17:41'),
	(3,'Super','Administrator','None','super-admin3@gmail.com','gAAAAABft3C6080kjOZsSoBfTnJPI9WAor1cXT9SaeZAZ9unykRtnXHV-FQmK_iXk30uzgQYbsBsTQ_UWrGdL31FwKN2T8tY0w==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,NULL,0,NULL,0,NULL,'JSQUB1TQ-68BNZMFJ-HCZ04IBE-8PBWXQYJ-TVYVXST9-IVQJS7RK-LYGBYYNP-A54B8EKC','2020-11-20 07:31:06','2020-12-31 22:22:58'),
	(4,'Super','Administrator','None','super-admin4@gmail.com','gAAAAABfvKlkZ1Oz0mVLGfTy3B1Ag8rKx2iZ-8M1TAb3_sYzeVs6Iw5v-4si-S-Sf1SZSUUCWLEBGvkt9tag2gqb7Tc7C0si-A==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,NULL,0,'EZZQU4NY-OE0VYVII-XLQOSK3O-BSSQATCZ-QTDRKGGC-WZLXWQZK-5R9QWOFG-SLAXQNHW',0,NULL,'F8ZCFZKB-EP1RALOK-DUE8MCMI-ZMVMF0CW-5IPZASPT-JBYANILS-2ZKUAN4L-BFKWNEXV','2020-11-24 06:34:12','2020-12-31 22:23:14'),
	(5,'Super','Administrator','None','super-admin5@gmail.com','gAAAAABf7Dr_BpRN6O2wIQzL65buJCQA94yVGVggRpdb6I-gMZBWO_b5WsRiRCtAMByzSKRwY473NRDP2TUAeTVYYy-J9VvZ2A==','super-admin','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,1,NULL,1,'VMBDG3PW-VF204BWW-WUYMDS39-H9WJKWJN-X0KXTKOR-K6Z9AIGQ-RUKCGZSG-S2LRQHFW',0,NULL,NULL,'2020-12-02 02:56:13','2020-12-30 08:31:59'),
	(6,'Super','Administrator 6','None','super-admin6@gmail.com','gAAAAABf7D5YLdtIZV648CB3jiNxmAxMOc7DIB-EahbBHKDpYN1ZUgRfUHHZAGI6fUv9sx6XYdIXeTva0RT1rBnUg1lQdDG3Mg==','super-admin-6','1996-01-01',20,1,'088888','8888888888',1,'jalan atas bawah',NULL,NULL,NULL,4,NULL,0,'BPU3FZ7V-NFEVC9AH-THWBMF8K-7ON0KOWA-HJOI2TA8-28U2Q2RR-DJVXH4LA-8ML7K1VT',0,NULL,NULL,'2020-12-30 08:46:16',NULL);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
