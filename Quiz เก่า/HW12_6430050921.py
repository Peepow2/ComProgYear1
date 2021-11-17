import numpy as np

def find_max_min_on_date(provinces,dates,data,date):
  
    ans = {}  ;  check_column = (dates == date)
    all_row_date_column = np.copy(data[:, check_column]) #ตรงนี้้มีเพื่อนแนะนำให้ก๊อปปี้ เพื่อป้องกันการเปลี่ยนข้อมูลครับ

    maxx = np.max(all_row_date_column, axis = 0)              ;   minn = np.min(all_row_date_column, axis = 0)  #เอาค่า maxx , minn ที่ได้ไปหา index แกน y ใน all_row_date_column จัดเก็บทั้งคู่เป็น check_row_max , check_row_min แล้วเทียบ check กับ provinces
    check_row_max = (all_row_date_column == maxx).flatten()   ;   check_row_min = (all_row_date_column == minn).flatten()
    list_of_max = (provinces[check_row_max]).tolist()         ;   list_of_min = (provinces[check_row_min]).tolist()
    ans['max'] = list_of_max                                  ;   ans['min'] = list_of_min
    
    return ans

def find_max_min_in_province(provinces,dates,data,province):
  
    ans = {}  ;  check_column = (provinces == province)
    province_row_all_column = np.copy(data[check_column, :]) #ตรงนี้้มีเพื่อนแนะนำให้ก๊อปปี้ เพื่อป้องกันการเปลี่ยนข้อมูลครับ

    maxx = np.max(province_row_all_column, axis = 1)              ;   minn = np.min(province_row_all_column, axis = 1)
    check_row_max = (province_row_all_column == maxx).flatten()   ;   check_row_min = (province_row_all_column == minn).flatten()
    list_of_max = (dates[check_row_max]).tolist()                 ;   list_of_min = (dates[check_row_min]).tolist()
    ans['max'] = list_of_max                                      ;   ans['min'] = list_of_min
    
    return ans

def find_average_growth(provinces,data,n):
    
    #เลือกหยิบ data มา (ทุกแถว , n column ท้าย) ใส่ลงใน data_n
    data_n = data[ : , - n :: ]
    #shift data ด้วยการ slice เก็บลงใน shifted
    shifted = data[ :  , (-n-1) : -1 : ]
    ans = (data_n - shifted)/shifted
    #หา mean แกน x เก็บเป็น array_mean , หา index array_mean เพื่อนำไปชี้ provinces , sort array_mean ก่อนจะนำเก็บใน answer
    array_mean = np.mean(ans , axis = 1)
    array_mean_index = np.array(np.argsort(array_mean), float)
    array_mean_sorted = np.sort(array_mean)
    #เอาข้อมูลมาเก็บด้วยกันด้วยเป็น (array 2 แถว n คอลลัมน์) , Transpose ให้มันอยู่ข้างกัน
    answer = np.array((array_mean_sorted,array_mean_index))
    answer = answer.T
    
    return [(float(x),provinces[int(y)]) for x,y in answer]

def normalize(data):

    maxx = (np.max(data , axis = 1)).reshape(data.shape[0],1) #ทรานส์โพส 1 มิติโดยใช้ .shape เพราะถ้า .T จะ Error
    ans = data/maxx
    
    return ans