# КЕВ
# 



import random
import timeit
import matplotlib.pyplot as plt  #графики

import numpy as np

#from Global_vars    import *
#from ALL_print_func import *
#from ALL_study_func import *




# Можно писать так время в разные перем => делать сразу несколько замеров
def My_timer( command , Time_beg = 0.0 , msg="def_msg: " ):
  if command == "Start": return timeit.default_timer()
  
  if command == "Stop" : 
    Time = timeit.default_timer()- Time_beg
    
    #print(Time)
    
    min  = 0
    sec  = 0
    msec = 0
    
    if Time >= 60:
        min = int(Time)%60
        Time = Time - min*60
        
    if Time >= 1:
        sec = int(Time)-1
        Time = Time - sec
        
    msec = int(Time*1000)  # 0.3875471909996122 *1000 = 387.5471909996122  и обрезаем
    
    
    
    if min >= 1:
      print (msg+ str(min) +"м "+str(sec)+"с "+str(msec)+"мс")
      return Time
    
    if sec >= 1:
      print (msg+str(sec)+"с "+str(msec)+"мс")
      return Time
      
    if msec >= 1:
      print (msg+str(msec)+"мс")
      return Time
      
    print (msg+"Меньше мс")
    return Time
    
  # Впихнуть сюда форматирование вывода через printf %
  # Уже не надо
  

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################



###################################

# Сколько сэлем выводить в 1 строке
print_row_len = 3

 
# Порог функции активации
bias = 7 #7  # для 1=7

# Итерации
iter_count = 5000  # 50 мало, 100 более-менее


DECREASE_COUNT = 1
INCREASE_COUNT = 1

###################################

# Самый главный двумерн массив весов
ALL_weights_old = []

buf_array_weights = []


##################################################################
##################################################################
##################################################################

############
# Подбираем числа для Дельты чтоб выдавал результат как МНК(мнк дает правильный)
# itera  , speed = Сходства K , C
# 300000  0,0001 = 51 53 54 54 58 61 64 71 81, всегда 99-100%
# 30000   0,0001 = лажа
# 300000  0,001 =  25 51 36 71 , 98-100
# 300000  0,000001 = лажа
# 300000  0,0005 = -101 4 71 82 660 , 99
# 300000  0,00025
# 100000  0,00025   По числам вроде норм(оч близко)

########### 
# НОВЫЙ обсчет % сходства по N число после запятой
# itera  , speed = Сходства K , C
# 300000 0.00025  = 87 87 93 93 98 100 100 100 101 106 , 99-100     по 2 числу
#
# 100000 0.0025 лажа = 55 79 , 98
# 100000 0.00025  = 93 93 96 100 103 109 111 114 114 , 100




# 180000 0.00025  = 88 92 94 94 94 95 96 96 98 , 99-100 

iter_count_delta = 180000  # 30000

# Скорость обучения
training_speed = 0.00025  # при 0.01 точно вычисляет 'C' (+- 1-3%) , зато с K лажа

# До какого числа после ',' жолжны совпадать числа чтоб считатся равными
# !!!! Числа 0.001 и 9.001 будут признаны РАВНЫМИ (надо доделать проверку)
num_after_comma = 2 # дефолт=2  ,  1 можно, но не точно  , 3 не найдет


# Для коэфф
line_koeff_mnk_k = []
line_koeff_mnk_c = []

line_koeff_delta_k = []
line_koeff_delta_c = []

############









###################################
 
# Цифры (Обучающая выборка)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
 
# Список всех вышеуказанных цифр
ARRAY_ALL_010101 = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
 

# Виды цифры 2 (Тестовая выборка)
#num21 = list('111001010100111') # 2 1 заменены на 0
#num21 = list('101001010100101') # 4 единицы заменены на 0
#num22 = list('101001100000111') # 4 единицы заменены на 0
#num23 = list('101001010100011') # 4 единицы заменены на 0

#num52 = list('111100010001111')
#num53 = list('111100011001111')
#num54 = list('110100111001111') # Это образцы для ПЯТЕРКИ
#num55 = list('110100111001011')
#num56 = list('111100101001111')











####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################




# m = [ [0 , 1 , 2 , 3 , 4 , 5 ] , ["00" , "01" , "02" , "10" , "11" , "12"  ] ]
# Позволяет выводить любые N-мерные массивы(list) с ЛЮБЫМИ типами данных     ЦВЕТНЫЕ
def UNIV_PRINT_ANY_ARRAY( arr , length_row, msg="def_msg" , recurs_level = 0 , arr_num = 0):

	print( "" )
	#print( "\n" + "#"*25 + " - Start print" )
	print( msg , end="" )
	
	data_type = str( type(arr[0]) )


	if recurs_level != 0: 
		print("Это все элементы mass["+str(arr_num)+"] , тип элементов([0])=" + data_type )
	#else:
	#	print("Тип определен как: ", data_type , end = "" )
	# Не убирать




	
	# Вывод ВСЕГО массива
	if data_type == "<class 'list'>": 
		arr_num = 0
		
		for mas in arr:
			# Рекурсия
			UNIV_PRINT_ANY_ARRAY(mas , length_row , "Вызвана рекурсия." , recurs_level+1 , arr_num) 
			arr_num += 1
			
		return # т к дальше гнать смысла нет





	
	curr_ind = 0
	for elem in arr: # каждый элем



		# Перенос строки
		if (curr_ind) % length_row == 0:
			print ("")
    
 
 
  
    
  
  
  
		# Вывод чисел
		if data_type == "<class 'int'>": 
	
				# Вернет СТРОКУ !!!!
				#elem = GET_COLORED( elem , "weight" )
				#elem = int(elem)
				
				end_sumb = ""
				
				
				
				
				
				
				# 1, 2,..., 9# 2 симв
				if elem >= 0 and elem <= 9:
					print ( "" , GET_COLORED( elem , "weight" ) , end=end_sumb)

				else:  # #-1 ... -9# 2 симв
				
					# -1 ... -9
					if elem <= -1 and elem >= -9:
						print ( GET_COLORED( elem , "weight" ) , end=end_sumb )    
						
					if  elem <= -10 :
						print ( "", GET_COLORED( elem , "weight" ) , end=end_sumb )    
						
					if  elem >= 10:
						print ( " ", GET_COLORED( elem , "weight" ) , end=end_sumb )    
						
						
						
					#else: #  -10 <= x <= 10  # 2 или 3 и более цифры
					#	print ( GET_COLORED( elem , "weight" ) , end=end_sumb )

  
  
  
  
  
  
		
		# Вывод строк (001010101)
		if data_type == "<class 'str'>": 
			# Строка => выводим эталон числа типа 0101101010
			print ( GET_COLORED( elem , "reference") , end=" " )
      
      
      
      
      
      
      
		if data_type == "<class 'float'>": 
			print ( elem , end=" " )
      
      
      
      
      
      
		curr_ind += 1
		# end for
		
		
	#print("\n" + "#"*25 + " - End print" , end = "")
	print( "" )
	return




# Возвращает СТРОКУ!!!!
# num = 1 любое число  или  символ(0/1)    type = weight , reference
def GET_COLORED( num , type="weight" , targ_color = "красный" ):
	
	
	colors = {
	  "черный"   : 30 ,
	  "красный"  : 31,
	  "зеленый"  : 32,
	  "желтый"   : 33,
	  "синий"    : 34,
	  "пурпурный" : 35,
	  "голубой"  : 36,
	  "белый"    : 37
	}
	
	
	####################################################
	if type == "color":
	  return "\x1b["+ str(colors.get(targ_color) ) + "m" + str(num) + "\x1b[0m"
	
	
	####################################################
	# STRING
	if type == "reference":    # эталон (01010101)
			
			if (num == "1"):
				return "\x1b[41m" + num + "\x1b[0m"   # Красный ФОН
			
			if (num == "0"):
				return "\x1b[8m" + num + "\x1b[0m"   # Невидимый
	
	
	
	####################################################
	
	# INT
	if type == "weight":    # Веса  INT

		#num = int(num)

		if num == 0:
			return "\x1b[33m" + str(num) + "\x1b[0m"   # Желтый
			
			
			
			
		#if num >= 1  and  num < bias:
		#	return "\x1b[32m" + str(num) + "\x1b[0m"   # Желтый
			
		#if num >= bias:
		#	return "\x1b[42m" + str(num) + "\x1b[0m"   # Зеленый
		
		if num >= 1:
		 	return "\x1b[42m" + str(num) + "\x1b[0m"   # Зеленый




		minus_bias = bias-bias-bias+1

		# от -1 до  -bias
		if num <= -1 and num >= minus_bias :
			return "\x1b[31m" + str(num) + "\x1b[0m"   # Красный
	
		if num < minus_bias:
			return "\x1b[41m" + str(num) + "\x1b[0m"   # Зеленый
	
	####################################################
	
	if type == "net":    # Суммы  INT   # 1  это 2?  False net =-3
	
		if num <= -1:
			return "\x1b[31m" + str(num) + "\x1b[0m"   # Красный
	
		if num >= 1 and num <= bias-1:
			return "\x1b[33m" + str(num) + "\x1b[0m"   # Желный
	
		if num >= bias:
			return "\x1b[32m" + str(num) + "\x1b[0m"   # Зеленый
	
	
	####################################################
	
	# оно никогда не выполнится(оставлю на всяк)
	return num




####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

# Выдаст массив с N рандомнымных чисел в заданном диапазоне
# НЕ юзать three
def GET_arr_random_int( min , max , count , parts = "two" ):

		ret_arr = []

		#print(min)
		#print(max)
		

		for i in range( 0 , count ):
			
			if parts == "one":
				return [random.randint(min, max) for i in range(count)]
				#ret_arr.append( random.randint (min, max) ) # рандом min ... max

			# Идеально ровное распеделение(Все числа выпали одинак кол-во раз)
			if parts == "two":
				
				step = int(max/2)  # при 1,10 => base=9 => step=4 # 1...4 5...9
	
				# диапазон min...max делится на равные(+-1) части между генераторами
				if i%2 == 0: 	ret_arr.append( random.randint ( min , step) ) # рандом
				else:					ret_arr.append( random.randint (step+1, max) ) # рандом 

			
			
			# Последний блок выпадает чаще других (больше всех других на 25%  (все по 6000, он 8300))
			# Все дело в if i % !N!    таких чисел меньше
			if parts == "three":
				
				step = int(max/3)+1 #1...10
				step2 = step*2 #11...20
				step3 = step*3 #21...30
		
				# диапазон min...max делится на равные(+-1) части между генераторами
				if i%3 == 0: 
					ret_arr.append( random.randint ( min , step) ) # рандом 
				else:
					if i%2 == 0:
						ret_arr.append(   random.randint ( step+1 , step2 )   ) # рандом
					else: # этот блок выпадает чаще других
						ret_arr.append(   random.randint ( step2+1, max)   ) # рандом


		'''
		arr_random_int = GET_arr_random_int( 0 , 9 , iter_count , "two" )

		arr_random_int.sort()

		for i in range(0,30):
			print ( i , " = " , arr_random_int.count(i) )


		exit()
		'''


		return ret_arr
 
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
 
def this_num_is(one_number_01, return_net=False , debug_mode=False , buf_array_weights = buf_array_weights):
    
    '''
    if bool(debug_mode):
          print("#"*45)
          #print("this_num_is ", one_number_09)
          print_weight(weights)
          print_01_num(one_number_09)
    '''
    # Рассчитываем взвешенную сумму
    net = 0
    for i in range(15):
      
        # old_net = net
      
        net += int(one_number_01[i])*buf_array_weights[i] # 0/1 * его вес(любой)
        
    '''  
        if bool(debug_mode):
           if i%3 == 0:
               print("")
          
           print( one_number_01[i], "*" , weights[i], "=> ",old_net, "+=" , int(one_number_09[i])*int(weights[i]), " == ", net  )
        
    
       
        
    if bool(debug_mode):
        print("\nФинальный net= ", net , "  Решение:", net >= bias , "\n") 
        print("#"*45)
        return str(net >= bias)+" net="+str(net)
        
		'''
    # Превышен ли порог? (Да - сеть думает, что это 2. Нет - сеть думает, что это другая цифра)
    if bool(return_net):
        
        if net >= bias:
          var="=====TRUE====="
        else:
          var="False"
          
        if net == 0:
          return  var + " net ="+str(net)
        
        if net <= -1:
          return  var + " net ="+ GET_COLORED(net , "net")
          
        if net >= 1 and net <= bias-1:
          return  var + " net ="+ GET_COLORED(net , "net")
          
        if net >= bias:
          return  var + " net ="+ GET_COLORED(net , "net")
          
        
        #print("Конец программы")
          
        
    else:
    
    	return net >= bias

    
    
    
    
    
    
  
# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease_old(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Уменьшаем связанный с ним вес на единицу
            buf_array_weights[i] -= 1
 
 
# Увеличение значений весов, если сеть ошиблась и выдала 0
def increase_old(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Увеличиваем связанный с ним вес на единицу
            buf_array_weights[i] += 1
 
 
 
 
 
 
 
 
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


UNIV_PRINT_ANY_ARRAY( ARRAY_ALL_010101[0] , 3 )
UNIV_PRINT_ANY_ARRAY( ARRAY_ALL_010101[4] , 3 )

UNIV_PRINT_ANY_ARRAY( ARRAY_ALL_010101[6] , 3 )
UNIV_PRINT_ANY_ARRAY( ARRAY_ALL_010101[7] , 3 )




# парам = для чего считаем веса
def CALC_WEIGHTS( str_target_number_010101 , arr_random_int):
 
	# Чистим и заного заполняем нулями(робит)
	buf_array_weights.clear()
	for k in range(15):
		buf_array_weights.append( 0 )

	#print("Новые буферные веса:", buf_array_weights)

	
	for i in range( iter_count ):

		rand_num = arr_random_int[i] # 0-9
  
  
  
		# сгенр число != целевому
		if rand_num != str_target_number_010101 :
				
			if this_num_is( ARRAY_ALL_010101[rand_num]  ):   # Если сеть выдала True/Да/1, то наказываем ее
				decrease_old( ARRAY_ALL_010101[rand_num] )
      
		else: # Если получилось число 2 или 5
			# Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
			if not this_num_is( ARRAY_ALL_010101[str_target_number_010101] ):
				increase_old( ARRAY_ALL_010101[str_target_number_010101] )
                
  ############################################################################
	

	return buf_array_weights.copy() 
	 # Без копии передаст прямую ССЫЛКУ!!! и ВСЕ образы будут == ПОСЛЕДНЕМУ состоянию buf_array_weights



# K и C ПРАВИЛЬНЫЕ(небольшая погрешность(<1%) в сравнении с онлайн решалками)
def CALC_LINE_KOEFF_MNK( str_target_number_010101 ):
	
	
	#	X = 0...14 (все числа)
	#	Y = 0 или 1
	
	
	XX = 0
	XY = 0
	
	SUM_X = 0
	SUM_Y = 0
	SUM_XY = 0
	SUM_XX = 0
	
	targ_num_01 = str_target_number_010101 #ARRAY_ALL_010101[3] # норм
	
	KOL_PNTS = len(str_target_number_010101) #15
	
	
	############################################################################
		
			
	for i in range( 0 , KOL_PNTS ): # 0...14 включительно    i = X
				
		XX = i*i
		XY = i* int(targ_num_01[i])
				
				
		SUM_X += i
		SUM_Y += int(targ_num_01[i])
				
		SUM_XY += XY
		SUM_XX += XX


	# Формула ВЕРНА!!!!
	k = (    KOL_PNTS * SUM_XY    -    SUM_X * SUM_Y   )  /  (  KOL_PNTS * SUM_XX - SUM_X**2 )  #pow(SUM_X, 2)   )
	c = (    SUM_Y - k * SUM_X    )    /  (   KOL_PNTS   );
			
	
	#print('Готовая прямая: ', k, '* X + ', c)
	return [k,c]
	
	
	

def CALC_LINE_KOEFF_DELTA( str_target_number_010101 ):

		
		
		# Коэффициент при x
		k = random.uniform(-5, 5) # -5 5
 
		# Свободный член уравнения прямой
		c = random.uniform(-5, 5) # -5 5



		for i in range( iter_count_delta ):
		
			# Получить случайную X координату точки (случ ИНДЕКС 0...14 в листе 001001001001001 )
			rand_X_0_14 = random.randint(0, 14)



			# Получить соответствующую Y координату точки ( 0 или 1 )
			true_result = int( str_target_number_010101[rand_X_0_14] ) # ( истинное значение )
			#print("true_result=",true_result)
 
 

    
			# Получить ответ сети
			out = (rand_X_0_14 * k) + c  # Высчитать y
			#print("out=",out)
			
			
			
			# Считаем ошибку сети
			delta = true_result - out
			#print("delta=", delta)
			
			
			
			# Меняем вес при x в соответствии с дельта-правилом
			k += delta*training_speed*rand_X_0_14
 
 
 
			# Меняем вес при постоянном входе в соответствии с дельта-правилом
			c += delta*training_speed
		
		return [k,c]

				
				
				

	
	



####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


# Генерируем рандомные числа
Time = My_timer("Start")

arr_random_int = GET_arr_random_int( 0 , 9 , iter_count , "two" )

My_timer("Stop" , Time , "Генерация " + str(iter_count) + " случ чисел заняла: " )


####################################################################################
          # ОБУЧЕНИЕ ДЛЯ КАЖДОГО ЧИСЛА


print ("\nОбсчет начат.")
Time = My_timer("Start")



# Учимся на 10 числах			ALL_weights_old[0 ... 9][0 ... 14]
for study_index in range(0,10) : 
	ALL_weights_old.append (CALC_WEIGHTS( study_index , arr_random_int ))



print ("Обсчет закончен.")
My_timer("Stop" , Time , "Обсчет 1 чисел занял: " )


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
          # ПЕЧАТЬ ВСЕХ ВЕСОВ



i = 0
for w in ALL_weights_old : 
	UNIV_PRINT_ANY_ARRAY( w , print_row_len , "Веса для числа "+str(i)+":")
	i += 1
	
	

# НЕ УДАЛЯТЬ
# ПРОВЕРКА ДЛЯ ВЕСОВЫХ
'''
TARGET_NUMBER_09 = 3

# Эталон
TARGET_NUMBER_01_CLEAN = ARRAY_ALL_010101[ TARGET_NUMBER_09 ] # [2]
TARGET_NUMBER_01_DAMAGED = list('110000010001111') # Сломаная

#############################################  



print ("Проверка по ЧИСТЫМ числам(увидит ли эталон)")

UNIV_PRINT_ANY_ARRAY( ALL_weights_old[TARGET_NUMBER_09] , print_row_len , "Веса искомого числа:")
UNIV_PRINT_ANY_ARRAY(   TARGET_NUMBER_01_CLEAN      , print_row_len , "Эталон искомого числа:" )

UNIV_PRINT_ANY_ARRAY(   TARGET_NUMBER_01_DAMAGED      , print_row_len , "Поврежденное число:" )



Time = My_timer("Start")

#
print("\nBias = ", bias )
for n in range(0,10):
	print( str(n) , " это ", TARGET_NUMBER_09 ,"? ",
		this_num_is( TARGET_NUMBER_01_DAMAGED , 1 , 0 , ALL_weights_old[ n ] ))

My_timer("Stop" , Time , "Прогон по 10 весам занял: " )

'''
# ПРОВЕРКА ДЛЯ ВЕСОВЫХ
# НЕ УДАЛЯТЬ








#print( "#"*40)
print ("\n\n")
print ( "#" * 45 )
print ( "#" * 60 )
print ( "#" * 45 )

#input("Для начала обсчета коэфф введите что-нибудь: ")

print ("\n\n\n") #\n\n\n")

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
	
			# ЧЕРЕЗ МОРО





# Сигмоида 
def nonlin(x,deriv=False):
		
		sigmoid = 1/(1+np.exp(-x))
	
		if(deriv==True):
				return sigmoid*(1-sigmoid)
		
		return sigmoid




	
# парам = для чего считаем веса
def CALC_WEIGHTS_TOPOR( str_target_number_010101 ):
 
	print(str_target_number_010101)
 
	# Чистим и заного заполняем нулями(робит)
	buf_array_weights.clear()
	for k in range(15):
		buf_array_weights.append( 0 )

	#print("Новые буферные веса:", buf_array_weights)

	
	for i in range( 6 ):

		ind = 0
		for one_true_result in str_target_number_010101:

			# Получить случайную X координату точки (случ ИНДЕКС 0...14 в листе 001001001001001 )
			#rand_X_0_14 = random.randint(0, 14)
			
			one_true_result = int(one_true_result)
			#print(one_true_result)
			
			rand_X_0_1  = 1 #random.randint(0, 1)
			
			#print(rand_X_0_1)
			
			if one_true_result == rand_X_0_1:
				#Угадал
				buf_array_weights[ind] += 1
			
			if one_true_result != rand_X_0_1:
				buf_array_weights[ind] -= 1
			
			
			ind += 1
			
			#print(buf_array_weights)
			
			#true_result = int( str_target_number_010101[rand_X_0_14] ) # ( истинное значение )
			#print("true_result=",true_result)
 
    
    
    
			# Получить ответ сети
			#out = (rand_X_0_14 * k) + c  # Высчитать y
			#print("out=",out)
			
			
			# Считаем ошибку сети
			#delta = true_result - out
			#print("delta=", delta)
			
			
			# Меняем вес при x в соответствии с дельта-правилом
			#k += delta*training_speed*rand_X_0_14
 
 
			# Меняем вес при постоянном входе в соответствии с дельта-правилом
			#c += delta*training_speed
		
	#return [k,c]

	

	return buf_array_weights.copy() 
	
 ############################################################################

#for i in range(0,10):



#num3 = list('111001111001111') # Чему учимся


### Прямая прогонка
mass = CALC_WEIGHTS_TOPOR( ARRAY_ALL_010101[6] )
UNIV_PRINT_ANY_ARRAY( mass , print_row_len , "Веса для числа:")























'''
# Обсчет
for i in range(0,10):
	
	
	
	
	
	#kc = CALC_LINE_KOEFF_MNK( ARRAY_ALL_010101[i] )
	kc = CALC_LINE_KOEFF_MNK( ALL_weights_old[i] )
	#print(kc)
	line_koeff_mnk_k.append( kc[0] )
	line_koeff_mnk_c.append( kc[1] )
	
	
	#kc = CALC_LINE_KOEFF_DELTA( ARRAY_ALL_010101[i] )
	#print(kc)
	#line_koeff_delta_k.append( kc[0] )
	#line_koeff_delta_c.append( kc[1] )
	
	
'''

#SUM_perc_shodstva_k = 0
#SUM_perc_shodstva_c = 0



# Вывод ВСЕГО
#for i in range( len(line_koeff_mnk_k) ):
#	print ( "MNK для " , i , ": K=" , line_koeff_mnk_k[i]   , " C=" , line_koeff_mnk_c[i])
	#print ( "DLT для " , i , ": K=" , line_koeff_delta_k[i] , " C=" , line_koeff_delta_c[i])
	
	
	#######################
'''
	if line_koeff_mnk_k[i] >= line_koeff_delta_k[i]:
		k_razn = line_koeff_mnk_k[i] - line_koeff_delta_k[i]
	else:
		k_razn = line_koeff_delta_k[i] - line_koeff_mnk_k[i]
		
		if k_razn < 0:
			k_razn *= -1
			
		
		
	if line_koeff_mnk_c[i] >= line_koeff_delta_c[i]:
		c_razn = line_koeff_mnk_c[i] - line_koeff_delta_c[i]
	else:
		c_razn = line_koeff_delta_c[i] - line_koeff_mnk_c[i]
		
		if c_razn < 0:
			c_razn *= -1		
			

	print("Разница :    K=", k_razn )
	print("Разница :    C=", c_razn ) 
	
	#######################
	
	otcl_k_percent = int( (line_koeff_mnk_k[i] / line_koeff_delta_k[i]) * 100 )
	otcl_c_percent = int( (line_koeff_mnk_c[i] / line_koeff_delta_c[i]) * 100 )
	
	if otcl_k_percent == 0: otcl_k_percent = int(line_koeff_delta_k[i]*100) #"Dev_by_zero"  
	if otcl_c_percent == 0: otcl_c_percent = int(line_koeff_delta_c[i]*100) #"Dev_by_zero" 
	
	
	# Делает полонительным
	if otcl_k_percent < 0: otcl_k_percent *= -1
	if otcl_c_percent < 0: otcl_c_percent *= -1
	
	
	
	
	mnk_k = line_koeff_mnk_k[i]
	del_k = line_koeff_delta_k[i]
	
	mnk_c = line_koeff_mnk_c[i]
	del_c = line_koeff_delta_c[i]
	
	
	powed = pow(10, num_after_comma)

	
	# Будет косяк если int() был не 0.0000001 => int=1 => 1-1=0(1число)  
	#,  а полный 0.00000 => получим int()=0 => 0-1 = -1
	
		
	if  int( mnk_k*(powed) )-1 == int( del_k*(powed) )-1 :
		# Считаем, что точность достаточная
		otcl_k_percent = 100
		print( GET_COLORED( "Достаточная точность K ( "+str(num_after_comma)+" число после ',' сошлось)" , "color" , targ_color = "зеленый" ))
	
	
	if  int( mnk_c*(powed) )-1 == int( del_c*(powed) )-1 :
		# Считаем, что точность достаточная
		otcl_c_percent = 100
		print( GET_COLORED( "Достаточная точность C ( "+str(num_after_comma)+" число после ',' сошлось)" , "color" , targ_color = "зеленый" ))
	
	
	SUM_perc_shodstva_k += otcl_k_percent
	SUM_perc_shodstva_c += otcl_c_percent
	
	
	print ("Сходство K составляет K=", otcl_k_percent , "%" )
	print ("Сходство C составляет C=", otcl_c_percent , "%" )
	print("")
'''
	
####################################################################################
####################################################################################

'''
print("Верификация достоверности коэффициентов:")
print("MNK ВСЕГДА дает одинаковый, стабильный результат, поэтому все сравниваем с ним")
print("MNK Был обсчитан вручную через онлайн-калькулятор, результаты вычислений тут и там полностью сходятся")
print("SUM  %K = ", SUM_perc_shodstva_k)
print("SUM  %C = ", SUM_perc_shodstva_c)

print("AVG Сходство DLT с MNK: K =", int(SUM_perc_shodstva_k/len(line_koeff_mnk_k)) , "%")
print("AVG Сходство DLT с MNK: C =", int(SUM_perc_shodstva_c/len(line_koeff_mnk_k)) , "%")
print("!!!  300%, 0%, 0% даст AVG = 100%")
'''

print("\n\n\n")





####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#print("К этому моменту имеем коэфф для всех чисел в списках(line_koeff_mnk_k,c  line_koeff_delta_k,c)")


'''
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')	# Эталоны
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
'''



'''
TARGET_NUMBER_01_CLEAN = ARRAY_ALL_010101[ 3 ]
TARGET_NUMBER_01_DAMAGED = list('111001111001111') # 3, пока чистая

# Для дельты просто меняем тут назв функции
buf = CALC_LINE_KOEFF_MNK( TARGET_NUMBER_01_CLEAN )

TARGET_K = buf[0]
TARGET_C = buf[1]


print ( "K=" , TARGET_K   , " C=" , TARGET_C)
'''






# Тут должна быть функция прогона и сверки этой прямой с этплонами прямых












#exit()























#print( GET_COLORED("a1a2a3a" , "color" , "красный")  )

print("\x1b[32mКонец программы\x1b[0m")
print("\n\n\n")

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
'''
	# настраиваем детали отрисовки графиков
	plt.figure(figsize=(8, 6))
	plt.title("Installations")
	plt.xlabel("Days")
	plt.ylabel("Installations")
	#plt.xticks([...], [...]) # можно назначить свои тики
	plt.autoscale(tight=True)

	# рисуем исходные точки
	plt.scatter(1, 2)
	
	
	
	#plt.plot(fx, f(fx), linewidth=2)
	plt.plot(1, 2, linewidth=2)
	plt.plot(2, 3, linewidth=2)
	plt.plot(3, 4, linewidth=2)
	
	#plt.legend(legend, loc="upper left")
	plt.grid()
	#plt.savefig('data.png', dpi=50)
	plt.show()
'''
	

'''
Если наша нейросеть правильно распознала 5 или отвергла не 5, то мы ничего не предпринимаем (все ведь замечательно!).

Если нейросеть ошиблась и распознала (неверную цифру) НЕ пятерку как 5, то мы должны ее наказать – мы уменьшаем веса тех связей, через которые прошел сигнал. Другими словами веса, связанные с возбудившимися входами, уменьшаются.

Если нейросеть ошиблась и распознала цифру 5 как НЕ пятерку (как любую другую), то мы должны увеличить все веса, через которые прошел сигнал. Таким образом мы как бы говорим сети, что такие связи, а значит и связанные с ними входы – правильные.
'''
'''
Алг обучения

Подать на входы нейросети цифру в строковом формате.
Если цифра распознана/отвергнута верно, то перейти к шагу 1.
Если сеть ошиблась и распознала неверную цифру как 5, то вычесть из всех связей, связанных с возбудившимися S-элементами единицу.
Если сеть ошиблась и отвергла цифру 5, то добавить единицу ко всем связям, связанным с возбудившимися S-элементами.
'''
'''
Чтобы сеть гарантированно научилась распознавать нужную нам цифру надо соблюсти два условия:

Добиться равномерности показа всех обучающих цифр.
Увеличить общее количество шагов обучения (50 тысяч или 100 тысяч).
'''

''' 

# Прогон по тестовой выборке
#print("Проверка  по ШУМНЫМ числам(смешанные)")
#print("Узнал чистую 2? ", this_num_is(num2))
#print("Узнал 2 в числе 1? ", this_num_is(num21,1))
#print("Узнал 2 в числе 2? ", this_num_is(num22,1))
#print("Узнал 2 в числе 3? ", this_num_is(num23,1,1))
#print("Узнал 2 в числе 4? ", this_num_is(num24,1))
#print("Узнал 2 в числе 5? ", this_num_is(num25,1))
#print("Узнал 2 в числе 6? ", this_num_is(num26,1))


#print("Узнал 21? ", this_num_is(num21,1)) 
#print("Узнал 22? ", this_num_is(num22,1)) 
#print("Узнал 23? ", this_num_is(num23,1)) 

'''


  
'''
# Генерируем случайное число от 0 до 4 
    j1=0 
    for j1 in range(9): 
      rand_num = random.randint (0, 4) 
      j1+=1 
# Генерируем случайное число от 5 до 9 
      j2=0 
    for j2 in range(9): 
      rand_num = random.randint (5, 9) 
      j2+=1 
    # Если получилось НЕ число 2
    if rand_num != 2:
        # Если сеть выдала True/Да/1, то наказываем ее
        if this_num_is(nums[rand_num]):
            decrease(nums[rand_num])
    # Если получилось число 5
    else:
        # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
        if not this_num_is(num2):
            increase(num2)
'''



# https://habrahabr.ru/post/94647/   цвета консоли
# https://neuralnet.info/chapter/???µN?N??µ??N?N?????N?/



'''
import numpy as np

# Сигмоида 
def nonlin(x,deriv=False):
    if(deriv==True):
        return f(x)*(1-f(x))
    return 1/(1+np.exp(-x))
'''






'''
Списки имеют большой набор функций:
append , extend — добавление;
insert — вставка;
index — найти индекс первого вхождения конкретного элемента;
count — подсчет повторов элемента;
remove , del — удаление элемента;
sort — сортировка;
reverse — реверс;
pop — извлечение элемента;






Если вы строите словарь со словами в виде ключей и количеством вхождений каждого слова в качестве значения, упрощается здесь как:

from collections import defaultdict
d = defaultdict(int)
for w in text.split():
  d[w] += 1




Функции/методы словаря
dict() — создание словаря;
len() — возвращает число пар;
clear() — удаляет все значения из словаря;
copy() — создает псевдокопию словаря;
deepcopy() — создает полную копию словаря;
fromkeys() — создание словаря;
get() — получить значение по ключу;
has_key() — проверка значения по ключу;
items() — возвращает список значений;
iteriyems() — возвращает итератор;
keys() — возвращает список ключей;
iterkeys() — возвращает итератор ключей;
pop() — извлекает значение по ключу;
popitem() — извлекает произвольное значение;
update() — изменяет словарь;
values() — возвращает список значений;
itervalues() — возвращает итератор на список значений.
in — оператор, проверяет наличие значения по ключу;
del — оператор, удаляет пару по ключу;
dict() — конструирует словарь с помощью последовательности.

'''












