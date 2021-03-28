from futu import *
from futu.common.constant import SubType, RET_OK, RET_ERROR
from futu.quote.open_quote_context import OpenQuoteContext
from futu.quote.quote_response_handler import StockQuoteHandlerBase
import pandas as pd
import matplotlib.pyplot as plt
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_market_snapshot(['HK.09888', 'HK.09988', 'HK.01024'])
if ret == RET_OK:
    df = pd.DataFrame(data, columns = ['code','update_time','last_price','open_price','high_price','low_price','close_price','prev_close_price'])
    print(df)

    for col in data.columns:
        print(col)

    # for ind in data.index:
    #     i = 0
    #     recordString = ""
    #     for item in data:
    #         if i > 0:
    #             recordString = recordString + ","
    #         recordString = recordString + str(data[item][ind])
    #         i = i + 1
    #     print(recordString)
    # print(data)
    # print(data['code'][0])    # 取第一条的股票代码
    # print(data['code'].values.tolist())   # 转为list

    df.plot(x='code', y=['open_price','low_price','high_price','last_price'], kind='bar')
    plt.show()
else:
    print('error:', data)
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽