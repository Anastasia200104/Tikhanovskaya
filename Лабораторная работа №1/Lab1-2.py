# TODO Найдите количество книг, которое можно разместить на дискете

v = 1.44 #Мб
stran = 100
strok = 50
simv = 25
simv_1 = 4 #байт

kniga = stran * strok * simv * simv_1 #в байтах
kniga_new = kniga / (1024 * 1024)


print("Количество книг, помещающихся на дискету:", int(v//kniga_new))