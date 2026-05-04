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

# VS Code 中的 Jupyter Notebook 快捷鍵(鍵盤流)
- https://markdownlivepreview.com/
- 如果你記不住這些，隨時在 VS Code 中按下 Ctrl + Shift + P 並輸入 Jupyter，它會列出所有可用的功能與對應的快捷鍵。

## 核心模式切換

|核心模式|**命令模式**|**編輯模式**|
|-|:-------------:|:-------------:|
|操作方法|按 `ESC` 鍵|按 `Enter` 鍵|
|畫面顯示狀態|儲存格左側的線會變細，且儲存格內沒有游標|儲存格左側會有一條粗線（顏色通常隨你的佈景主題，如藍色或紫色），且儲存格內可以看到閃爍的游標|

### 命令模式下儲存格操作

|   指令按鍵   |指令說明|
| :--: | :--: |
| **Ｙ** |切換為程式碼 (Code)|
| **Ｍ** |切換為標記 (Markdown)|
|A|向上新增儲存格|
|B|向下新增儲存格|
| (連續按)D,D |刪除選中的儲存格|
|X|剪下儲存格|
|C|複製儲存格|
|V|貼上儲存格|
|Z|復原上一個操作|
|O| 隱藏或顯示儲存格的輸出結果 (Output)|
|I, I| 中斷 Kernel（當程式跑太久卡住時）（遇到無窮迴圈時的救命藥）|
|0, 0| 重啟 Kernel（程式亂掉時，砍掉重練最快）|
|J / K| 向上或向下移動選取框|
|Down / Up| 向上或向下移動選取框|
|   Ctrl + /   | `註解/取消註解` 選取的程式碼 |

### 其他操作

|快捷鍵組合| 指令說明|
| :-: | :-: |
|Ctrl + Enter| 執行當前儲存格（留在原位）|
|Shift + Enter| 執行當前儲存格，並跳到下一個（若下方沒格則會新建）（最常用，像翻書一樣往下跑） |
|Alt + Enter| 執行當前儲存格，並在下方插入新格|
|Ctrl + Up / Down| 直接捲動頁面，但選取框不動，適合在看長程式碼時使用|
|Shift + L| 切換顯示程式碼行號|
| Ctrl + Shift + P 輸入Run All 並按 Enter | 執行全部 (Run All)|

# SQLite3 與 MySQL(PyMySQL)

- ２者類別差異之處

|                         SQLite3                         |                                           MySQL(PyMySQL)                                           |
| :------------------------------------------------------: | :------------------------------------------------------------------------------------------------: |
|                          檔案型                          |                                          客戶端/伺服器型                                          |
|          不需要安裝伺服器軟體，直接讀寫硬碟檔案          |                           用來連接 MySQL 或 MariaDB 伺服器的「驅動程式」                           |
|       資料庫就是一個副檔名為 .db 或 .sqlite 的檔案       |       資料庫運行在伺服器上（可能是本機或雲端），你需要透過 IP、連接埠 (Port)、帳號密碼來存取       |
| 雖然支援多個連線讀取，但在「寫入」時會鎖定整個資料庫檔案 |             支援高併發，可以同時處理成千上萬個使用者的讀寫請求，適合網站後端或大型系統             |
|               資料類型比較寬鬆（動態類型）               |                                         資料類型嚴謹且豐富                                         |
|  不支援一些進階的 SQL 功能（例如複雜的使用者權限管理）  |                          擁有完整的權限控管系統（可以設定誰能讀、誰能改）                          |
|         提交指令：在執行 execute() 後通常會生效         | 提交指令：**預設不會自動提交**，在 PyMySQL 執行 INSERT/CREATE 後，一定要加 `conn.commit()` |

- 在 CREATE 語法上的差異

| CREATE 語法                                      | SQLite3                                            | MySQL(PyMySQL)                                         |
| ------------------------------------------------ | :------------------------------------------------- | :----------------------------------------------------- |
| ID                                               | id `integer` primary key **autoincrement** | id `int` primary key **auto_increment**        |
| 自動遞增                                         | autoincrement                                      | auto_increment(有底線)                                 |
| 整數                                             | integer                                            | int                                                    |
| 文字、字串                                       | text                                               | VARCHAR(N)：需要指定長度N                              |
| 日期時間格式                                     | text                                               | datatime                                               |
| unique(複合唯一約束)                             | 寫法（二選一）                                     | 寫法（三選一）                                         |
| 寫法 A：使用 CONSTRAINT 關鍵字（推薦，最標準）   | CONSTRAINT uq_規則名字 UNIQUE (欄位1, 欄位2)       | CONSTRAINT uq_規則名字 UNIQUE (欄位1, 欄位2)           |
| 寫法 B：不具名寫法（系統自動命名）               | UNIQUE (欄位1, 欄位2)                              | UNIQUE (欄位1, 欄位2)                                  |
| 寫法 C：具名唯一鍵UNIQUE [KEY] [規則名字] (欄位) | ❌                                                 | **UNIQUE KEY** uq_規則名字 UNIQUE (欄位1, 欄位2) |

- 在 INSERT 語法上的差異
  > SQLite3 用 `insert or ignore`：遇到重複資料，它會**優雅地跳過**，程式繼續執行。
  > MySQL(PyMySQL) 用 `insert ignore`：遇到重複資料，它會**優雅地跳過**，程式繼續執行。
  >

| INSERT 語法 |                               SQLite3                               |                          MySQL(PyMySQL)                          |
| :---------: | :-----------------------------------------------------------------: | :---------------------------------------------------------------: |
| 佔位符符號 |                        使用問號 ? 作為佔位符                        |                        使用 %s 作為佔位符                        |
|    寫法    | `insert or ignore` into 資料表名稱 (欄位名稱) **values(?)** | `insert ignore` into 資料表名稱 (欄位名稱) **values(%s)** |

# PyMySQL套件

- pip install pymysql
- pip list 查目前環境套件有那些
- .gitigmore

  - 把 .venv 、 .vscode 寫入（隱藏／忽略資料夾，不上傳Github）
- vscode 建立 test.jpynb

  - 用 .venv，記得在進入 Jupyter 後，先確認右下角或右上角的 Kernel 是不是指向 ./.venv/bin/python。如果不是，用剛才提到的 Ctrl + Shift + P 搜 Select Kernel 來切換。
  - import pandas as pd
  - Select Kemel => 選 Install/enable suggested extensions Python + Jupyter
  - 選 Python Environments...
  - 2擇一，優先選.venv
    - 選 .venv(X.XX.XX)(Python X.XX.XX).venv\Scripts\python.exe    Recommended
    - 選 Create Python Environment
  - 再run程式碼import pandas as pd
  - (新視窗)Running cells with '.venv(X.XX.XX)(Python X.XX.XX)' requires the ipykemel package.
    - 選項： Install , Chamge Kemel , More Info , Cancel
    - 選 Install => 安裝 ipykemel 套件
  - 避開SSL驗證問題
    - 改用JSON格式 api_url 注意！
    - import requests, io
    - 要寫2行
      - resp = requests.get(api_url), verify=False)
      - ❌df = pd.read_csv(io.StringIO(resp.text))
      - df = pd.read_json(io.StringIO(resp.text))
  - import sqlite3
  - 建立資料表
  - def使用pymysql不是sqlite3
    - 2者的語法有差異，寫def create_table()時要注意！！
      - 寫入 SQLite ❌sqlite3.connect()-->(本次不使用)開發測試、本地儲存
        - ✅integer  ❌int
        - id integer primary key autoincrement
      - 寫入 MySQL  ✅pymysql.connect()-->生產環境、多人存取
        - id int primary key auto_increment
        - SQLite, MySQL型態差異
        - 數值 ✅int  ❌integer
        - 文字 ✅varchar()  ❌text
        - 日期時間格式 ✅datatime  ❌text
        - unique key uq_site_datacreationdate (site,datacreationdate)
  - 建立table => def create_table()
  - def使用pymysql不是sqlite3
    - 改 id int primary key auto_increment,
    - 改 site varchar(50)
    - 改 county varchar(20)
    - 改 pm25 int
    - 改 datacreationdate datetime
    - 改 itemunit varchar(20)
    - 改 unique key uq_site_datacreationdate (site,datacreationdate)  # uq是 Unique 的縮寫(唯一性約束)
    - global 區域、全域問題
  - 插入 def insert_data(data)
    - values(?, ?, ?, ?, ?)要改 values(%s, %s, %s, %s, %s)
  - 打開資料庫 => def open_db() + TiDBcloud
  - TiDB進入的操作
    - 首頁
    - 資料庫
    - 右上角黑色框 connect
    - （新視窗）滑到最下方 => 必填資訊
    - host, port, user, password, database, ssl
      - 下午改 ssl={"ca":None}
  - TiDB網站下載 `isrgrootxl.pem`
  - [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) https://inloop.github.io/sqlite-viewer/
    - 將 pm25.db 檔案直接拖移至網頁上
    - pass
- 手動建立 .venv 環境

  1. 建立新的虛擬環境
     在 VS Code 的終端機（Terminal）輸入：
     ```
     # 建立虛擬環境
     python -m venv .venv
     ```
  2. 安裝必要套件
     ```
     # 安裝核心套件
     pip install ipykernel
     ```
  3. 重新指向 Kernel
     1. 回到程式碼檔案(.py .ipynb)
     2. 點擊右上角的 "Select Kernel"
     3. 選擇 "Python Environments..."
     4. 找到剛才建立的那個 `.venv` 路徑
- 手動指定解釋器 (Interpreter)

  1. 按下鍵盤 `Ctrl + Shift + P`
  2. 輸入 `Python: Select Interpreter` 並點選它
  3. 在選單中找路徑包含 `.venv` 的那一項（應該會顯示 `Python 3.14.4 ('.venv': venv)`），點選它
- 自動生成 `requirements.txt`

  - 在終端機左側有出現 (.venv)輸入
    ```
    pip freeze > requirements.txt
    ```
    1. **requirements.txt** 不能打錯字！
    2. pip freeze：列出目前環境中所有安裝的套件與精確版本號。
    3. \>：將輸出的內容導向（寫入）到檔案。
    4. requirements.txt：目標檔案名稱（如果檔案已存在，會直接覆蓋）。
- 定時自動執行Python腳本

  - Scheduled Workflow 設定
    1. 在專案下，新增Folder，名稱 `.github`
    2. 在 .github 下，新增Folder，名稱 `workflows`
    3. 在 workflows 下，新增file，副檔名 `.yml`
       - 課程上 `scheduled.yml` 是老師給的
       - 修改 .yml 內容
         1. 上方第5列 - cron: '`0 0` * * *' # 每天國際標準時間 00：00 (台灣時間 08:00)
            > 改為 - cron: '`59 15` * * *'
            > 每天國際標準時間 00：00 (台灣時間 23:59)
            >
         2. 下方倒數第3列 run: python `your_script_name.py`
            > 改為專案要 run 的檔案，例： `pm25.py`
            >
         3. 下方倒數第1列 `API_KEY`: ${{ secrets.`MY_API_KEY` }}
            > 將 .env 裡的所有內容一筆一筆寫入 `name`: ${{  secrets.`name` }}
            >
            >> `age`: ${{  secrets.`age` }}
            >>
            >
- 在GitHub使用自動化腳本

  1. 進入GitHub該專案，點 `Settings`
  2. (新畫面)左側欄位，點 `Secrets and variables`
     - 下拉選單，點 `Actions`
  3. (新畫面)右側欄位最下方 **Repository secrets**，點綠色框 `New repository secret`
  4. (新畫面)：將 .env 裡的 `key` = `values` 一筆一筆輸入
     1. Name 輸入 `key`
     2. Secret 輸入 `values`
     3. 按 Add secret
  5. 上方欄位，點 `Actions`
  6. (新畫面)左側欄位第3列，會看到與 `scheduled.yml` 裡一樣的 name: **Scheduled Python Script** 點擊
  7. 點擊後，右側會看見藍色框裡的 `Run workflow` 點擊
  8. (跳出視窗)點 `Run workflow`
  9. (新畫面)點 `run-python`
