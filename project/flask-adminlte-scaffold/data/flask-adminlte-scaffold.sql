/*
 Navicat MySQL Data Transfer

 Source Server         : mysql.jingsky.com
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : mysql.jingsky.com
 Source Database       : flask-adminlte-scaffold

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : utf-8

 Date: 10/08/2019 12:51:35 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `tb_item`
-- ----------------------------
DROP TABLE IF EXISTS `tb_item`;
CREATE TABLE `tb_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `parent_id` int(11) NOT NULL,
  `url` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `tb_item`
-- ----------------------------
BEGIN;
INSERT INTO `tb_item` VALUES ('1', '系统管理', '2018-11-29 17:30:06', '2018-11-29 17:30:09', '0', ''), ('2', '用户管理', '2018-11-29 17:30:21', '2018-11-29 17:30:25', '1', '/go_user_list'), ('3', '角色管理', '2018-11-29 17:30:48', '2018-11-29 17:30:50', '1', '/sys/gotoRoleManager'), ('4', '菜单管理', '2018-11-29 17:31:07', '2018-11-29 17:31:10', '1', '/sys/goEditItem'), ('5', '个人中心', '2018-11-29 17:31:24', '2018-11-29 17:31:26', '0', ''), ('6', '修改密码', '2018-11-29 17:31:41', '2018-11-29 17:31:44', '5', ''), ('7', '权限管理', '2018-11-29 17:34:58', '2018-11-29 17:35:01', '1', '/sys/goEditRoleItem');
COMMIT;

-- ----------------------------
--  Table structure for `tb_role`
-- ----------------------------
DROP TABLE IF EXISTS `tb_role`;
CREATE TABLE `tb_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `tb_role`
-- ----------------------------
BEGIN;
INSERT INTO `tb_role` VALUES ('1', '管理员', '2018-11-29 17:11:30', '2018-11-29 17:11:33'), ('2', '普通用户', '2018-11-29 17:27:30', '2018-11-29 17:27:33'), ('4', '新用户', '2018-12-05 19:24:49', '2018-12-05 19:24:49');
COMMIT;

-- ----------------------------
--  Table structure for `tb_role_item`
-- ----------------------------
DROP TABLE IF EXISTS `tb_role_item`;
CREATE TABLE `tb_role_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(64) NOT NULL,
  `item_name` varchar(64) NOT NULL,
  `role_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_id` (`role_id`,`item_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `tb_role_item_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `tb_role` (`id`),
  CONSTRAINT `tb_role_item_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `tb_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `tb_role_item`
-- ----------------------------
BEGIN;
INSERT INTO `tb_role_item` VALUES ('1', '管理员', '系统管理', '1', '1', '2018-11-29 17:34:16', '2018-11-29 17:34:20'), ('2', '管理员', '权限管理', '1', '7', '2018-11-29 17:35:33', '2018-11-29 17:35:35'), ('3', '管理员', '角色管理', '1', '3', '2018-12-04 19:19:25', '2018-12-04 19:19:28'), ('5', '管理员', '用户管理', '1', '2', '2018-12-08 17:42:53', '2018-12-08 17:42:55'), ('6', '管理员', '菜单管理', '1', '4', '2018-12-14 20:10:37', '2018-12-14 20:10:39');
COMMIT;

-- ----------------------------
--  Table structure for `tb_user`
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `pwd` char(32) NOT NULL,
  `role_id` int(11) NOT NULL,
  `enabled` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `tb_user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `tb_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `tb_user`
-- ----------------------------
BEGIN;
INSERT INTO `tb_user` VALUES ('1', 'admin', '202cb962ac59075b964b07152d234b70', '1', '1', '2018-11-29 17:12:32', '2018-11-29 17:12:36'), ('3', '23232323', 'd9b1d7db4cd6e70935368a1efb10e377', '1', '1', '2018-12-10 20:03:37', '2018-12-10 20:03:37'), ('4', 'admin11', 'd9b1d7db4cd6e70935368a1efb10e377', '1', '1', '2018-12-10 20:04:04', '2018-12-10 20:04:04'), ('5', '1223123', 'd9b1d7db4cd6e70935368a1efb10e377', '1', '1', '2018-12-10 20:04:19', '2018-12-10 20:04:19'), ('6', '44444', 'd9b1d7db4cd6e70935368a1efb10e377', '1', '1', '2018-12-10 20:04:29', '2018-12-10 20:04:29'), ('8', 'aaa', 'd9b1d7db4cd6e70935368a1efb10e377', '1', '1', '2018-12-10 20:04:45', '2018-12-10 20:04:45'), ('9', 'san', '3049a1f0f1c808cdaa4fbed0e01649b1', '2', '1', '2018-12-10 20:04:54', '2018-12-10 20:04:54'), ('13', '444444444', 'bf9f8d1f05dc08cc3b02e8fcf2c2ba57', '1', '1', '2018-12-11 17:25:19', '2019-10-08 11:53:01'), ('15', 'mark', 'e10adc3949ba59abbe56e057f20f883e', '1', '1', '2019-10-08 10:30:15', '2019-10-08 10:30:15');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
