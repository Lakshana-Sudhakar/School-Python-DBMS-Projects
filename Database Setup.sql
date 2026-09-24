1) creating the goddamn table
CREATE TABLE 1c (id INT PRIMARY KEY,
day VARCHAR(10) NOT NULL,
period1 VARCHAR(20),
period2 VARCHAR(20),
break1 VARCHAR(20),
period3 VARCHAR(20),
period4 VARCHAR(20),
period5 VARCHAR(20),
lunch VARCHAR(20),
period6 VARCHAR(20),
period7 VARCHAR(20),
period8 VARCHAR(20),
period9 VARCHAR(20));

2) inserting values
-1a
INSERT INTO 1a VALUES
(1,'Monday', 'English', 'Math', 'BREAK', 'EVS', 'Hindi', 'Social', 'LUNCH', 'English', 'Math', 'EVS', 'Games'),
(2,'Tuesday', 'Hindi', 'Social', 'BREAK', 'Games', 'Math', 'English', 'LUNCH', 'Math', 'Hindi', 'Social', 'Math'),
(3,'Wednesday', 'Math', 'English', 'BREAK', 'Hindi', 'Social', 'EVS', 'LUNCH', 'Math', 'EVS', 'Games', 'Hindi'),
(4,'Thursday', 'EVS', 'Games', 'BREAK', 'Math', 'English', 'Hindi', 'LUNCH', 'Social', 'Math', 'Hindi', 'English'),
(5,'Friday', 'Social', 'Hindi', 'BREAK', 'English', 'Math', 'EVS', 'LUNCH', 'Math', 'English', 'Games', 'EVS');

-1b
INSERT INTO 1b VALUES
(1,'Monday', 'Math', 'Games', 'BREAK', 'Hindi', 'English', 'EVS', 'LUNCH', 'Social', 'Hindi', 'English', 'Math'),
(2,'Tuesday', 'Social', 'English', 'BREAK', 'Math', 'Games', 'Hindi', 'LUNCH', 'EVS', 'Social', 'Math', 'English'),
(3,'Wednesday', 'English', 'Hindi', 'BREAK', 'EVS', 'Math', 'Social', 'LUNCH', 'Games', 'English', 'EVS', 'Math'),
(4,'Thursday', 'Hindi', 'Social', 'BREAK', 'English', 'EVS', 'Games', 'LUNCH', 'Math', 'Hindi', 'English', 'Social'),
(5,'Friday', 'Games', 'Math', 'BREAK', 'EVS', 'English', 'Social', 'LUNCH', 'Hindi', 'Math', 'EVS', 'English');

-1c
INSERT INTO 1c VALUES
(1,'Monday', 'EVS', 'Hindi', 'BREAK', 'English', 'Social', 'Math', 'LUNCH', 'Games', 'Social', 'Hindi', 'English'),
(2,'Tuesday', 'English', 'Math', 'BREAK', 'Social', 'Hindi', 'EVS', 'LUNCH', 'Games', 'EVS', 'English', 'Social'),
(3,'Wednesday', 'Hindi', 'EVS', 'BREAK', 'Math', 'English', 'Games', 'LUNCH', 'Social', 'Math', 'Hindi', 'EVS'),
(4,'Thursday', 'Social', 'Math', 'BREAK', 'EVS', 'Hindi', 'English', 'LUNCH', 'English', 'Games', 'Social', 'Math'),
(5,'Friday', 'English', 'Social', 'BREAK', 'Hindi', 'EVS', 'Math', 'LUNCH', 'Games', 'EVS', 'Math', 'Hindi');

3) Creating teacher table
CREATE TABLE engteach (id INT,
day VARCHAR(10),
period1 VARCHAR(10),
period2 VARCHAR(10),
BREAK varchar(10),
period3 VARCHAR(10),
period4 VARCHAR(10),
period5 VARCHAR(10),
LUNCH varchar(10),
period6 VARCHAR(10),
period7 VARCHAR(10),
period8 VARCHAR(10),
period9 VARCHAR(10),
period10 VARCHAR(10));

4) inserting into teacher table
- engteach
INSERT INTO engteach VALUES
(1,'Monday','1a','','BREAK','1a','','','LUNCH','','','','1c',''),
(2,'Tuesday','1b','','BREAK','1b','','','LUNCH','','','1c','',''),
(3,'Wednesday','','1a','BREAK','','','','LUNCH','1a','','','1c',''),
(4,'Thursday','','','BREAK','','1a','','LUNCH','1c','','','','1a'),
(5,'Friday','1a','','BREAK','','1c','','LUNCH','','','1a','1c','');

- mteach(math)
INSERT INTO mteach VALUES
(1,'Monday','','1a','BREAK',' ',' ',' ','LUNCH','1a',' ',' ','1b',' '),
(2,'Tuesday',' ','1b','BREAK',' ',' ',' ','LUNCH','1a',' ',' ','1b',' '),
(3,'Wednesday','1c','1a','BREAK',' ',' ',' ','LUNCH','1a',' ',' ','1c',' '),
(4,'Thursday',' ','1a','BREAK',' ',' ',' ','LUNCH','1a',' ',' ','1a',' '),
(5,'Friday',' ','1b','BREAK',' ',' ',' ','LUNCH','1b',' ','1c','1b',' ');

- hteach (hindi)
INSERT INTO hteach VALUES
(1,'Monday',' ',' ','BREAK','1a',' ',' ','LUNCH',' ','1a',' ','1c',' '),
(2,'Tuesday','1b',' ','BREAK',' ','1b',' ','LUNCH',' ','1b',' ',' ',' '),
(3,'Wednesday',' ',' ','BREAK','1c',' ',' ','LUNCH',' ','1c',' ',' ',' '),
(4,'Thursday','1a',' ','BREAK',' ','1c',' ','LUNCH',' ','1a',' ',' ',' '),
(5,'Friday','1b',' ','BREAK',' ','1c',' ','LUNCH',' ','1a',' ',' ',' ');

- etach(evs)
INSERT INTO eteach VALUES
(1,'Monday',' ','1a','BREAK',' ',' ',' ','LUNCH','1c',' ',' ',' ','1b'),
(2,'Tuesday',' ',' ','BREAK','1b',' ',' ','LUNCH','1b',' ',' ',' ','1b'),
(3,'Wednesday','1a',' ','BREAK',' ','1b',' ','LUNCH',' ','1b',' ',' ',' '),
(4,'Thursday','1c',' ','BREAK',' ','1c',' ','LUNCH',' ','1c',' ',' ',' '),
(5,'Friday',' ',' ','BREAK',' ','1b',' ','LUNCH',' ','1c',' ',' ',' ');

- steach(social)
INSERT INTO steach VALUES
(1,'Monday','1a',' ','BREAK','1a',' ',' ','LUNCH','1c',' ',' ',' ','1a'),
(2,'Tuesday',' ','1b','BREAK',' ',' ',' ','LUNCH','1a',' ',' ','1b',' '),
(3,'Wednesday','1c',' ','BREAK',' ',' ',' ','LUNCH','1a',' ',' ',' ','1c'),
(4,'Thursday',' ','1b','BREAK',' ',' ',' ','LUNCH','1c',' ',' ','1c',' '),
(5,'Friday',' ','1a','BREAK',' ',' ',' ','LUNCH','1b',' ',' ',' ','1b');

- gteach(games)
INSERT INTO gteach VALUES
(1,'Monday',' ','1b','BREAK',' ',' ',' ','LUNCH',' ','1a',' ',' ',' '),
(2,'Tuesday',' ','1b','BREAK',' ',' ',' ','LUNCH',' ','1b',' ',' ','1a'),
(3,'Wednesday',' ',' ','BREAK','1a',' ',' ','LUNCH',' ','1b',' ',' ',' '),
(4,'Thursday',' ','1a','BREAK',' ',' ',' ','LUNCH',' ','1a',' ',' ',' '),
(5,'Friday',' ','1b','BREAK',' ',' ',' ','LUNCH',' ','1c',' ',' ',' ');
