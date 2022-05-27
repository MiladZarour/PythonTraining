import paramiko


class ssh_keywords():

    session = None
    channel = None
    timeout = 15
    SGA = {
        "hostname": "SGA",
        "ip": "169.254.4.10",
        "port": 22,
        "username": "swupdate",
        "password": "swupdate",
        "prompt": "~ $"
    }

    HPA = {
        "hostname": "HPA",
        "ip": "169.19.0.1",
        "port": 22,
        "username": "root",
        "password": "root",
        "prompt": "#"
    }

    Linux = {
        "hostname": "Linux",
        "prompt": "$ "
    }

    current_host = None

    def connect_to_SGA(self, retries=10, interval=2):
        """
        Establishes an ssh session and a shell-channel to the SGA 
        Args:
            Retries: Number of times to attempt connecting
            Interval: Time in seconds between attempts
        Returns:

        """
        if self.session is not None and self.current_host == self.SGA:
            return
        retry_cnt = 0
        while retry_cnt < retries:
            try:
                self.session = paramiko.SSHClient()
