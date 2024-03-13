sql = {'select_data': '''
                        SELECT *
                        FROM stock
                        WHERE USE_YN = 'Y'
                        '''
    , 'insert_data': '''
                INSERT INTO stock_price (code, seq, PROCE)
                VALUES (:1, stock_seq.NEXTVAL, :2)

       '''
       }
# 정해진 시간 마다
# 조회 종목의 현재가를 수집하여 stock_price 테이블에 저장
import cx_Oracle
import naver_price
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import datetime
import pythonProject.python_lib.mylogger as logger

log = logger.make_logger("stock.log", "get_stock.py")
seoul = pytz.timezone("Asia/seoul")


def fn_current_price():
    log.info("fn_current_price start!!")
    conn = cx_Oracle.connect("study", "study", "127.0.0.1:1521/xe")
    cur = conn.cursor()
    cur.execute(sql['select_data'])
    rows = cur.fetchall()
    try:
        for row in rows:
            print(row)
            code = row[0]
            nm = row[1]
            price = naver_price.get_price(code)
            cur.execute(sql['insert_data'], [code, price])
    except Exception as e:  # 오류났을때
        log.exception(str(e))
        conn.rollback()
    else:  # 정상처리시
        conn.commit()
    finally:  # 오류, 정상 모두 마지막에 수행됨.
        conn.close()


if __name__ == '__main__':
    log.info("start stock scheduler")
    sched = BlockingScheduler()
    sched.add_job(fn_current_price, 'interval', minutes=2, timezone=seoul)
    sched.start()
