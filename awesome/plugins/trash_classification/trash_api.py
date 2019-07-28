import aiohttp
from jieba import posseg


async def get_the_sort_of_trash(trash: str) -> str:
    sort = None
    count = 1
    all_of_trash = ''
    all_of_trash_list = []
    url = f'https://laji.lr3800.com/api.php?name={trash}'
    async with aiohttp.request('GET', url) as resp:
        response = await resp.json(content_type='text/html')
        if response['code'] == 200:
            if len(response['newslist']) == 1:
                for information in response['newslist']:
                    sort = information['type']

            else:
                for information in response['newslist']:
                    if information['name'] == trash:
                        sort = information['type']
                        break
                    else:
                        all_of_trash_list.append(information['name'])
                        all_of_trash = "\n".join(all_of_trash_list)

    if sort is not None:
        trash_sort = {0: '可回收垃圾', 1: '有害垃圾', 2: '厨余垃圾', 3: '其他垃圾'}
        classification = trash_sort[sort]
        return f'{trash}属于{classification}'
    if all_of_trash_list:
        return f'找到了多种相关垃圾，有:\n{all_of_trash}\n请再次输入，查询您想要的结果'
    return '查询失败，垃圾未找到'


def participle(msg: str) -> str:
    words = posseg.lcut(msg)
    trash = ''
    for word in words:
        if word.flag == 'n' or word.flag == 'nr':
            if not word.word == '垃圾':
                trash += word.word
    return trash