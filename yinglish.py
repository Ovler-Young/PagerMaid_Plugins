from asyncio import sleep
from pagermaid import log
from pagermaid.listener import listener
from pagermaid.utils import alias_command
import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)

def chaos (x, y, chaosrate):
    if random.random() > chaosrate:
        return x
    if x in {'[', ']'}:
        return ''
    if x in {'，'}:
        return '…'
    if x in { '!', '！',}:
        return '‼‼‼'
    if x in { '。'}:
        return '❗'
    if len(x) > 1 and random.random() < 0.1:
        return f'{x[0]}…{x}'
    if len(x) > 1 and random.random() < 0.4:
        return f'{x[0]}♥{x}'
    if y == 'n' and random.random() < 0.1:
        x = '⭕' * len(x)
        return f'…{x}'
    if x in { '\……n', '\♥n'}:
        return '\n'
    if x in { '…………'}:
        return '……'
    else:
        if y == 'n' and random.random() < 0.2:
            x = '⭕' * len(x)
        return f'……{x}'

def chs2yin(s, chaosrate =0.8):
    return ''.join(chaos (x, y, chaosrate) for x, y in pseg.cut(s))

@listener(is_plugin=True, outgoing=True, command=alias_command("yinglish"),description="能把中文和英文翻译成淫语的翻译机！",
          parameters="<message>|要转换的内容")
async def yinglish(context):
    if context.text and not context.via_bot and not context.forward and not context.parameter:
        await context.edit(f"你没说话我转换个啥")
    elif context.text and context.parameter and not context.via_bot and not context.forward:
        s=str(context.parameter)
        outputtext=chs2yin(s)
        await context.edit(f"{outputtext}")
        await log(f"转换啦！从{context.parameter}变成了{str(outputtext)}!!!")
    else :
        await context.edit("error")