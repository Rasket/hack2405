class test1():

    ask = { 0: ("В ходе работы Вашего заведения образуются перерабатываемые бумажные отходы?", [(0, "Да"), (1,"Нет")]),
            1: ("Ваше заведение сдаёт макулатуру?", [(0, "Да"), (1,"Нет")]),
            2: ("Какая часть бумажных отходов перерабатывается?", [(0,"Менее 30%"), (1, "Оклоло 50%"), (2,"Более 70%")]),
           
            3: ("В ходе работы Вашего заведения образуются отходы, которые можно переработать вместе с металлом (алюминий, фольгу, металлические предметы и упаковку)?", [(0, "Да"), (1,"Нет")]),           
            4: ("Ваше заведение сдаёт отходы такого типа на переработку?", [(0, "Да"), (1,"Нет")]),
            5: ("Какая часть отходов перерабатывается?", [(0,"Менее 30%"), (1, "Оклоло 50%"), (2,"Более 70%")]),
           
            6: ("В ходе работы Вашего заведения образуются пластиковые отходы?", [(0, "Да"), (1,"Нет")]),
            7: ("Ваше заведение сдаёт отходы такого типа на переработку?", [(0, "Да"), (1,"Нет")]),
            8: ("Какая часть отходов перерабатывается?", [(0,"Менее 30%"), (1, "Оклоло 50%"), (2,"Более 70%")]),
            
            9: ("В ходе работы Вашего заведения образуются отходы тетрапак и их аналоги?", [(0, "Да"), (1,"Нет")]),
            10: ("Ваше заведение сдаёт отходы такого типа на переработку?", [(0, "Да"), (1,"Нет")]),
            11: ("Какая часть отходов перерабатывается?", [(0,"Менее 30%"), (1, "Оклоло 50%"), (2,"Более 70%")]),
            
            12: ("В ходе работы Вашего заведения образуются отходы из стекла?", [(0, "Да"), (1,"Нет")]),
            13: ("Ваше заведение сдаёт отходы такого типа на переработку?", [(0, "Да"), (1,"Нет")]),
            14: ("Какая часть отходов перерабатывается?", [(0,"Менее 30%"), (1, "Оклоло 50%"), (2,"Более 70%")]),


            15: ("Ваше заведение сдаёт на переработку вышедшие из строя расходные материалы (батарейки, аккумуляторы, ртутные лампы)?", ["Да", "Нет", "Только часть", "Заведение не использует подобное"]),
            
            
            'end': ("",[])}

    def __init__(self):
        self.question = 0
        self.recomend = ""
        self.result_recykle = 0

    def start():
        return test1.ask[0]

    def asked(self, question, answer):
        self.question = question
        return self.next(answer)

    def next(self, choice):
        
        if self.question == 0:
            if choice == 0:
                self.question = 1
            else:
                self.result_recykle += 5
                self.question  = 3
        
        elif self.question == 1:
            if choice == 0:
                self.question = 2
            else:
                self.question = 3
        
        elif self.question == 2:
            self.question = 3
            if choice == 0:
                self.result_recykle += 1
            elif choice == 1:
                self.result_recykle += 3
            else:
                self.result_recykle += 5

        elif self.question == 3:
            if choice == 0:
                self.question = 4
            else:
                self.result_recykle += 5
                self.question = 6
        
        elif self.question == 4:
            if choice == 0:
                self.question = 5
            else:
                self.question = 6
        
        elif self.question == 5:
            self.question = 6
            if choice == 0:
                self.result_recykle += 1
            elif choice == 1:
                self.result_recykle += 3
            else:
                self.result_recykle += 5
        
        
        elif self.question == 6:
            if choice == 0:
                self.question = 7
            else:
                self.result_recykle += 5
                self.question = 9
        
        elif self.question == 7:
            if choice == 0:
                self.question = 8
            else:
                self.question = 9
        
        elif self.question == 8:
            self.question = 9
            if choice == 0:
                self.result_recykle += 1
            elif choice == 1:
                self.result_recykle += 3
            else:
                self.result_recykle += 5

        elif self.question == 9:
            if choice == 0:
                self.question = 10
            else:
                self.result_recykle += 5
                self.question = 12
        
        elif self.question == 10:
            if choice == 0:
                self.question = 11
            else:
                self.question = 12
        
        elif self.question == 11:
            self.question = 12
            if choice == 0:
                self.result_recykle += 1
            elif choice == 1:
                self.result_recykle += 3
            else:
                self.result_recykle += 5

        elif self.question == 12:
            if choice == 0:
                self.question = 13
            else:
                self.result_recykle += 5
                self.question = 15
        
        elif self.question == 13:
            if choice == 0:
                self.question = 14
            else:
                self.question = 15
        
        elif self.question == 14:
            self.question = 15
            if choice == 0:
                self.result_recykle += 1
            elif choice == 1:
                self.result_recykle += 3
            else:
                self.result_recykle += 5

        elif self.question == 15:
            self.question = 16 
            if choice == 2:
                self.result_recykle += 3
            if choice in [0, 3]:
                self.result_recykle += 6
            if self.result_recykle < 12:
                self.recomend += "Ваше заведение уделяет несдостаточно внимания переработке непищевых отходов\n"
            elif self.result_recykle < 17:
                self.recomend += "Ваше заведение, активно участвует в переработке "

        return test1.ask[self.question]
