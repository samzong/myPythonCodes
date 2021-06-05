# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

if __name__ == '__main__':
    
    from sqlalchemy import create_engine
    from sqlalchemy import text
    
    engine = create_engine("mysql+pymysql://root:luchuanjia@127.0.0.1:3306/letsdesk_m5")
    conn = engine.connect()
    
    query = text("SELECT  eq_seq FROM s_equipment WHERE eq_seq like '%/%';")
    
    s = conn.execute(query)
    res = s.fetchall()
    
    for r in res:
        print(type(r), r)
    
    import pandas as pd
    
    df = pd.DataFrame(res)
    
    df.to_csv('/Users/Alex/Desktop/eq2.csv', index=False)
