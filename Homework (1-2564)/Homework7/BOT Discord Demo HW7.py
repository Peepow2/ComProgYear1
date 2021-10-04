import discord
import math
import random
import json

with open('config.json') as json_file:
    TOKEN = json.load(json_file)['DISCORD_TOKEN']
client = discord.Client()

random.seed(1111)
exam_info = []
all_questions = ['HW1 ถึง HW7 อันไหนยากสุด', 'คิดว่าจะได้เกรดอะไร', 'TA/อาจารย์ คนไหนอธิบายได้เข้าใจง่ายที่สุด', 'การบ้านไหนที่ชอบที่สุด', 'TA คนไหนตอบคุณเยอะสุด']
all_questions.sort()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    msg = message.content
    uid = message.author.id
    if msg.startswith('.sign_in'):
        sign_in(uid, msg.split()[1], exam_info)
        await message.author.send(get_welcome_and_rules_msg())
        await message.author.send(get_question(uid, exam_info, all_questions) + " --> ")
    elif msg.startswith('.answer'):
        submit_answer(uid, " ".join(msg.split()[1:]), exam_info)
        info = get_student_info(uid, exam_info)
        for i in range(len(info[3])):
            await message.author.send(info[2][i] + " --> " + info[3][i])
        question = get_question(uid, exam_info, all_questions)
        if question != "end":
            question += " -->"
        await message.author.send(question)

def sign_in(uid, sid, exam_info):
    if len(exam_info) == 0:
        exam_info += [[uid, sid, [], [], 0]]
    ids = []; idu = [];
    size = len(exam_info)
    for i in range(size):
        idu += [exam_info[i][0]]
        ids += [exam_info[i][1]]
        if (uid not in idu) and (ids not in sid):
            exam_info += [[uid, sid, [], [], 0]]
    return exam_info

def get_welcome_and_rules_msg():
    Rules = str("")
    # Rules += "พ่อมึงตาย ISUS มึงเข้ามาสอบทำไมวะ เขียนชื่อแล้วก็ออกไป คะแนนก็ได้เท่ากับตอนที่มึงสอบจริงนั่นแหละนะ"
    Rules += "สวัสดีครับนักศึกษาทุกคน วันนี้เป็นวันสอบวิชาการเขียนโปรแกรมนะครับ" + "\n"
    Rules += "มีเวลา 180 นาท" + "\n"
    Rules += "ข้อสอบมี 2 ส่วน คือ ปรนัย และเขียนโปรแกรมนะครับโปรดตรวจสอบให้เรียบร้อยก่อนทำ" + "\n"
    Rules += "อนุญาตให้เปิดตำราที่เตรียมไว้ได้ แต่ห้ามหาจากเว็บไซต์" + "\n"
    Rules += "ระหว่างการสอบถ้ามีปัญหาให้ความกรรมการคุมสอบเท่านั้น ห้ามติดต่อกับผู้อืนที่ไม่ได้รับอนุญาต" + "\n"
    Rules += "หากทำผิดกฏการสอบ จะได้รับ F ในวิชานี้และบังคับถอนวิชาที่เหลือทั้งหมด"
    return Rules     

def get_student_info(uid, exam_info):
    for temp in exam_info:
      if uid == temp[0]:
        return temp
    return None

def get_question(uid, exam_info, all_questions):
    idx = int(random.random() * len(all_questions) // 1)
    temp = get_student_info(uid, exam_info)
    while all_questions[idx] in temp[2]:
        if len(temp[2]) == len(all_questions):
            return "end"
        else:
            idx = int(random.random() * len(all_questions) // 1)
    temp[2] += [all_questions[idx]]
    return all_questions[idx]

def submit_answer(uid, answer, exam_info):
    info = get_student_info(uid, exam_info)
    if int(info[4]) == len(info[3]):
        info[3] += [answer]
    info[4] += 1
    return 

# --------------------------- Driver Code ---------------------------
client.run(TOKEN)
