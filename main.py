#托卵発見時、解の比較行わない、解の移動距離mはレヴィフライト(1 <= m < machins / 2 + 1)
#托卵発見率0.1%

import initialization
import current_genetation
import update
import fitness
import egg
import matplotlib.pyplot as plt
import numpy as np
import time

starting_population_size = 100
number_of_generations =100
num = 1


def start_all(type, egg_rate):
    np.set_printoptions(threshold=np.inf)

    global starting_population_size
    global number_of_generations

    answer_best = []
    answer_worst = []
    answer_ave = []
    best = []
    worst = []
    ave = []
    finish = []
    finish_list = []
    best_list = []

    for j in range(num):

        all_data = current_genetation.SavedData()
        curr_gen = current_genetation.CurrentGeneration()

        machines = 0
        x = 0
        y = 0
        json_cost_name = type + '_cost.json'
        json_flow_name = type + '_flow.json'

        if type == 'easy':
            machines = 9
            x = 3
            y = 3

        if type == 'flat':
            machines = 12
            x = 1
            y = 12

        if type == 'hard':
            machines = 24
            x = 5
            y = 6

    
        curr_gen = initialization.start(json_cost_name, json_flow_name, machines, x, y, curr_gen)

        all_data.save_curr_gen_data(initialization.init_best, initialization.init_worst, initialization.init_ave)

        temp_best = initialization.init_best
        temp_finish = 0
        best_list.append(temp_best)

        for i in range(number_of_generations):
            #print(i)

            #解の更新
            curr_gen = update.switch_R(x, y, curr_gen, machines)

            curr_gen = fitness.judge_curr_gen(machines, x, y, curr_gen)

            #托卵の処理
            curr_gen = egg.switch(machines, x, y, curr_gen, egg_rate)

            curr_gen = fitness.judge_curr_gen(machines, x, y, curr_gen)

            all_data.save_curr_gen_data(curr_gen.best(), curr_gen.worst(), curr_gen.ave())
            #print(curr_gen.best())
            #print(curr_gen.worst())
            #print(curr_gen.ave())
            if curr_gen.best() < temp_best:
                temp_finish = i + 1
                temp_best = curr_gen.best()
                finish_list.append(temp_finish)
                best_list.append(temp_best)
            #if i == number_of_generations / 2:
                #print('half')

        print("egg_count : " + str(egg.egg_count))
        print(j)
        if j == 0:
            best = all_data.bests[0:number_of_generations + 1].copy()
            worst = all_data.worsts[0:number_of_generations + 1].copy()
            ave = all_data.averages[0:number_of_generations + 1].copy()
        else:
            for i in range(number_of_generations + 1):
                best[i] += all_data.bests[i + (number_of_generations + 1) * j]
                worst[i] += all_data.worsts[i + (number_of_generations + 1) * j]
                ave[i] += all_data.averages[i + (number_of_generations + 1) * j]

        answer_best.append(curr_gen.best())
        answer_worst.append(curr_gen.worst())
        answer_ave.append(curr_gen.ave())
        finish.append(temp_finish)
    print(answer_best)
    print(answer_worst)
    print(answer_ave)
    sum = 0
    for i in range(num):
        sum += answer_best[i]
    print("best_average" + str(sum/num))   
    print(finish_list)
    print(best_list)
    print(finish)
    for i in range(number_of_generations + 1):
        best[i] = best[i] / num
        worst[i] = worst[i] / num
        ave[i] = ave[i] / num
    end = time.time()
    time_diff = end - start
    print("time" + str(time_diff))
    plt.plot(range(len(worst)), worst, '--', color ='#ff7f00',label='worst')
    plt.plot(range(len(ave)), ave, '-.', color ='#4daf4a',label='average')
    plt.plot(range(len(best)), best, '-', color = '#377eb8', label='best')
    plt.title('CS_3_hard_50000')
    plt.xlabel('generation')
    plt.ylabel('fitness')
    if type == 'easy':
        plt.ylim([4000, 11000])
    elif type == 'hard':
        plt.ylim([10000, 50000])
    elif type == 'flat':
        plt.ylim([10000, 32500])
    plt.legend()
    plt.show()
    print(best)
    print(worst)
    print(ave)

if __name__ == '__main__':
    start = time.time()
    start_all('hard', 0.001)
    

    #end = time.time()
    #time_diff = end - start
    #print(time_diff)
    

    