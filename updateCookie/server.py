import ctypes
import json
import os
import pprint
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from updateCookie_Util import *

app = FastAPI()
目前电话 = ''


def get_list_item_by_index(data_list):
    """根据索引获取列表项"""
    cnt = 0
    for x in data_list:
        print(f'{cnt} -- {x}')
        cnt += 1
    index = int(input("请输入要获取的列表项索引:"))
    if index < 0 or index >= len(data_list):
        raise Exception("索引超出范围")

    return (data_list[index])


def addEnv(file_path, name, value, run=False, taskName=''):
    global 目前电话
    文件路径 = os.path.dirname(os.path.abspath(__file__)) + "\\" + 目前电话 + '-' + file_path
    if not os.path.exists(文件路径):
        # 文件不存在,创建文件并写入内容
        with open(文件路径, 'w') as f:
            content = {'name': name, 'value': value, 'remark': 目前电话, 'run': run, 'taskName': taskName}
            json.dump(content, f)

    else:
        # 文件已存在,判断内容是否相同
        with open(文件路径, 'r') as f:
            content = json.load(f)

        if content['value'] != value:
            content['value'] = value
            content['remark'] = 目前电话
            content['run'] = run
            content['taskName'] = taskName
            # 内容不同,修改内容
            with open(文件路径, 'w') as f:
                f.write(json.dumps(content, ensure_ascii=False))


class Buffer(BaseModel):
    url: str
    method: str
    host: str
    path: str
    body: str
    headers: dict
    queries: dict
    context: dict


@app.post("/xapi.weimob.com")
def 统一快乐星球(data: Buffer):
    name = 'X-WX-Token'
    addEnv(f"{data.headers['Host']}.txt", 'tyklxq_cookies', data.headers[name], True, '微信小程序-统一快乐星球')
    return data.headers[name]


@app.post("/ucode-openapi.aax6.cn")
def 甄爱粉俱乐部(data: Buffer):
    name = 'Authorization'
    addEnv(f"{data.headers['Host']}.txt", 'zaf_auth', data.headers[name], True, '微信小程序-甄爱粉俱乐部')
    return data.headers[name]


@app.post("/m.jissbon.com")
def 杰士邦安心福利社(data: Buffer):
    name = 'Access-Token'
    addEnv(f"{data.headers['Host']}.txt", 'jsbaxfls', data.headers[name], True, '杰士邦安心福利社')
    return data.headers[name]


@app.post("/www.kozbs.com")
def 植白说(data: Buffer):
    name = 'X-Dts-Token'
    addEnv(f"{data.headers['Host']}.txt", 'zbsxcx', data.headers[name], True, '植白说')
    return data.headers[name]


@app.post("/kraftheinzcrm.kraftheinz.net.cn")
def 卡夫味(data: Buffer):
    name = 'token'
    addEnv(f"{data.headers['Host']}.txt", 'kfw_data', data.headers[name], True, '卡夫味')
    return data.headers[name]


@app.post("/api.wincheers.net")
def 罗技粉丝俱乐部(data: Buffer):
    name = 'Authorization'
    addEnv(f"{data.headers['Host']}.txt", 'ljfsjlbCookie', data.headers[name], True, '罗技粉丝俱乐部')
    return data.headers[name]


@app.post("/web.meituan.com")
def 美团(data: Buffer):
    name = 'token'
    addEnv(f"{data.headers['Host']}.txt", 'bd_mttoken', data.headers[name])
    return data.headers[name]


@app.post("/api.yqslmall.com")
def 元气森林(data: Buffer):
    name = 'Authorization'
    addEnv(f"{data.headers['Host']}.txt", 'yqsl', data.headers[name].replace('Bearer ', ''), True, '元气森林')
    return data.headers[name]


@app.post("/apichuanti.scleader.cn")
def 引体向上(data: Buffer):
    name = 'Authorization'
    addEnv(f"{data.headers['Host']}.txt", 'ytxs', data.headers[name].replace('Bearer ', ''), True, '引体向上')
    return data.headers[name]


@app.post("/consumer-api.quncrm.com")
def 雀巢专业餐饮大厨精英荟(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'qczy_token',
           f"{data.headers['X-Access-Token']}#{data.headers['X-Account-Id']}", True, '微信小程序-雀巢专业餐饮大厨精英荟')
    return ""


@app.post("/smp-api.iyouke.com")
def meiyang会员积分(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'my_auth',
           data.headers['Authorization'], True, '微信小程序-meiyang会员积分')
    return ""


@app.post('/app.fjxzj.com')
def 康佰家(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'kbj_token',
           data.headers['token'], True, '微信小程序-康佰家')
    return ""


@app.post("/uic.youzan.com")
def 朵茜情调生活馆(data: Buffer):
    if 'Extra-Data' in data.headers:
        extra = json.loads(data.headers['Extra-Data'])
        addEnv(f"{data.headers['Host']}.txt", 'dqqdshgck',
               f"{data.queries['access_token']}#{extra['sid']}#{extra['sid']}", True, '微信小程序-朵茜情调生活馆')
    return ""

@app.post("/h5.youzan.com")
def xbox聚乐部(data: Buffer):
    if 'Extra-Data' in data.headers:
        extra = json.loads(data.headers['Extra-Data'])
        addEnv(f"{data.headers['Host']}.txt", 'xbox_data',
               extra['sid'], True, 'xbox俱乐部V2')
    return ""

@app.post('/api.gaojihealth.cn')
def 高济健康(data: Buffer):
    if 'userId' in data.queries:
        addEnv(f"{data.headers['Host']}.txt", 'wx_gjjkpro_data',
               f"{data.queries['userId']}&{data.headers['Authorization']}", True, '高济健康pro小程序签到')
    return ""


@app.post('/channel.cheryfs.cn')
def 好奇车生活(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'hqcshck', data.headers['accountId'], True, '好奇车生活签到')
    return data


@app.post('/yx.jsh.com')
def 卡萨帝(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'ksdck', data.headers['Authorization'], True, '卡萨帝')
    return ""


@app.post('/fscrm.kraftheinz.net.cn')
def 卡夫亨(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'kfh_data', data.headers['token'], True, '卡夫亨')
    return ""


@app.post('/clubwx.hm.liby.com.cn')
def 立白小白白会员(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'lbvip',
           f"{data.headers['unionId']}#{data.headers['X-wxde54fd27cb59db51-Token']}", True, '立白小白白会员俱乐部')
    return ""


@app.post('/mmembership.lenovo.com.cn')
def 联想(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'lx_data',
           f"{data.headers['accessToken']}#{data.headers['serviceToken']}#{data.headers['SERVICE-AUTHENTICATION']}#{data.headers['lenovoId']}")
    return ""


@app.post('/www.milkcard.mall.ryytngroup.com')
def 认养一头牛(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'ryytn_data', data.headers['X-Auth-Token'], True, '微信小程序-认养一头牛商城')
    return ""


@app.post('/apis.folidaymall.com')
def 托迈酷客(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'tmkk', data.headers['Authorization'].replace('Bearer ', ''), True, '托迈酷客')
    return ""


@app.post('/fwdt.shengongshe.org')
def 申工社(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'sgs', data.headers['Token'], True, '申工社')
    return ""


@app.post('/qualcomm.growthideadata.com')
def 骁龙骁友会(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'wx_xlxyh_data',
           f"{data.headers['sessionKey']}&{data.headers['userId']}", True, '微信小程序_骁龙骁友会')
    return ""


@app.post('/customer.yueyequan.cn')
def 悦野圈(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'yyq_data',
           f"{data.headers['cookie']}&{data.headers['cookie'].split('userid=')[1].split(';')[0]}", True, '悦野圈')
    return ""


@app.post('/mystore-01api.watsonsvip.com.cn')
def 屈臣氏(data: Buffer):
    addEnv(f"{data.headers['Host']}1.txt", 'qcsAuthorization', data.headers['Authorization'])
    addEnv(f"{data.headers['Host']}2.txt", 'qcsunionId', data.headers['unionId'], True, '屈臣氏')
    return ""


@app.post('/wx-fulishe.msx.digitalyili.com')
def 伊利会员福利社(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'ylhyencryptsessionid', data.queries['encryptsessionid'], True, '伊利会员福利社')
    return ""

@app.post('/midend.icar-ecology.com')
def 奇瑞EV(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", 'cheryev', data.headers['Authorization'].replace('Bearer ', ''), True, 'V3')
    return ""

@app.post('/hweb-mbf.huazhu.com')
def 华住(data: Buffer):
    # pprint.pprint(data.headers)
    addEnv(f"{data.headers['Host']}.txt", 'huazhu_cookies', data.headers['Cookie'], True, '微信小程序-华住签到')
    return ""

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)
    目前电话 = get_list_item_by_index(config['phoneList'])
    隐藏cmd对话框()
    uvicorn.run(app, host="0.0.0.0", port=8989)
