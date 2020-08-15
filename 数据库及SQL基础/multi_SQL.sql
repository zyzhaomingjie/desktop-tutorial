#1.查询同时存在1课程和2课程的情况
SELECT * 
  FROM student1
 WHERE name IN (SELECT t3.name 
                FROM course1 t1
                LEFT JOIN student_course1 t2
                  ON t1.id = t2.courseid
                LEFT JOIN student1 t3
                  ON t2.studentid = t3.id
               WHERE t2.courseid in ('1', '2')
               GROUP BY t3.name
              HAVING COUNT(1)= 2);

#3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
SELECT t1.id, t1.name, AVG(t2.score) AS avg_score
  FROM student1 t1 
  LEFT JOIN  student_course1 t2
    ON t1.id = t2.studentid
 GROUP BY t1.id, t1.name
HAVING avg_score>=60;

#4.查询在student_course表中不存在成绩的学生信息
SELECT t1.*
  FROM student1 t1 
  LEFT JOIN  student_course1 t2
    ON t1.id = t2.studentid
 WHERE t2.score is null;

#5.查询所有有成绩的
SELECT t1.id, t1.name, t1.age, t1.sex
  FROM student1 t1 
  LEFT JOIN  student_course1 t2
    ON t1.id = t2.studentid
 WHERE t2.score is not null
 GROUP BY t1.id, t1.name, t1.age, t1.sex;

#6.查询学过编号为1并且也学过编号为2的课程的同学的信息
SELECT * 
  FROM student1
 WHERE name IN (SELECT t3.name 
                FROM course1 t1
                LEFT JOIN student_course1 t2
                  ON t1.id = t2.courseid
                LEFT JOIN student1 t3
                  ON t2.studentid = t3.id
               WHERE t2.courseid in ('1', '2')
               GROUP BY t3.name
              HAVING COUNT(1)= 2);

#7.检索1课程分数小于60，按分数降序排列的学生信息
SELECT t3.id, t3.name, t3.age, t3.sex
  FROM course1 t1
  LEFT JOIN student_course1 t2
    ON t1.id = t2.courseid
  LEFT JOIN student1 t3
    ON t2.studentid = t3.id
 WHERE t2.courseid = '1'
   AND t2.score < 60
 ORDER BY t2.score DESC;

#8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
SELECT t1.courseid, AVG(t1.score) AS avg_score
  FROM student_course1 t1
 GROUP BY t1.courseid
 ORDER BY avg_score DESC, t1.courseid ASC;

#9.查询课程名称为"数学"，且分数低于60的学生姓名和分数
SELECT t3.name, t2.score
  FROM course1 t1
  LEFT JOIN student_course1 t2
    ON t1.id = t2.courseid
  LEFT JOIN student1 t3
    ON t2.studentid = t3.id
 WHERE t1.name = '数学'
   AND t2.score < 60;