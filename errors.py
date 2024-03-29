# Ниже представлен фрагмент кода с обработкой ошибок в участке программы. Какие моменты упустил написавший его разработчик? Как этот фрагмент можно улучшить?
def do_some_inner_stuff(parameter: int) -> None:
    # some control stuff with parameter
    if parameter > 10:
        raise ValueError("The parameter cannot be greater than 10.")
    elif parameter < 0:
        raise OSError("Some OS error due to negative parameter.")


def do_some_stuff(parameter: int) -> None:
    try:
        do_some_inner_stuff(parameter)
    except Exception:
        raise Exception("Task parameter is invalid. Terminating.")


def run_task(parameter: int) -> None:
    try:
        do_some_stuff(parameter)
    except Exception as exc:
        print(exc)

# общий except блок:
# В данном коде все ошибки отлавливаются общим Exception. Это недостаточно информативно, лучше использовать более конкретные указания на ошибки, чтобы точнее определить, из-за чего именно программа выдаёт ошибку.
        
# добавить комментарии:
# можно добавить комментарии к функциям do_some_inner_stuff и do_some_stuff, что эти функции делают.
        

# Ниже представлены два фрагмента кода с разными способами запуска пула рабочих процессов в некотором фрагменте многопоточной программы. Расскажите, в чем отличие этих двух методов запуска? Какой из них в какой ситуации предпочтительнее и почему?
        
# with ThreadPoolExecutor(max_workers=100) as executor:
#     for result in executor.map(task, items):
#         do_some_stuff_with(result)
# with ProcessPoolExecutor(max_workers=100) as executor:
#     for result in executor.map(task, items):
#         do_some_stuff_with(result)
        
# 1. ThreadPoolExecutor: 
# ThreadPoolExecutor предоставляет пул потоков для выполнения задач. Он работает следующим образом: вы создаете экземпляр ThreadPoolExecutor, указывая количество рабочих потоков, и отправляете задачи на выполнение в пуле.
        
# ThreadPoolExecutor автоматически управляет пулом потоков и распределяет задачи между рабочими потоками, что делает его удобным инструментом для асинхронного выполнения задач.
        
# Различные сценарии использования ThreadPoolExecutor: параллельная загрузка данных из сети, обработка больших объемов текста и многозадачная обработка изображений:
        
# 2. ProcessPoolExecutor: ProcessPoolExecutor предоставляет пул процессов для выполнения задач. Этот инструмент полезен, когда задачи могут выполняться независимо и имеют высокую вычислительную нагрузку. Это особенно полезно, когда есть задачи, которые могут выполняться независимо друг от друга, и необходимо максимально использовать ресурсы многопроцессорных систем.
        
# ProcessPoolExecutor автоматически управляет процессами, что делает его мощным инструментом для параллельного выполнения задач.
        
# Выбор между ThreadPoolExecutor и ProcessPoolExecutor зависит от характера задач.
# Потоки vs. Процессы: ThreadPoolExecutor использует потоки, работающие в пределах одного процесса, в то время как ProcessPoolExecutor использует отдельные процессы для каждой задачи. Это позволяет ProcessPoolExecutor избегать проблем с Global Interpreter Lock (GIL), которые могут возникнуть в ThreadPoolExecutor.
        
# Ресурсы и производительность: ThreadPoolExecutor обычно требует меньше системных ресурсов, так как потоки делят один и тот же адресное пространство процесса. Однако ProcessPoolExecutor может обеспечить более высокую производительность в случае многозадачных вычислений, так как каждая задача выполняется в отдельном процессе.
        
# Сериализация данных: В ProcessPoolExecutor данные, передаваемые между процессами, должны быть сериализованы и десериализованы. Это может потребовать дополнительных усилий и влиять на производительность. В ThreadPoolExecutor такой необходимости нет.
        
# Для некоторых задач может быть полезно использовать обе технологии параллельно, в зависимости от характера задач в вашем приложении.
# Io bound 

        
def complex_task(value: int) -> int:
    # some calculations
    return value

def some_loop(length: int) -> list[int]:
    # calculated_list = []
    # for i in range(length):
    #     calculated_list.append(complex_task(i))
    # return calculated_list
    # calculated_list = [complex_task(i) for i in range(length)]
    # return calculated_list

    for i in range(length):
        yield complex_task(i)