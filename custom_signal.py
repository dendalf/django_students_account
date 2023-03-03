from django.dispatch import Signal

signal1 = Signal()
signal2 = Signal()


def func1(*args, **kwargs):
    print(f'FUNC1: {args} - {kwargs}')


def func2(*args, **kwargs):
    print(f'FUNC2: {args} - {kwargs}')


def func3(*args, **kwargs):
    print(f'FUNC3: {args} - {kwargs}')


def func4(*args, **kwargs):
    print(f'FUNC4: {args} - {kwargs}')


signal1.connect(func1)
signal1.connect(func3)

signal2.connect(func2)
signal2.connect(func4)

signal1.send(sender='Test 1 signal 1', val1=46, val2='sup')
signal2.send(sender='Test 1 signal 2', val1=58, val2='nothing much')

signal1.disconnect(func3)

signal1.send(sender='Test 1 signal 1', val1=46, val2='sup')
signal2.send(sender='Test 1 signal 2', val1=58, val2='nothing much')
