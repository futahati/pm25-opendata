- tidbcloud

- https://auth.tidbcloud.com/

# 建立資料庫
- show databases; // 請列出目前伺服器上所有的資料庫
- create database test; //目前已內建
- use test; // 切換並開始使用名為 'test' 的資料庫

# 建立資料表
- use test; // 切換並開始使用名為 'test' 的資料庫
- show tables;
- create table if not exists shop(
id int primary key auto_increment,
item varchar(50) unique,
qty int default 1,
amount decimal(6, 2) default 0.0,
created_at datetime default current_timestamp
);

- unique(唯一)
- default(預設值)
- current_timestamp(時間記)
- datetime / timestamp
- 修改時區 set time_zone="+08:00";

# CRUD語法

### Create
- insert into shop(item) values("test123");
- insert into shop(qty, amount, item) values(10, 6666.66, "test123");
- insert into shop values (1, "samsung notebook", 10, 2490.99, "2026-04-12 14:42:22");

### Read
- select * from shop;
- SELECT * FROM test.shop;
- select item, qty from shop;
- select item as 商品名稱, qty as 數量 from shop;
- select item, amount from shop where amount >= 10;
- select item, amount from shop where id=5; // where 是用於比較時，使用 = 號
- select * from shop order by qty desc;  //預設asc

### Update
- UPDATE shop SET item="LG Notebook" WHERE id=4;
- UPDATE shop SET item="LG Notebook", qty=86 WHERE id=4;
- UPDATE shop SET created_at="2026-04-12 15:25:22";

### Delete
- delete from shop;  // 清除資料表內容
- delete from shop where id=3; // where 指定條件


### Drop
- drop database test;
- drop table shop;


### Alter （針對資料表的欄位）
- alter table shop add column note text; // 新增欄位
- alter table shop modify column amount DECIMAL(10, 2); // 修改欄位型態
- alter table shop change column created_at update_date TIMESTAMP; // 修改欄位名稱，要帶原本的型態
- alter table shop drop column qty; // 刪除欄位

