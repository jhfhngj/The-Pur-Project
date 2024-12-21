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
        endline = 0
        loopstart = 0
        i = 0
        while i < len(lines):
            line = lines[i]
            loop += 1
            loopm = False
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
            elif startwith(line, "while"):
                loopm = True
                loopstart = i
                if get(line)[1] == False:
                    loopm = False
                    i = endline
            elif startwith(line, "end"):
                if loopm = False:
                    continue
                if loopm = True:
                    i = loopstart
            else:
                print("Unrecognized command:",line, "at line/occurrence", loop)
                break
            
