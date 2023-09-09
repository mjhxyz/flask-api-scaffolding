CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `test`;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '班级名称',
  `add_time` datetime NOT NULL COMMENT '添加时间',
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class`
VALUES (1, '三年二班', '2023-09-09 01:23:42', NULL);
INSERT INTO `class`
VALUES (2, '四年三班', '2023-09-09 01:23:54', NULL);
INSERT INTO `class`
VALUES (3, '天才班', '2023-09-09 01:24:05', NULL);
INSERT INTO `class`
VALUES (4, '劳改班', '2023-09-09 01:24:15', NULL);
-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '名称',
  `age` int(20) NOT NULL COMMENT '年龄',
  `class_id` int(11) NOT NULL COMMENT '班级ID',
  `balance` int(11) NOT NULL DEFAULT 0 COMMENT '拥有的余额',
  `add_time` datetime NOT NULL COMMENT '添加日期',
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改日期',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student`
VALUES (
    1,
    '毛某',
    18,
    1,
    9000,
    '2023-09-09 01:24:32',
    NULL
  );
INSERT INTO `student`
VALUES (
    2,
    '关羽',
    19,
    1,
    5000,
    '2023-09-09 01:24:43',
    NULL
  );
INSERT INTO `student`
VALUES (
    3,
    '赵云',
    22,
    2,
    4000,
    '2023-09-09 01:24:52',
    NULL
  );
INSERT INTO `student`
VALUES (
    4,
    '张飞',
    18,
    3,
    8000,
    '2023-09-09 01:25:05',
    NULL
  );
INSERT INTO `student`
VALUES (
    6,
    '黄忠',
    21,
    4,
    6000,
    '2023-09-09 01:25:19',
    NULL
  );
INSERT INTO `student`
VALUES (
    7,
    '马超',
    17,
    3,
    7000,
    '2023-09-09 01:26:04',
    NULL
  );
SET FOREIGN_KEY_CHECKS = 1;