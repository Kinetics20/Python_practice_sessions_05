from hidden_gems.ex_1.design_patterns_oop.builder.after.budget_box_builder import BudgetBoxBuilder
from hidden_gems.ex_1.design_patterns_oop.builder.after.director import Director
from hidden_gems.ex_1.design_patterns_oop.builder.after.my_computer_builder import MyComputerBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()