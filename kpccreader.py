import os
def get(stra):
    stra = str(stra)
    return os.path.splitext(stra)
def gets(stra):
    return tuple(str(stra).split("."))
def startwith(str, startwith):
    return bool(gets(str)[0] == startwith)
def endwith(endint, str, endwith):
    return bool(gets(str)[endint] == endwith)
class Code(list):
    code = []
    def convert_ftl(t):
        code = []
        with open(t, "r") as f:
            ret = f.read()
        for line in ret:
            code.append(line)
    def run(lines):
        varname = []
        varval = []
        code = []
        loop = 0
        for line in lines:
            
            loop += 1
            if os.path.splitext(f"{line}")[0] == "print":
                print(os.path.splitext(f"{line}")[1])
            elif get(f"{line}")[0] == "in":
                il = input()
                varname.append(get(line)[1])
                varval.append(il)
            elif get(f"{line}")[0] == "printv":
                if not varname.count(get(f"{line}")[1]) == 0:
                    do = varname.index(get(f"{line}")[1])
                    print(varval[do])
            elif gets(line)[0]  == "ifvrev":                       
                if not varname.count(gets(line)[1]) == 0:
                    kaki = varval[varname.index(get(line)[1])]
                    if kaki == gets(line)[2]:
                        varname.append(gets(line)[3])
                        varval.append(True)
                    else:
                        varname.append(gets(line)[3])
                        varval.append(False)
            elif gets(line)[0] == "error":
                print(f"{gets(line)[1]} error: {gets(line)[2]}")
                break
                        # elif get(line)[0] == "rmvar":
            #     if varname.index(get(line)[1]) != 0:
            #         varval.pop(varname.index(get(line)[1]))
            #         varname.pop(varname.index(get(line)[1]))
            
            elif startwith(line, "avar"):
                if varname.count(gets(line)[1]) != 0:
                    if varname.count(gets(line)[2]) != 0:
                        done = float(float(varval[varname.index(gets(line)[1])]) + float(varval[varname.index(gets(line)[2])]))
                        varname.append(gets(line)[3])
                        varval.append(done)
                        
            else:
                print("Unrecognized command:",line, "at line/occurrence", loop)
                break
            
code =['print.Pur Adder', 'print.What do you want to add first?', 'in.one', 'print.Add with?', 'in.two', 'avar.one.two.done', 'printv.done']
Code.run(code)