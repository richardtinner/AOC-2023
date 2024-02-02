HIGH_PULSE = 1
LOW_PULSE = 0
pulse_text = {LOW_PULSE: 'low', HIGH_PULSE: 'high'}


class Module:
    def __init__(self, output_list, name):
        self.output_list = output_list
        self.name = name

    def send_pulse(self, sent_from, pulse, n):
        # if self.name == 'rx':
        #     print(sent_from, ' -', pulse_text[pulse], '->', self.name)
        return []

    def init_inputs(self, inputs):
        pass


class FlipFlop(Module):
    def __init__(self, output_list, name):
        super().__init__(output_list, name)
        self.moduleOn = False

    def send_pulse(self, sent_from, pulse, n):
        # print(sent_from, ' -', pulse_text[pulse], '->', self.name)
        if pulse == LOW_PULSE:
            # Flip state and then send pulse with type depending on state
            self.moduleOn = not self.moduleOn
            if self.moduleOn:
                # send high pulse
                return [(x, self.name, HIGH_PULSE) for x in self.output_list]
            else:
                # send low pulse
                return [(x, self.name, LOW_PULSE) for x in self.output_list]
        else:
            # ignore high pulse
            return []


class Conjunction(Module):
    def __init__(self, output_list, name):
        super().__init__(output_list, name)
        self.input_dict = dict()

    def send_pulse(self, sent_from, pulse, n):
        if self.name == 'dh' and pulse == HIGH_PULSE:
            print('n = ', n, sent_from, ' -', pulse_text[pulse], '->', self.name)

        # First update the pulse type for the pulse received
        self.input_dict[sent_from] = pulse
        all_high = True

        # If all pulse types are High then send low pulse
        # otherwise send high pulse
        for i in self.input_dict.values():
            if not i:
                all_high = False
                break

        if all_high:
            return [(x, self.name, LOW_PULSE) for x in self.output_list]
        else:
            return [(x, self.name, HIGH_PULSE) for x in self.output_list]

    def init_inputs(self, inputs):
        for i in inputs.values():
            for output in i.output_list:
                if output == self.name:
                    self.input_dict[i.name] = False


class Broadcast(Module):
    def __init__(self, output_list, name):
        super().__init__(output_list, name)

    def send_pulse(self, sent_from, pulse, n):
        # print(sent_from, ' -', pulse_text[pulse], '->', self.name)
        return [(module, self.name, pulse) for module in self.output_list]


class ModuleFactory():
    def create_module(self, module_txt):
        module_type = module_txt.split('->')[0]
        module_output = module_txt.split('->')[1].replace(" ", "").split(',')
        if module_type[0] == '%':
            return FlipFlop(module_output, module_type[1:].strip())
        elif module_type[0] == '&':
            return Conjunction(module_output, module_type[1:].strip())
        elif module_type[0] == 'b':
            return Broadcast(module_output, 'broadcaster')
        else:
            return Module([], module_type.strip())


module_map = dict()

with open("input20.txt") as my_file:
    # read file and create modules
    mf = ModuleFactory()
    for line in my_file:
        module = mf.create_module(line.strip())
        module_map[module.name] = module

    # Conjunctions need to be initialised with inputs
    for module in module_map.values():
        module.init_inputs(module_map)

    total_low = 0
    total_high = 0
    for n in range(1, 20000):
        #print('====== ', n, '======')
        # Initialise the pulse list with the broadcast pulse which will be the first pulse
        # And then keep sending the pulses in order until the there are no more to send
        send_pulse_list = []
        bcst_module = module_map['broadcaster']
        send_pulse_list.append((bcst_module, 'button', LOW_PULSE))

        for pulse in send_pulse_list:
            if pulse[2] == HIGH_PULSE:
                total_high += 1
            else:
                total_low += 1

            new_pulse_list = pulse[0].send_pulse(pulse[1], pulse[2], n)
            if len(new_pulse_list) > 0:
                for np in new_pulse_list:
                    if np[0] in module_map:
                        module = module_map[np[0]]
                        send_pulse_list.append((module, np[1], np[2]))
                    else:
                        module = mf.create_module(np[0] + " ->")
                        send_pulse_list.append((module, np[1], np[2]))

    print("Low = ", total_low, " High = ", total_high, "low * high = ", total_low * total_high)
