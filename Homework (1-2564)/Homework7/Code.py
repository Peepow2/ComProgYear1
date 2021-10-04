# HW7: Discord Examiner bot
# พิมพ์ เลขประจำตัว ชื่อ และนามสกุลของนิสิต
# 6431130621 พีรวิชญ์ สดสวย
def get_student_info(uid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    # คืนผลเป็นข้อมูลการสอบของนิสิตที่มี uid ตรงกับ uid ที่ function รับเข้ามา
    if len(exam_info) == 0:
        exam_info += [[uid, sid, [], [], 0]]
    ids = []; idu = [];
    size = len(exam_info)
    for i in range(size):
        idu += [exam_info[0]]
        ids += [exam_info[1]]
        if (uid not in idu) and (ids not in sid):
            exam_info += [[uid, sid, [], [], 0]]
    return exam_info

def get_student_info(uid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    # คืนผลเป็นข้อมูลการสอบของนิสิตที่มี uid ตรงกับ uid ที่ function รับเข้ามา
    if len(exam_info) == 0:
        exam_info += [[uid, sid, [], [], 0]]
    ids = []; idu = [];
    size = len(exam_info)
    for i in range(size):
        idu += [exam_info[0]]
        ids += [exam_info[1]]
        if (uid not in idu) and (ids not in sid):
            exam_info += [[uid, sid, [], [], 0]]
    return exam_info

def get_welcome_and_rules_msg():
    # เขียนโปรแกรมในส่วนนี้
    # คืนผลเป็นข้อความต้อนรับและกฎกติกาในการสอบ โดยให้นิสิตสมมุติว่าถ้าตัวเองเป็นกรรมการคุมสอบ 
    # จะมีการกล่าวต้อนรับอย่างไร และมีกฎกติกาอะไรต้องแจ้งบ้าง ออกทางหน้าจอ

    Rules = str("")
    # print("พ่อมึงตาย ISUS มึงเข้ามาสอบทำไมวะ เขียนชื่อแล้วก็ออกไป คะแนนก็ได้เท่ากับตอนที่มึงสอบจริงนั่นแหละนะ")
    Rules += "สวัสดีครับนักศึกษาทุกคน วันนี้เป็นวันสอบวิชาการเขียนโปรแกรมนะครับ" + "\n"
    Rules += "มีเวลา 180 นาท" + "\n"
    Rules += "ข้อสอบมี 2 ส่วน คือ ปรนัย และเขียนโปรแกรมนะครับโปรดตรวจสอบให้เรียบร้อยก่อนทำ" + "\n"
    Rules += "อนุญาตให้เปิดตำราที่เตรียมไว้ได้ แต่ห้ามหาจากเว็บไซต์" + "\n"
    Rules += "ระหว่างการสอบถ้ามีปัญหาให้ความกรรมการคุมสอบเท่านั้น ห้ามติดต่อกับผู้อืนที่ไม่ได้รับอนุญาต" + "\n"
    Rules += "หากทำผิดกฏการสอบ จะได้รับ F ในวิชานี้และบังคับถอนวิชาที่เหลือทั้งหมด"
    return Rules     

def get_student_info(uid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    # คืนผลเป็นข้อมูลการสอบของนิสิตที่มี uid ตรงกับ uid ที่ function รับเข้ามา
    for temp in exam_info:
      if uid == temp[0]:
        return temp
    return None

def get_question(uid, exam_info, all_questions):
    idx = int(random.random() * len(all_questions))
    temp = get_student_info(uid, exam_info)
    while all_questions[idx] == temp[2]:
        if len(temp[2]) == len(all_questions):
            return "end"
        else:
            idx = int(random.random() * len(all_questions))
        temp[2] += [all_questions[idx]]
        return all_questions[idx]

def submit_answer(uid, answer, exam_info):
    info += get_student_info(uid, exam_info)
    if int(info[4]) == len(info[3]):
        info[3] += [answer]
    info[4] += 1
    
client.run(TOKEN)
