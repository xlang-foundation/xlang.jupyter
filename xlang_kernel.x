import sys
args = get_args()
for arg in args:
    sys.argv.append(arg)
def do_execute(code,silent,store_history,user_expressions,allow_stdin):
    print("xlang,do_execute,code:",code)
import kernel_bridge
kernel_bridge.Run(do_execute)

