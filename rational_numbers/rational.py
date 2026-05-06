class Rational:
    #Создание объекта класса   
    def create(numer, denom):
        try:
            if not all([type(k)==int for k in [numer, denom]]): raise TypeError
            elif denom == 0: raise ZeroDivisionError
            elif numer == 0:
                result = Rational()
                result.num = 0
                result.den = 1
                return result
            
            [ab_num, ab_den] = [abs(numer), abs(denom)]
            [base, div] = [max([ab_num, ab_den]), min([ab_num, ab_den])]
            while base%div !=0:
                base, div = div, base%div
            result, sign = Rational(), int((numer/abs(numer))*(denom/abs(denom)))
            result.num = sign*int(ab_num/div)
            result.den = abs(int(ab_den/div))
            return result
        except TypeError: print("ERROR: create() must have integer only")
        except ZeroDivisionError: print("ERROR: denominator shouldn't be zero")
    
    #Деконструкция обекта класса
    try:
        def to_int(rational):
            if not type(rational) == Rational: raise TypeError
            return rational.num // rational.den
        
        def to_float(rational):
            if not type(rational) == Rational: raise TypeError 
            return rational.num / rational.den
        
        def to_list(rational):
            if not type(rational) == Rational: raise TypeError
            return [rational.num, rational.den]
        
    #Арифметические операции + сравнение (добавить сокращение дробей!!!)

        def add(a, b):
            if not all([type(k) == Rational for k in [a, b]]): raise TypeError
            return Rational.create(a.num*b.den + b.num*a.den, a.den*b.den)
        
        def sub(a, b):
            if not all([type(k) == Rational for k in [a, b]]): raise TypeError
            return Rational.create(a.num*b.den - b.num*a.den, a.den*b.den)
        
        def mul(a, b):
            if not all([type(k) == Rational for k in [a, b]]): raise TypeError
            return Rational.create(a.num*b.num, a.den*b.den)
        
        def div(a, b):
            if not all([type(k) == Rational for k in [a, b]]): raise TypeError
            return Rational.create(a.num*b.den, a.den*b.num)
        
        def compare(a, b):
            result = a.num*b.den - b.num*a.den
            return result/abs(result) if result != 0 else 0
    
    except TypeError: print("ERROR: must have rational only")       

    #Алгербаические операции
    def power(r, power):
        try:
            if not [type(k) for k in [r, power]] == [Rational, int]: raise TypeError
            if power>=0: return Rational.create(r.num**power, r.den**power)
            else: return Rational.create(r.den**-power, r.num**-power)
        except TypeError: print("ERROR: must have rational as base and integer as exponent")