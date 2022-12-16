from datetime import datetime as dt
 
def calc_logger(data,res):
    time = dt.now()
    a,b,move = data
    with open('log.txt','a') as file:
        file.write(f'{a} {move} {b}  = {res}: {time}\n')