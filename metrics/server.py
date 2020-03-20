import asyncio
import os
import json
import tempfile

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.metrics = {}
        self.storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        method = self.validate_method(data.decode())
        if not method:
            resp = self.generate_error('wrong command')
        else:
            if method == 'put':
                resp = self.store_data(data.decode())
            if method == 'get':
                resp = self.get_data(data.decode())
        self.transport.write(resp.encode())

    def generate_error(self, error_code):
        error_string = 'error\n{}\n\n'.format(error_code)

        return error_string

    def store_data(self, data):
        metrics = self.get_storage()

        method, key, value, timestamp = data.split()
        if key not in metrics:
            metrics[key] = list()
            metrics[key].append([value, timestamp])
        else:
            count = 0
            for item in metrics[key]:
                if item[1] == timestamp:
                    print('here32')
                    count += 1
            if count == 0:
                print('here')
                metrics[key].append([value, timestamp])

        # print(metrics)
        self.set_storage(metrics)

        return 'ok\n\n'

    def set_storage(self, contents):
        with open(self.storage_path, 'w') as f:
            f.write(json.dumps(contents))

    def get_storage(self):
        if not os.path.exists(self.storage_path):
            return {}

        with open(self.storage_path, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return json.loads(raw_data)

            return {}

    def get_data(self, data):
        metrics = self.get_storage()
        method, key = data.split()
        response_string = 'ok\n'
        if key == '*':
            for metrics_key in metrics:
                for metrics_set in metrics[metrics_key]:
                    response_string += '{} {} {}\n'.format(metrics_key, metrics_set[0], metrics_set[1])
        else:
            if key in metrics:
                for metrics_set in metrics[key]:
                    response_string += '{} {} {}\n'.format(key, metrics_set[0], metrics_set[1])
        response_string += '\n'

        print(method, key)
        return response_string

    def validate_method(self, data):
        if 'get' in data:
            return 'get'
        elif 'put' in data:
            return 'put'
        else:
            return False

def run_server(host, port):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        os.remove(storage_path)

    loop = asyncio.get_event_loop()

    coro = loop.create_server(
         ClientServerProtocol,
         host, port
     )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    run_server('127.0.0.1', 8888)
