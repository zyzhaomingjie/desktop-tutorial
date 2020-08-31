/*
Navicat MySQL Data Transfer

Source Server         : zhaomingjie
Source Server Version : 80021
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80021
File Encoding         : 65001

Date: 2020-08-31 19:34:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Procedure structure for calc_student_stat
-- ----------------------------
DROP PROCEDURE IF EXISTS `calc_student_stat`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `calc_student_stat`()
BEGIN

TRUNCATE TABLE student_stat;

INSERT INTO student_stat 
  (name,
   teacher,
   subject,
   score,
   avg_score,
   total_score,
   score_rate)
	SELECT t1.name,
		   t1.teacher,
		   t1.subject,
		   t1.score,
		   t2.avg_score,
		   t3.total_score,
		   CONCAT(ROUND(t1.score / t3.total_score * 100, 2), '%') AS score_rate
      FROM (SELECT b.name,
				   c.teacher,
				   c.subject,
			       a.student_id,
				   a.subject_id,
				   a.score
			  FROM score a
			  LEFT JOIN student b
				ON a.student_id = b.id
			  LEFT JOIN subject c
				ON a.subject_id = c.id) t1
	  LEFT JOIN (SELECT subject_id,
					    AVG(score) AS avg_score
				   FROM score
				  GROUP BY subject_id) t2
		ON t1.subject_id = t2.subject_id
	  LEFT JOIN (SELECT student_id,
						SUM(score) AS total_score
				   FROM score
				  GROUP BY student_id) t3
	    ON t1.student_id = t3.student_id;

END
;;
DELIMITER ;
