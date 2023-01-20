import kernel_bridge
import sys
args = get_args()
for arg in args:
    sys.argv.append(arg)

_kernelObj = None

def XlangOutput(info):
    if _kernelObj != None:
        _kernelObj.send_stdout(info)
code_module = new_module()
code_module.setprimitive("Output",XlangOutput)

def do_execute(kernelObj,code,silent,store_history,
    user_expressions,allow_stdin):
    global _kernelObj
    _kernelObj = kernelObj
    retVal = code_module.runfragment(code)
kernel_bridge.Run(do_execute)

