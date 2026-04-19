import pandas as pd
import requests, io
import pymysql
from datetime import datetime
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 使用api取得資料
def get_data():
    try:
        # csv格式
        # api_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=af57253c-e838-46da-a1f5-12b43afd75f3&limit=1000&sort=datacreationdate%20desc&format=CSV"
        # json格式
        api_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=846e44e1-8cc5-4893-ad87-c79d2d383706&limit=1000&sort=datacreationdate%20desc&format=JSON"
        resp = requests.get(api_url, verify=False)
        # df = pd.read_csv(io.StringIO(resp.text))
        df = pd.read_json(io.StringIO(resp.text))
        df1 = df.drop_duplicates(subset=["site", "datacreationdate"]).dropna()
        data = df1.values.tolist()

        return data
    
    except Exception as e:
        print(e)

    return None


# 插入資料
# 使用 MySQL(PyMySQL) 語法
def insert_data(data):
    try:
        # sqlite 與 mysql 的 佔位符 寫法不一樣，注意！  %s是佔位符，與f-strings無關
        sqlstr = "insert ignore into data (site,county,pm25,datacreationdate,itemunit) values(%s, %s, %s, %s, %s)"
        cursor.executemany(sqlstr, data)  # 大量執行
        conn.commit()  # 手動存檔

        if cursor.rowcount == 0:
            print("目前無更新資料。")
        else:
            print(f"新增{cursor.rowcount}筆資料。")

    except Exception as e:
        print(e)


# 建立雲端連線
# 使用 MySQL(PyMySQL) 語法
def open_db():
    # host=os.getenv("HOST") ← os.getenv()本地端dotenv使用
    try:
        conn = pymysql.connect(
            host=os.environ.get("HOST"),
            port=int(os.environ.get("PORT")),
            user=os.environ.get("NAME"),
            password=os.environ.get("PASSWORD"),
            database=os.environ.get("DATABASE"),
            ssl={"ca":None}
        )

        cursor = conn.cursor()

        return conn, cursor
    
    except Exception as e:
        print(e)

    return None, None


# 建立資料表
# 使用 MySQL(PyMySQL) 語法
def create_table():
    global conn, cursor
    try:
        # sqlite 與 mysql 寫法不一樣，注意！
        sqlstr = '''
        create table if not exists data(
        id int primary key auto_increment,
        site varchar(50),
        county varchar(20),
        pm25 int,
        datacreationdate datetime,
        itemunit varchar(20),
        unique key uq_site_datacreationdate (site, datacreationdate)
        )
        '''

        index = cursor.execute(sqlstr)  # 單筆執行
        conn.commit()  # 手動存檔

        if index:
            print("建立資料表成功。")

    except Exception as e:
        print(e)


print("=="*30)
start_time = datetime.now()
print(f"運行開始時間：{start_time}")

conn, cursor = open_db()
# print(conn, cursor)

if conn is not None:
    create_table()
    data = get_data()
    if data:
        insert_data(data)

    conn.close()  # 關閉連線，要不然資料庫會出錯
else:
    print("資料庫開啟失敗。")

print("=="*30)
end_time = datetime.now()
print(f"運行結束時間：{start_time}")

print("=="*30)
print(f"執行時間：{end_time-start_time}")

# print(data)