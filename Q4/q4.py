import csv
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


if __name__ == "__main__":

    f = open('q4.csv', encoding='utf-8')
    data = csv.reader(f)


    riding = []
    quit = []
    riding_quit = []
    r = []
    q = []
    rq = []
    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])
        riding.append(row[4]+row[6])
        quit.append(row[5]+row[7])
        riding_quit.append(row[4]+row[5]+row[6]+row[7])
        r.append(row[3])
        q.append(row[3])
        rq.append(row[3])
        
    riding2 = riding.copy()
    quit2 = quit.copy()
    riding_quit2 = riding_quit.copy()
    riding.sort()
    quit.sort()
    riding_quit.sort()
    riding_quit.reverse()
    riding.reverse()
    quit.reverse()
    
    subway_r = []
    subway_q = []
    subway_rq = []
    r2 = []
    q2 = []
    rq2 = []

    plt.subplot(1,3,1)
    for i in range(0,30):
        idx = riding2.index(riding[i])
        subway_r.append(riding2[idx])
        r2.append(r[idx])
    plt.title('출근시간 승차한 승객 수')
    plt.xlabel('정거장')
    plt.ylabel('사용자 수(명)')
    plt.xticks(rotation=90,fontsize=5)
    plt.bar(r2, subway_r)

    plt.subplot(1,3,2)
    for i in range(0,30):
        idx = quit2.index(quit[i])
        subway_q.append(quit2[idx])
        q2.append(q[idx])
    plt.title('출근시간 하차한 승객 수')
    plt.xlabel('정거장')
    plt.xticks(rotation=90, fontsize=5)
    plt.bar(q2, subway_q)

    plt.subplot(1,3,3)
    for i in range(0,30):
        idx = riding_quit2.index(riding_quit[i])
        subway_rq.append(riding_quit2[idx])
        rq2.append(rq[idx])
    plt.title('출근시간 승하차한 승객 ')
    plt.xlabel('정거장')
    plt.xticks(rotation=90, fontsize=5)
    plt.bar(rq2, subway_rq)

    plt.show()
    
        


            
