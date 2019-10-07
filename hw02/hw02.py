import re

from date import area


def jianyan(idcard):
      #按照国标检验身份证号
           
      reg = idcard[:6]  # 地区字段
      brith = idcard[6:14]  # 生日字段
      year = brith[0:4]  # 年
      month = brith[4:6]  # 月
      day = brith[6:8]  # 日
      sex = idcard[16]  # 性别字段


      if(re.match(r"\d{17}",idcard)):
            
            if reg in area.keys():
                  print("出生地区为:" + area[reg]) 
            else :
                  print("身份证号码地区非法!")
            
            if (int(year) % 4 == 0 or (int(year) % 100 == 0 and int(year)%4 == 0 )):
            # 闰年出生日期的合法性正则表达式
                  ereg=re.compile('[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
            else:
            # 平年出生日期的合法性正则表达式
                  ereg=re.compile('[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')      

            if(re.match(ereg,idcard)):
                  print ("出生日期为:" + year + "年" + month + "月" + day + "日")     
            else:
                  print("身份证号码出生日期非法!")

      
            if int(sex) % 2 == 1:
                  print("性别为：男")      
            else:
                  print("性别为：女")

            jiaoyan(idcard)  # 检验身份证最后一位

      else:
            print("身份证含非法字符！")


            
def jiaoyan(idcard):
      
      x = idcard[17]
      
      quan = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
      jys =['1','0','X','9','8','7','6','5','4','3','2']
      sum = 0
      j = 1
      
      for i in range(0,17) :
            if j < 18:
                  sum += int(idcard[i])*quan[i] 
                  j +=1
      y = sum % 11

      if jys[y] == x:
            print("校验码最终检验结果为: True")
      else:
            print("校验码最终检验结果为: False")
            


def idcard():
      
      idcard = input("请输入身份证号(十八位):")
      while len(idcard) != 18:
            idcard = input("请重新输入身份证号(十八位):")

      jianyan(idcard)
      


idcard()











