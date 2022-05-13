import math
import scipy.optimize
import numpy as np

import Front
from Front import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal


def to_date(lin):
    day = lin[0] + lin[1]
    month = lin[3] + lin[4]
    year = lin[6] + lin[7]
    return year + month + day


class product:
    params = [-1, -1]
    percent = 0
    product_id = 0
    store_id = 0
    product_number = 0
    last_price = 0
    min_price = -1
    purchase_price = 0
    max_price = -1

    def percentCounter(self):
        self.percent = self.last_price / 100.0;

    def minPriceCounter(self):
        self.min_price = max(self.last_price - 30 * self.percent, self.purchase_price)

    def maxPriceCounter(self):
        self.max_price = 2 * min(self.last_price + 30 * self.percent, self.purchase_price * 2)


class Parser:
    def setData(self, costs_file, prices_file):
        self.costs_file_ = costs_file
        self.prices_file_ = prices_file

    def parse(self):
        self.products_dict = dict()
        f = open(self.costs_file_, 'r')
        temp_file = f.readlines()

        names = dict()
        first_string = list(temp_file[0].split('"'))
        for i in range(len(first_string)):
            names[first_string[i]] = i

        for i in range(1, len(temp_file)):
            elements_list = temp_file[i]
            elements_list = list(elements_list.split('"'))
            elements_list[names['PRODUCT_ID']] = int(elements_list[names['PRODUCT_ID']])
            elements_list[names['PRODUCT_ID']] = 100 * elements_list[names['PRODUCT_ID']] + int(elements_list[names['STORE_ID']][2::])
            self.products_dict[elements_list[names['PRODUCT_ID']]] = product()
            self.products_dict[elements_list[names['PRODUCT_ID']]].purchase_price = float(elements_list[names['PURCHASE_PRICE']])
            self.products_dict[elements_list[names['PRODUCT_ID']]].store_id = elements_list[names['STORE_ID']]
            self.products_dict[elements_list[names['PRODUCT_ID']]].product_id = elements_list[names['PRODUCT_ID']] // 100

        f = open(self.prices_file_, 'r')
        temp_file = f.readlines()
        res = []
        names = dict()
        first_string = temp_file[0]
        first_string = first_string.replace('\n', '')
        first_string = list(first_string.split(';'))
        for i in range(len(first_string)):
            names[first_string[i]] = i

        for i in range(1, len(temp_file)):
            elements_list = temp_file[i]
            elements_list = list(elements_list.split(';'))
            elements_list[names['PRODUCT_ID']] = int(elements_list[names['PRODUCT_ID']])
            res.append(elements_list)
        res = sorted(res, key=lambda base_prices: to_date(base_prices[names['DATE']]))
        for i in range(0, len(res)):
            res[i][names['PRODUCT_ID']] = 100 * res[i][names['PRODUCT_ID']] + int(res[i][names['STORE_ID']][2::])
            if (res[i][3] != "PROMO"):
                if (not (res[i][names['PRODUCT_ID']] in self.products_dict.keys())):
                    self.products_dict[res[i][names['PRODUCT_ID']]] = product()
                    self.products_dict[res[i][names['PRODUCT_ID']]].product_id = res[i][names['PRODUCT_ID']] // 100
                self.products_dict[res[i][names['PRODUCT_ID']]].last_price = float(res[i][names['PRICE']])
        return self.products_dict

class Optimizer:
    type_of_model = ''  # тип модели
    model_file_ = ''  # файл с моделью
    output_file = 'output_file.txt'  # products_dictыproducts_dictод отproducts_dictета
    type_of_optimization = ''  # тип оптимизации
    step_ = 0  # размер шага
    start_ = 1.0  # начальное значение
    bound_mar_rev_min = -1e18  # минимальное ограничение(на данном шаге)
    bound_mar_rev_max = 1e18  # максимальное ограничение(на данном шаге)
    number_of_steps_ = 0  # количестproducts_dictо шагоproducts_dict
    prices_file_ = 'PRICES_HISTORY_DAILY.txt'  # файл с ценами
    costs_file_ = 'COSTS.txt'  # файл с себестоимостями
    generated_costs_file_ = 'gen.txt'  # файл для записи


    def setData(self,model_type, rev_or_margin, start, step, number_of_steps, prices_file, costs_file, model_file,
                generated_costs_file):
        self.type_of_model = model_type
        self.type_of_optimization = rev_or_margin
        self.number_of_steps_ = number_of_steps
        self.step_ = step
        self.output_file = "t1.txt"
        self.model_file_ = model_file
        self.start_ = start
        self.bound_mar_rev_min = -1e18  # минимальное ограничение(на данном шаге)
        self.bound_mar_rev_max = 1e18
        self.prices_file_ = prices_file
        self.costs_file_ = costs_file
        self.generated_costs_file_ = generated_costs_file

    def run(self, ui_class):
        Parser.setData(Parser, self.costs_file_, self.prices_file_)
        self.products_dict = Parser.parse(Parser)

        for i in self.products_dict.keys():
            self.products_dict[i].percentCounter()
            self.products_dict[i].minPriceCounter()
            self.products_dict[i].maxPriceCounter()

        # таблица формул

        f = open(self.model_file_, 'r')
        temp_file = f.readlines()
        res = []
        for i in range(1, len(temp_file)):
            elements_list = temp_file[i]
            elements_list = list(elements_list.split(','))
            elements_list[2] = int(elements_list[2]) * 100 + 1 + int(elements_list[3])
            self.products_dict[elements_list[2]].params = [float(elements_list[0]), float(elements_list[1])]

        self.can_opt = []  # список всех товаров, для которых есть все необходимые данные
        for i in self.products_dict.keys():
            if (self.products_dict[i].min_price != -1 and self.products_dict[i].max_price != -1 and self.products_dict[i].params != [-1,-1]):
                self.can_opt.append(i)

        def val(curr_price, pr_id):
            if (self.type_of_model == 'linear'):
                m = curr_price + 5
                return max(0, self.products_dict[pr_id].params[0] + m * self.products_dict[pr_id].params[
                    1])  # константный параметр , коэф. при функции от цены

            if (self.type_of_model == 'log10'):
                if (curr_price + 5 <= 0):
                    return -1e9
                mlog = math.log10(curr_price + 5)
                return max(0, self.products_dict[pr_id].params[0] + mlog * self.products_dict[pr_id].params[1])

            if (self.type_of_model == 'loge'):
                if (curr_price + 5 <= 0):
                    return -1e9
                mlog = math.log(curr_price + 5)
                return max(0, self.products_dict[pr_id].params[0] + mlog * self.products_dict[pr_id].params[1])

        def revenue(curr_prices):
            if (self.type_of_optimization == 'revenue'):
                if (-margin(curr_prices) > self.bound_mar_rev_max or margin(curr_prices) < self.bound_mar_rev_min):
                    return 1e9
            res = 0
            for i in range(len(self.can_opt)):
                res += val(curr_prices[i], self.can_opt[i]) * curr_prices[i]
            return -res

        def margin(curr_prices):
            if (self.type_of_optimization == 'margin'):
                if (-revenue(curr_prices) > self.bound_mar_rev_max or -revenue(curr_prices) < self.bound_mar_rev_min):
                    return 1e9
            res = 0
            for i in range(len(self.can_opt)):
                res += val(curr_prices[i], self.can_opt[i]) * (
                        curr_prices[i] - self.products_dict[self.can_opt[i]].purchase_price)
            return -res


        curr_prices = []
        base_prices = []
        self.elements_bounds = ()

        for i in self.can_opt:
            curr_prices.append(
                float(self.products_dict[i].min_price) + 0.000001) # заполняем массив минимальными возможными ценами
            base_prices.append(self.products_dict[i].last_price)  #
            if (self.products_dict[i].min_price >= self.products_dict[i].max_price):
                self.products_dict[i].min_price, self.products_dict[i].max_price = self.products_dict[i].max_price, self.products_dict[
                    i].min_price
            self.elements_bounds = self.elements_bounds + ((self.products_dict[i].min_price, self.products_dict[i].max_price),)
        base_prices = np.array(base_prices)
        arr_res = []
        doub = -revenue(base_prices), -margin(base_prices)
        arr_res.append(doub)
        self.margin0 = margin(base_prices)
        self.revenue0 = revenue(base_prices)

        for i in range(self.number_of_steps_):
            if (self.type_of_optimization == 'revenue'):
                self.bound_mar_rev_max = - (self.start_ + self.step_) * self.margin0
                self.bound_mar_rev_min = - self.start_ * self.margin0
                for j in range(len(self.can_opt)):
                    while ((curr_prices[j] - self.products_dict[self.can_opt[j]].purchase_price) * val( curr_prices[j], self.can_opt[j]) < (
                            curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000 - self.products_dict[
                        self.can_opt[j]].purchase_price) * val( curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000,
                                                          self.can_opt[j]) and -margin( np.array(curr_prices)) < (
                                   self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                                   curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) < self.products_dict[
                               self.can_opt[j]].max_price):
                        curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                    while ((curr_prices[j] - self.products_dict[self.can_opt[j]].purchase_price) * val( curr_prices[j], self.can_opt[j]) <
                           (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000 - self.products_dict[
                               self.can_opt[j]].purchase_price) * val
                               (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j]) and -margin(
                                np.array(curr_prices)) <
                           (self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                                   curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) >
                           self.products_dict[self.can_opt[j]].min_price):
                        curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                max_x = scipy.optimize.minimize(revenue, np.array(curr_prices), bounds=self.elements_bounds)

            if (self.type_of_optimization == 'margin'):
                self.bound_mar_rev_max = - (self.step_ + self.start_) * self.revenue0
                self.bound_mar_rev_min = - self.start_ * self.revenue0
                #
                for j in range(len(self.can_opt)):
                    while (curr_prices[j] * val( curr_prices[j], self.can_opt[j]) < (
                            curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) * val(
                            curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j]) and -revenue(
                        np.array(curr_prices)) < (
                                   self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                                   curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) <
                           self.products_dict[self.can_opt[j]].max_price):
                        curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                    while (curr_prices[j] * val( curr_prices[j], self.can_opt[j]) <
                           (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) * val(
                                curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000,
                                self.can_opt[j])
                           and -revenue( np.array(curr_prices)) <
                           (self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                                   curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) >
                           self.products_dict[self.can_opt[j]].min_price):
                        curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                #
                max_x = scipy.optimize.minimize(margin, np.array(curr_prices), bounds=self.elements_bounds)
            new_x = max_x.x
            for j in range(len(self.can_opt)):
                if (abs(new_x[j] - self.products_dict[self.can_opt[j]].last_price) < self.products_dict[self.can_opt[j]].percent):
                    new_x[j] = self.products_dict[self.can_opt[j]].last_price
            self.bound_mar_rev_max = 1e9
            self.bound_mar_rev_min = -1e9
            self.start_ += self.step_
            doub = -revenue( new_x), -margin( new_x)
            arr_res.append(doub)
            Ui_MainWindow.progress_bar_add(ui_class, 1)
        self.start_ -= self.step_ * self.number_of_steps_
        return arr_res


    def printpoint(self, k):
        def val(curr_price, pr_id):
            if (self.type_of_model == 'linear'):
                m = curr_price + 5
                return max(0, self.products_dict[pr_id].params[0] + m * self.products_dict[pr_id].params[
                    1])  # константный параметр , коэф. при функции от цены

            if (self.type_of_model == 'log10'):
                if (curr_price + 5 <= 0):
                    return -1e9
                mlog = math.log10(curr_price + 5)
                return max(0, self.products_dict[pr_id].params[0] + mlog * self.products_dict[pr_id].params[1])

            if (self.type_of_model == 'loge'):
                if (curr_price + 5 <= 0):
                    return -1e9
                mlog = math.log(curr_price + 5)
                return max(0, self.products_dict[pr_id].params[0] + mlog * self.products_dict[pr_id].params[1])

        def revenue(curr_prices):
            if (self.type_of_optimization == 'revenue'):
                if (-margin(curr_prices) > self.bound_mar_rev_max or margin(curr_prices) < self.bound_mar_rev_min):
                    return 1e9
            res = 0
            for i in range(len(self.can_opt)):
                res += val(curr_prices[i], self.can_opt[i]) * curr_prices[i]
            return -res

        def margin(curr_prices):
            if (self.type_of_optimization == 'margin'):
                if (-revenue(curr_prices) > self.bound_mar_rev_max or -revenue(curr_prices) < self.bound_mar_rev_min):
                    return 1e9
            res = 0
            for i in range(len(self.can_opt)):
                res += val(curr_prices[i], self.can_opt[i]) * (
                        curr_prices[i] - self.products_dict[self.can_opt[i]].purchase_price)
            return -res

        curr_prices = []
        for i in self.can_opt:
            curr_prices.append(float(self.products_dict[i].min_price) + 0.000001)
        if (self.type_of_optimization == 'revenue'):
            self.bound_mar_rev_max = - (self.start_ + self.step_ * (k + 1)) * self.margin0
            self.bound_mar_rev_min = - (self.start_ + self.step_ * k) * self.margin0
            for j in range(len(self.can_opt)):
                while ((curr_prices[j] - self.products_dict[self.can_opt[j]].purchase_price) * val( curr_prices[j], self.can_opt[j]) < (
                        curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000 - self.products_dict[
                    self.can_opt[j]].purchase_price) * val(
                    curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j]) and -margin( np.array(curr_prices)) < (
                               self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                               curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) < self.products_dict[
                           self.can_opt[j]].max_price):
                    # print(-margin(curr_prices))
                    curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                while ((curr_prices[j] - self.products_dict[self.can_opt[j]].purchase_price) * val( curr_prices[j], self.can_opt[j]) <
                       (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000 - self.products_dict[self.can_opt[j]].purchase_price) * val
                           (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j]) and -margin( np.array(curr_prices)) <
                       (self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                               curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) >
                       self.products_dict[self.can_opt[j]].min_price):
                    curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
            max_x = scipy.optimize.minimize(revenue, np.array(curr_prices), bounds=self.elements_bounds)

        if (self.type_of_optimization == 'margin'):
            self.bound_mar_rev_max = - (self.start_ + self.step_ * (k + 1)) * self.revenue0
            self.bound_mar_rev_min = - (self.start_ + self.step_ * k) * self.revenue0
            for j in range(len(self.can_opt)):
                while (curr_prices[j] * val( curr_prices[j], self.can_opt[j]) < (curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) * val(
                        curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j]) and -revenue( np.array(curr_prices)) < (
                               self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                               curr_prices[j] + self.products_dict[self.can_opt[j]].max_price / 1000) < self.products_dict[
                           self.can_opt[j]].max_price):
                    curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
                while (curr_prices[j] * val( curr_prices[j], self.can_opt[j]) <
                       (curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) * val(
                            curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000, self.can_opt[j])
                       and -revenue( np.array(curr_prices)) <
                       (self.bound_mar_rev_min + self.bound_mar_rev_max) / 2 and (
                               curr_prices[j] - self.products_dict[self.can_opt[j]].max_price / 1000) >
                       self.products_dict[self.can_opt[j]].min_price):
                    curr_prices[j] += self.products_dict[self.can_opt[j]].max_price / 1000
            max_x = scipy.optimize.minimize(margin, np.array(curr_prices), bounds=self.elements_bounds)
        new_x = max_x.x
        for j in range(len(self.can_opt)):
            if (abs(new_x[j] - self.products_dict[self.can_opt[j]].last_price) < self.products_dict[self.can_opt[j]].percent):
                new_x[j] = self.products_dict[self.can_opt[j]].last_price

        fil = open(self.generated_costs_file_, 'w')
        fil.write("PRODUCT_ID GENERATED_PRICE\n")
        for j in range(len(self.can_opt)):
            fil.write(str(self.can_opt[j]) + "; ")
            fil.write(str(new_x[j]) + "\n")
        fil.close()






