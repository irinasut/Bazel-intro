py_library(
    name = 'greetings',
    srcs = ['greetings.py'],        
)

py_binary(
    name = 'hello',
    main = 'hello.py',
	srcs = ['hello.py'],
    deps = [':greetings'],
)