import copy
import psutil
import time
import threading
from queue import Queue
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


queue = Queue()
CPU_COUNT = psutil.cpu_count()


def get_cpu_usage():
    while True:
        if queue.empty():
            queue.put(psutil.cpu_percent(percpu=True))
        time.sleep(0.050)


def create_datagram():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    initial = [i for i in range(1, CPU_COUNT+1)]
    bars = plt.bar(initial, 100, facecolor='green', alpha=0.75)

    def animate(frame):
        local_data = queue.get()
        for i in range(CPU_COUNT):
            bars[i].set_height(local_data[i])

    ani = FuncAnimation(fig, animate, frames=CPU_COUNT, interval=60)
    plt.show()


if __name__ == '__main__':
    queue.put(psutil.cpu_percent(percpu=True))
    t1 = threading.Thread(target=get_cpu_usage)
    t2 = threading.Thread(target=create_datagram)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("END")
