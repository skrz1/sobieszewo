import re
spl_line = " "

acl_line1 = "              ▟███████▙   ███████████  ███▙   ███  ████████████  ██████████▙   ███     ███  ████▙     ▟████"
acl_line2 = "             ▟██▛    ▜█▙  ███          ████▙  ███       ███      ███     ▝██▊  ███     ███  ███▜█▙   ▟█▛███"
acl_line3 = "▟█████▙ ▟█▛  ███          ███▄▄▄▄▄▄▄   ███▜█▙ ███       ███      ███     ▗██▊  ███     ███  ███ ▜█▙ ▟█▛ ███"
acl_line4 = "██   ▜███▛   ███          ███▀▀▀▀▀▀▀   ███ ▜█▙███       ███      ██████████▛   ███     ███  ███  ▜███▛  ███"
acl_line5 = "██   ▟███▙   ▜██▙    ▟█▛  ███          ███  ▜████       ███      ███   ▜██▙    ▜██▖   ▗██▛  ███   ▝▀▘   ███"
acl_line6 = "▜█████▛ ▜███  ▜███████▛   ███████████  ███   ▜███       ███      ███    ▜██▙    ▜███████▛   ███         ███"

acv_line1 = "      ▟▀▀▀▙  ▟▀▀▀▙"
acv_line2 = "▜▙ ▟▛ █   █  ▜▄▄▄█"
acv_line3 = " ▜▆▛  ▜▄▄▄▛ ▄ ▄▄▄▛"

hcl_line1 = "          ▟██████████████████████████████████████████████████████████████▛    ▟██████████████▛  ▄▄▄ ▄ ▄"
hcl_line2 = "         ▟██████████████████████████████████████████████████████████████▛    ▟██████████████▛    █  █▀█"
hcl_line3 = "                                                                   ▟███▛    ▟███▛      ▟███▛           "
hcl_line4 = "       ▟███▛      ▟███████████████████████████████▌      ▟███▛    ▟███▛    ▟███▛      ▟███▛            "
hcl_line5 = "      ▟███▛      ▟████████████████████████████████▊     ▟███▛    ▟███▛    ▟███▛      ▟███▛             "
hcl_line6 = "     ▟███▛      ▟███▛             ▟███▛   ▟███▛▐███    ▟███▛    ▟███▛    ▟███▛      ▟███▛              "
hcl_line7 = "    ▟████████████████████████▛   ▟███▛   ▟███▛  ███▎  ▟███▛    ▟███▛    ▟██████████████▛               "
hcl_line8 = "   ▟████████████████████████▛   ▟███▛   ▟███▛   ▐██▌ ▟███▛    ▟███▛    ▟██████████████▛                "
hcl_line9 = "  ▟███▛      ▟███▛             ▟███▛   ▟███▛     ██▊▟███▛    ▟███▛                                     "
hcl_line10 =" ▟███▛      ▟█████████████████████████████▛      ▐█████▛    ▟███████████████████████▛                  "
hcl_line11 ="▟███▛      ▟█████████████████████████████▛        ████▛    ▟███████████████████████▛                   "


# MATHEMATICS FUNCTIONS
def ac_FACTORIAL(value):
    answer = 1
    if(value < 0):
        answer = 1/0
    if(value != 0 or value != 1):
        for i in range(int(value)):
            answer = answer * (i+1)
    return answer

def ac_xPI(value):
    answer = value * 3.14159265358979323846264338328
    return answer

def ac_xe(value):
    answer = value * 2.71828182845904523536028747135
    return answer

def ac_ex(value):
    answer = 2.71828182845904523536028747135**value
    return answer

def ac_DEG2RAD(value):
    answer = value/180 * ac_xPI(1)
    return answer

def ac_RAD2DEG(value):
    answer = value/ac_xPI(1) * 180
    return answer

def ac_DEG2GRA(value):
    answer = value/360*400
    return answer

def ac_RAD2GRA(value):
    answer = ac_DEG2GRA(ac_RAD2DEG(value))
    return answer

def ac_GRA2DEG(value):
    answer = value/400*360
    return answer

def ac_GRA2RAD(value):
    answer = ac_DEG2RAD(ac_GRA2DEG(value))
    return answer

def ac_SIN(value):
    if value >= 0:
        oy_side = 1
    else:
        oy_side = -1

    value_abs = abs(value)
    half_circle = 0
    while value_abs > 180:
        value_abs -= 180
        half_circle += 1

    if half_circle % 2 == 0:
        ox_side = 1
    else:
        ox_side = -1

    if value_abs > 90:
        value_abs = 180 - value_abs

    value_abs = ac_DEG2RAD(value_abs)

    answer_abs = value_abs - value_abs**3/ac_FACTORIAL(3) + value_abs**5/ac_FACTORIAL(5) - value_abs**7/ac_FACTORIAL(7) \
                 + value_abs**9/ac_FACTORIAL(9) - value_abs**11/ac_FACTORIAL(11) + value_abs**13/ac_FACTORIAL(13) \
                 - value_abs**15/ac_FACTORIAL(15) + value_abs**17/ac_FACTORIAL(17) - value_abs**19/ac_FACTORIAL(19)
    answer = answer_abs * oy_side * ox_side
    return answer

def ac_COS(value):
    value_2 = value + 90
    answer = ac_SIN(value_2)
    return answer

def ac_TAN(value):
    sinus = ac_SIN(value)
    cosinus = ac_COS(value)
    answer = sinus/cosinus
    return answer

def ac_COT(value):
    answer = 1/ac_TAN(value)
    return answer

def ac_CRD(value):
    answer = 2 * ac_SIN(value/2)
    return answer

def ac_ASIN(value):
    angle = 0
    if abs(value) > 1:
        angle = 1/0
    else:
        for i in range(20):
            angle_k = angle - ac_RAD2DEG((ac_SIN(angle)-value)/ac_COS(angle))
            angle = angle_k
    answer = angle
    return answer

def ac_ACOS(value):
    angle = 90 - ac_ASIN(value)
    print(angle)

def ac_ATAN(value):
    side = value * 0.7071067811865476
    side_norm = side / (side**2 + 0.5)**0.5
    answer = ac_ASIN(side_norm)
    return answer

def ac_ACOT(value):
    answer = 90 - ac_ATAN(value)
    return answer

def ac_ACRD(value):
    if value > 2:
        answer = 1/0
    else:
        answer = 2*ac_ASIN(value/2)
    return answer

def ac_LOGe(value):
    x = 1
    run = True
    if value <= 0:
        x = 1/0

    x1000 = 0
    while value > 1000:
        value = value/1000
        x1000 += 1

    while run == True:
        x_k = x - (ac_ex(x)-value)/ac_ex(x)
        x = x_k
        if ac_ex(x)-value < 0.0000000001:
            run = False
    answer = x + x1000*6.907755278982137
    return answer

def ac_LOG10(value):
    answer = ac_LOGe(value)/2.302585092994046
    return answer

def ac_LOGx(value, base):
    answer = ac_LOGe(value)/ac_LOGe(base)
    return answer

def ac_SINH(value):
    answer = (ac_ex(value)-ac_ex(-value))/2
    return answer

def ac_COSH(value):
    answer = (ac_ex(value)+ac_ex(-value))/2
    return answer

def ac_TANH(value):
    answer = ac_SINH(value)/ac_COSH(value)
    return answer

def ac_COTH(value):
    answer = 1/ac_TANH(value)
    return answer

def ac_ARSINH(value):
    answer = ac_LOGe(value + (value**2 + 1)**(-2))
    return answer

def ac_ARCOSH(value):
    answer = ac_LOGe(value + (value**2 - 1)**(-2))
    return answer

def ac_ARTANH(value):
    answer = 0.5*ac_LOGe((1+value)/(1-value))
    return answer

def ac_ARCOTH(value):
    answer = 0.5*ac_LOGe((value+1)/(value-1))
    return answer

# CALCULUS AND SOLVER
def ac_POW(value1, value2):
    answer = value1**value2
    return answer

def ac_ROOT(value1, value2):
    answer = value1**(1/value2)
    return answer

def string_to_numbers(input_string):
    # Substitute basic operations
    if input_string == "ADD":
        result = input_string.replace("ADD", "+")
        return result
    elif input_string == "SUB":
        result = input_string.replace("SUB", "-")
        return result
    elif input_string == "MUL":
        result = input_string.replace("MUL", "*")
        return result
    elif input_string == "DIV":
        result = input_string.replace("DIV", "/")
        return result
    elif input_string == "(":
        return input_string
    elif input_string == ")":
        return input_string

    # Define a regular expression to match the pattern
    factorial_pattern = r'ac_FACTORIAL\(([-+\d.]+)\)'
    pi_pattern = r'ac_xPI\(([-+\d.]+)\)'
    xe_pattern = r'ac_xe\(([-+\d.]+)\)'
    ex_pattern = r'ac_ex\(([-+\d.]+)\)'
    pow_pattern = r'ac_POW\(([-+\d.]+),([-+\d.]+)\)'
    root_pattern = r'ac_ROOT\(([-+\d.]+),([-+\d.]+)\)'
    rad2deg_pattern = r'ac_rad2deg\(([-+\d.]+)\)'
    deg2rad_pattern = r'ac_deg2rad\(([-+\d.]+)\)'
    deg2gra_pattern = r'ac_deg2gra\(([-+\d.]+)\)'
    rad2gra_pattern = r'ac_rad2gra\(([-+\d.]+)\)'
    gra2deg_pattern = r'ac_gra2deg\(([-+\d.]+)\)'
    gra2rad_pattern = r'ac_gra2rad\(([-+\d.]+)\)'
    sin_pattern = r'ac_SIN\(([-+\d.]+)\)'
    cos_pattern = r'ac_COS\(([-+\d.]+)\)'
    tan_pattern = r'ac_TAN\(([-+\d.]+)\)'
    cot_pattern = r'ac_COT\(([-+\d.]+)\)'
    asin_pattern = r'ac_ASIN\(([-+\d.]+)\)'
    acos_pattern = r'ac_ACOS\(([-+\d.]+)\)'
    atan_pattern = r'ac_ATAN\(([-+\d.]+)\)'
    acot_pattern = r'ac_ACOT\(([-+\d.]+)\)'
    crd_pattern = r'ac_CRD\(([-+\d.]+)\)'
    acrd_pattern = r'ac_ACRD\(([-+\d.]+)\)'
    loge_pattern = r'ac_LOGe\(([-+\d.]+)\)'
    log10_pattern = r'ac_LOG10\(([-+\d.]+)\)'
    logx_pattern = r'ac_LOGx\(([-+\d.]+),([-+\d.]+)\)'
    sinh_pattern = r'ac_SINH\(([-+\d.]+)\)'
    cosh_pattern = r'ac_COSH\(([-+\d.]+)\)'
    tanh_pattern = r'ac_TANH\(([-+\d.]+)\)'
    coth_pattern = r'ac_COTH\(([-+\d.]+)\)'
    arsinh_pattern = r'ac_ARSINH\(([-+\d.]+)\)'
    arcosh_pattern = r'ac_ARCOSH\(([-+\d.]+)\)'
    artanh_pattern = r'ac_ARTANH\(([-+\d.]+)\)'
    arcoth_pattern = r'ac_ARCOTH\(([-+\d.]+)\)'


    # Use regular expression to extract values from the input string
    factorial_match = re.match(factorial_pattern, input_string)
    pi_match = re.match(pi_pattern, input_string)
    xe_match = re.match(xe_pattern, input_string)
    ex_match = re.match(ex_pattern, input_string)
    pow_match = re.match(pow_pattern, input_string)
    root_match = re.match(root_pattern, input_string)
    rad2deg_match = re.match(rad2deg_pattern, input_string)
    deg2rad_match = re.match(deg2rad_pattern, input_string)
    deg2gra_match = re.match(deg2gra_pattern, input_string)
    rad2gra_match = re.match(rad2gra_pattern, input_string)
    gra2deg_match = re.match(gra2deg_pattern, input_string)
    gra2rad_match = re.match(gra2rad_pattern, input_string)
    sin_match = re.match(sin_pattern, input_string)
    cos_match = re.match(cos_pattern, input_string)
    tan_match = re.match(tan_pattern, input_string)
    cot_match = re.match(cot_pattern, input_string)
    asin_match = re.match(asin_pattern, input_string)
    acos_match = re.match(acos_pattern, input_string)
    atan_match = re.match(atan_pattern, input_string)
    acot_match = re.match(acot_pattern, input_string)
    crd_match = re.match(crd_pattern, input_string)
    acrd_match = re.match(acrd_pattern, input_string)
    loge_match = re.match(loge_pattern, input_string)
    log10_match = re.match(log10_pattern, input_string)
    logx_match = re.match(logx_pattern, input_string)


    sinh_match = re.match(sinh_pattern, input_string)
    cosh_match = re.match(cosh_pattern, input_string)
    tanh_match = re.match(tanh_pattern, input_string)
    coth_match = re.match(coth_pattern, input_string)
    arsinh_match = re.match(arsinh_pattern, input_string)
    arcosh_match = re.match(arcosh_pattern, input_string)
    artanh_match = re.match(artanh_pattern, input_string)
    arcoth_match = re.match(arcoth_pattern, input_string)


    if factorial_match:
        factorial_value = float(factorial_match.group(1))
        function_name = 'ac_FACTORIAL'
        result = globals()[function_name](factorial_value)
        return result

    elif pi_match:
        pi_value = float(pi_match.group(1))
        function_name = 'ac_xPI'
        result = globals()[function_name](pi_value)
        return result

    elif xe_match:
        xe_value = float(xe_match.group(1))
        function_name = 'ac_xe'
        result = globals()[function_name](xe_value)
        return result

    elif ex_match:
        ex_value = float(ex_match.group(1))
        function_name = 'ac_ex'
        result = globals()[function_name](ex_value)
        return result

    elif pow_match:
        x_value = float(pow_match.group(1))
        exponent_value = float(pow_match.group(2))
        function_name = 'ac_POW'
        result = globals()[function_name](x_value, exponent_value)
        return result

    elif root_match:
        x_value = float(root_match.group(1))
        exponent_value = float(root_match.group(2))
        function_name = 'ac_ROOT'
        result = globals()[function_name](x_value, exponent_value)
        return result

    elif rad2deg_match:
        rad2deg_value = float(rad2deg_match.group(1))
        function_name = 'ac_RAD2DEG'
        result = globals()[function_name](rad2deg_value)
        return result

    elif deg2rad_match:
        deg2rad_value = float(deg2rad_match.group(1))
        function_name = 'ac_DEG2RAD'
        result = globals()[function_name](deg2rad_value)
        return result

    elif deg2gra_match:
        deg2gra_value = float(deg2gra_match.group(1))
        function_name = 'ac_DEG2GRA'
        result = globals()[function_name](deg2gra_value)
        return result

    elif rad2gra_match:
        rad2gra_value = float(rad2gra_match.group(1))
        function_name = 'ac_RAD2GRA'
        result = globals()[function_name](rad2gra_value)
        return result

    elif gra2deg_match:
        gra2deg_value = float(gra2deg_match.group(1))
        function_name = 'ac_GRA2DEG'
        result = globals()[function_name](gra2deg_value)
        return result

    elif gra2rad_match:
        gra2rad_value = float(gra2rad_match.group(1))
        function_name = 'ac_GRA2RAD'
        result = globals()[function_name](gra2rad_value)
        return result

    elif sin_match:
        sin_value = float(sin_match.group(1))
        function_name = 'ac_SIN'
        result = globals()[function_name](sin_value)
        return result

    elif cos_match:
        cos_value = float(cos_match.group(1))
        function_name = 'ac_COS'
        result = globals()[function_name](cos_value)
        return result

    elif tan_match:
        tan_value = float(tan_match.group(1))
        function_name = 'ac_TAN'
        result = globals()[function_name](tan_value)
        return result

    elif cot_match:
        cot_value = float(cot_match.group(1))
        function_name = 'ac_COT'
        result = globals()[function_name](cot_value)
        return result

    elif asin_match:
        asin_value = float(asin_match.group(1))
        function_name = 'ac_ASIN'
        result = globals()[function_name](asin_value)
        return result

    elif acos_match:
        acos_value = float(acos_match.group(1))
        function_name = 'ac_ACOS'
        result = globals()[function_name](acos_value)
        return result

    elif atan_match:
        atan_value = float(atan_match.group(1))
        function_name = 'ac_ATAN'
        result = globals()[function_name](atan_value)
        return result

    elif acot_match:
        acot_value = float(acot_match.group(1))
        function_name = 'ac_ACOT'
        result = globals()[function_name](acot_value)
        return result

    elif crd_match:
        crd_value = float(crd_match.group(1))
        function_name = 'ac_CRD'
        result = globals()[function_name](crd_value)
        return result

    elif acrd_match:
        acrd_value = float(acrd_match.group(1))
        function_name = 'ac_ACRD'
        result = globals()[function_name](acrd_value)
        return result

    elif loge_match:
        loge_value = float(loge_match.group(1))
        function_name = 'ac_LOGe'
        result = globals()[function_name](loge_value)
        return result

    elif log10_match:
        log10_value = float(log10_match.group(1))
        function_name = 'ac_LOG10'
        result = globals()[function_name](log10_value)
        return result

    elif logx_match:
        x_value = float(logx_match.group(1))
        base_value = float(logx_match.group(2))
        function_name = 'ac_LOGx'
        result = globals()[function_name](x_value, base_value)
        return result

    elif sinh_match:
        sinh_value = float(sinh_match.group(1))
        function_name = 'ac_SINH'
        result = globals()[function_name](sinh_value)
        return result

    elif cosh_match:
        cosh_value = float(cosh_match.group(1))
        function_name = 'ac_COSH'
        result = globals()[function_name](cosh_value)
        return result

    elif tanh_match:
        tanh_value = float(tanh_match.group(1))
        function_name = 'ac_TANH'
        result = globals()[function_name](tanh_value)
        return result

    elif coth_match:
        coth_value = float(coth_match.group(1))
        function_name = 'ac_COTH'
        result = globals()[function_name](coth_value)
        return result

    elif arsinh_match:
        arsinh_value = float(arsinh_match.group(1))
        function_name = 'ac_ARSINH'
        result = globals()[function_name](arsinh_value)
        return result

    elif arcosh_match:
        arcosh_value = float(arcosh_match.group(1))
        function_name = 'ac_ARCOSH'
        result = globals()[function_name](arcosh_value)
        return result

    elif artanh_match:
        artanh_value = float(artanh_match.group(1))
        function_name = 'ac_ARTANH'
        result = globals()[function_name](artanh_value)
        return result

    elif arcoth_match:
        arcoth_value = float(arcoth_match.group(1))
        function_name = 'ac_ARCOTH'
        result = globals()[function_name](arcoth_value)
        return result

    # Return numbers
    number_pattern = re.compile(r'[+-]?\d*\.?\d+')
    matches = number_pattern.findall(input_string)
    if matches:
        numbers = [int(match) if '.' not in match else float(match)
               for match in matches]
        return numbers[0]

    else:
        return "Invalid input format"

def ac_CALC(number, function_string):
    function_number = function_string.replace("X", str(number))
    terms = function_number.split(";")
    values = []
    for i in range(len(terms)):
        value = string_to_numbers(terms[i])
        values.append(value)
        i += 1
    math_operation = ''.join(map(str, values))
    result = eval(math_operation)
    return result

def ac_eDIFF(number, function):
    h = 0.000005

    x1 = number + h
    y1 = ac_CALC(x1, function)

    x2 = number - h
    y2 = ac_CALC(x2, function)

    diff = (y1-y2)/(2*h)
    return diff

##################################################################
def alfacentrum(command,main_text,var,last_var,set_var,set_index_var,code,location1,set_logical,end_logical):
    """
    Here you can add additional commands
    [input]
    command - name of command e.g. 'ADD' 5;
    main_text - value of command e.g. ADD '5';
    var - returns the entire list of variables;
    last_var - it is a list of data that will be displayed on output;
    set_var - returns selected variable;
    set_index_var - returns the location of the variable data;
    """

    if (command == 'ac_FACTORIAL'):
        location = var.index(main_text)
        try:
            var[set_index_var + 1]
        except IndexError:
            var.append(int(0))
        var[set_index_var + 1] = ac_FACTORIAL(int(var[location + 1]))

    elif(command == 'ac_xPI'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_xPI(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_xPI(float(var[location + 1]))

    elif(command == 'ac_xe'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_xe(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_xe(float(var[location + 1]))

    elif(command == 'ac_ex'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ex(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ex(float(var[location + 1]))

    elif(command == 'ac_DEG2RAD'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_DEG2RAD(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_DEG2RAD(float(var[location + 1]))

    elif(command == 'ac_RAD2DEG'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_RAD2DEG(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_RAD2DEG(float(var[location + 1]))

    elif(command == 'ac_DEG2GRA'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_DEG2GRA(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_DEG2GRA(float(var[location + 1]))

    elif(command == 'ac_RAD2GRA'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_RAD2GRA(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_RAD2GRA(float(var[location + 1]))

    elif(command == 'ac_GRA2DEG'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_GRA2DEG(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_GRA2DEG(float(var[location + 1]))

    elif(command == 'ac_GRA2RAD'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_GRA2RAD(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_GRA2RAD(float(var[location + 1]))

    elif(command == 'ac_SIN'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_SIN(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_SIN(float(var[location + 1]))

    elif(command == 'ac_COS'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_COS(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_COS(float(var[location + 1]))

    elif(command == 'ac_TAN'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_TAN(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_TAN(float(var[location + 1]))

    elif(command == 'ac_COT'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_COT(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_COT(float(var[location + 1]))

    elif(command == 'ac_CRD'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_CRD(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_CRD(float(var[location + 1]))

    elif(command == 'ac_ASIN'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ASIN(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ASIN(float(var[location + 1]))

    elif(command == 'ac_ACOS'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ACOS(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ACOS(float(var[location + 1]))

    elif(command == 'ac_ATAN'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ATAN(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ATAN(float(var[location + 1]))

    elif(command == 'ac_ACOT'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ACOT(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ACOT(float(var[location + 1]))

    elif(command == 'ac_ACRD'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ACRD(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ACRD(float(var[location + 1]))

    elif(command == 'ac_LOGe'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_LOGe(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_LOGe(float(var[location + 1]))

    elif(command == 'ac_LOG10'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_LOG10(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_LOG10(float(var[location + 1]))

    elif(command == 'ac_POW'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] ** int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] ** float(main_text))

    elif(command == 'ac_ROOT'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] ** (1/int(main_text)))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] ** (1/float(main_text)))

    elif(command == 'ac_LOGx'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = ac_LOGx(var[set_index_var+1], int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = ac_LOGx(var[set_index_var+1], float(main_text))

    elif(command == 'ac_SINH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_SINH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_SINH(float(var[location + 1]))

    elif(command == 'ac_COSH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_COSH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_COSH(float(var[location + 1]))

    elif(command == 'ac_TANH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_TANH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_TANH(float(var[location + 1]))

    elif(command == 'ac_COTH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_COTH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_COTH(float(var[location + 1]))

    elif(command == 'ac_ARSINH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ARSINH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ARSINH(float(var[location + 1]))

    elif(command == 'ac_ARCOSH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ARCOSH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ARCOSH(float(var[location + 1]))

    elif(command == 'ac_ARTANH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ARTANH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ARTANH(float(var[location + 1]))

    elif(command == 'ac_ARCOTH'):
        location = var.index(main_text)
        end = True
        try:
            var[set_index_var + 1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var + 1] = ac_ARCOTH(int(var[location + 1]))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var + 1] = ac_ARCOTH(float(var[location + 1]))



    ##############################################################
    elif(command == 'ac_eDIFF'):
        main_text = str(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type("A")):
                var.append(int(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = ac_eDIFF(var[set_index_var+1], str(main_text))
            elif (type(var[set_index_var + 1]) == type(0.0)):
                var[set_index_var + 1] = ac_eDIFF(var[set_index_var+1], str(main_text))

    elif(command == 'ac_CALC'):
        main_text = str(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type("A")):
                var.append(int(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = ac_CALC(var[set_index_var+1], str(main_text))
            elif (type(var[set_index_var + 1]) == type(0.0)):
                var[set_index_var + 1] = ac_CALC(var[set_index_var+1], str(main_text))



    ##############################################################
    elif(command == "ac_LOGO"):
        last_var.append(acl_line1)
        last_var.append(acl_line2)
        last_var.append(acl_line3)
        last_var.append(acl_line4)
        last_var.append(acl_line5)
        last_var.append(acl_line6)
        last_var.append(spl_line)
        last_var.append(acv_line1)
        last_var.append(acv_line2)
        last_var.append(acv_line3)
        last_var.append(spl_line)
        last_var.append(spl_line)
        last_var.append(hcl_line1)
        last_var.append(hcl_line2)
        last_var.append(hcl_line3)
        last_var.append(hcl_line4)
        last_var.append(hcl_line5)
        last_var.append(hcl_line6)
        last_var.append(hcl_line7)
        last_var.append(hcl_line8)
        last_var.append(hcl_line9)
        last_var.append(hcl_line10)
        last_var.append(hcl_line11)




    return var,last_var,set_var,set_index_var,code,location1,set_logical,end_logical

def empty():
    empty = False #change this to False if you want to use plugin
    return empty