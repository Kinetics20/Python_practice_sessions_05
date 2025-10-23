from hidden_gems.ex_1.design_patterns_oop.builder.before_2.my_computer import MyComputer

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
