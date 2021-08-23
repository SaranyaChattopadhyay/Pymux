import subprocess

#Configure and check yum configuration on localhost
def yumConfigurationLocal(ip):
    subprocess.run(['mkdir', '/dvd'])
    subprocess.run(['mount', '/dev/cdrom', '/dvd'])
    subprocess.run(['echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local'])
    subprocess.run(['chmod', '+x', '/etc/rc.d/rc.local'])
    subprocess.run('echo', '"[dvd1]"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('echo', '"[dvd2]"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
    output = subprocess.run(['yum', 'repolist'])
    if output.returncode == 0:
        print("Yum configuration successful!")
    else:
        print("Yum configuration unsuccessful!")

#Configyre and check yum configuration on remote machine
def yumConfigureRemote(ip):
    subprocess.run(['ssh', f'root@{ip}', 'mkdir', '/dvd', '&&', 'mount', '/dev/cdrom', '/dvd', '&&', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local', '&&', 'chmod', '+x', '/etc/rc.d/rc.local', '&&', 'echo', '"[dvd1]"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"[dvd2]"', '>>', '/etc/yum.repo.d/dvd.repo', '&&', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repo.d/dvd.repo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo'])
    output = subprocess.run(['yum', 'repolist'])
    if output.returncode == 0:
        print("Yum configuration successful!")
    else:
        print("Yum configuration unsuccessful!")

#Install packages on local
def installPackageLocal(package):
    output = subprocess.run(['yum', 'install', f'{package}', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install packages on local
def installPackageRemote(ip, package):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', f'{package}', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install and start webserver service on localhost
def webserverLocal():
    output = subprocess.run(['yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install and start webserver service on remote machine
def webserverLocal(ip):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)


if __name__ == "__main__":
    yumConfigureRemote("192.168.31.87")

