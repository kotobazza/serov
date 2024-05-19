import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QMessageBox

class Decision(QMainWindow):
    table = 0
    alpha = 0.6
    probabilities = [0.1, 0.4, 0.4, 0.1]
    equal_probability = 0.25
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбираем проект")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.mainVLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainVLayout)
        self.setGeometry(100, 400, 440, 400)
        

        self.mainLabel = QLabel(f"Производит выбор из 8 представленных в таблицу проектов\nна основе выбора методом голосования из критериев: Вальдса,\nСэвиджа, Гурвица (a = {self.alpha}),Лапласа, Байеса(p = {self.probabilities})")
        self.mainVLayout.addWidget(self.mainLabel)

        self.projectsTable = QTableWidget(8, 4)
        self.projectsTable.setHorizontalHeaderLabels(["z1", "z2", "z3", "z4"])
        self.projectsTable.setVerticalHeaderLabels([f"x{i}" for i in range(1, 9)])
        self.projectsTable.setFixedHeight(270)

        self.mainVLayout.addWidget(self.projectsTable)
        
        self.calculateButton = QPushButton("Определить оптимальный проект")
        self.calculateButton.clicked.connect(self.checkDataTable)
        self.mainVLayout.addWidget(self.calculateButton)


        self.defaultButton = QPushButton("Добавить значения по умолчанию")
        self.defaultButton.clicked.connect(self.defaultInsertion)
        self.mainVLayout.addWidget(self.defaultButton)

        
        
        
        self.resultWidget = QWidget()
        self.resultLayout = QVBoxLayout()
        self.resultWidget.setLayout(self.resultLayout)
        self.mainVLayout.addWidget(self.resultWidget)
        
        self.resultWidget2 = QWidget()
        self.resultLayout2 = QVBoxLayout()
        self.resultWidget2.setLayout(self.resultLayout2)
        self.mainVLayout.addWidget(self.resultWidget2)

        self.order = {
            "Вальдса": self.calculateWalds,
            "Сэвиджа": self.calculateSavage,
            "Гурвица": self.calcutaleGurvets,
            "Байеса": self.calculateBias,
            "Лапласа":self.calculateLaplas
        }

    def defaultInsertion(self):
        self.defaultTable = [
                                [6, 7, 8, 10],
                                [4, 5, 6, 13],
                                [10, 6, 5, 11],
                                [8, 9, 7, 9],
                                [1, 2, 1, 2],
                                [2, 1, 2, 4],
                                [3, 3, 2, 2],
                                [4, 1, 3, 3] 
                            ]
        for row in range(8):
            for col in range(4):
                self.projectsTable.setItem(row, col, QTableWidgetItem(str(self.defaultTable[row][col])))
    
    def checkDataTable(self):
        self.table = []
        for row in range(self.projectsTable.rowCount()):
            rowData = []
            for col in range(self.projectsTable.columnCount()):
                item = self.projectsTable.item(row, col)
                if item is None:
                    QMessageBox.critical(self, "Ошибка заполнения", "Не все поля таблицы заполнены")
                    return
                elif not item.text().isdigit():
                    QMessageBox.critical(self, "Ошибка заполнения", "Не все поля таблицы заполнены правильно")
                    return
                else:
                    value = int(item.text())
                    
                rowData.append(value)
            self.table.append(rowData)

        self.calculate()

    
        

    def calculate(self):
    
        results_winners = []
        results_values = []

        for criteria_name in self.order.keys():
            values, result = self.order[criteria_name]()
            print(criteria_name, f": x{values.index(result)+1} = {round(result, 3)}")
            results_values.append(round(result, 3))
            results_winners.append(values.index(result)+1)
        
        self.createResultTable(results_winners, results_values)


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


    def createResultTable(self, results_winners, results_values):
        self.resize(670, 800)
        self.setMinimumWidth(670)
        
        orderList = list(self.order.keys())
        
        self.clearLayout(self.resultLayout)
        self.clearLayout(self.resultLayout2)


        tlabel = QLabel("Результаты подсчета каждого критерия и оптимальное значение по критерию")
        ttable = QTableWidget(len(orderList), 3)
        ttable.setHorizontalHeaderLabels(["Критерий", "Значение", "Оптимальный проект"])
        #ttable.setVerticalHeaderLabels(orderList)
        ttable.setFixedHeight(180)
        for column in range(ttable.columnCount()):
            ttable.horizontalHeader().resizeSection(column, ttable.horizontalHeader().sectionSizeHint(column))


        for i in range(len(orderList)):
            ttable.setItem(i, 0, QTableWidgetItem(orderList[i]))
            ttable.setItem(i, 1, QTableWidgetItem(str(results_values[i])))
            ttable.setItem(i, 2, QTableWidgetItem(f"x{results_winners[i]}"))

        self.resultLayout.addWidget(tlabel)
        self.resultLayout.addWidget(ttable)

        label = QLabel("Результаты выбора каждого из критериев оценивания представлены в таблице:")
        self.resultLayout2.addWidget(label)
        orderList.append("Сумма")
        table = QTableWidget(8, 6)
        table.setHorizontalHeaderLabels(orderList)
        table.setVerticalHeaderLabels([f"x{i}" for i in range(1, 9)])
        table.setFixedHeight(270)


        for i in range(len(results_winners)):
            table.setItem(results_winners[i]-1, i, QTableWidgetItem("+"))
            

        projects_counts = []
        for i in range(1, 9):
            projects_counts.append(results_winners.count(i))

        for i in range(8):
            table.setItem(i, 5, QTableWidgetItem(str(projects_counts[i])))
            
                
        self.resultLayout2.addWidget(table)

        max_value = max(projects_counts)
        resultLabel = QLabel(f"Итого: оптимальным проектом избирается x{projects_counts.index(max_value)+1} со значением {max_value} голоса/ов")
        self.resultLayout2.addWidget(resultLabel)


    def calculateWalds(self):
        min_walds_values = []

        for i in range(len(self.table)):
            min_walds_values.append(min(self.table[i]))
        result = max(min_walds_values)
        return min_walds_values, result


    def calculateSavage(self):
        risksTable = []
        
        Q=[]
        
        for i in zip(*self.table):
            Q.append(max(i))
        
        for i in range(len(self.table)):
            row = []
            for j in range(len(self.table[0])):
                row.append(Q[j] - self.table[i][j])
            
            risksTable.append(row)

        max_savage_values = []
        for i in range(len(risksTable)):
            max_savage_values.append(max(risksTable[i]))
        result = min(max_savage_values)
        return max_savage_values, result



    def calcutaleGurvets(self):
        min_gurvets_values = []

        for i in range(len(self.table)):
            min_gurvets_values.append(min(self.table[i]))

        max_gurvets_values = []

        for i in range(len(self.table)):
            max_gurvets_values.append(max(self.table[i]))

        gurvets_values = []
        for i in range(len(min_gurvets_values)):
            gurvets_values.append(min_gurvets_values[i]*self.alpha + max_gurvets_values[i]*(1-self.alpha))
        
        return gurvets_values, max(gurvets_values)
        

    def calculateLaplas(self):
        sums = [sum(self.equal_probability * value for value in row) for row in self.table]
        return sums, max(sums)

    def calculateBias(self):
        bias_values = []
        for i in range(len(self.table)):
            summ = 0
            for j in range(len(self.table[0])):
                summ += self.table[i][j] * self.probabilities[j]
            bias_values.append(summ)

        return bias_values, max(bias_values)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Decision()
    mainWin.show()
    sys.exit(app.exec())

