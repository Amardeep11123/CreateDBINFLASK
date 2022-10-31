-- (A) USERS TABLE
CREATE TABLE menu (
  id INTEGER,
  name TEXT NOT NULL,
  img_path TEXT NOT NULL,
  value INTEGER,
  PRIMARY KEY("id" AUTOINCREMENT)
);
 
CREATE INDEX `idx_name`
  ON `menu` (`name`);

-- (B) DUMMY DATA
INSERT INTO "menu" VALUES
(1,'Run001','/static/images/test1.PNG','10'),
(2,'Run002','/static/images/test2.PNG','20'),
(3,'Run003','/static/images/test3.PNG','30'),
(4,'Papra','/static/images/test4.PNG','50');