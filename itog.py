import numpy as np
import matplotlib.pyplot as plt


def file_reader():
    print('Введите имя файла размера txt. Пример: myfile.txt ')
    name_file = input()
    try:
        with open(name_file, "r") as file: # открытие и считывание данных файла в двумерный массив.
            data = np.loadtxt(file)
    except:
        print('Файл не существует или произошла ошибка.\n','Попробуйте еще раз')
        return file_reader()

    return data

def choose_gragh():
    for_choise = {1: 1, 2: 3, 3: 5, 4: 7}
    print('Для построение определенного графика нажмите:', '\n', '1:Для построение графика S11', '\n',
          '2:Для построение графика S21', '\n', '3:Для построение графика S12', '\n',
          '4:Для построение графика S22')
    print(type(for_choise))
    inp = input()
    try:
        int(inp)
    except ValueError:
        print('Некорректный ввод')
        return choose_gragh()


    try:
        for_choise[int(inp)]

    except KeyError:
        print('Неверный ключ')
        return choose_gragh()

    return int(inp)


def draw_function(x,y,passer,name):
    a=0;b=0
    for_choise = {1: 1, 2: 2}

    if passer==True:
        print('Способ задания границ графика:\n', 'Для задания границ вручную нажмите 1\n',
              'Для задания границ автоматически нажмите 2')
        choise = input()
    else:
        print('Введите границы для наложения оконной функции')
        choise = 1

    try:
        int(choise)
    except ValueError:
        print('Некорректный ввод')
        return draw_function(x,y,passer,name)
    if (name==1 and for_choise[int(choise)]==1):
        for_choise[int(choise)] =3
    try:

        if for_choise[int(choise)]==2:
            fig = plt.figure()
            ax = fig.add_subplot()
            plt.ylabel('Дб')
            if name==1:
                plt.xlabel('frequency')
                plt.title('Спектральная плотность')
            else:
                plt.xlabel('time[ns]')
                plt.title('Временное представление')
            plt.plot(x, y, color='indigo', linewidth=1.5)
            plt.show()
            return
        if for_choise[int(choise)]==1:
            print('Введите левую границу [нс]')
            a = input()
            print('Введите правую границу [нс]')
            b = input()
            try:
                float(a) and float(b)
            except ValueError:
                print('Некорректный ввод')
                return draw_function(x,y,passer,name)

            if a>=b:
                print('Некорректный ввод!Левая граница больше правой!Повторите ввод.')
                return draw_function(x,y,passer,name)


            fig = plt.figure()
            ax = fig.add_subplot()
            plt.ylabel('Дб')
            if name==1:
                plt.xlabel('frequency')
                plt.title('Спектральная плотность')
            else:
                plt.xlabel('time[ns]')
                plt.title('Временное представление')
            plt.xlim(float(a) * pow(10, -9), float(b) * pow(10, -9))
            plt.plot(x, y, color='indigo', linewidth=1.5)
            plt.show()
            return float(a) * pow(10, -9), float(b) * pow(10, -9)
        if for_choise[int(choise)]==3:
            print('Введите левую границу [МГц]')
            c = input()
            print('Введите правую границу [МГц]')
            d = input()
            try:
                float(c) and float(d)
            except ValueError:
                print('Некорректный ввод')
                return draw_function(x,y,passer,name)
            if float(c)>=float(d):
                print('Некорректный ввод!Левая граница больше правой!Повторите ввод.')
                return draw_function(x,y,passer,name)


            fig = plt.figure()
            ax = fig.add_subplot()
            plt.ylabel('Дб')
            if name==1:
                plt.xlabel('frequency')
                plt.title('Спектральная плотность')

            plt.xlim(float(c) * pow(10, 6), float(d) * pow(10, 6))
            plt.plot(x, y, color='indigo', linewidth=1.5)
            plt.show()
            return
    except KeyError:
        print('Некорректный ввод')
        return draw_function(x,y,passer,name)


def find_mind_value(array_x,array_y,a, b):


    indexes = np.where((array_x>=a) & (array_x<=b))[0]

    rusult_array = np.delete(array_y,indexes)

    return  np.mean(rusult_array)


data=file_reader()

i=choose_gragh()

frequency = data[:, [0]]  # Массив частот
Res = data[:, [1]]
Im = data[:, [2]]

function_value = ((Im * 1j) + Res)[:,0]   # Массив значений функции, график которого будем строить

print('Построение спектральной плотности до фильтрации.')
draw_function(frequency,20*np.log10(abs(function_value)),True,1) #Построение выбранной функции
time_graph_representation = np.fft.ifft(function_value) #обратное преобразование Фурье, переход к временной характеристике
time_graph_representation_null=np.fft.fftshift(time_graph_representation)

N_massive = np.arange(0,frequency.size,1)

range_time_field= (frequency.size-1)/(frequency[-1]-frequency[0])

step = range_time_field/frequency.size

x_of_timefield= -range_time_field/2+step*N_massive
print('Построение графика во временной области без фильтрации.')
draw_function(x_of_timefield,20*np.log10(abs(time_graph_representation_null)),True,0)

a,b= draw_function(x_of_timefield,20*np.log10(abs(time_graph_representation_null)),False,0)


massive_window_function_y=np.arange(0.001,frequency.size,1)


mid_value= find_mind_value(x_of_timefield,20*np.log10(abs(time_graph_representation_null)),a,b)
print(mid_value)

for i in range(x_of_timefield.size):
    if x_of_timefield[i]<a or x_of_timefield[i]>b:
        massive_window_function_y[i]=mid_value
    else:
        massive_window_function_y[i]=0.0001



window_function_r= 10**(massive_window_function_y/20)

windf_on_time= window_function_r*time_graph_representation_null
print('Построение графика во временной области с наложением окна.')
draw_function((x_of_timefield),20*np.log10(abs((windf_on_time))),True,0)
frequency_gragh_filtr = np.fft.fft(windf_on_time)

print('Построение спектральной плотности с фильтрацией.')
draw_function(frequency,20*np.log10(abs(frequency_gragh_filtr)),True,1)


