def queryFormat(param={}):
    if len(param) > 0:
        str =  ""
        for x in param:
            str += f"{x}={param.get(x)}&"
            filtered =  str.rstrip('&')
        return filtered
    else:
        return ''