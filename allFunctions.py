import subprocess
def yumConfigureRemote(ip):
    subprocess.run(['ssh', f'root@{ip}', 'mkdir', '/dvd', '&&', 'mount', '/dev/cdrom', '/dvd', '&&', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local', '&&', 'chmod', '+x', '/etc/rc.d/rc.local', '&&', 'echo', '"[dvd1]"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"[dvd2]"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repo.d/dvd.repo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo'])
    #subprocess.run(['mkdir', '/dvd'])
    #subprocess.run(['mount', '/dev/cdrom', '/dvd'])
    #subprocess.run(['echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local'])
    #subprocess.run(['chmod', '+x', '/etc/rc.d/rc.local'])
    #subprocess.run('echo', '"[dvd1]"', '>>', '/etc/yum.repo.d/dvd.repo')
    #subprocess.run('echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repo.d/dvd.repo')
    #subprocess.run('echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
    #subprocess.run('echo', '"[dvd2]"', '>>', '/etc/yum.repo.d/dvd.repo')
    #subprocess.run('echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repo.d/dvd.repo')
    #subprocess.run('echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
    output = subprocess.run(['yum', 'repolist'])
    if output.returncode == 0:
        print("Yum configuration successful!")
    else:
        print("Yum configuration unsuccessful!")

if __name__ == "__main__":
    yumConfigureRemote("192.168.31.87")

