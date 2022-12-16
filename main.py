from input import get_data
import racional
import complex
import logger

data = get_data()
if 'j' in data[0]:
    result = complex.complex_result(data)
    print(result)
else:
    result = racional.racional_result(data)
    print(result)

logger.calc_logger(data,result)