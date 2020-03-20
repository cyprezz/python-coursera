import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=None):
        command = "put {} {} {}\n".format(key, value, timestamp)
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(command.encode())
            data = sock.recv(1024)
            data = data.decode("utf8")
        return data

    def get(self, key):
        try:
            command = "get {}\n".format(key)
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.sendall(command.encode())
                data = sock.recv(1024)
                data = data.decode("utf8")
                if data:
                    data = data.split("\n")
                    metrics = dict()
                    if data[0] == 'ok':
                        data = data[1:]
                        for response in data:
                            if response:
                                row = response.split(' ')
                                if row[0] not in metrics:
                                    metrics[row[0]] = list()
                                    if len(row) == 3:
                                        val = (int(row[2]), float(row[1]))
                                        metrics[row[0]].append(val)
                                else:
                                    if len(row) == 3:
                                        val = (int(row[2]), float(row[1]))
                                        metrics[row[0]].append(val)
                        return metrics
                    elif data[0] == 'error':
                        raise ClientError(data[1])
                    else:
                        raise ClientError("not valid response")
                else:
                    raise ClientError("not valid response")
        except ClientError as err:
            raise ClientError(err)


class ClientError(Exception):
    pass

class ClientSocketError(Exception):
    pass

class ClientProtocolError(Exception):
    pass

