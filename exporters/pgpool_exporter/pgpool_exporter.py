import psycopg2
import time
import json
from prometheus_client import Counter,Gauge,Summary,Histogram
from prometheus_client import start_http_server


pg_primary_nodes_cnt = Gauge('pg_primary_nodes_cnt', 'count of pg primary nodes', ['pg_host'])
pg_standby_nodes_cnt = Gauge('pg_standby_nodes_cnt', 'count of pg standby nodes', ['pg_host'])

def check_pg_active_nodes(db_host, db_port, db_name, db_user, db_password):
    try:
        conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        cur = conn.cursor()
        cur.execute("show pool_nodes")
        rows = cur.fetchall()
        primary_cnt=0
        standby_cnt=0
        for row in rows:
            if row[5] == 'primary' and row[3] == '2':
                primary_cnt = primary_cnt + 1
            elif row[5] == 'standby' and row[3] == '2':
                standby_cnt = standby_cnt + 1
        pg_primary_nodes_cnt.labels(pg_host=db_host).set(primary_cnt)
        pg_standby_nodes_cnt.labels(pg_host=db_host).set(standby_cnt)
    except Exception as inst:
        print inst
    finally:
        conn.close()
    
if __name__ == '__main__':
    start_http_server(8000)
    print "Begin to export pg cluster metrics..."
    with open("/opt/pg_conf/pg.json") as f:
        pg_config = json.load(f)
    while True:
        check_pg_active_nodes(pg_config["db_host"], pg_config["db_port"], pg_config["db_name"], pg_config["db_user"], pg_config["db_password"])
        time.sleep(10)
