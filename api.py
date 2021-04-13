import requests
import json

proxies = {"http": "127.0.0.1:8080"}


def login(url: str, user: str, password: str) -> str:
    """登录"""

    data = '{"username":"%s","password":"%s"}' % (user, password)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json; charset=UTF-8"}
    response = requests.post("http://%s/api/user/login" % url, data=data, headers=headers)
    if response.status_code != 200:
        print("登录失败，请检查网络是否错误")
        exit(0)

    data = response.json()
    return data['data']['token']


def del_host(task, url, headers):
    """删除 task_id 对应的主机"""
    headers['Content-Type'] = 'application/json; charset=UTF-8'
    # 先对任务进行停止
    post_data = '{"task_id":%s}' % str(task).replace("'", '"')
    stop_url = 'http://' + url + '/api/task/batch_stop/'
    response = requests.post(stop_url, headers=headers, data=post_data)
    print(response.json())
    # 再进行删除操作
    post_data = '{"task_id":%s,"del_task_data":true}' % str(task).replace("'", '"')
    # print(post_data)
    final_url = 'http://' + url + '/api/task/delete/'
    response = requests.post(url=final_url, headers=headers, data=post_data)

    print(response.content)

    pass

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.114 Safari/537.36",
    'Content-Type': 'application/json; charset=UTF-8'}


def del_title_host(title: str, url, user, password):
    """删除指定标题的 任务数据"""
    url = url
    token = login(url, user, password)
    headers['token'] = token
    result = []
    page_num = 1
    while True:
        title_url = 'http://' + url + '/api/site/?page=%d&size=1000&tabIndex=0&ts=1618224528539&title=' % page_num + title
        response = requests.get(title_url, headers=headers)
        title_data = response.json()
        items = title_data['items']

        if items == []:
            break
        for i in items:
            task_id = i['task_id']
            if task_id not in result:
                result.append(task_id)

        page_num += 1

        # print(result)
        # print(response.json())
    del_host(result, url, headers)





def del_same_task(url, user, password):
    """删除相同 url 的任务"""
    url = url
    token = login(url, user, password)
    headers['token'] = token

    result = []
    page = 1
    while True:
        find_task_url = 'http://' + url + '/api/task/?page=%d&size=1000' % page
        response = requests.get(url=find_task_url, headers=headers)
        data = response.json()
        if data['items'] == []:
            break
        page += 1
        result += data['items']

    data_id = []
    data_target = []
    del_task_id = []
    for i in result:
        data_id.append(i['_id'])
        data_target.append(i['target'])

    i = 0
    while True:
        # print(len(data_target))

        if len(del_task_id) == 10:
            del_host(del_task_id, url, headers)
            del_task_id = []
        if i == len(data_target) - 1:
            break
        if data_target.count(data_target[i]) != 1:
            # print(1)
            scend_target_index = data_target.index(data_target[i], 1)

            if int(data_id[scend_target_index], 16) > int(data_id[i], 16):
                del_task_id.append(data_id[scend_target_index])
                data_id.pop(scend_target_index)
                data_target.pop(scend_target_index)
            else:
                del_task_id.append(data_id.pop(i))
                data_target.pop(i)
        i += 1

    # print(del_task_id)
    del_host(del_task_id, url, headers)


def domain_exp():
    """导出子域名"""
    pass


if __name__ == '__main__':
    del_same_task()
