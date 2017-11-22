import requests, json
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/api/v4/members/evanyou/answers'

header = {
    "Cookie": 'aliyungf_tc=AQAAAC9ztFcacwYAzSX7OmZHPYWeTGTa; q_c1=b21c475342674ef89190e84ffc6df191|1511234177000|1511234177000; _zap=9cfee274-7e92-47ad-8563-958afb1b872b; d_c0="ACACjkw5twyPTuc-7mWXR_ZkM4cA_J5N-9Q=|1511234372"; r_cap_id="YTAyZGE5YTk3MTAwNDIyNWE5ZDVlY2IwYTMxZTA1YjQ=|1511244944|4f4fb2a79df95e9dbb5ed1240358abe8ea9281c7"; cap_id="MGZlNzA0MGNmN2U2NDc2YzgzODg2YjM3ZjU3MTg3ODE=|1511244944|f5a9726f6d4229277d326984c685616136136706"; capsion_ticket="2|1:0|10:1511245235|14:capsion_ticket|44:MGQ5NWEwZTBlY2U5NGM5MWE1ZDA0YWE3YzI4ZTE3MTg=|bc9d658dd2c7ff8e055e7f89de8bec3feb26799a4845b16a6004e323dd1964bb"; z_c0="2|1:0|10:1511245240|4:z_c0|92:Mi4xU3BrTkFBQUFBQUFBSUFLT1REbTNEQ1lBQUFCZ0FsVk50eE1CV3dDdExCdUs3YlF5TXk4ZmJyVzM3Y2FxeUkzbWxB|aa703eb0d687c0fe5830e1c14d4ae8678c5659d714515649b3ba7e90bfc03a9c"; __utma=51854390.1325370535.1511244945.1511244945.1511244945.1; __utmc=51854390; __utmz=51854390.1511244945.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20130530=1^3=entry_date=20130530=1; _xsrf=4fe7f8f3-f32e-4a95-bae5-bf7774325d1c',
    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
}

offsetNum = 0

limitNum = 20

dataList = []

def getAnswers():
    print(offsetNum)
    param = {
        "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,collapsed_by,suggest_edit,comment_count,can_comment,content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp,upvoted_followees;data[*].author.badge[?(type=best_answerer)].topics",
        "offset": offsetNum,
        "limit": limitNum,
        "sort_by": "created"
    }
    r = requests.get(url, headers = header, params=param)
    data = json.loads(r.text)
    global dataList
    dataList = data['data']
    if (len(dataList) == 20):
        nextPage()

def nextPage():
    if (len(dataList) == 20):
        f = open("answers.txt", "a", encoding='utf-8')  
        for i in dataList:
            print(i['question']['title'])
            f.write(i['question']['title'])
        f.close()
        global offsetNum
        offsetNum += 20
        getAnswers()

if __name__ == '__main__':
    getAnswers()
