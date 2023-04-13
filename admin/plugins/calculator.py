



'''
name = models.CharField(max_length = 150, null=True, verbose_name='Title')
service = models.ForeignKey(to="settings.Service", on_delete=models.CASCADE, null=True)
up = models.IntegerField(default=0, verbose_name='unit price')
ebb =  models.IntegerField(default=0, verbose_name='Extra bedroom unit Price')
efb =  models.IntegerField(default=0, verbose_name='Extra floor bill')
nb =  models.IntegerField(default=0, verbose_name='Number of bedroom')
nf =  models.IntegerField(default=0, verbose_name='Number of floor')
mncb =  models.IntegerField(default=0, verbose_name='Maximum number of category bedroom')
mncf =  models.IntegerField(default=0, verbose_name='Maximum number of category floor')
total = models.IntegerField(default=0)
'''

def function1(data=dict):
    total = 0
    for x in data.values():
        total =  total + int(x)
    return total


def general_engine_calc(data=dict):
    try:
        total = 0
        up = data.get('up') # unit price
        ebb = data.get('ebb') # extra bedroom unit
        nb = data.get('nb') # number of bedroom
        efb = data.get('efb') # extra floor bill
        nf = data.get('nf') # number of floor
        mncb = data.get('mncb') # maximum number of category bedroom
        mncf = data.get('mncf') # maximum number of category floor

        mncs = data.get('mncs') # maximum number of category sitting room
        ns = data.get('ns') # number of sitting room
        esrup = data.get('esrup') # extra sitting room unit price
        
        if (nb <= mncb) and (nf <= mncf) and (ns <= mncs):
            total = up
        else:
            res1 = (nb - mncb) * ebb
            res2 = (nf - mncf) * efb
            res3 = (ns - mncs) * esrup
            total =  res1 + res2 + res3 + up
            # print(total, res1, res2)
        return abs(total)
        
    except:
        # if error occurs
        return 0


