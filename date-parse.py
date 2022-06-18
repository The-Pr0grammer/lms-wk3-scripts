import sys
import datetime
f = open('./apache_access', 'rb')
o = open('./dp_output.txt', 'wb')

arg_format='%Y-%m-%d %H:%M:%S'
start=datetime.datetime.strptime(sys.argv[1],arg_format)
end=datetime.datetime.strptime(sys.argv[2],arg_format)

def parse_dates(s, e):
        with open("./apache_access") as apache_file:
                for line in apache_file:
                        input=line.split()[3][1:];
                        l_format='%d/%b/%Y:%H:%M:%S';
                        i_f=datetime.datetime.strptime(input,l_format);
                        if i_f > start and i_f < end:
                                print(line)

        f.close()
        o.close()

parse_dates(start,end)