import subprocess

#Configure and check yum configuration on local machine
def yumConfigurationLocal(ip):
    subprocess.run(['sudo', 'mkdir', '/dvd'])
    subprocess.run(['sudo', 'mount', '/dev/cdrom', '/dvd'])
    subprocess.run(['sudo', 'echo', '"mount /dev/cdrom /dvd"', '>>', '/etc/rc.d/rc.local'])
    subprocess.run(['sudo', 'chmod', '+x', '/etc/rc.d/rc.local'])
    subprocess.run('sudo', 'echo', '"[dvd1]"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('sudo', 'echo', '"baseurl=file:///dvd/AppStream"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('sudo', 'echo', '"[dvd2]"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('sudo', 'echo', '"baseurl=file:///dvd/BaseOS"', '>>', '/etc/yum.repo.d/dvd.repo')
    subprocess.run('sudo', 'echo', '"gpgcheck=0"', '>>', '/etc/yum.repo.d/dvd.repo')
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

#Install packages on local machine
def installPackageLocal(package):
    output = subprocess.run(['sudo', 'yum', 'install', f'{package}', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install packages on remote machine
def installPackageRemote(ip, package):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', f'{package}', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install and start webserver service on localhost
def webserverLocal():
    output = subprocess.run(['sudo', 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Install and start webserver service on remote machine
def webserverLocal(ip):
    output = subprocess.run(['ssh', f'root@{ip}', 'yum', 'install', 'httpd', '-y', '&&', 'systemctl', 'start', 'httpd'])
    print(output)

#Create a new user user on local machine
def userCreateLocal(username):
    output = subprocess.run('sudo', 'useradd', f'{username}')
    if output.returncode == 0:
        print("User creation successful!")
    else:
        print("User creation unsuccessful!")

#Create a new user user on remote machine
def userCreateRemote(ip, username):
    output = subprocess.run('ssh', f'root@{ip}', 'useradd', f'{username}')
    if output.returncode == 0:
        print("User creation successful!")
    else:
        print("User creation unsuccessful!")

#Delete an existing user on local machine
def userDelLocal(username):
    output = subprocess.run('sudo', 'userdel', '-r', f'{username}')
    if output.returncode == 0:
        print("User deletion successful!")
    else:
        print("User deletion unsuccessful!")

#Delete an existing user user on remote machine
def userCreateRemote(ip, username):
    output = subprocess.run('ssh', f'root@{ip}', 'userdel', '-r', f'{username}')
    if output.returncode == 0:
        print("User deletion successful!")
    else:
        print("User deletion unsuccessful!")



if __name__ == "__main__":
    yumConfigureRemote("192.168.31.87")

