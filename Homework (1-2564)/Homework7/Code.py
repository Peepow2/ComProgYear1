# HW7: Discord Examiner bot
# พิมพ์ เลขประจำตัว ชื่อ และนามสกุลของนิสิต
# 6431130621 พีรวิชญ์ สดสวย
def sign_in(uid, sid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    # ตรวจสอบว่า uid หรือ sid มีอยู่ใน exam_info แล้วหรือไม่ 
    # ถ้ามีอยู่แล้วก็ไม่ต้องทำอะไร แต่ถ้ายังไม่มีก็เพิ่มสมาชิก [uid, sid, [], [], 0] เข้าไปใน exam_info
    for temp in exam_info:
      if uid == temp[0] or sid == temp[1]:
        return
    exam_info += [[uid, sid, [], [], 0]]
    return     

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
    # เขียนโปรแกรมในส่วนนี้
    # จะคืนผลเป็นคำถามจาก questions ที่ถูกชี้ด้วย qidx ถ้า ณ ตำแหน่งนั้นยังไม่มีคำถาม function นี้จะต้องไปสุ่มเลือกคำถาม
    # เลือกมาจาก all_questions ซึ่งจะต้องเป็นคำถามที่นิสิตยังไม่ได้ตอบ
    # นอกจากจะคืนผลแล้ว function นี้จะต้องเพิ่มคำถามที่ได้ ต่อท้าย questions ด้วย
    # แต่หากว่าคำถามหมดแล้วก็จะคืนคำว่า end มาให้โดยไม่เปลี่ยนแปลงใดๆกับ questions
    temp = get_student_info(uid, exam_info)
    idx = 0
    for i in exam_info:
        if temp == i:
            break;
        idx += 1
    if idx >= len(all_questions): idx = -1
    if len(exam_info[idx][2]) == len(all_questions):
        return "end"
    q = int(0); Found_question = False
    while (q == 0 or Found_question):
        q = (random.random() * len(all_questions)) // 1
        Found_question = False
        ques = str("")
        if q < 10:
            ques = str("Q" + "0" + str(int(q)))
        else:
            ques = str("Q" + str(int(q)))
        if ques in exam_info[idx][2]:
            Found_question = True
    return ques   

def submit_answer(uid, answer, exam_info):
    # เขียนโปรแกรมในส่วนนี้












    return     
