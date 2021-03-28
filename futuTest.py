from futu import *
from futu.common.constant import ProtoFMT
from futu.common.sys_config import SysConfig
from futu.quote.open_quote_context import OpenQuoteContext

SysConfig.set_proto_fmt(ProtoFMT.Protobuf)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()