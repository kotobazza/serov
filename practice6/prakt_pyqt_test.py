import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel

class DecisionMakingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Decision Making App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget(8, 4)  # 8 опций и 4 состояния
        self.layout.addWidget(self.table)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_decision_criteria)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Result will be displayed here")
        self.layout.addWidget(self.result_label)

    def calculate_decision_criteria(self):
        # Пример данных для демонстрации
        data = []
        for row in range(self.table.rowCount()):
            rowData = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                value = int(item.text()) if item else 0
                rowData.append(value)
            data.append(rowData)

        # Вызов функций для вычисления критериев
        results = {
            'Wald': self.wald_criterion(data),
            'Savage': self.savage_criterion(data),
            'Laplace': self.laplace_criterion(data),
            'Bayes': self.bayes_criterion(data, [0.25, 0.25, 0.25, 0.25]),  # равномерное распределение вероятностей
            'Hurwicz': self.hurwicz_criterion(data, 0.5)  # Коэффициент пессимизма/оптимизма
        }

        # Метод голосования
        final_decision = self.voting_method(results)

        self.result_label.setText(f"Selected Option: {final_decision}")

    def wald_criterion(self, data):
        min_values = [min(option) for option in data]
        return min_values.index(max(min_values))

    def savage_criterion(self, data):
        max_in_columns = [max(column) for column in zip(*data)]
        regret_matrix = [[max_in_columns[j] - data[i][j] for j in range(len(data[i]))] for i in range(len(data))]
        max_regret = [max(option) for option in regret_matrix]
        return max_regret.index(min(max_regret))

    def laplace_criterion(self, data):
        avg_values = [sum(option) / len(option) for option in data]
        return avg_values.index(max(avg_values))

    def bayes_criterion(self, data, probabilities):
        expected_values = [sum(data[i][j] * probabilities[j] for j in range(len(data[i]))) for i in range(len(data))]
        return expected_values.index(max(expected_values))

    def hurwicz_criterion(self, data, alpha):
        hurwicz_values = [alpha * max(option) + (1 - alpha) * min(option) for option in data]
        return hurwicz_values.index(max(hurwicz_values))

    def voting_method(self, results):
        vote_counts = [0] * 8
        for criterion, option in results.items():
            vote_counts[option] += 1
        return vote_counts.index(max(vote_counts))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = DecisionMakingApp()
    mainWin.show()
    sys.exit(app.exec())