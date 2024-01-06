"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
"""
import time


s = "07:05:45PM"


def timeConversion(s):
    time_input = time.strptime(s, "%I:%M:%S%p")
    time_str = time.strftime("%H:%M:%S", time_input)
    return time_str


# Obtém o tempo atual em segundos desde --->>>>1/1/1970<<<<-----
time_now = time.time()
# exemplos de uso


# Obtendo a Hora Atual:
current_time = time.localtime()
print(f"Hora atual: {time.strftime('%H:%M:%S', current_time)}")


# Atraso de Execução:
print("Início")
time.sleep(2)  # Atrasa a execução por 2 segundos
print("Fim após atraso de 2 segundos")


# Medindo o Tempo de Execução:
start_time = time.time()
# Código para medir o tempo de execução
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time} segundos")


# Formatando Timestamps:
timestamp = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(f"Timestamp formatado: {formatted_time}")


# Convertendo String para Objeto de Tempo:
time_string = "2023-12-28 14:30:00"
time_object = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(f"Objeto de tempo: {time_object}")

# Obtendo o Tempo Atual em Segundos desde a Época:
current_time_seconds = time.time()
print(f"Tempo atual em segundos desde a época: {current_time_seconds}")


# Obtendo Componentes Individuais de Tempo:
current_time = time.localtime()
year, month, day, hour, minute, second = current_time.tm_year, current_time.tm_mon, current_time.tm_mday, current_time.tm_hour, current_time.tm_min, current_time.tm_sec
print(f"Ano: {year}, Mês: {month}, Dia: {day}, Hora: {hour}, Minuto: {minute}, Segundo: {second}")


# Calculando Diferença entre Duas Datas:

date_string1 = "2023-01-01"
date_string2 = "2023-12-31"

date1 = time.strptime(date_string1, "%Y-%m-%d")
date2 = time.strptime(date_string2, "%Y-%m-%d")

time_difference = time.mktime(date2) - time.mktime(date1)
days_difference = int(time_difference / (24 * 3600))

print(f"Diferença em dias entre as datas: {days_difference} dias")
