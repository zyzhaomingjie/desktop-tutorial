#一共有多少不同的用户
INSERT INTO users select userid from tags; COMMIT;
INSERT INTO users select userid from ratings; COMMIT;
SELECT COUNT(DISTINCT userid) FROM users;

#一共有多少不同的电影
INSERT INTO movies_diff select movieid from tags; COMMIT;
INSERT INTO movies_diff select movieid from ratings; COMMIT;
INSERT INTO movies_diff select movieid from movies; COMMIT;
INSERT INTO movies_diff select movieid from links; COMMIT;
INSERT INTO movies_diff select movieid from genome_scores; COMMIT;
SELECT COUNT(DISTINCT movieid) FROM movies_diff;

#一共有多少不同的电影种类
SELECT COUNT(DISTINCT SUBSTRING_INDEX(SUBSTRING_INDEX(a.`genres`, '|', b.help_topic_id + 1), '|', - 1))
  FROM movies a 
  JOIN mysql.help_topic b 
    ON b.help_topic_id < (LENGTH(a.`genres`) - LENGTH(REPLACE(a.`genres`, '|', '')) + 1);

#一共有多少电影没有外部链接
SELECT COUNT(DISTINCT movieid)
  FROM movies_diff
 WHERE NOT EXISTS (SELECT DISTINCT movieid FROM links);

#2018年一共有多少人进行过电影评分
SELECT COUNT(DISTINCT userid)
  FROM ratings
 WHERE SUBSTR(DATE_FORMAT(date, '%Y-%m-%d %H:%i:%s'), 1, 4) = '2018';

#2018年评分5分以上的电影及其对应的标签
SELECT a.movieid, a.tag, b.rating
  FROM tags a
 INNER JOIN ratings b
    ON a.movieid = b.movieid
   AND b.rating = '5'
   AND SUBSTR(DATE_FORMAT(b.date, '%Y-%m-%d %H:%i:%s'), 1, 4) = '2018'
 GROUP BY a.movieid, a.tag, b.rating;