class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, nome_cpu, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(nome_cpu, cpu_cores, cpu_clock)

    def mostrar_config(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostrar_CPU()

    class GPU:  # Nested Class
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f'GPU: {self.nome} - {self.memoria_gb} GB')

    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def mostrar_CPU(self):
            print(
                f'CPU: {self.nome} - {self.cores} núcleos - {self.clock_ghz} ghz')


# Utilização
PC_1 = Computador('Dell XPS', 'GTX 1660 Super', 12, 'Ryzen 5 4500', 8, 4.6)

PC_1.mostrar_config()
