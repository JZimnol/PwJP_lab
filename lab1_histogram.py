import copy
import psutil
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


lock = threading.Lock()
datagram_data = psutil.cpu_percent(percpu=True)


def get_cpu_usage():
    global datagram_data
    while True:
        lock.acquire()
        datagram_data = psutil.cpu_percent(percpu=True)
        lock.release()
        time.sleep(0.200)


def create_datagram():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    initial = [i for i in range(1, psutil.cpu_count()+1)]
    bars = plt.bar(initial, 100, facecolor='green', alpha=0.75)

    def animate(frame):
        lock.acquire()
        local_data = copy.copy(datagram_data)
        lock.release()
        bars[frame].set_height(local_data[frame])

    ani = FuncAnimation(fig, animate, frames=psutil.cpu_count(), interval=10)
    plt.show()


if __name__ == '__main__':
    t1 = threading.Thread(target=get_cpu_usage)
    t2 = threading.Thread(target=create_datagram)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("END")
