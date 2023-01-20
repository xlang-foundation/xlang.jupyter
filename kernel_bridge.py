from ipykernel.kernelbase import Kernel

g_cb_from_xlang = None

class KernelObj:
    _kernel = None
    def __init__(self,k):
        self._kernel = k 
    def send_stdout(self,outputInfo):
        stream_content = {'name': 'stdout', 'text': outputInfo}
        self._kernel.send_response(
            self._kernel.iopub_socket,
            'stream',stream_content)
    def send_response(self,msg_type,content):
        self._kernel.send_response(
        self._kernel.iopub_socket,
            msg_type,content)

class Xlang_Kernel(Kernel):
    implementation = 'xlang'
    implementation_version = '0.1'
    language = 'python'  # will be used for
                         # syntax highlighting
    language_version = '1.0'
    language_info = {'name': 'xlang',
                     'mimetype': 'text/plain',
                     'extension': '.x'}
    banner = "xlang interactive"
    kernelObj = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kernelObj = KernelObj(self)
    def do_execute(self, code, silent,
                    store_history=True,
                    user_expressions=None,
                    allow_stdin=False):
            g_cb_from_xlang(self.kernelObj,
                            code,silent,
                            store_history,
                            user_expressions,
                            allow_stdin)
            # We return the exection results.
            return {'status': 'ok',
                    'execution_count':
                        self.execution_count,
                    'payload': [],
                    'user_expressions': {},
                }

def Run(cb_in_xlang):
    global g_cb_from_xlang
    g_cb_from_xlang = cb_in_xlang
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(
        kernel_class=Xlang_Kernel)
