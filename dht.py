import RPi.GPIO as GPIO
import time

class DHT11():
    # test results should be [4, 3, 4, 9, 9, 10, 10, 10, 4, 3, 3, 4, 3, 3, 4, 4, 3, 4, 3, 9, 10, 4, 3, 9, 3, 3, 4, 3, 3, 10, 10, 10, 4, 3, 9, 10, 10, 10, 10, 10]
    # test_raw_data_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def __init__(self, pin, sample_interval=2, debug=0):
        self.__pin = pin
        self.debug = debug

        self.sample_interval = max(sample_interval, 2)

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        self.temperature = 0
        self.humidity = -1

    def read(self):
        raw_data = self.__collect_raw_data()

        if self.debug:
            print("Raw Data:")
            print(raw_data)

        duration_data = self.__raw_2_duration(raw_data)

        if self.debug:
            print("Duration_data: ")
            print(duration_data)
            print("Length of duration data: ", len(duration_data))


        bit_data = self.__duration_2_bits(duration_data)

        if self.debug:
            print("Bit Data: ")
            print(bit_data)
            print("Length of Bit_data: ", len(bit_data))


        byte_data = self.__bits_2_bytes(bit_data)
        if self.debug:
            print("Byte Data: ")
            print(byte_data)
            print("Length of Byte_data: ", len(byte_data))

        checksum = self.__calculate_checksum(byte_data)
        if self.debug:
            print("Checksum: ", checksum)
            print("byte_data[4]", byte_data[4])


        if checksum != byte_data[4]:
            self.temperature = 0
            self.humidity = -1
            return self.temperature, self.humidity

        print(byte_data)

        self.humidity = byte_data[0]
        self.temperature = byte_data[2]

        return self.temperature, self.humidity


    def __shake_with_sensor(self):

        GPIO.setup(self.__pin, GPIO.OUT)

        # 主机的握手命令
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(self.__pin, GPIO.LOW)
        time.sleep(0.02)
        # 端口设置为输入，并上拉高电平，等待DHT11传感器响应
        GPIO.setup(self.__pin, GPIO.IN, GPIO.PUD_UP)


    def __collect_raw_data(self):

        raw_data = []

        self.__shake_with_sensor()

        stable_count = 0
        max_stable_count = 100
        last_data = -1

        while True:
            current_data = GPIO.input(self.__pin)
            raw_data.append(current_data)
            if current_data != last_data:
                stable_count = 0
                last_data = current_data
            else:
                stable_count +=1

            if stable_count > max_stable_count:     # 数据pin稳定100个指令周期无变化，直接退出
                break

        return raw_data

    def __raw_2_duration(self, raw_data):
        " 用状态机实现数据转换"

        STATE_LAST_HIGH = 1
        STATE_LAST_LOW = 2
        STATE_DATA_HIGH = 3
        STATE_DATA_LOW = 4

        state = STATE_LAST_HIGH

        length = 0
        lengths = []

        raw_data.reverse()

        for data in raw_data:

            length += 1

            if state is STATE_LAST_HIGH:
                if data is GPIO.LOW:
                    state = STATE_LAST_LOW
                    continue
                else:
                    continue

            if state is STATE_LAST_LOW:
                if data is GPIO.HIGH:
                    state = STATE_DATA_HIGH
                    length = 0
                    continue
                else:
                    continue

            if state is STATE_DATA_HIGH:
                if data is GPIO.LOW:
                    lengths.append(length)
                    state = STATE_DATA_LOW
                    continue
                else:
                    continue

            if state is STATE_DATA_LOW:
                if data is GPIO.HIGH:
                    state = STATE_DATA_HIGH
                    length = 0
                    continue
                else:
                    continue


        lengths.reverse()

        return lengths[-40:]

    def __duration_2_bits(self, lengths):

        bits = []

        threshold = min(lengths) + (max(lengths) - min(lengths))/2

        bits = [True if data > threshold else False for data in lengths]

        return bits

    def __bits_2_bytes(self, bits):

        bytes = []

        # print(bits)

        for index in range(0,len(bits),8):
            byte = 0
            for bit in bits[index : (index+8)]:
                byte = (byte <<1) | bit

            bytes.append(byte)

        return bytes


    def __calculate_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255



