import sys
from LOPInfer import LOPInfer

if __name__ == '__main__':
    ip = "192.168.50.11"
    port = 12345
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    if len(sys.argv) > 3:
        bandwidth_file_path = str(sys.argv[3])
    else:
        bandwidth_file_path = None
    LOPInf = LOPInfer(parallel_approach="select",
                                         ip=ip, port=port)
    LOPInf.start_server(bandwidth_file_path=bandwidth_file_path)
