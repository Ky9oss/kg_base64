import sys
import argparse
import base64
import textwrap








#将输入的文件转化为base64,并返回base64编码
def base64_to_file(filename):
    with open(filename, 'r') as t:
        myread = t.read()
        if myread:
            # base64是用64个字符表示二进制
            mystring = base64.b64decode(myread).decode('utf-8')        
        else:
            print('错误！文件中没有数据！')

            #print(base64.b64decode(mystring).decode('utf-8'))
            sys.exit()
        return mystring
    #with open("test.txt", 'r') as t:
    #    myreadline = t.readline() #只读一行
    #with open("test.txt", 'r') as t:
    #    myreadlines = t.readlines() #读所有行放进了list


def output_shell(mystring):
    print(mystring)

def output_file(mystring, filename):
    with open(filename, 'w') as t:
        t.write(mystring)


def main(myargs):


    if not myargs.quite:
        print(textwrap.dedent(
        '''

        ██╗  ██╗██╗   ██╗ ██████╗  ██████╗ ███████╗███████╗
        ██║ ██╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗██╔════╝██╔════╝
        █████╔╝  ╚████╔╝ ██║  ███╗██║   ██║███████╗███████╗
        ██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║╚════██║╚════██║
        ██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████║███████║
        ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                                                      
        '''))

    if myargs.fileInput:
        mystring = base64_to_file(myargs.fileInput)
        if not mystring:
            if not myargs.quite:
                print("[ToT] 文件为空或文件不存在！")
            sys.exit()
    else:
        if not myargs.quite:
            print('[ToT] 请选择-fi参数来指定您要编码的内容，使用-h选项已获取更多信息')
        sys.exit()


    if myargs.fileOutput:
        output_file(mystring, myargs.fileOutput)
        if not myargs.quite:
            print(f"[^_^] base64编码已写入{myargs.fileOutput}")

    if not myargs.quite:
        output_shell(mystring)





if __name__ == '__main__':
        #使用argparse库
        myparser = argparse.ArgumentParser(
        prog='kgdecode64', 
        description='This is a simple base64-decoding tool :)', 
        formatter_class=argparse.RawDescriptionHelpFormatter, #表示description和epilog不需要自动换行
        epilog=textwrap.dedent( #textwrap.dedent表示自动将多行字符串的前面的空白补齐
        '''
        examples:
          python kgdecode64 -fi target.txt -fo base64.txt -q
        '''
        ))
        
        myparser.add_argument('-fi', "--fileInput", help="input a file and decode it with base64")
        myparser.add_argument('-fo', "--fileOutput", help="output string in a file ")
        myparser.add_argument('-q', "--quite", action="store_true", help="no output in shell")
        myargs = myparser.parse_args()

        main(myargs)


