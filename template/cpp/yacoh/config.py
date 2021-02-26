name='Main'

compile_options = '-std=c++11 -O2 -Wall -Wextra -pedantic -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG'.split()

compile_command = ['g++'] + compile_options + ['-o', 'Main', '../Main.cpp']

run_command = [
    './Main'
]
