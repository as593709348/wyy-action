导入请求，base64，json，hashlib
从Crypto.Cipher导入AES
def加密（密钥，文本）：
    cryptor = AES.new（key.encode（'utf8'），AES.MODE_CBC，b'0102030405060708'）
    长度= 16                    
    count = len（text.encode（'utf-8'））     
    如果（count％length！= 0）：
        加=长度-（计数％长度）
    其他：
        加= 16             
    垫= hr（添加）
    文本1 =文本+（填充*添加）    
    密文= cryptor.encrypt（text1.encode（'utf8'））          
    cryptedStr = str（base64.b64encode（密文），encoding ='utf-8'）
    返回cryptedStr
def md5（str）：
    hl = hashlib.md5（）
    hl.update（str.encode（encoding ='utf-8'））
    返回hl.hexdigest（）
def保护（文本）：
    返回{ “PARAMS”：加密（ 'TA3YiYCfY2dDJQgg'，加密（ '0CoJUm6Qyw8W8jud'，文本））， “encSecKey”： “84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210”}


s = requests.Session（）
标头= {}
url =“ https://music.163.com/weapi/login/cellphone”
url2 =“ https://music.163.com/weapi/point/dailyTask”
url3 =“ https://music.163.com/weapi/v1/discovery/recommend/resource”
logindata = {
    “ phone”：input（），
    “国家代码”：“ 86”，
    “密码”：md5（input（）），
    “ rememberLogin”：“ true”，
}
标头= {
        'User-Agent'：'Mozilla / 5.0（Windows NT 10.0; Win64; x64）AppleWebKit / 537.36（KHTML，like Gecko）Chrome / 84.0.4147.89 Safari / 537.36'，
        “ Referer”：“ http://music.163.com/”，
        “ Accept-Encoding”：“ gzip，deflate”，
        }
标头2 = {
        'User-Agent'：'Mozilla / 5.0（Windows NT 10.0; Win64; x64）AppleWebKit / 537.36（KHTML，like Gecko）Chrome / 84.0.4147.89 Safari / 537.36'，
        “ Referer”：“ http://music.163.com/”，
        “ Accept-Encoding”：“ gzip，deflate”，
        “ Cookie”：“ os = pc; osver = Microsoft-Windows-10-Professional-build-10586-64bit; appver = 2.0.3.131777; channel = netease; __remember_me = true;”
        }

res = s.post（url = url，data = protect（json.dumps（logindata）），headers = headers2）
tempcookie = res.cookies
object = json.loads（res.text）
如果object ['code'] == 200：
    print（“登录成功！”）
其他：
    print（“登录失败！请检查密码是否正确！” + str（object ['code']））
    退出（对象['代码']）

res = s.post（url = url2，data = protect（'{“ type”：0}'），headers = headers）
object = json.loads（res.text）
如果object ['code']！= 200和object ['code']！=-2：
    print（“签到时发生错误：” + object ['msg']）
其他：
    如果object ['code'] == 200：
        print（“签到成功，经验+” + str（object ['point']））
    其他：
        print（“重复签到”）


res = s.post（url = url3，data = protect（'{“ csrf_token”：“'+ requests.utils.dict_from_cookiejar（tempcookie）['__ csrf'] +'”}'），headers = headers）
object = json.loads（res.text，strict = False）
对于x in object ['recommend']：
    url ='https：//music.163.com/weapi/v3/playlist/detail？csrf_token ='+ requests.utils.dict_from_cookiejar（tempcookie）['__csrf']
    数据= {
        'id'：x ['id']，
        'n'：1000，
        'csrf_token'：requests.utils.dict_from_cookiejar（tempcookie）['__ csrf']，
    }
    res = s.post（URL，protect（json.dumps（data）），headers = headers）
    object = json.loads（res.text，strict = False）
    缓冲区= []
    计数= 0
    对于object ['playlist'] ['trackIds']中的j：
        data2 = {}
        data2 [“ action”] =“播放”
        data2 [“ json”] = {}
        data2 [“ json”] [“下载”] = 0
        data2 [“ json”] [“ end”] =“ playend”
        data2 [“ json”] [“ id”] = j [“ id”]
        data2 [“ json”] [“ sourceId”] =“”
        data2 [“ json”] [“ time”] =“ 240”
        data2 [“ json”] [“ type”] =“歌曲”
        data2 [“ json”] [“ wifi”] = 0
        buffer.append（data2）
        计数+ = 1
        如果count> = 310：
            打破
    如果count> = 310：
        打破
url =“ http://music.163.com/weapi/feedback/weblog”
postdata = {
    “日志”：json.dumps（缓冲区）
}
res = s.post（URL，protect（json.dumps（postdata）））
object = json.loads（res.text，strict = False）
如果object ['code'] == 200：
    打印（“刷单成功！共” + str（count）+“首”）
    出口（）
其他：
    print（“发生错误：” + str（object ['code']）+ object ['message']）
    退出（对象['代码']）
