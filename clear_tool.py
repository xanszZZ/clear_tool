import argparse
import os
import textwrap

def main(sys,ip,path):
    if sys == 'l':
        os.system(f"sed -i '/{ip}/d' /var/log/{path}")
        print(f"Linux{path}日志清理完成")
    if sys == 'w' and path:
        os.system(f'findstr /v {ip} {path}.log > {path}_new.log')
        os.system('net stop w3svc')
        os.system(f'del {path}.log')
        os.system(f'rename {path}_new.log {path}.log')
        os.system('net start w3svc')
        print("iis日志清理完成")
    else:
        os.system(f'findstr /v {ip} access.log > access_new.log')
        os.system('del access.log')
        os.system('rename access_new.log access.log')
        os.system(f'findstr /v {ip} error.log > error_new.log')
        os.system('del error.log')
        os.system('rename error_new.log error.log')
        print("apache日志清理完成")


if __name__ == '__main__':
    banner = """ 
         _____   _       _____       ___   _____   
        /  ___| | |     | ____|     /   | |  _  \  
        | |     | |     | |__      / /| | | |_| |  
        | |     | |     |  __|    / / | | |  _  /  
        | |___  | |___  | |___   / /  | | | | \ \  
        \_____| |_____| |_____| /_/   |_| |_|  \_\ 
                                                version: 0.0.1
                                                author:  xans
    """
    print(banner)
    # 使用argparse去解析命令行传来的参数
    parser = argparse.ArgumentParser(description="clear tool",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
        python3 clear.py -s w -u 192.168.1.108 
        '''))
    # 添加参数
    parser.add_argument("-s", "--sys", dest="sys", type=str, help="input a system")
    parser.add_argument("-u", "--ip", dest="ip", type=str, help="input a ip")
    parser.add_argument("-p", "--path", dest="path", type=str, help="input a path")
    # 把参数的值解析到对象中
    args = parser.parse_args()

    main(args.sys,args.ip,args.path)