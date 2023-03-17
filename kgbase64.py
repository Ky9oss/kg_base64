import sys
import argparse
import base64
import textwrap








#将输入的文件转化为base64,并返回base64编码
def file_to_base64(filename):
    with open(filename, 'r') as t:
        myread = t.read()
        if myread:
            # base64是用64个字符表示二进制
            mybase64 = base64.b64encode(myread.encode('utf-8'))
        else:
            print('错误！文件中没有数据！')

            #print(base64.b64decode(mybase64).decode('utf-8'))
            sys.exit()
        return mybase64.decode() #去掉b' '
    #with open("test.txt", 'r') as t:
    #    myreadline = t.readline() #只读一行
    #with open("test.txt", 'r') as t:
    #    myreadlines = t.readlines() #读所有行放进了list

#将输入的字符串转化为base64,并返回base64编码
def string_to_base64(input_str):
    mybase64 = base64.b64encode(input_str.encode('utf-8'))
    return mybase64.decode()

def output_shell(mybase64):
    print(mybase64)

def output_file(mybase64, filename):
    with open(filename, 'w') as t:
        t.write(mybase64)


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
        if myargs.string:
            if not myargs.quite:
                print('[ToT] 不能同时选择-s和-fi！')
            sys.exit()
        mybase64 = file_to_base64(myargs.fileInput)
        if not mybase64:
            if not myargs.quite:
                print("[ToT] 文件为空或文件不存在！")
            sys.exit()
    elif myargs.string:
        try:
            mybase64 = string_to_base64(myargs.string)
        except Exception as e:
            if not myargs.quite:
                print(f"[ToT] {e}")
            sys.exit()
    else:
        if not myargs.quite:
            print('[ToT] 请选择-s或-fi参数来指定您要编码的内容，使用-h选项已获取更多信息')
        sys.exit()


    if myargs.fileOutput:
        output_file(mybase64, myargs.fileOutput)
        if not myargs.quite:
            print(f"[^_^] base64编码已写入{myargs.fileOutput}")

    if not myargs.quite:
        output_shell(mybase64)





if __name__ == '__main__':
        #使用argparse库
        myparser = argparse.ArgumentParser(
        prog='kgbase64', 
        description='This is a simple base64-encoding tool :)', 
        formatter_class=argparse.RawDescriptionHelpFormatter, #表示description和epilog不需要自动换行
        epilog=textwrap.dedent( #textwrap.dedent表示自动将多行字符串的前面的空白补齐
        '''
        examples:
          python kgbase64.py -s lalala
          python kgbase64 -fi target.txt -fo base64.txt -q
        '''
        ))
        
        myparser.add_argument('-s', "--string", help="input a string and encode it with base64")
        myparser.add_argument('-fi', "--fileInput", help="input a file and encode it with base64")
        myparser.add_argument('-fo', "--fileOutput", help="output base64 codes in a file ")
        myparser.add_argument('-q', "--quite", action="store_true", help="no output in shell")
        myargs = myparser.parse_args()

        main(myargs)


