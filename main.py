import random
# k = 0
# while k not in range(100, 250):
#     k = int(input('Ведите количетво конфет от 250 до 100 - '))
# input('нажмите клавишу Enter для жеребьёвки')
# q = random.randint(1, 2)
# if q == 1:
#     print("Вы ходите первым")
# else:
#     print('Вы ходите вторым')
# while k > 0 :
#     if q == 1:
#         p = 0
#         m = 0
#         while p not in range(1, 29):
#             p = int(input('Ведите количетво конфет которое хотите взять, но не больше 28 - '))
#         k = k - p
#         if k <= 0:
#             print('Вы выиграли!!!')
#             break
#         else:
#              print(f'Оталось {k} конфет')
#         if k > 84:
#             m = random.randint(1, 28)
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k in range(57, 85):
#             m = random.randint(1, 17)
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k in range(29,57 ):
#             m = 1
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k <= 28:
#             m = k
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}, компьютер победил!!!')
#     else:
#         if k > 84:
#             m = random.randint(1, 28)
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k in range(57, 85):
#             m = random.randint(1, 17)
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k in range(29, 57):
#             m = 1
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}')
#         elif k <= 28:
#             m = k
#             k = k - m
#             print(f'компьютер взял {m} конфет, оталоь - {k}, компьютер победил!!!')
#             break
#         p = 0
#         m = 0
#         while p not in range(1, 29):
#             p = int(input('Ведите количетво конфет которое хотите взять, но не больше 28 - '))
#         k = k - p
#         if k <= 0:
#             print('Вы выиграли!!!')
#             break
#         else:
#             print(f'Оталось {k} конфет')



#
# input('нажмите клавишу Enter для жеребьёвки')
# qx = random.randint(1, 2)
# di1 = {}
# dl = []
# dr = []
# for i in range(1, 10):
#     di1[i] = i
#     dl.append(f'{di1[i]}')
#     dr.append(int(di1[i]))
#
#
# print(f'  {dl[0]}  {dl[1]}  {dl[2]}')
# print(f'  {dl[3]}  {dl[4]}  {dl[5]}')
# print(f'  {dl[6]}  {dl[7]}  {dl[8]}\n')
# p1 = -4
# p2 = -1
# i_ = 0
# sum = [-90, 0]
# ount = 0
# if qx == 1:
#     print('Вы ходите первым')
#     while p2 not in sum:
#         while i_ not in dr:
#             i_ = int(input('Введите номер клетки - '))
#         dr.remove(i_)
#         ount = ount +1
#
#         di1[i_] = 0
#         dl[i_ - 1] = 'x'
#
#         print(f'  {dl[0]}  {dl[1]}  {dl[2]}')
#         print(f'  {dl[3]}  {dl[4]}  {dl[5]}')
#         print(f'  {dl[6]}  {dl[7]}  {dl[8]}\n')
#         i_ = 0
#         if di1[1] + di1[2] + di1[3] == 0:
#             p2 = 0
#         elif di1[4] + di1[5] + di1[6] == 0:
#             p2 = 0
#         elif di1[7] + di1[8] + di1[9] == 0:
#             p2 = 0
#         elif di1[1] + di1[4] + di1[7] == 0:
#             p2 = 0
#         elif di1[2] + di1[5] + di1[8] == 0:
#             p2 = 0
#         elif di1[3] + di1[6] + di1[9] == 0:
#             p2 = 0
#         elif di1[1] + di1[5] + di1[9] == 0:
#             p2 = 0
#         elif di1[3] + di1[5] + di1[7] == 0:
#             p2 = 0
#
#         i_2 = random.choice(dr)
#
#         dr.remove(i_2)
#         di1[i_2] = -30
#         dl[i_2 - 1] = '0'
#         ount = ount + 1
#
#         i_2 = 0
#         print(f'  {dl[0]}  {dl[1]}  {dl[2]}')
#         print(f'  {dl[3]}  {dl[4]}  {dl[5]}')
#         print(f'  {dl[6]}  {dl[7]}  {dl[8]}\n')
#         if di1[1] + di1[2] + di1[3] == -90:
#             p2 = -90
#         elif di1[4] + di1[5] + di1[6] == -90:
#             p2 = -90
#         elif di1[7] + di1[8] + di1[9] == -90:
#             p2 = -90
#         elif di1[1] + di1[4] + di1[7] == -90:
#             p2 = -90
#         elif di1[2] + di1[5] + di1[8] == -90:
#             p2 = -90
#         elif di1[3] + di1[6] + di1[9] == -90:
#             p2 = -90
#         elif di1[1] + di1[5] + di1[9] == -90:
#             p2 = -90
#         elif di1[3] + di1[5] + di1[7] == -90:
#             p2 = -90
#         if p2 == -90:
#             print('Вы проиграли')
#         elif p2 == 0:
#             print('Вы выиграли')
#         if ount == 9:
#             print('ничья')
#             break
# else:
#     print('Вы ходите вторым')
#     while p2 not in sum:
#         i_2 = random.choice(dr)
#         ount = ount + 1
#
#         dr.remove(i_2)
#         di1[i_2] = -30
#         dl[i_2 - 1] = '0'
#
#         i_2 = 0
#         print(f'  {dl[0]}  {dl[1]}  {dl[2]}')
#         print(f'  {dl[3]}  {dl[4]}  {dl[5]}')
#         print(f'  {dl[6]}  {dl[7]}  {dl[8]}\n')
#         if di1[1] + di1[2] + di1[3] == -90:
#             p2 = -90
#         elif di1[4] + di1[5] + di1[6] == -90:
#             p2 = -90
#         elif di1[7] + di1[8] + di1[9] == -90:
#             p2 = -90
#         elif di1[1] + di1[4] + di1[7] == -90:
#             p2 = -90
#         elif di1[2] + di1[5] + di1[8] == -90:
#             p2 = -90
#         elif di1[3] + di1[6] + di1[9] == -90:
#             p2 = -90
#         elif di1[1] + di1[5] + di1[9] == -90:
#             p2 = -90
#         elif di1[3] + di1[5] + di1[7] == -90:
#             p2 = -90
#         while i_ not in dr:
#             i_ = int(input('Введите номер клетки - '))
#         dr.remove(i_)
#
#         di1[i_] = 0
#         dl[i_ - 1] = 'x'
#         ount = ount + 1
#
#         print(f'  {dl[0]}  {dl[1]}  {dl[2]}')
#         print(f'  {dl[3]}  {dl[4]}  {dl[5]}')
#         print(f'  {dl[6]}  {dl[7]}  {dl[8]}\n')
#         if di1[1] + di1[2] + di1[3] == 0:
#             p2 = 0
#         elif di1[4] + di1[5] + di1[6] == 0:
#             p2 = 0
#         elif di1[7] + di1[8] + di1[9] == 0:
#             p2 = 0
#         elif di1[1] + di1[4] + di1[7] == 0:
#             p2 = 0
#         elif di1[2] + di1[5] + di1[8] == 0:
#             p2 = 0
#         elif di1[3] + di1[6] + di1[9] == 0:
#             p2 = 0
#         elif di1[1] + di1[5] + di1[9] == 0:
#             p2 = 0
#         elif di1[3] + di1[5] + di1[7] == 0:
#             p2 = 0
#
#         if p2 == -30:
#             print('Вы проиграли')
#         elif p2 == 0:
#             print('Вы выиграли')
#         if ount == 9:
#             print('ничья')
#             break


f = open('file1.txt','w')
f.write('11e7t2q\n')
f.write('aaarbbbbbll')
f.close()

f = open('file1.txt','r')
si = int(0)
sub2 = ''
si2 = 1
si4 = ''
f2 = open('file2.txt','w')
for l in f:
    lnew = ''
    print(l)
    j = 0
    n = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    if l[0] in n:
        sub = ''
        for i in l:
            if i in n:
                sub = sub + i
                si = int(sub)
            else:
                sub = ''
                # print(si)
                for iz in range(si):
                    lnew = lnew + i
        print(lnew)
        f2.write(f'{lnew}')
    else:
        for i in range(len(l)):
            if i == len(l)-1:
                if si2 != 1:
                    si4 = str(si2)
                    sub2 = sub2 + si4 + l[i - 1]
                elif si2 == 1:
                    si4 = str(si2)
                    sub2 = sub2 + l[i]
                break
            if l[i] == l[i+1]:
                si2 = si2 + 1
            elif l[i] != l[i+1] :
                if si2 != 1:
                    si4 = str(si2)
                    sub2 = sub2 + si4 + l[i - 1]
                    si2 = 1
                elif si2 == 1:
                    si4 = str(si2)
                    sub2 = sub2 + l[i]
                    si2 = 1
    print(sub2)
f.close()
f2.write(f'{sub2}')
f2.close()







